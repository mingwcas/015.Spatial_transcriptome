#!/usr/bin/env python3
"""验收论文目录是否符合 09_生信分析/AGENT.md 规范。

用法:
    python3 tools/verify_papers.py [目录 ...]     # 默认检查 09_生信分析 下所有论文

退出码 0 表示全部通过；1 表示有目录不合格（不合格原因打印到 stdout）。
"""
import json
import re
import sys
from pathlib import Path

REQUIRED = ["01_metadata", "02_methods", "03_figures", "04_reports", "05_pipeline_inventory"]

# AGENT.md 模板里的占位句；出现即说明只生成了骨架而没有真实内容
PLACEHOLDERS = [
    "引用论文 Methods 段落原文",
    "一句话说明该方法解决什么问题",
    "完整抄录原文图注",
    "该 panel 传达的核心发现",
    "论文信息抬头",
]

SKIP_DIRS = {"scripts"}


def check(paper: Path) -> list[str]:
    problems = []
    for sub in REQUIRED:
        d = paper / sub
        if not d.is_dir():
            problems.append(f"缺少 {sub}/")
        elif not any(d.iterdir()):
            problems.append(f"{sub}/ 为空")

    meta = paper / "01_metadata"
    if meta.is_dir():
        jsons = list(meta.glob("*.json"))
        if not jsons:
            problems.append("01_metadata/ 无 json")
        else:
            try:
                json.loads(jsons[0].read_text())
            except Exception as e:
                problems.append(f"metadata.json 解析失败: {e}")

    if not any((paper / "02_methods").glob("*.md")) if (paper / "02_methods").is_dir() else True:
        problems.append("02_methods/ 无方法文件")
    if not any((paper / "03_figures").glob("*.md")) if (paper / "03_figures").is_dir() else True:
        problems.append("03_figures/ 无图文件")

    for sub in ("02_methods", "03_figures", "04_reports", "05_pipeline_inventory"):
        d = paper / sub
        if not d.is_dir():
            continue
        for f in d.rglob("*.md"):
            text = f.read_text(encoding="utf-8", errors="ignore")
            for ph in PLACEHOLDERS:
                if ph in text:
                    problems.append(f"{f.relative_to(paper)} 含模板占位符“{ph}”")
                    break
    return problems


def main():
    base = Path("09_生信分析")
    targets = [Path(p) for p in sys.argv[1:]] or sorted(
        p for p in base.iterdir() if p.is_dir() and p.name not in SKIP_DIRS
    )

    failed = 0
    for paper in targets:
        problems = check(paper)
        if problems:
            failed += 1
            print(f"✗ {paper.name}")
            for p in problems:
                print(f"    - {p}")
        else:
            print(f"✓ {paper.name}")

    print(f"\n{len(targets) - failed}/{len(targets)} 通过")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
