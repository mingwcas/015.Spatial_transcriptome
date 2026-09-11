# ED Fig. 9 — SPLIT Improvements for Breast Panel

## Caption（原文）
> Extended Data Fig. 9 | SPLIT improvements and comparison of segmentation approaches for Breast panel. a, UMAPs of Xenium cell-level data obtained before (raw) and after count correction for Breast panel and default (5 µm) or ProSeg segmentation. b-g, Metrics obtained before (raw) and after count correction for different segmentations and count correction methods for Breast panel: biological conservation (b); batch correction (c); number of cells (d); median number of genes (e); strength of T cell contamination by malignant cells (f); cosine similarity of Xenium with Chromium snRNA-seq T cell pseudo-bulk profiles (g). h, GSEA showing T cell exhaustion signatures near malignant cells for Breast panel.

## Panel-by-Panel 解读

### Panel a — UMAP比较
**结论**：乳腺癌panel的SPLIT校正同样显著改善细胞类型分离。

**关键数据**：
- Raw: 混合cluster
- SPLIT: 清晰分离

### Panel b,c — SCIB指标
**结论**：乳腺癌数据验证了Lung panel的发现：SPLIT在生物conservation和批次校正上表现最佳。

**关键数据**：
- SPLIT: 最高生物conservation
- 批次效应最小化

### Panel d,e — 细胞数和基因数
**结论**：与Lung panel一致，ovrlpy/ResolVI减少细胞数，SPLIT保留更多细胞同时提高纯度。

**关键数据**：
- SPLIT保留细胞结构
- Ovrlpy 0.7细胞数最少

### Panel f — T细胞污染
**结论**：乳腺癌T细胞同样显示恶性细胞污染，SPLIT有效减少。

**关键数据**：
- Top 20恶性标记数减少
- ProSeg+SPLIT最优

### Panel g — 与Chromium的相似度
**结论**：SPLIT提高与Chromium snRNA-seq的相似度。

**关键数据**：余弦相似度增加

### Panel h — GSEA富集
**结论**：乳腺癌T细胞邻近恶性细胞时显示耗竭特征，与Lung一致。

**关键数据**：
- Exhausted T cell markers
- SPLIT后富集更显著

## 总体结论
ED Fig. 9在乳腺癌数据中验证了Lung panel的所有发现，证明SPLIT的普遍适用性。

## 关联 Figures / Extended Data
- **Fig. 4** — Lung panel的完整比较
