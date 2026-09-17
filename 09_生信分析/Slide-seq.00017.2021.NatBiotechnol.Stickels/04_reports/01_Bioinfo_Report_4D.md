# 四维度生信分析报告 — Slide-seqV2 Near-Cellular Resolution

> **论文**: Highly sensitive spatial transcriptomics at near-cellular resolution with Slide-seqV2
> **DOI**: https://doi.org/10.1038/s41587-020-0739-1
> **平台**: Slide-seq (Slide-seqV2)
> **完成日期**: 2021 (Published December 2020)

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| Barcoded bead synthesis | Split-pool phosphoramidite synthesis | Akta Oligopilot 10 | 415 unique barcodes, 10μm beads |
| Bead indexing | Monobase sequencing-by-ligation | PuckCaller (MATLAB) | 14 split-pool bases, 3 ligation modes |
| Image processing | Fluorescence basecalling | PuckCaller | Direct basespace conversion |
| Data processing | Slide-seq tools pipeline | slideseq-tools (GitHub) | DGE matrix generation |
| Read alignment | STAR alignment | STAR-2.5.2a | GRCm38.81 genome |
| Barcode matching | Hamming distance matching | cmatcher.cpp | ≤1 mismatch tolerance |
| Dendritic enrichment | Differential expression | Custom R/Python | 213 genes (FC>2, q<0.05) |
| Gene clustering | K-means + gap-statistic | clusterProfiler | 4 spatial clusters |
| Trajectory inference | RNA velocity | scVelo 0.1.25 | Latent time estimation |
| Pseudotime analysis | Monocle3 | monocle3 (beta) | Developmental ordering |
| Spatial LT fitting | 3D surface fitting | MATLAB 2017a | 80μm grid |
| GO enrichment | Over-representation analysis | clusterProfiler R | Cellular component, Biological process |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|---------|-------------|
| Fig. 1 | Slide-seqV2灵敏度提升 (~9x UMI counts) | Histogram, Spatial heat map, Bar plot |
| Fig. 2 | Dendritically enriched mRNAs (213 genes, 4 clusters) | Heat map, Spatial profiles, QQ plot |
| Fig. 3 | Cortical developmental trajectory (1,043 spatial LT genes) | Spatial map with arrows, Density plot, GO enrichment |
| Supplementary Fig. 1 | Monobase sequencing strategy | Schematic diagrams |
| Supplementary Fig. 2 | Bead barcode clonality | Barcode distribution |
| Supplementary Fig. 3 | Comparison with Visium and HDST | Box/violin plots |
| Supplementary Fig. 4-5 | smFISH validation, sensitivity/reproducibility | Images, Scatter plots |
| Supplementary Fig. 6-8 | Additional analyses and method comparisons | Various |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| Bead synthesis | Akta Oligopilot 10 | - | 商业 (GE Healthcare) |
| Sequencing | SOLiD / Monobase | - | 商业/开源 |
| Image processing | PuckCaller | GitHub | 开源 (MATLAB) |
| Illumina demultiplex | Picard | 2.18.14 | 开源 |
| Pre-alignment | Drop-seq tools | 2.3.0 | 开源 |
| Alignment | STAR | 2.5.2a | 开源 |
| DGE matrix | slideseq-tools | GitHub | 开源 |
| Velocity | scVelo | 0.1.25 | 开源 |
| Pseudotime | Monocle3 | beta | 开源 |
| Clustering | Seurat | 2.3.4 | 开源 |
| Clustering | clusterProfiler | R package | 开源 |
| Visualization | MATLAB | 2017a | 商业 |
| Visualization | Python | 3.7 | 开源 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| RNA velocity | Dynamical modeling | 推断发育轨迹方向和时间 |
| Latent time (LT) | Dimensionality reduction | 连续发育状态估计 |
| Monocle3 | Trajectory inference | 细胞命运决策建模 |
| K-means clustering | Unsupervised learning | 基因表达模式聚类 |
| Gap-statistic | Model selection | 最优聚类数目确定 |
| Hamming distance | String matching | Barcode匹配 (≤1 mismatch) |
| L1 norm test | Distribution comparison | 空间非随机性检验 |
| FDR correction | Multiple testing | Storey (2002) 方法 |
| Pearson correlation | Linear correlation | Spatial LT相关性分析 |

---

## 局限性 / Limitation

1. **技术依赖**: 需要专业设备（confocal microscope, flow cell system）进行puck sequencing
2. **通量限制**: 每个puck ~200M reads，单次实验成本较高
3. **敏感性**: 仍低于droplet scRNA-seq (~44% detection efficiency)
4. **厂商关联**: 部分作者持有相关专利 (Macosko, Chen)
