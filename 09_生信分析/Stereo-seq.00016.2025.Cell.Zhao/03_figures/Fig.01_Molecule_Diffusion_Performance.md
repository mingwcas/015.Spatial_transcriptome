# Fig. 1 — Stereo-seq V2 exhibits better molecule diffusion performance

## Caption（原文）
> (A) Workflow of Stereo-seq V2.
> (B and C) Scatterplot showing the gene expression correlations between Stereo-seq V1, V2, and MERFISH. Data from each technique were merged, normalized (UMI count per million UMIs), and log-transformed. R represents the Pearson correlation coefficient.
> (D) Spatial visualization of region-restricted genes Neurod6 and Cnp, and the fitted corresponding tissue boundary lines in Stereo-seq V1 and V2 data. Binsize = 50.
> (E) Line plot showing the mean expression of Neurod6, Cnp, Cpne7, Wipf3, and Hpca at different distances to the tissue boundary line. The line was smoothed using Numpy.convolve package.
> (F) Bar plot showing the left-width at half-maximum (LWHM) of expression intensity around the boundary line for Neurod6, Cnp, Cpne7, Wipf3, and Hpca. Data are represented as mean ± 95% confidence interval (CI). p value was calculated using pairwise t test.
> See also Figure S1.

## Panel-by-Panel 解读

### Panel A — Workflow
**结论**：Stereo-seq V2工作流程包含：FFPE样本处理（脱蜡、复水、去交联）、随机引物捕获、原位逆转录和连接、cDNA释放、PCR扩增、文库构建和测序。

**关键数据**：该流程实现了对FFPE样本的总RNA空间分析。

### Panel B and C — Correlation Analysis
**结论**：Stereo-seq V2与V1和MERFISH的基因表达高度相关（r² = 0.83），表明平台间一致性良好。

**关键数据**：Pearson相关系数R ≈ 0.83（V1 vs V2）；V2与MERFISH同样高度相关。

### Panel D — Spatial Visualization
**结论**：V2在组织边界处显示出更清晰的基因表达边界，分子扩散更少。

**关键数据**：Neurod6和Cnp在V2中边界更锐利。

### Panel E — Expression vs Distance
**结论**：V2的标记基因在边界处表达下降更快，表明扩散更少。

**关键数据**：V2曲线在边界处更陡峭。

### Panel F — LWHM Quantification
**结论**：V2的LWHM值显著低于V1，表明更好的空间分辨率。

**关键数据**：LWHM: V2 < V1，p < 0.05 (pairwise t test)。

## 总体结论
Stereo-seq V2通过改进的随机引物捕获策略，显著减少了分子扩散，提高了空间分辨率，使得组织边界处的基因表达更精确。

## 关联 Figures / Extended Data
- ED Fig. S1 (Quality control and spatial visualization of marker genes)
