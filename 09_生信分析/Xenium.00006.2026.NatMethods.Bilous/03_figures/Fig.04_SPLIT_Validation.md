# Fig. 4 — SPLIT Improvements and Comparison of Segmentation Approaches

## Caption（原文）
> Fig. 4 | SPLIT improvements and comparison of segmentation approaches. a, UMAPs of Xenium cell-level data obtained before (raw) and after count correction for the Lung and 5K panels, and default or ProSeg segmentation. Colored by cell-type annotation. b–f, Metrics obtained before (raw) and after count correction for different segmentations and count correction methods: biological conservation and batch correction metrics from SCIB (higher is better) (b); number of cells (c); median number of genes (d); strength of T cell contamination by malignant cells (e). Assessed by the number of malignant marker genes (with N = 20 markers) found in the top 20 ranks. f, Cosine similarity of Xenium with Chromium snRNA-seq T cell pseudo-bulk profiles. g, GSEA showing T cell exhaustion signatures near malignant cells before and after SPLIT correction.

## Panel-by-Panel 解读

### Panel a — UMAP比较
**结论**：SPLIT校正后，细胞类型分离显著改善，尤其在5K panel和ProSeg分割条件下。

**关键数据**：
- SPLIT后细胞类型cluster更紧凑、分离更好
- 两种分割方法均有效

### Panel b — SCIB生物Conservation和批次校正指标
**结论**：SPLIT在生物conservation上表现最佳，不引入额外批次效应；ResolVI在某些情况下降低iLISI。

**关键数据**：
- SPLIT: 最高生物conservation
- ResolVI: 有时降低批次混合度

### Panel c — 细胞数保留
**结论**：ResolVI和ovrlpy显著减少细胞数（低表达细胞被过滤），SPLIT保留更多细胞。

**关键数据**：
- Ovrlpy 0.5/0.7: 细胞数大幅减少
- SPLIT: 保留大部分细胞

### Panel d — 中位基因数
**结论**：校正方法减少污染后，剩余细胞表达更多基因，表明数据纯度提高。

**关键数据**：
- SPLIT校正后基因数增加
- Ovrlpy/ResolVI后细胞减少但基因数可能升高

### Panel e — T细胞污染强度
**结论**：所有校正方法减少T细胞中的恶性标记基因；SPLIT效果最佳，ProSeg+SPLIT组合最优。

**关键数据**：
- Top 20中恶性标记数：Raw > Ovrlpy > ResolVI > SPLIT

### Panel f — 与Chromium参考的余弦相似度
**结论**：SPLIT产生与Chromium snRNA-seq最相似的T细胞表达谱，验证生物学保真度。

**关键数据**：
- SPLIT: 最高余弦相似度
- Raw数据相似度较低

### Panel g — GSEA富集分析
**结论**：SPLIT校正后，邻近恶性细胞的T细胞显示显著耗竭特征（HAVCR2, CTLA4, PDCD1, LAG3, CXCL13），而Raw数据未能检测到。

**关键数据**：
- Canonical T cell markers: 高富集
- Exhausted T cell: SPLIT后显著富集

## 总体结论
Fig. 4全面验证了SPLIT的优越性：最佳细胞类型分离、最高生物学保真度、完整保留细胞数，并揭示了T细胞耗竭特征。

## 关联 Figures / Extended Data
- ED Fig. 9 — 乳腺癌panel的验证结果
- ED Fig. 10 — Top预测基因详细列表
