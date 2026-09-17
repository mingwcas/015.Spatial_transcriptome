# Fig. 1 — Overview of Experimental Design and Data Processing Pipeline

## Caption（原文）
> Fig. 1 Overview of experimental design and data processing pipeline. a) The experimental design involved the use of reference tissues, namely, adult mouse hippocampus, E12.5 mouse eye, and adult mouse olfactory bulb. We performed sST on these reference tissues using diverse technologies categorized by their distinct spatial indexing strategies. These techniques encompassed microarray-based methods (e.g., 10X Genomics Visium), bead-based approaches (such as HDST, BMKMANU S1000 (abbreviation: BMK S1000), and Slide-seq), polonies or nanoballs techniques (Stereo-seq and PIXEL-Seq), and microfluidic-based methodologies like DBiT-seq. Additionally, the reference tissues were subjected to single-nuclei RNA-sequencing (snRNA-seq) using the 10X platform. The cadasSTre datasets underwent a series of processing steps. Initially, spatial barcodes, their corresponding locations, and expression profiles were generated. Subsequently, reads within regions with known morphology were selectively retained, and downsampling was performed to mitigate the impact of sequencing depth variations. Count matrices were then generated for sensitivity and diffusion calculations. This was followed by cell state annotation and a comprehensive analysis of cell-to-cell communication. b) The visualization of total counts across the spatial dimension for datasets generated using each platform for reference tissues is shown. The distances from center to center, used in creating the plot, are presented alongside the name of each sST method. The length of the black bar in the visualization corresponds to a distance of 500 microns.

## Panel-by-Panel 解读

### Panel 1a — Experimental Design Overview
**结论**：本研究设计了系统性的空间转录组技术比较框架，使用三种参考组织（成年鼠海马体、E12.5鼠眼球、成年鼠嗅球）和六种sST技术。

**关键数据**：
- 6种sST方法：Visium、HDST、BMKMANU S1000、Slide-seq、Stereo-seq、PIXEL-seq、DBiT-seq
- 3种参考组织类型
- 22个实验（6种技术 × 多种组织类型）

### Panel 1b — Total Counts Visualization
**结论**：不同平台在空间表达覆盖和总counts方面存在显著差异。

**关键数据**：
- Stereo-seq、Visium、BMKMANU S1000可覆盖几乎整个右侧脑组织和整个E12.5胚胎
- Slide-seq V2由于捕获面积有限，只能覆盖部分组织
- DBiT-seq的捕获大小取决于微流控通道宽度

## 总体结论
Fig. 1建立了本研究的核心框架：使用标准化参考组织和统一分析流程，对6种主流sST技术进行系统性的灵敏度、扩散控制和下游分析能力比较。

## 关联 Figures / Extended Data
- Supplementary Figure 1 — spot大小和中心距离比较
- Supplementary Figure 2-4 — H&E图像验证组织处理一致性
