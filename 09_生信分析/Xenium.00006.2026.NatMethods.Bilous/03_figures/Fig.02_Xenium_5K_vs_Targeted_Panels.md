# Fig. 2 — Comparison of Xenium 5K and Targeted Panels

## Caption（原文）
> Fig. 2 | Comparison of Xenium prime (5K) and targeted (Lung) panels. a, UMAP visualization of lung cancer samples based on 194 genes common to the Xenium 5K panel, Xenium Lung panel and Chromium data. Xenium UMAPs are restricted to samples profiled with both Lung and 5K panels. Cells are colored according to their annotated cell types at Level 2.1. b, Distribution of transcript counts per cell in the Xenium 5K, Xenium Lung and Chromium datasets, restricted to the common genes. c, Scatterplot showing average expression of common genes in matched samples from the Xenium 5K and Xenium Lung panels. d, Scatterplot showing cell-type composition in matched samples from the Xenium 5K and Xenium Lung panels. e, Scatterplots comparing average expression of the 194 common genes between Chromium and Xenium Lung, and between Chromium and Xenium 5K, in CD8+ T cells and malignant cells. Analyses are based on matched samples from two donors (L1 and L3) profiled with all three assays. Extended comparisons across all cell types, and a direct comparison between Xenium Lung and Xenium 5K panels, are shown in Extended Data Figs. 3 and 4. R, Spearman's rank correlation coefficient; P values were computed using a two-sided t-test and were not adjusted for multiple comparisons, given the small number (n = 6) of independent donor-level tests. The dashed line indicates the identity (y = x). A solid line indicating generalized linear model (GLM) fit is shown for visualization only.

## Panel-by-Panel 解读

### Panel a — 194共有基因的UMAP比较
**结论**：在共有基因限制下，5K和Lung panel显示相当的细胞类型分离，但约60%的5K细胞因低转录本计数未通过质控。

**关键数据**：
- 194个共有基因用于公平比较
- 5K panel约60%细胞未通过QC

### Panel b — 转录本计数分布
**结论**：5K panel在相同基因集下检测到显著更少的转录本，敏感性低于Lung panel和Chromium。

**关键数据**：
- 5K panel转录本检测显著减少
- Lung panel和Chromium敏感性相当

### Panel c — 基因表达一致性
**结论**：5K和Lung panel在匹配样本中显示合理相关性，但5K panel一致显示较低敏感性。

**关键数据**：
- Spearman R = 0.73 (P < 2.2×10⁻¹⁶)

### Panel d — 细胞类型组成一致性
**结论**：尽管敏感性差异，5K和Lung panel在细胞类型组成上表现良好一致性。

**关键数据**：
- 高细胞类型组成一致性

### Panel e — 与Chromium参考的比较
**结论**：两种Xenium panel与Chromium均有良好一致性，5K panel在敏感性上更接近Chromium。

**关键数据**：
- CD8+ T cells: R = 0.70-0.89
- Malignant cells: R = 0.74-0.89

## 总体结论
Fig. 2揭示了Xenium面板设计的关键权衡：5K panel提供更广基因覆盖但牺牲了每个基因的检测敏感性；靶向panel在有限基因上达到更深检测。

## 关联 Figures / Extended Data
- ED Fig. 3 — Cross-panel一致性详细分析
- ED Fig. 4 — 各细胞类型的表达相关性
