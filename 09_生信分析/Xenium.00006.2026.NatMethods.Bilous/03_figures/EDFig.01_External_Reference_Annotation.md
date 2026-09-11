# ED Fig. 1 — Annotation of Xenium Data Using External References

## Caption（原文）
> Extended Data Fig. 1 | Annotation of Xenium data using external references. a, Cell-type composition for all Xenium samples using external references, grouped by donor and colored by cell type. The side color bar indicates the panel. b, Adjusted Rand Index (ARI) comparing RCTD annotations from matched vs. external references. Color indicates the panel; * denotes samples where tumor cells were not detected. c, Confusion matrix comparing cell-type annotations from external (rows) and matched (columns) reference data. d, UMAPs of all cells grouped by panel, colored by RCTD-assigned cell types using external Chromium data.

## Panel-by-Panel 解读

### Panel a — 外部参考的细胞类型组成
**结论**：使用外部参考进行注释时，细胞类型组成与使用匹配参考大体一致。

**关键数据**：各donor的细胞类型分布

### Panel b — ARI比较
**结论**：匹配与外部参考的注释整体一致，恶性细胞注释更具挑战性。

**关键数据**：
- 大部分样本ARI > 0.7
- 部分样本恶性细胞未检测到（*标记）

### Panel c — 混淆矩阵
**结论**：外部和匹配参考的注释高度一致，主要差异在恶性细胞的患者特异性亚型。

**关键数据**：对角线高值表示一致

### Panel d — UMAP可视化
**结论**：使用外部参考时，细胞类型分布与匹配参考相似。

**关键数据**：各panel的UMAP cluster结构一致

## 总体结论
ED Fig. 1证明RCTD使用外部参考也具有良好的注释一致性，为缺乏匹配样本的研究提供参考。

## 关联 Figures / Extended Data
- **Fig. 1c** — 匹配参考的细胞类型组成
