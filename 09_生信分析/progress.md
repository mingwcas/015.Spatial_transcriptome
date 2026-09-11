# 论文处理进度跟踪

> 自动任务状态文件，每篇论文处理后更新本文件

> 更新于: 2026-09-12 00:10:00

> 总论文数: 33 | ✅ 已完成: 6 | ⏳ 待处理: 27

---

## 已完成论文

| # | 平台 | 年份 | 期刊 | 第一作者 | 目录 |
|---|------|------|------|------|------|
| 01 | Visium | 2016 | Science | Ståhl | `09_生信分析/Visium.00001.2016.Science.Ståhl/` |
| 02 | Visium | 2018 | NatProtoc | Salmén | `09_生信分析/Visium.00002.2018.NatProtoc.Salmén/` |
| 03 | Visium HD | 2025 | NatGenet | Oliveira | `09_生信分析/Visium.00003.2025.NatGenet.Oliveira/` |
| 04 | Xenium | 2025 | NatCommun | Ren | `09_生信分析/Xenium.00004.2025.NatCommun.Ren/` |
| 05 | Xenium | 2025 | NatMethods | Salas | `09_生信分析/Xenium.00005.2025.NatMethods.Salas/` |
| 06 | Xenium | 2026 | NatMethods | Bilous | `09_生信分析/Xenium.00006.2026.NatMethods.Bilous/` |

---

## 待处理论文（按处理顺序）

| 顺序 | # | 平台 | 年份 | 期刊 | 第一作者 | PDF 文件 |
|------|---|------|------|------|------|---------|
| 1 | 07 | Xenium | 2026 | eLife | Hallinan | `02.2026.eLife.Xenium_off_target_probe_binding.pdf` |
| 2 | 08 | MERSCOPE | 2015 | Science | Chen | `03.2015.Science.MERSCOPE_highly_multiplexed_RNA_profiling.pdf` |
| 3 | 09 | MERSCOPE | 2018 | Science | Moffitt | `03.2018.Science.MERSCOPE_hypothalamic_preoptic_region.pdf` |
| 4 | 10 | MERSCOPE | 2023 | Nature | Kumar | `03.2023.Nature.MERSCOPE_human_breast_atlas.pdf` |
| 5 | 11 | MERSCOPE | 2023 | Nature | Yao | `03.2023.Nature.MERSCOPE_mouse_brain_cell_atlas.pdf` |
| 6 | 12 | CosMx | 2026 | CellRepMed | Zhang | `04.2026.CellRepMed.CosMx_SCLC_TME_heterogeneity.pdf` |
| 7 | 13 | GeoMx | 2022 | FrontOncol | Hernandez | `05.2022.FrontOncol.GeoMx_immunoprofiling_opportunities.pdf` |
| 8 | 14 | GeoMx | 2026 | ImmunoAdv | Park | `05.2026.ImmunoAdv.GeoMx_dMMR_CRC_immunotherapy.pdf` |
| 9 | 15 | Stereo-seq | 2022 | Science | Wei | `06.2022.Science.Stereo-seq_axolotl_brain_regeneration.pdf` |
| 10 | 16 | Stereo-seq | 2025 | Cell | Zhao | `06.2025.Cell.Stereo-seqV2_total_RNA_FFPE.pdf` |
| 11 | 17 | Slide-seq | 2021 | NatBiotechnol | Stickels | `07.2021.NatBiotechnol.Slide-seqV2_near_cellular_resolution.pdf` |
| 12 | 18 | Slide-seq | 2024 | NatMethods | You | `07.2024.NatMethods.Slide-seq_comparison_sequencing_based_methods.pdf` |
| 13 | 19 | Slide-seq | 2025 | NatCommun | Feng | `07.2025.NatCommun.Slide-seq_molecular_cartography_DS_brain.pdf` |
| 14 | 20 | DBiT-seq | 2020 | Cell | Liu | `08.2020.Cell.DBiTseq_deterministic_barcoding.pdf` |
| 15 | 21 | DBiT-seq | 2023 | NatBiotechnol | Liu | `08.2023.NatBiotechnol.DBiTseq_spatial_CITEseq.pdf` |
| 16 | 22 | DBiT-seq | 2024 | Cell | Bai | `08.2024.Cell.DBiTseq_RNA_biology_FFPE.pdf` |
| 17 | 23 | Open-ST | 2024 | Cell | Schott | `09.2024.Cell.OpenST_high_res_3D.pdf` |
| 18 | 24 | Open-ST | 2025 | CellSyst | Pentimalli | `09.2025.CellSyst.OpenST_ECM_3D_TME.pdf` |
| 19 | 25 | Open-ST | 2025 | STARProtoc | Schott | `09.2025.STARProtoc.OpenST_3D_protocol.pdf` |
| 20 | 26 | FISSEQ | 2014 | Science | Lee | `10.2014.Science.FISSEQ_subcellular_RNA_seq.pdf` |
| 21 | 27 | FISSEQ | 2015 | NatProtoc | Lee | `10.2015.NatProtoc.FISSEQ_RNA_in_situ_sequencing.pdf` |
| 22 | 28 | FISSEQ | 2020 | Cell | Chen | `10.2020.Cell.FISSEQ_Alzheimer_disease.pdf` |
| 23 | 29 | STARmap | 2018 | Science | Wang | `11.2018.Science.STARmap_3D_intact_tissue.pdf` |
| 24 | 30 | STARmap | 2023 | Science | Zeng | `11.2023.Science.STARmapPLUS_translatomics_molecular_resolution.pdf` |
| 25 | 31 | STARmap | 2026 | NatProtoc | Ren | `11.2026.NatProtoc.STARmapPLUS_mRNA_life_cycle.pdf` |
| 26 | 32 | IlluminaSpatial | 2023 | NatCommun | Janesick | `12.2023.NatCommun.IlluminaSpatial_mapping_TME.pdf` |
| 27 | 33 | Spatial-ATAC-Hi-C | 2026 | NatMethods | Wang | `13.2026.NatMethods.Spatial-ATAC-Hi-C_chromatin_architecture.pdf` |

---

## 自动化配置

- **Workflow 文件**: `.github/workflows/batch_process.yml`
- **触发时间**: 北京时间 0:00–8:00 AM（UTC 前一天 16:00 – 当天 0:00，每分钟触发）
- **进度文件**: `09_生信分析/progress.md`
- **每轮处理**: 最多 3 篇论文
- **验收规则**: 符合 `09_生信分析/AGENT.md` 约定结构，否则删除重新入队
