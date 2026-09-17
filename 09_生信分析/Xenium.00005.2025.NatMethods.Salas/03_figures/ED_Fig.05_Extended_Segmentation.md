# Extended Data Fig. 5 — Extended Benchmarking of Segmentation Strategies

## Caption（原文）
> Extended benchmarking of segmentation strategies. a. Localization of regions of interest. b. Regions of interest representing the cells identified using different segmentation algorithms. c. Heat map representing the segmentation metrics of all segmentation strategies. d. Adjusted rand index (ARI) between the different outputs produced by combinations of segmentation algorithms, hyperparameters and expansions. e. Scatter plot representing the number of reads assigned and the negative marker purity of different assessed segmentation strategies.

## Panel-by-Panel 解读

### Panel a — ROI Localization
**结论**：展示评估区域在组织切片中的位置
**关键数据**：ROI位置标注

### Panel b — Segmentation Outputs
**结论**：不同分割算法在相同ROI的细胞识别结果
**关键数据**：160×160 μm ROI，DAPI背景+彩色细胞mask

### Panel c — Segmentation Metrics Heatmap
**结论**：所有分割策略的综合质量指标热图
**关键数据**：多维度评估指标

### Panel d — ARI Between Strategies
**结论**：不同分割配置间的ARI一致性分析
**关键数据**：315配置 → 52 top performers

### Panel e — Reads vs NCP Scatter
**结论**：转录本分配量与标记物纯度的权衡
**关键数据**：各策略名称和颜色标注

## 总体结论
本图为Fig. 3的扩展版本，提供了更详细的分割策略基准测试结果，包括ROI定位、可视化比较和315种配置的全面评估。

## 关联 Figures / Extended Data
- Fig. 3 — 主要分割策略比较
