# ED Fig. 7 — Extended Exploration of SVF Identification

## Caption（原文）
> Extended Data Fig. 7 | Extended exploration of the SVF identification. a. Running time of the different algorithms used to identify SVFs. The running times depending on the number of cells used as an input are shown as a line plot (left), together with a bar plot representing the processing times of different algorithms when using 5.000 cells (middle) and the predicted running times for each algorithm when using a full dataset (~150.000 cells) (right). b. Spatial map of the manually annotated domains identified in the mouse brain section (ROI2) (replicate 1, left) and the domains identified by different algorithms. c. Ranked performance of different algorithms in identifying tissue domains in mouse brain sections (ROI 2), using the manually segmented domains as a reference. Four metrics are used: Adjusted Rand index (ARI), variability index (VI), NMI and Fowlkes-Mallows Index (FMI). Different numbers of domains are predicted, based on the number of domains included in the hierarchical annotation of the tissue done manually.

## Panel-by-Panel 解读

### Panel a — Running Time Comparison
**结论**：不同 SVF 识别算法的运行时间比较
**关键数据**：
- 算法：Giotto kmeans, Giotto rank, Seurat, HOTSPOT, SOMDE, SINFONIA, spatialDE, hvg, Squidpy MoranI, Squidpy GearyC
- 运行时间范围：12秒 (hvg) 到 132天 (Seurat)
- 预测 150,000 cells 的运行时间

### Panel b — Spatial Domain Visualization
**结论**：手动注释的 domain 与不同算法预测的 domain 空间分布比较
**关键数据**：mouse brain ROI2，replicate 1

### Panel c — Performance Ranking
**结论**：不同算法在识别组织 domain 方面的性能排名
**关键数据**：
- 评估指标：ARI, NMI, FMI, VI
- 预测 domain 数量：5, 6, 10, 14, 16
- 算法：BANKSY, SPACEL, STAGATE, SpaGCN, deepST, NNGE, SILT, Baysor, Giotto, Seurat

## 总体结论
Extended Data Fig. 7 提供了空间可变特征（SVF）识别算法的系统性评估，包括运行时间和性能两个维度。研究发现不同算法在准确性和计算效率方面存在显著权衡，为选择合适的 SVF 识别方法提供了依据。

## 关联 Figures / Extended Data
- **ED Fig. 4** — 平台比较
- **ED Fig. 5** — 分割策略比较
- **ED Fig. 6** — 预处理流程分析
- **Fig. 4** — 预处理流程优化
