# ED Fig. 2 — Biological Conservation and Batch Integration Scores

## Caption（原文）
> Extended Data Fig. 2 | Biological conservation and batch integration scores. a, Default data, including all Xenium datasets processed with default segmentations and Chromium datasets processed with the standard pipeline. Corresponding UMAPs are shown in Fig. 1d. b, NSCLC datasets restricted to the 194 genes shared between 5K and Lung panels. For Xenium data, samples from six shared donors are included; for Chromium, all NSCLC samples are used. Corresponding UMAPs are shown in Fig. 2a. c, Chromium data restricted to the genes present in the Xenium panel. Corresponding UMAPs are shown in Extended Data Fig. 3h. d, Xenium data processed using nuclear segmentation. Color represents the goodness score.

## Panel-by-Panel 解读

### Panel a — 默认数据分析
**结论**：所有Xenium数据集显示高生物conservation和低批次效应。

**关键数据**：
- iLISI评分高
- Silhouette Batch评分高

### Panel b — 194共有基因分析
**结论**：在共有基因限制下，Xenium和Chromium仍保持良好细胞类型分离。

**关键数据**：
- Calinski-Harabasz评分维持
- Davies-Bouldin评分可接受

### Panel c — Chromium基因限制分析
**结论**：Chromium数据即使限制在Xenium panel基因集内，仍能达到清晰细胞类型分离。

**关键数据**：证明Xenium的细胞类型分离受限不是基因数量问题

### Panel d — 核分割数据质量
**结论**：核分割处理的数据质量评分良好。

**关键数据**：Goodness score深色表示高评分

## 总体结论
ED Fig. 2展示Xenium数据在多种条件下的批次效应和生物conservation表现，证实数据质量可靠。

## 关联 Figures / Extended Data
- **Fig. 1d** — 对应UMAP
- **Fig. 2a** — 194基因UMAP
