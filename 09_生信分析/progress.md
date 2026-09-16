# 论文处理进度跟踪

> 自动任务状态文件，每篇论文处理后更新本文件

> 更新于: 2026-09-16 13:15:00

> 总论文数: 33 | ✅ 合规完成: 11 | 🔧 需重构: 0 | ⏳ 待处理: 22

---

## 已完成论文（符合 AGENT.md 规范）

| # | 平台 | 年份 | 期刊 | 第一作者 | 目录 |
|---|------|------|------|------|------|
| 01 | Visium | 2016 | Science | Ståhl | `09_生信分析/Visium.00001.2016.Science.Stahl/` |
| 03 | Visium HD | 2025 | NatGenet | Oliveira | `09_生信分析/Visium.00003.2025.NatGenet.Oliveira/` |
| 04 | Xenium | 2025 | NatCommun | Ren | `09_生信分析/Xenium.00004.2025.NatCommun.Ren/` |
| 05 | Xenium | 2025 | NatMethods | Salas | `09_生信分析/Xenium.00005.2025.NatMethods.Salas/` |
| 06 | Xenium | 2026 | NatMethods | Bilous | `09_生信分析/Xenium.00006.2026.NatMethods.Bilous/` |
| 07 | Xenium | 2026 | eLife | Hallinan | `09_生信分析/Xenium.00007.2026.eLife.Hallinan/` |
| 08 | MERSCOPE | 2015 | Science | Chen | `09_生信分析/MERSCOPE.00001.2015.Science.Chen/` |
| 09 | MERSCOPE | 2018 | Science | Moffitt | `09_生信分析/MERSCOPE.00002.2018.Science.Moffitt/` |

---

## 待清理

- `09_生信分析/Visium.00001.2025.NatGenet.Oliveira.LOCALESAMPLE/` — 废弃样板，与 #03 重复，暂不纳入论文计数
- `09_生信分析/MAPS.00007.2026.bioRxiv.Chen/` — 单文件报告，暂不纳入本批 33 篇 PDF 任务

---

## 待处理论文（按处理顺序）

| 顺序 | # | 平台 | 年份 | 期刊 | 第一作者 | PDF 文件 |
|------|---|------|------|------|------|---------|
| 1 | 12 | CosMx | 2026 | CellRepMed | Zhang | `04.2026.CellRepMed.CosMx_SCLC_TME_heterogeneity.pdf` |
| 5 | 13 | GeoMx | 2022 | FrontOncol | Hernandez | `05.2022.FrontOncol.GeoMx_immunoprofiling_opportunities.pdf` |
| 6 | 14 | GeoMx | 2026 | ImmunoAdv | Park | `05.2026.ImmunoAdv.GeoMx_dMMR_CRC_immunotherapy.pdf` |
| 7 | 15 | Stereo-seq | 2022 | Science | Wei | `06.2022.Science.Stereo-seq_axolotl_brain_regeneration.pdf` |
| 8 | 16 | Stereo-seq | 2025 | Cell | Zhao | `06.2025.Cell.Stereo-seqV2_total_RNA_FFPE.pdf` |
| 9 | 17 | Slide-seq | 2021 | NatBiotechnol | Stickels | `07.2021.NatBiotechnol.Slide-seqV2_near_cellular_resolution.pdf` |
| 10 | 18 | Slide-seq | 2024 | NatMethods | You | `07.2024.NatMethods.Slide-seq_comparison_sequencing_based_methods.pdf` |
| 11 | 19 | Slide-seq | 2025 | NatCommun | Feng | `07.2025.NatCommun.Slide-seq_molecular_cartography_DS_brain.pdf` |
| 12 | 20 | DBiT-seq | 2020 | Cell | Liu | `08.2020.Cell.DBiTseq_deterministic_barcoding.pdf` |
| 13 | 21 | DBiT-seq | 2023 | NatBiotechnol | Liu | `08.2023.NatBiotechnol.DBiTseq_spatial_CITEseq.pdf` |
| 14 | 22 | DBiT-seq | 2024 | Cell | Bai | `08.2024.Cell.DBiTseq_RNA_biology_FFPE.pdf` |
| 15 | 23 | Open-ST | 2024 | Cell | Schott | `09.2024.Cell.OpenST_high_res_3D.pdf` |
| 16 | 24 | Open-ST | 2025 | CellSyst | Pentimalli | `09.2025.CellSyst.OpenST_ECM_3D_TME.pdf` |
| 17 | 25 | Open-ST | 2025 | STARProtoc | Schott | `09.2025.STARProtoc.OpenST_3D_protocol.pdf` |
| 18 | 26 | FISSEQ | 2014 | Science | Lee | `10.2014.Science.FISSEQ_subcellular_RNA_seq.pdf` |
| 19 | 27 | FISSEQ | 2015 | NatProtoc | Lee | `10.2015.NatProtoc.FISSEQ_RNA_in_situ_sequencing.pdf` |
| 20 | 28 | FISSEQ | 2020 | Cell | Chen | `10.2020.Cell.FISSEQ_Alzheimer_disease.pdf` |
| 21 | 29 | STARmap | 2018 | Science | Wang | `11.2018.Science.STARmap_3D_intact_tissue.pdf` |
| 22 | 30 | STARmap | 2023 | Science | Zeng | `11.2023.Science.STARmapPLUS_translatomics_molecular_resolution.pdf` |
| 23 | 31 | STARmap | 2026 | NatProtoc | Ren | `11.2026.NatProtoc.STARmapPLUS_mRNA_life_cycle.pdf` |
| 24 | 32 | IlluminaSpatial | 2023 | NatCommun | Janesick | `12.2023.NatCommun.IlluminaSpatial_mapping_TME.pdf` |
| 25 | 33 | Spatial-ATAC-Hi-C | 2026 | NatMethods | Wang | `13.2026.NatMethods.Spatial-ATAC-Hi-C_chromatin_architecture.pdf` |

---

## 自动化配置

- **Runner 脚本**: `batch_process.sh`（每轮 3 篇，串行）
- **触发时间**: 北京时间 0:05（cron）
- **进度文件**: `09_生信分析/progress.md`
- **验收规则**: 符合 `09_生信分析/AGENT.md` 约定结构，否则删除重新入队

---

## 原文核对修正

本文件早期版本存在编号错漏，已修正：
- `02.2025.NatCommun.*` 与 `02.2025.NatMethods.*` 同属 Xenium 次序，对应 #04/#05
- `01.2025.NatGenet.VisiumHD` 对应 #03
