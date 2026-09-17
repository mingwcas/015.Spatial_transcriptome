# Extended Data Fig. 4 — Comparison of Xenium with SRT Platforms

## Caption（原文）
> Comparison of Xenium with SRT platforms. a. Spatial map of SRT datasets, colored by region. The scRNA-seq dataset is represented as a UMAP colored by region of origin. b. Stacked bar plot representing the percentage of transcripts assigned to cells in each datasets after Cellpose. c. SRT/scRNA-seq gene efficiency ratios of different SRT methods in the hippocampal (left) and thalamic (right) regions. d. Box plot representing the negative coexpression purity (NCP) of each SRT method, including only genes with an efficiency ratio below 1. e. Pairwise comparison of the detection efficiency between each SRT and scRNA-seq dataset in the cortical region. f. Density plots illustrate the cumulative proportion of reads depending on their distance from the centroid for individual genes across technologies. g. Regions of interest corresponding to resegmented datasets across platforms.

## Panel-by-Panel 解读

### Panel a — Spatial Maps
**结论**：展示各SRT数据集的空间分布和scRNA-seq的UMAP投影
**关键数据**：按脑区着色

### Panel b — Transcript Assignment
**结论**：Cellpose分割后各数据集转录本分配到细胞的比例
**关键数据**：堆叠条形图显示分配率差异

### Panel c — Gene Efficiency Ratios
**结论**：海马和丘脑区域各SRT方法相对于scRNA-seq的基因检测效率
**关键数据**：箱线图展示效率比分布

### Panel d — Negative Coexpression Purity
**结论**：各SRT方法的负共表达纯度比较
**关键数据**：仅包括效率比<1的基因

### Panel e — Pairwise Detection Efficiency
**结论**：各平台间基因检测效率的配对比较
**关键数据**：中位比值标注

### Panel f — Spatial Resolution
**结论**：各平台转录本到细胞质心的距离分布
**关键数据**：累积密度曲线

### Panel g — Resegmentation Results
**结论**：统一resegmentation后各平台的转录本分配
**关键数据**：DAPI背景+黄色转录本点

## 总体结论
本图系统比较了Xenium与其他主流空间转录组平台（MERFISH、Slide-seq、Visium等）在相同脑组织样本上的性能差异，揭示了各平台在灵敏度、空间分辨率和噪声水平上的特点。

## 关联 Figures / Extended Data
- Fig. 3 — 主要分割策略比较
