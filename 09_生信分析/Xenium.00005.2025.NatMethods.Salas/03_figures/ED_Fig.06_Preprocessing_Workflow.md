# ED Fig. 6 — Extended Analysis on Preprocessing

## Caption（原文）
> Extended Data Fig. 6 | Extended analysis on preprocessing. a. Workflow of the different preprocessing steps and parameters considered in the assessment of the best preprocessing workflow. b. Heat map representing the Adjusted Rand Index (ARI) between the clusters derived from the different preprocessing workflows and the ground truth cell type labels. Preprocessing workflows are sorted from best (bottom) to worst (top) based on their median ARI. Datasets are also sorted based on their median ARI, indicating in which datasets it was possible to recover the original cell type labels better (right) and in which ones it was more difficult to achieve (left). A summary of the processing setups is summarized on the left part of the panel, with every row representing a specific step in the preprocessing workflow and every color representing the specific hyperparameter/ algorithm chosen. In addition, specific characteristics of the simulated datasets are included on the top part of the panel in the form of dot plot. c. Heat map representing the mean Adjusted Rand Index (ARI) between the clusters obtained when applying the most optimal preprocessing workflow (identified in Fig. 4c) to different Xenium datasets and the clusters obtained with the same workflow, but modifying different preprocessing steps, specified in the x-axis, in the different Xenium datasets (y-axis). A reduced ARI signifies decreased similarity between clustering outputs, highlighting a more pronounced impact on the workflow when altering a specific parameter. d. Same as C, but using Fowlkes-Mallows Index (FMI) to measure the similarity between the clustering outputs. A low FMI indicates differences between the clustering outputs, suggesting a more pronounced impact on the workflow when altering a specific parameter. e. Same as C, but using the variability index (VI) to measure the similarity between the clustering outputs. A high VI indicates important differences between the clustering outputs, suggesting a more pronounced impact on the workflow when altering a specific parameter.

## Panel-by-Panel 解读

### Panel a — Preprocessing Workflow
**结论**：展示了预处理流程的不同步骤和参数，包括 HVG 选择、归一化、对数转换、缩放、PCA、KNN 和聚类
**关键数据**：
- HVG: Yes/No
- Normalization: Library-size based (target sum 10, 100, 1000), SCTransform, None
- Log transformation: Yes/No
- Scaling: Yes/No
- PCs: 10, 20, 30, all
- KNN: 10, 12, 16, 30, 50
- Clustering: Leiden SLM, Louvain

### Panel b — ARI Heat Map
**结论**：不同预处理流程产生的聚类与真实细胞类型标签的 ARI 比较
**关键数据**：
- 数据集：h_breast_1, h_breast_ilc, alzheimers, human_spinal_chord, mouse_realmouse, ms_brain 等
- 25 个不同的 Xenium 数据集
- Workflows 按 median ARI 排序

### Panel c — ARI Sensitivity Analysis
**结论**：最优预处理流程中各步骤改变对聚类结果的影响（ARI）
**关键数据**：减少的 ARI 表示更大的影响

### Panel d — FMI Sensitivity Analysis
**结论**：最优预处理流程中各步骤改变对聚类结果的影响（FMI）
**关键数据**：低 FMI 表示更大影响

### Panel e — VI Sensitivity Analysis
**结论**：最优预处理流程中各步骤改变对聚类结果的影响（VI）
**关键数据**：高 VI 表示更大差异

## 总体结论
Extended Data Fig. 6 系统性地评估了预处理流程中各参数的影响，确定了最佳预处理工作流程，为 Xenium 数据的标准化分析提供了重要参考。关键发现包括归一化方法、HVG 选择和聚类算法对最终结果的重要影响。

## 关联 Figures / Extended Data
- **ED Fig. 4** — 平台比较
- **ED Fig. 5** — 分割策略比较
- **Fig. 4** — 预处理流程优化
- **ED Fig. 7** — SVF 识别算法
