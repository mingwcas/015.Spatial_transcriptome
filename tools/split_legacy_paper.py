#!/usr/bin/env python3
"""把旧单文件格式的论文目录重构为 AGENT.md 规范的多文件结构。

用法: python3 tools/split_legacy_paper.py <paper_dir>

只做机械切分：按 '## NN.' / '## Fig. N' 标题拆成独立文件，
不改写任何内容。已存在的目标目录不覆盖。
"""
import re
import sys
from pathlib import Path


def split_markdown(text, pattern):
    """按 heading 正则切分为 [(title, body), ...]，丢弃前言。"""
    parts = re.split(pattern, text, flags=re.MULTILINE)
    # parts[0] 是首个标题之前的内容（文件头）
    return [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts) - 1, 2)]


def slugify(title, maxlen=60):
    """标题 -> 文件名片段：保留字母数字与下划线，空格转下划线。"""
    s = re.sub(r"[^\w\s-]", "", title)
    s = re.sub(r"[\s\-]+", "_", s.strip())
    return s[:maxlen].strip("_")


def main():
    if len(sys.argv) != 2:
        sys.exit("用法: split_legacy_paper.py <paper_dir>")

    paper = Path(sys.argv[1])
    if not paper.is_dir():
        sys.exit(f"不是目录: {paper}")

    jobs = [
        ("02_methods.md", "02_methods", r"^## (\d+\..*)$", "method"),
        ("03_figures.md", "03_figures", r"^## (Fig\.\s*\d+.*)$", "figure"),
    ]

    for legacy_name, out_name, pattern, kind in jobs:
        legacy = paper / legacy_name
        if not legacy.exists():
            print(f"跳过（不存在）: {legacy}")
            continue

        outdir = paper / out_name
        outdir.mkdir(exist_ok=True)

        sections = split_markdown(legacy.read_text(encoding="utf-8"), pattern)
        for idx, (title, body) in enumerate(sections, 1):
            if kind == "method":
                # "01. 名称" -> "01_名称.md"
                num, _, name = title.partition(".")
                fname = f"{int(num):02d}_{slugify(name)}.md"
                content = f"# Method: {name.strip()}\n\n{body}\n"
            else:
                # "Fig. 1 — 标题"
                m = re.match(r"Fig\.\s*(\d+)\s*[—-]?\s*(.*)", title)
                num, name = (m.group(1), m.group(2)) if m else (str(idx), title)
                fname = f"Fig.{int(num):02d}_{slugify(name)}.md"
                content = f"# Fig. {num} — {name.strip()}\n\n{body}\n"

            dest = outdir / fname
            if dest.exists():
                print(f"已存在，跳过: {dest.name}")
                continue
            dest.write_text(content, encoding="utf-8")
            print(f"写入: {out_name}/{fname}")

    # 重命名报告文件以匹配规范
    renames = [
        ("04_report_4D.md", "04_reports/01_Bioinfo_Report_4D.md"),
        ("05_inventory.md", "05_pipeline_inventory/01_Code_Data_Inventory.md"),
    ]
    for src_name, dst_rel in renames:
        src = paper / src_name
        dst = paper / dst_rel
        if not src.exists():
            continue
        dst.parent.mkdir(exist_ok=True)
        if dst.exists():
            print(f"已存在，跳过: {dst_rel}")
            continue
        src.rename(dst)
        print(f"移动: {src_name} -> {dst_rel}")

    # 旧文件删除（内容已拆分完毕）
    for legacy_name, out_name, _, _ in jobs:
        legacy = paper / legacy_name
        if legacy.exists() and any((paper / out_name).glob("*.md")):
            legacy.unlink()
            print(f"删除旧文件: {legacy_name}")


if __name__ == "__main__":
    main()
