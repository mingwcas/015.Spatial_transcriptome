# Fig. 2 — FISSEQ与单细胞RNA-seq比较

## Caption（原文）
> Comparing single-cell RNA-seq with FISSEQ. (a) A typical single-cell RNA-seq can generate more than one million reads per cell, but <10% represent unique reads from cDNAs, and they are composed largely of structural and/or housekeeping genes (i.e., ribosome-related). Many genes of interest are found near the detection limit with a large coefficient of variation, and the high correlation reported for single-cell RNA-seq is typically due to housekeeping genes. (b) The current version of FISSEQ combines mRNA reads from ~40 cells to obtain a comparable result, but the high correlation between biological replicates in FISSEQ results from mostly cell type–specific expression markers.

## Panel-by-Panel 解读

### Panel a — 单细胞RNA-seq读取分布
**结论**：单细胞RNA-seq虽然读取数量大，但大部分为管家基因，目标基因在检测限附近

**关键数据**：
- iPS RNA-seq：35,000 reads/cell
- 仅32%为预期随机变异范围内的基因
- ~30个基因落在核糖体和RNA加工相关类别
- POU5F1, KLF4, SOX2等干性基因表达量低
- RNA-seq：~4,000 mRNAs/cell
- Pearson's r = 0.9（生物重复相关性主要由管家基因驱动）

### Panel b — FISSEQ读取分布
**结论**：FISSEQ读取数量少但富含细胞类型特异性标记物

**关键数据**：
- Fibro FISSEQ：8,000 reads/40 cells (~200 reads/cell)
- FISSEQ：~700 mRNAs/region
- TGFBI, SPARC, ITGB1, Collagen, TIMP3, ZFN480, FN1等成纤维细胞特异性基因高表达
- Pearson's r = 0.9（相关性由细胞类型特异性基因驱动）
- 功能性重要转录本在FISSEQ中富集>10倍（相比单细胞RNA-seq）

## 总体结论
Fig. 2揭示了FISSEQ与单细胞RNA-seq的根本差异：虽然FISSEQ读取深度较低（~200 vs ~40,000 mRNA reads/cell），但其独特的富集特性使得功能性重要转录本（细胞类型特异性标记物）在FISSEQ中被过度代表。这意味着FISSEQ特别适合细胞类型鉴定和功能分类，而非全转录组定量。

## 关联 Figures / Extended Data
- **Fig. 6** — 数据分析步骤
- 论文正文中的"Comparisons with single-cell RNA-seq"部分
