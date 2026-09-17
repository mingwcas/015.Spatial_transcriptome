# 论文精读审计报告

> 时间：2026-09-18
> 审计对象：`09_生信分析/` 下全部 33 篇完成论文（外加 2 个其他目录）
> 审计工具：`tools/audit_papers.py`（机械可验），并辅以 6 路并发子代理人工审计
> 审计方式：先子代理 deep-dive（17 篇有 JSON 产出）+ 6 个空响应失败 case → 改为 Python 全文自动化（35 个目录）

## 总览

| 判定 | 数量 | 占比 |
|---|---|---|
| ✅ **pass** | 26 / 35 目录 (含 33 篇中 25 篇) | 74% |
| ⚠️ **needs_fix** | 8 / 35 | 23% |
| ❌ **reject** | 1 / 35 (MAPS，本任务范畴外) | 3% |

**33 篇目标论文的真实分布**：25 pass / 8 needs_fix / 0 reject。所有 needs_fix 均为同一类系统性缺陷（详见下）。

## 严重度分布

- critical: 1 个（MAPS 弃样，不在 33 篇内）
- major: 67 个，全部为"方法文件涉及 Figures 引用了 03_figures/ 中不存在的 Fig.N"
- minor: 14 个，全部为"引用了 ED Fig.N"——规范 §3.3 明文允许不单独建 ED 图文件

## 系统性缺陷：方法→图引用 mismatch

**症状**：方法文件中的"涉及 Figures"小节按论文原文编号引用所有图（Fig.3、Fig.7、Fig.11、Fig.16…），但 `03_figures/` 目录只录入了部分图（图号较大的 ED/Supplementary 没单独建文件）。规范 §3.3 说"Extended Data 不单独为 ED Fig 开章节"，但没说方法文件中如何引用未单独录的图。

**影响论文**（8 篇）：
1. **DBiT-seq.00021.2023.NatBiotechnol.Liu**：7 处 major（Fig.3/4/5/7）
2. **IlluminaSpatial.00032.2023.NatCommun.Janesick**：14 处 major（Fig.7–12）
3. **MERSCOPE.00004.2023.Nature.Yao**：2 处 major（Fig.9/14）
4. **Slide-seq.00017.2021.NatBiotechnol.Stickels**：7 处 major（Fig.4/6/7/8/9）
5. **Spatial-ATAC-Hi-C.00033.2026.NatMethods.Wang**：7 处 major（Fig.6/7/8）
6. **Xenium.00004.2025.NatCommun.Ren**：10 处 major（Fig.7–16）
7. **Xenium.00005.2025.NatMethods.Salas**：8 处 major
8. **Xenium.00007.2026.eLife.Hallinan**：7 处 major（Fig.4/5/6/9/11）

**示例**：
- `IlluminaSpatial #32/02_methods/05_Xenium_Workflow.md` 中说 `Fig. 8` / `Fig. 9`，但 03_figures/ 只录到了 Fig.01–06
- `Slide-seq #17/02_methods/10_Trajectory_Analysis_scVelo.md` 中引用 Fig.7/8，但目录里只有 Fig.01–03

**两种修复方式**（需用户决策，二选一）：
1. **为缺失图编号补建 ED Fig 文件**（工作量较大，可能要补 40+ 文件）
2. **更新规范**：在方法文件中允许 `Fig.N` 引用指向"论文中的 Fig.N"而不要求本地有对应文件（语义澄清 0 改动）

## 已通过审计的 25 篇（一览）

| # | 平台 | 年份 | 期刊 | 作者 | n_methods | n_figures |
|---|---|---|---|---|---|---|
| 01 | Visium | 2016 | Science | Ståhl | — | — |
| 02 | Visium | 2018 | NatProtoc | Salmén | — | — |
| 03 | Visium HD | 2025 | NatGenet | Oliveira | — | — |
| 06 | Xenium | 2026 | NatMethods | Bilous | — | — |
| 08-11 | MERSCOPE | 2015–23 | Sci/Nat | Chen/Moffitt/Kumar/Yao | (partly) | — |
| 12 | CosMx | 2026 | CellRepMed | Zhang | — | — |
| 13 | GeoMx | 2022 | FrontOncol | Hernandez | — | — |
| 14 | GeoMx | 2026 | ImmunoAdv | Park | — | — |
| 15-16 | Stereo-seq | 2022/25 | Sci/Cell | Wei/Zhao | — | — |
| 18 | Slide-seq | 2024 | NatMethods | You | — | — |
| 19 | Slide-seq | 2025 | NatCommun | Feng | — | — |
| 20 | DBiT-seq | 2020 | Cell | Liu | — | — |
| 22 | DBiT-seq | 2024 | Cell | Bai | — | — |
| 23 | Open-ST | 2024 | Cell | Schott | — | — |
| 24-25 | Open-ST | 2025 | CellSyst/STARProtoc | Pentimalli/Schott | — | — |
| 26-28 | FISSEQ | 2014–20 | Sci/NatProtoc/Cell | Lee/Lee/Chen | — | — |
| 29-31 | STARmap | 2018–26 | Sci/NatProtoc | Wang/Zeng/Ren | — | — |

(完整 n_methods/n_figures 数据见 `tools/audit_papers.py` 输出)

## 内容质量抽查（人工审计补充）

抽样 6 篇 deep-dive（worker 返回 JSON 的）：
- 原文引用块全部含具体参数/术语（如 Visium #02 "4% formaldehyde/10 min", MERSCOPE #01 "1→0/0→1 error rates 10%/4%", Stereo-seq #15 "DNB、220nm、500/715nm"）
- 解读部分普遍落地到具体方法名/参数值，套话占比较低
- 名词表均含定义（非空词条）
- 平台名全部合规

## 局限与未审计项

- 本审计**全部依赖产物文件**，未打开 PDF 比对原文逐字（无源访问）
- 子代理 deep-dive 6 路 worker 中有 2 路全部返回 null（GeoMx #13/14, FISSEQ #27 等 12 篇），改由 Python 自动化补齐
- 解读逻辑/生物学准确性需要领域专家复核，本审计仅做机械一致性检查

