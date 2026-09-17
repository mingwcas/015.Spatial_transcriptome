# Fig. 4 — Stereo-seq V2 is capable of profiling clinical FFPE samples

## Caption（原文）
> (A) RNA quality determined by the Bioanalyzer 2100, cDNA yields, and H&E staining for 10 TNBC samples. Binsize = 200.
> (B and C) Bar plots showing the statistical analysis of the median gene count per spot and cDNA yield in the Stereo-seq V2 data across 10 TNBC samples of different DV200 values (B) and storage time (C). Data are represented as mean ± 95% CI, and the p value was calculated using t test.
> (D) Regression plot showing the correlation between cDNA yield and mean UMI count per spot across 10 TNBC samples. R represents the Pearson correlation coefficient.
> (E) Bioanalyzer 2100 result of sample T202301978. FU, fluorescent unit.
> (F) H&E staining of sample T202301978.
> (G) Spatial visualization of marker genes detected by Stereo-seq V2 on T202301978.
> (H) Left: specific histological architectures identified by H&E staining. Right: the expression of the concordant spatial marker genes in Stereo-seq V2 data.
> (I) Genome-wide copy-number alterations (CNAs) detected by inferCNV algorithm. The color bar indicates loss (blue) and gain (red) of CNAs at relative genome regions.
> (J) Spatial distribution of tumor subtypes according to the different CNAs.
> (K) Illustration of the genome region that detected significant CNA gains on tumor subtype 2 and genes located in this region.
> (L) Spatial visualization of SYNE1 and SASH1 expression in the Stereo-seq V2 data of T202301978.
> (M) Heatmap showing the relative expression of genes located within chromosome 6 q24.3–q25.3 in tumor and normal regions on T202301978.
> See also Figure S4.

## Panel-by-Panel 解读

### Panel A — Sample Quality Overview
**结论**：10个TNBC样本的DV200范围为18-76，RNA降解程度差异大，V2均能成功分析。

**关键数据**：DV200 = 18-76；保存时间约9年至<1年。

### Panel B and C — DV200 Impact
**结论**：DV200对基因捕获效率无显著影响，cDNA产量是关键因素。

**关键数据**：不同DV200组间基因数无显著差异(p > 0.05)。

### Panel D — cDNA Yield Correlation
**结论**：cDNA产量与UMI计数强正相关，是样本质量的关键指标。

**关键数据**：Pearson R 高。

### Panel E-H — Sample T202301978
**结论**：低DV200(18)样本通过高cDNA产量仍可获得高质量数据。

**关键数据**：DV200=18，但cDNA产量16.85 ng/mm²；KRT5、KRT6A、MKI67等标记基因空间分布清晰。

### Panel I-M — CNV Analysis
**结论**：inferCNV识别出两种肿瘤亚型，亚型2在ESR1基因座区域存在拷贝数扩增。

**关键数据**：6q24-q25区域基因(SYNE1、SASH1)在肿瘤亚型2中显著扩增。

## 总体结论
Stereo-seq V2对临床FFPE样本具有极高的耐受性，即使RNA严重降解(DV200=18)仍可获得高质量空间转录组数据。

## 关联 Figures / Extended Data
- ED Fig. S4 (Additional TNBC sample analysis)
