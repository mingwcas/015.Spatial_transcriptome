# Extended Data Fig. 6 — Extended Analysis on Preprocessing

## Caption（原文）
> Extended analysis on preprocessing. a. Workflow of the different preprocessing steps and parameters. b. Heat map representing the ARI between clusters derived from different preprocessing workflows and ground truth cell type labels. c. Heat map representing the mean ARI when modifying different preprocessing steps. d. Same as C, but using FMI. e. Same as C, but using VI.

## Panel-by-Panel 解读

### Panel a — Workflow Diagram
**结论**：预处理流程各步骤及可选参数的详细图示
**关键数据**：每行代表一个步骤，每种颜色代表一个参数选择

### Panel b — ARI Heatmap
**结论**：不同预处理工作流与地面真值的一致性排序
**关键数据**：工作流从最优（底部）到最差（顶部）排序

### Panel c — Sensitivity Analysis (ARI)
**结论**：修改各预处理参数对ARI的影响
**关键数据**：ARI下降程度反映参数重要性

### Panel d — Sensitivity Analysis (FMI)
**结论**：修改各预处理参数对FMI的影响
**关键数据**：低FMI表示参数影响大

### Panel e — Sensitivity Analysis (VI)
**结论**：修改各预处理参数对VI的影响
**关键数据**：高VI表示聚类差异显著

## 总体结论
本图提供了预处理优化的扩展分析，详细展示了各参数的敏感性，帮助用户理解哪些步骤对最终结果影响最大，从而进行针对性优化。

## 关联 Figures / Extended Data
- Fig. 4 — 主要预处理优化结果
