# Fig. 3 — Cell Segmentation Strategies Comparison

## Caption（原文）
> Comparison of different segmentation strategies applied to Xenium data. Multiple algorithms including Cellpose (nuclei and cyto models), binning, clustermap, watershed, Mesmer, and Baysor were evaluated. Segmentation quality was assessed using negative marker purity and number of reads assigned. Different hyperparameters and expansion distances were tested in a grid search of 315 configurations.

## Panel-by-Panel 解读

### Panel a — Segmentation Strategy Overview
**结论**：展示不同分割策略的算法原理和输出差异
**关键数据**：涵盖7+种分割方法

### Panel b — ROI Visualization
**结论**：不同分割策略在相同区域的细胞边界识别结果对比
**关键数据**：ROI大小 160×160 μm

### Panel c — Segmentation Metrics Heatmap
**结论**：综合评估各分割策略的多个质量指标
**关键数据**：315种配置 → 52 top performers

### Panel d — ARI Between Strategies
**结论**：不同分割策略之间的一致性分析
**关键数据**：ARI值用于衡量策略间相似性

### Panel e — Reads Assigned vs NCP
**结论**：转录本分配数量与负标记物纯度的权衡关系
**关键数据**：最优策略在两者间取得平衡

## 总体结论
本图系统比较了多种细胞分割算法在Xenium数据上的表现，揭示了不同策略在转录本分配准确性和细胞边界识别上的差异，为用户选择最优分割方案提供了量化依据。

## 关联 Figures / Extended Data
- Extended Data Fig. 5 — 扩展分割基准测试
