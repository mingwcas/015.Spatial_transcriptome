# Fig. 5 — Visium and Xenium integration derive differentially expressed genes in triple-positive receptor ROI

## Caption（原文）
> a Xenium spatial plot for ERBB2 (HER2—gray), ESR1 (estrogen receptor—green), and PGR (progesterone receptor—magenta) decoded transcripts. Scale bar = 1 mm. b Closer view of triple-positive ROI. Scale bar = 0.2 mm. c Corresponding H&E image. d Cell types contained within ROI reveal that this is a DCIS #2 tumor epithelium. e Individual Xenium spatial plots from (b). f Chromium scFFPE-seq yields only about 30 cells that are positive for PGR, but these cells do not express ERBB2 or ESR1. g Triple-positive region is identified in Visium (given a priori knowledge from Xenium) and is h part of a distinct cluster (see Fig. 2b). i Spot interpolation (see Supp. Fig. 10) provides cell type frequencies within each Visium spot. Color code legend is shown in (d). j Visium H&E and four representative differentially expressed genes in the tumor epithelium (94 genes; log2FC > 1.5; p-value < 0.05) revealed by Visium data across the whole transcriptome. Scale bar = 1 mm. Differential expression was performed in Loupe Browser (see "Methods"), which performs a variant of the negative binomial exact test (for small gene counts), or a fast asymptotic beta test derived from edgeR (for large gene counts). P-values were adjusted for multiple testing using the Benjamini–Hochberg procedure to control for the false discovery rate. Both the Xenium and Visium experiments were performed in replicate on two serial sections, with one representative section from each technology shown here.

## Panel-by-Panel 解读

### Panel a — 三种受体的空间分布
**结论**：Xenium 空间图展示了 ERBB2（HER2）、ESR1（雌激素受体）和 PGR（孕激素受体）解码转录本的分布，主要为 ERBB2+ 和 ERBB2+/ESR1+ 双阳性区域。

**关键数据**：比例尺 = 1 mm；组织块病理注释为 HER2+/ER+/PR−。

### Panel b, c — 三阳性 ROI 放大视图及对应 H&E
**结论**：放大视图展示了一个小型三阳性（ERBB2+/ESR1+/PGR+）DCIS 区域，位于脂肪细胞附近，由 DCIS #2 肿瘤上皮组成，缺乏 KRT15+ 肌上皮细胞层。

**关键数据**：比例尺 = 0.2 mm；该 ROI 由 DCIS #2 肿瘤上皮细胞构成。

### Panel d — ROI 内细胞类型
**结论**：ROI 内的细胞类型组成证实该区域为 DCIS #2 肿瘤上皮。

**关键数据**：主要为 DCIS #2 肿瘤上皮细胞。

### Panel e — 各受体单独空间图
**结论**：单独展示了 ERBB2、ESR1 和 PGR 的 Xenium 空间分布，确认三阳性区域的存在。

**关键数据**：三种受体在同一区域共表达。

### Panel f — scFFPE-seq 中 PGR+ 细胞
**结论**：scFFPE-seq 数据中仅约 30 个 PGR+ 细胞，且这些细胞不共表达 ESR1 或 ERBB2，说明 scFFPE-seq 未能检测到三阳性细胞。

**关键数据**：约 30 个 PGR+ 细胞；不共表达 ERBB2 或 ESR1。

### Panel g, h — Visium 中的三阳性区域
**结论**：在已知 Xenium 结果的先验知识下，三阳性区域在 Visium 中仅对应 5-6 个 spots，属于 Cluster 12，可能被忽略。

**关键数据**：5-6 个 Visium spots；属于 Cluster 12。

### Panel i — Spot 插值分析
**结论**：通过"spot 插值"方法将 Xenium 数据映射到 Visium spots，提供了三阳性区域内各 spot 的细胞类型频率信息。

**关键数据**：Spot 插值方法实现了 Xenium-Visium 数据整合。

### Panel j — 全转录组差异表达分析
**结论**：Visium 数据揭示了肿瘤上皮中 94 个差异表达基因（log2FC > 1.5; p-value < 0.05），展示了四个代表性差异表达基因。

**关键数据**：94 个差异表达基因（PGR+ vs PGR− DCIS #1）；44 个差异表达基因（PGR+ vs PGR− DCIS #2）；差异表达使用负二项精确检验或 edgeR 衍生的渐近 beta 检验；p 值经 Benjamini-Hochberg 校正。

## 总体结论
该图展示了 Visium 和 Xenium 数据整合如何发现和表征一个小型三阳性受体（ERBB2+/ESR1+/PGR+）DCIS 区域——该区域在病理注释中被标记为 HER2+/ER+/PR−。Xenium 的高分辨率首先检测到这些稀疏的三阳性细胞，而 Visium 提供了全转录组信息。通过 spot 插值方法，研究人员能够获得该区域的细胞类型组成和全转录组差异表达分析结果。这一发现表明，仅在 5.5 mm × 7.5 mm 的切片中就存在一个可能改变分类和治疗方案的三阳性区域。

## 关联 Figures / Extended Data
- Fig. 2b, c（Visium 聚类和空间分布）
- Fig. 3（Xenium 数据质量）
- Supp. Figure 10（Spot 插值方法）
- Supp. Figure 11（基因本体分析）
