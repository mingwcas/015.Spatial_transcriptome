# ED Fig. 5 — Extended Benchmarking of Segmentation Strategies

## Caption（原文）
> Extended Data Fig. 5 | Extended benchmarking of segmentation strategies. a. Localization of regions of interest represented in Extended Data Fig. 5b and Fig. 3c. b. Regions of interest representing the cells identified using different segmentation algorithms in a region of interest outlined in Extended Data 5B. DAPI background is represented as a background and individual isolated color-specific masks represent individual cells. Segmentation strategies were selected to represent different segmentation outputs, as described in Fig. 3c. Each ROI represents an area of 160 x 160 μm. c. Heat map representing the segmentation metrics of all segmentation strategies described in Fig. 3d. d. Adjusted rand index (ARI) between the different outputs produced by combinations of segmentation algorithms, hyperparameters and expansions when applied to human breast sections. Segmentation methods included Cellpose Proportion of assigned reads (CPn: nuclei, CPc: cyto models), binning (bins), clustermap (CM), watershed (WA), Mesmer, Baysor (BA) and Baysor with prior segmentation (Baysor Px.x). Xenium segmentation were also included in the comparison (XENIUM cel, XENIUM nuc). Hyperparameters for each method are described in methods. Methods on the y-axis were colored depending on the expansion performed after segmentation. 315 evaluated configurations of the grid search were reduced to the shown 52 top performers per hyperparameter group (highest negative marker purity). e. Scatter plot representing the number of reads assigned (x-axis) and the negative marker purity (y-axis) of different assessed segmentation strategies in human breast tumor samples. The name and color of each segmentation strategy are represented as in Fig. 3d.

## Panel-by-Panel 解读

### Panel a — ROI Localization
**结论**：展示 Extended Data Fig. 5b 和 Fig. 3c 中使用的感兴趣区域位置
**关键数据**：ROI 空间定位图

### Panel b — ROI Segmentation Comparison
**结论**：不同分割算法在相同 ROI 区域的分割结果可视化
**关键数据**：160×160 μm 区域，color-specific masks，DAPI 背景

### Panel c — Segmentation Metrics Heat Map
**结论**：所有分割策略的分割指标热图
**关键数据**：多种分割指标比较

### Panel d — ARI Comparison (Human Breast)
**结论**：人类乳腺癌样本上不同分割算法、超参数和膨胀组合的 ARI 比较
**关键数据**：
- Cellpose nuclei (CPn) 和 cyto (CPc) 模型
- Baysor with prior (Baysor Px.x)
- Xenium cell 和 nucleus
- Mesmer (r20, r30, r40)
- 315 种配置评估，52 种 top performers

### Panel e — Reads vs Negative Marker Purity
**结论**：分割策略的 reads 分配数量与负标记纯度的权衡
**关键数据**：散点图展示不同策略的平衡点

## 总体结论
Extended Data Fig. 5 提供了分割策略的系统性基准测试，比较了包括 Cellpose、Mesmer、Baysor、Watershed 和 Xenium 原生分割在内的多种方法，为 Xenium 数据分析中的分割策略选择提供了详细参考。

## 关联 Figures / Extended Data
- **ED Fig. 4** — 平台比较
- **Fig. 3** — 主要分割策略比较
- **ED Fig. 6** — 预处理流程分析
- **ED Fig. 7** — SVF 识别算法
