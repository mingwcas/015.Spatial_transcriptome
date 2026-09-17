# Fig. 4 — Preprocessing Workflow Optimization

## Caption（原文）
> Assessment of preprocessing workflows for Xenium data. Different combinations of normalization, feature selection, dimensionality reduction, and clustering methods were systematically evaluated. The optimal workflow was identified based on ARI between derived clusters and ground truth cell type labels.

## Panel-by-Panel 解读

### Panel a — Workflow Overview
**结论**：展示预处理流程的各个步骤及其可选参数
**关键数据**：涵盖标准化、特征选择、降维、聚类等步骤

### Panel b — ARI Comparison Across Workflows
**结论**：不同预处理流程与地面真值的一致性比较
**关键数据**：ARI值排序，最优流程位于底部

### Panel c — Sensitivity Analysis (ARI)
**结论**：各预处理参数对最终聚类结果的影响程度
**关键数据**：修改单个参数导致ARI下降的程度

### Panel d — Sensitivity Analysis (FMI)
**结论**：使用FMI指标的补充敏感性分析
**关键数据**：低FMI表示参数修改影响较大

### Panel e — Sensitivity Analysis (VI)
**结论**：使用VI指标的补充敏感性分析
**关键数据**：高VI表示聚类结果差异显著

## 总体结论
本图建立了Xenium数据的标准化预处理流程，通过系统评估确定了最优参数组合，并量化了各步骤对最终细胞类型鉴定结果的影响，为Xenium数据分析提供了最佳实践指南。

## 关联 Figures / Extended Data
- Extended Data Fig. 6 — 扩展预处理分析
