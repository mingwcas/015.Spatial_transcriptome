# 代码与数据清单 — Slide-seqV2 Near-Cellular Resolution

---

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| PuckCaller (Image processing) | https://github.com/MacoskoLab/PuckCaller/ | MIT | MATLAB image processing & basecalling |
| slideseq-tools (Data pipeline) | https://github.com/MacoskoLab/slideseq-tools | MIT | Complete analysis pipeline |
| Slide_seqv2 (Analysis) | https://github.com/rstickels/Slide_seqv2 | MIT | Custom analysis scripts |
| scVelo | https://github.com/theislab/scvelo (v0.1.25) | BSD | RNA velocity analysis |
| Monocle3 | https://github.com/cole-trapnell-lab/monocle3 (beta) | Artistic-2.0 | Trajectory inference |
| Drop-seq tools | https://github.com/broadinstitute/Drop-seq (v2.3.0) | BSD | Pre-alignment processing |
| Picard | https://broadinstitute.github.io/picard/ (v2.18.14) | MIT | BAM processing |
| STAR aligner | https://github.com/alexdobin/STAR (v2.5.2a) | GPL | RNA-seq alignment |
| Seurat | https://github.com/satijalab/seurat (v2.3.4) | GPL-3.0 | scRNA-seq integration |
| clusterProfiler | https://guangchuangyu.github.io/software/clusterProfiler/ | Artistic-2.0 | GO enrichment |
| Starfish | https://github.com/spacetx/starfish | BSD-3-Clause | smFISH counting |

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| Raw sequencing data | Broad Institute Single Cell Portal | SCP815 | "Sensitive spatial genome-wide expression profiling at cellular resolution" |
| Source data | Nature Biotechnology | DOI: 10.1038/s41587-020-0739-1 | 所有主图source data |
| Mouse brain scRNA-seq | Saunders et al. Cell 2018 | GEO: GSE116470 | Cell type markers reference |
| Reference genome | GRCm38.81 | Ensembl | Mouse genome annotation |
| Supplementary Table 1 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | UMI comparisons |
| Supplementary Table 2 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | Marker gene counts |
| Supplementary Table 3 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | 213 dendritic genes |
| Supplementary Table 4 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | 1,349 spatial genes |
| Supplementary Table 5 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | Trajectory genes |
| Supplementary Table 6 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | Oligo sequences |
| Supplementary Table 7 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | Puck metadata |
| Supplementary Table 8 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | Pipeline runtime |
| Supplementary Dataset 1 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | 213 genes spatial reconstructions |
| Supplementary Dataset 2 | Nature Biotech Supplementary | DOI: 10.1038/s41587-020-0739-1 | All spatial gene plots |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| Barcoded bead synthesis | ⚠️ 部分受限 | 需化学合成设备或商业采购 (ChemGenes) |
| Puck sequencing | ⚠️ 部分受限 | 需专业显微镜和flow cell设备 |
| Image processing/basecalling | ✅ 可完全复现 | PuckCaller开源MATLAB代码 |
| Slide-seq tools pipeline | ✅ 可完全复现 | 完整pipeline开源，多步骤文档完善 |
| scVelo trajectory analysis | ✅ 可完全复现 | scVelo开源，版本明确 |
| Monocle3 analysis | ✅ 可完全复现 | Monocle3开源可用 |
| Dendritic enrichment analysis | ✅ 可完全复现 | 自定义R/Python代码在GitHub |
| Spatial LT fitting | ✅ 可完全复现 | MATLAB代码可复用 |
| GO enrichment | ✅ 可完全复现 | clusterProfiler标准工具 |
| smFISH validation | ⚠️ 部分受限 | 需商业probe sets (Molecular Instruments) |
| Comparison with Visium/HDST | ⚠️ 部分受限 | 需下载参考数据或商业平台 |
| Full experimental reproduction | ❌ 无法直接复现 | 需原始样本、仪器和试剂 |

---

## 状态说明

- ✅ **可完全复现**（工具/代码开源可获取）
- ⚠️ **部分受限**（需注册/需商业许可/需专业设备）
- ❌ **无法直接复现**（需原始样本/仪器）
