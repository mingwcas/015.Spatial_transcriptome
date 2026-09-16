# Fig. 5 — Computational workflow

## Caption（原文）
> Fig. 5 | Overview of the computational steps for Spatial Transcriptomics. a, FASTQ files are merged, quality trimming is performed, reads are aligned to the genome, gene counting is done, spatial-barcode demultiplexing and UMI filtering remove amplification duplicates; output is a unique-gene-count matrix per spatial spot. b, image alignment and spatial spot/tissue detection use bright-field tissue and fluorescence spot images, outputting adjusted coordinates and an alignment matrix. c, outputs are visualized/analyzed in ST Viewer, or R/Python for more customizable analysis.

## Panel-by-Panel 解读
### Panel a — 测序数据处理
**结论**：FASTQ被转为去UMI重复的spot×gene计数矩阵。
**关键数据**：输出包含TSV矩阵、BED分子位置和log（Methods Step 156）。
### Panel b — 图像配准与检测
**结论**：明场图和荧光spot图共同确定组织下spot坐标。
**关键数据**：输出调整坐标和3×3 affine alignment matrix。
### Panel c — 可视化分析
**结论**：矩阵、坐标和形态图可在ST Viewer、R或Python中联合分析。
**关键数据**：Viewer支持Linux、Mac和Windows；R/Python更可定制。

## 总体结论
ST Pipeline和ST Spot Detector分别解决分子计数与空间定位，二者输出通过坐标整合为可解释的空间转录组数据。

## 关联 Figures / Extended Data
- Fig. 1：实验输入；Fig. 7：输出质量分布。
