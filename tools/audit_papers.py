#!/usr/bin/env python3
"""审计 09_生信分析/ 下所有论文目录。

机械可验项：
1. verifier（结构 + 占位符）
2. 方法->图引用：方法文件中"涉及 Figures"指向的 Fig.N 是否存在
3. 报告虚构图号：04_report 维度二引用的 Fig.N/ED Fig.N 是否存在
4. 平台名合规（不属于规范 = critical）
"""
import json
import re
import subprocess
import sys
from pathlib import Path

PLATFORMS = {"Visium", "Visium HD", "Xenium", "MERSCOPE", "CosMx", "GeoMx",
             "Stereo-seq", "Slide-seq", "DBiT-seq", "Open-ST", "FISSEQ",
             "STARmap", "IlluminaSpatial", "Spatial-ATAC-Hi-C"}

PLATFORM_PREFIX_RE = re.compile(r"^([A-Za-z][A-Za-z\-]*(?:\s+[A-Z][A-Za-z]*)?)\.\d{5}\.")


def list_actual_figs(fig_dir):
    if not fig_dir.is_dir():
        return set(), set()
    mains, eds = set(), set()
    for f in sorted(fig_dir.glob("*.md")):
        stem = f.stem
        m = re.match(r"Fig[._]?(\d+)", stem)
        if m:
            n = int(m.group(1))
            (eds if stem.upper().startswith("ED") else mains).add(n)
    return mains, eds


def extract_fig_refs(text):
    refs_main, refs_ed = set(), set()
    for m in re.finditer(r"\b(ED\s+)?Fig\.?\s*(\d+)", text, re.I):
        ed = m.group(1) is not None
        n = int(m.group(2))
        if 0 < n <= 30:
            (refs_ed if ed else refs_main).add(n)
    return refs_main, refs_ed


def check_paper(paper_dir):
    name = paper_dir.name
    issues = []

    m = PLATFORM_PREFIX_RE.match(name)
    platform = m.group(1) if m else None
    platform_ok = platform in PLATFORMS

    try:
        r = subprocess.run(
            ["python3", "tools/verify_papers.py", str(paper_dir)],
            capture_output=True, text=True, timeout=30,
        )
        verifier_pass = (r.returncode == 0)
        if not verifier_pass:
            issues.append({"severity": "critical", "file": "(structure)",
                           "detail": "verify_papers.py 失败"})
    except Exception as e:
        verifier_pass = False
        issues.append({"severity": "critical", "file": "(structure)",
                       "detail": f"运行验证器错误: {e}"})

    fig_dir = paper_dir / "03_figures"
    actual_mains, actual_eds = list_actual_figs(fig_dir)

    methods_dir = paper_dir / "02_methods"
    if methods_dir.is_dir():
        for mf in sorted(methods_dir.glob("*.md")):
            text = mf.read_text(encoding="utf-8", errors="ignore")
            sec_m = re.search(r"## 涉及 [Ff]igures\s*\n(.*?)(?=\n## |\Z)", text, re.S)
            if not sec_m:
                continue
            sec = sec_m.group(1)
            refs_m, refs_e = extract_fig_refs(sec)
            for n in refs_m:
                if n not in actual_mains:
                    issues.append({"severity": "major",
                                   "file": str(mf.relative_to(paper_dir)),
                                   "detail": f"涉及 Figures 引用 Fig.{n}，但 03_figures/ 中不存在"})
            for n in refs_e:
                if n not in actual_eds:
                    issues.append({"severity": "minor",
                                   "file": str(mf.relative_to(paper_dir)),
                                   "detail": f"涉及 Figures 引用 ED Fig.{n}；规范 §3.3 允许 ED 不单独录"})

    report = paper_dir / "04_reports" / "01_Bioinfo_Report_4D.md"
    if report.is_file():
        text = report.read_text(encoding="utf-8", errors="ignore")
        sec_m = re.search(r"## 维度二[:：][^\n]*\n(.*?)(?=\n## |\Z)", text, re.S)
        if sec_m:
            refs_m, refs_e = extract_fig_refs(sec_m.group(1))
            for n in refs_m:
                if n not in actual_mains:
                    issues.append({"severity": "major",
                                   "file": "04_reports/01_Bioinfo_Report_4D.md",
                                   "detail": f"维度二引用 Fig.{n}，但 03_figures/ 中不存在"})
            for n in refs_e:
                if n not in actual_eds:
                    issues.append({"severity": "minor",
                                   "file": "04_reports/01_Bioinfo_Report_4D.md",
                                   "detail": f"维度二引用 ED Fig.{n}；规范允许 ED 不单独录"})

    return {
        "paper": name,
        "verifier_pass": verifier_pass,
        "platform_name_conforms": platform_ok,
        "platform_actual": platform,
        "n_methods_files": len(list(methods_dir.glob("*.md"))) if methods_dir.is_dir() else 0,
        "n_figures_files": (len(actual_mains) + len(actual_eds)) if fig_dir.is_dir() else 0,
        "issues": issues,
        "severity_counts": {
            "critical": sum(1 for x in issues if x["severity"] == "critical"),
            "major": sum(1 for x in issues if x["severity"] == "major"),
            "minor": sum(1 for x in issues if x["severity"] == "minor"),
        },
        "overall_verdict": (
            "reject" if any(x["severity"] == "critical" for x in issues)
            else "needs_fix" if any(x["severity"] == "major" for x in issues)
            else "pass"
        ),
    }


def main():
    if len(sys.argv) > 1:
        targets = [Path(p) for p in sys.argv[1:]]
    else:
        base = Path("09_生信分析")
        targets = sorted(p for p in base.iterdir()
                         if p.is_dir() and p.name not in {"scripts"})
    out = [check_paper(t) for t in targets]
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
