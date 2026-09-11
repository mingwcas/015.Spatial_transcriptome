# Fig. 2 — Evaluation of False Positives

## Caption（原文）
> Fig. 2 | Evaluation of false positives. a Spatial distribution of gene calls (left) and negative control calls (right) in COAD samples profiled by CosMx 6K and Xenium 5K. Color intensity indicates mean call count per probe in each 8 × 8 μm bin. b Total call counts and Moran's I for common genes (2552), platform-specific genes (3623 for CosMx 6K and 2449 for Xenium 5K), negative probes (NegProbe, 20 for CosMx 6K and 40 for Xenium 5K), and negative codes (NegCode, 324 for CosMx 6K and 609 for Xenium 5K) detected by CosMx 6K and Xenium 5K across the shared regions shown in (a). Each data point represents one target. Center lines indicate the median value, and lower and upper hinges represent the 25th and 75th percentiles, respectively. The whiskers denote 1.5× the interquartile range. c Histogram showing the log10-transformed signal proportions of individual negative probes and codes, pooled across COAD, HCC, and OV tissues. d H&E staining and transcript distribution inside and outside COAD tissue regions. Red dashed line outlines the Stereo-seq v1.3 region used for diffusion analysis; solid lines mark extra-tissue regions with high transcript levels. Color intensity indicates mean-normalized transcript count of each 8 × 8 μm bin. Scale bars, 1 mm. e Evaluation of transcript diffusion in COAD. The x-axis and y-axis represent the mean-normalized transcript counts and the distance to tissue edge for bins outside the tissue, respectively. Color intensity indicates the number of bins. f Ratio of the mean transcript count in extra-tissue bins to that in intra-tissue bins. Hollow circles indicate the ratio calculated for each of the three cancer types (n = 3). Data are presented as mean values +/−SEM.

## Panel-by-Panel 解读

### Panel a — Spatial Distribution of Gene vs Negative Control Calls
**结论**：CosMx 6K在负对照中表现出更强的空间聚集和背景干扰，而Xenium 5K在负对照区域信号更低，空间变异性更小。
**关键数据**：8 × 8 μm bin水平每个探针的平均call计数（颜色强度）

### Panel b — Total Call Counts and Moran's I
**结论**：CosMx 6K检测到更多的总calls，但表现出更强的负对照信号空间自相关（Moran’s I），表明背景干扰更显著。
**关键数据**：
- 共有基因（Common genes）: 2,552个
- CosMx 6K特有基因: 3,623个
- Xenium 5K特有基因: 2,449个
- CosMx 6K负探针（NegProbe）: 20个
- Xenium 5K负探针: 40个
- CosMx 6K负码（NegCode）: 324个
- Xenium 5K负码: 609个

### Panel c — Negative Control Signal Proportions
**结论**：归一化后，Xenium 5K表现出更低的负对照信号比例。且两个平台中负探针信号均强于负码，提示非特异性探针结合是iST平台背景噪声的主要来源。
**关键数据**：Log10转换的负对照信号比例（合并COAD、HCC、OV组织数据）

### Panel d — Transcript Diffusion Beyond Tissue Boundary
**结论**：在Stereo-seq v1.3和Visium HD FFPE中均观察到组织边界外的转录本扩散现象。
**关键数据**：H&E染色和转录本分布（组织内外），红色虚线标注Stereo-seq v1.3扩散分析区域，标尺1 mm

### Panel e — Diffusion Distance vs Normalized Transcript Count
**结论**：转录本扩散随距离增加而减少，但Stereo-seq v1.3在组织外bins中仍保持较高的标准化转录本计数。
**关键数据**：x轴=标准化转录本计数，y轴=到组织边缘的距离（μm），颜色强度=bin数量

### Panel f — Diffusion Level Comparison
**结论**：Stereo-seq v1.3的扩散水平（3.4×）显著高于Visium HD FFPE，表明Visium HD FFPE具有更有效的扩散控制。
**关键数据**：组织外bins平均转录本/组织内bins平均转录本的比值（n=3癌症类型），Stereo-seq v1.3比值约为3.4

## 总体结论
Fig. 2全面评估了四种ST平台的假阳性风险。iST平台中，Xenium 5K在背景噪声控制方面显著优于CosMx 6K。对于sST平台，Stereo-seq v1.3表现出约3.4倍于Visium HD FFPE的转录本扩散，提示样本固定和通透化条件对空间定量准确性有重要影响。

## 关联 Figures / Extended Data
- **Supplementary Fig. 5a-e** — iST平台背景噪声详细分析
- **Supplementary Fig. 5f-h** — Stereo-seq v1.3和Visium HD FFPE扩散详细分析
