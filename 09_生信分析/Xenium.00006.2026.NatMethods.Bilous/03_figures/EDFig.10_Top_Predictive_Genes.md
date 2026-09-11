# ED Fig. 10 — Top Predictive Genes for T Cell Proximity

## Caption（原文）
> Extended Data Fig. 10 | Top predictive genes for T cell proximity to malignancy across segmentations. Top 20 gene importances for logistic regression models trained to predict T cells located near versus distant from malignant cells using the lung gene panel. Gene importances are ranked by their mean across samples for each count correction method. a, Results using 5 µm segmentation. b, Results using ProSeg segmentation.

## Panel-by-Panel 解读

### Panel a — 5µm分割的Top基因
**结论**：SPLIT校正后，预测T细胞接近恶性细胞的top基因中恶性标记显著减少，T细胞标记增加。

**关键数据**：
- Raw: 大量恶性标记（KRT7, MUC1等）
- SPLIT: T细胞标记（CD8A, CD3D等）占主导

### Panel b — ProSeg分割的Top基因
**结论**：ProSeg分割的原始数据已较少恶性污染，SPLIT进一步增强T细胞信号。

**关键数据**：
- ProSeg减少部分污染
- SPLIT进一步改善

## 总体结论
ED Fig. 10详细展示了SPLIT如何改变预测T细胞空间邻近性的关键基因，验证其减少非特异性信号的能力。

## 关联 Figures / Extended Data
- **Fig. 4g** — GSEA富集分析
- **Fig. 4e** — Top 20恶性标记数量统计
