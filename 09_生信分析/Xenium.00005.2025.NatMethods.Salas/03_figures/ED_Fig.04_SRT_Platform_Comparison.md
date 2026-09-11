# ED Fig. 4 — Comparison of Xenium with SRT Platforms

## Caption（原文）
> Extended Data Fig. 4| Comparison of Xenium with SRT platforms. a. Spatial map of SRT datasets, colored by region. The scRNA-seq dataset is represented as a UMAP colored by region of origin. b. Stacked bar plot representing the percentage of transcripts assigned to cells in each datasets after Cellpose. c. SRT/scRNA-seq gene efficiency ratios of different SRT methods in the hippocampal (left) and thalamic (right) regions. Boxplots represent the distribution of the efficiencies, divided in quartiles, where the central line represents the median efficiency. Gene ratios are represented as individual dots. d. Box plot representing the negative coexpression purity (NCP) of each SRT method, including only genes with an efficiency ratio below 1. Boxplots represent the distribution of the NCP scores, divided in quartiles, where the central line represents the median NCP. NCP scores are represented as individual dots for each method. e. Pairwise comparison of the detection efficiency between each SRT and scRNA-seq dataset in the cortical region. For each pair, a scatter plot of the number of transcripts detected per gene in SRT method 1 (y-axis) and SRT method 2 (x-axis) is included. Only common genes are included in the comparison. Red line represents x=y. The median of ratios for each pair of methods is included (bottom, right). Spots of each subplot are colored by the method that presented a higher median in each comparison. f. Density plots illustrate the cumulative proportion of reads depending on their distance from the centroid for individual genes across technologies. Values indicate the proportions of reads that are found at distances greater than or equal to the specified distance. g. Regions of interest corresponding to resegmented datasets across platforms. DAPI staining is shown as a background and reads assigned to resegmented cells are overlaid as yellow dots.

## Panel-by-Panel 解读

### Panel a — Spatial Map of SRT Datasets
**结论**：展示不同 SRT 平台数据集的空间分布，按脑区着色
**关键数据**：MERSCOPE, MERFISH, CosMx, Xenium, HS-ISS, Molecular Cartography 6个平台

### Panel b — Transcript Assignment Percentage
**结论**：Cellpose 分割后各平台转录本分配到细胞的比例
**关键数据**：堆叠柱状图显示分配率和未分配率

### Panel c — SRT/scRNA-seq Gene Efficiency Ratios
**结论**：不同 SRT 方法在海马区和丘脑区的基因检测效率与 scRNA-seq 的比值
**关键数据**：箱线图显示中位数和四分位数分布

### Panel d — Negative Coexpression Purity (NCP)
**结论**：各 SRT 方法的负共表达纯度，用于评估基因检测准确性
**关键数据**：NCP 分数分布，中位数

### Panel e — Pairwise Detection Efficiency Comparison
**结论**：两两平台间检测效率比较，识别各平台的相对优势
**关键数据**：散点图，x=y 红线，中位比值

### Panel f — Read Distance Distribution
**结论**：reads 到细胞质心的距离分布，反映检测精确性
**关键数据**：累积密度图

### Panel g — Resegmented Datasets ROI
**结论**：各平台重分割后的感兴趣区域，DAPI 背景 + 黄色转录本点
**关键数据**：DAPI 染色 + reads overlay

## 总体结论
Extended Data Fig. 4 系统性地比较了 Xenium 与其他五种主要 SRT 平台（MERSCOPE, MERFISH, CosMx, HS-ISS, Molecular Cartography）在检测效率、转录本分配和基因特异性方面的表现，为 Xenium 在空间转录组领域的定位提供了全面参考。

## 关联 Figures / Extended Data
- **ED Fig. 5** — 分割策略比较
- **ED Fig. 6** — 预处理流程分析
- **ED Fig. 7** — SVF 识别算法比较
