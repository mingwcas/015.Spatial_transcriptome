# Fig. 5 — Spatial 3D genome and epigenome co-profiling of GBM sample

## Caption（原文）
> a, H&E staining of tissue sample NU03747 from a patient with GBM. Region selected for the spatial experiment is highlighted in the black square box. b, Copy number profiles inferred from pseudobulk spatial Hi-C data in GBM sample (top). The copy number gains in chr7 and chr12 are highlighted in red circle. Heatmap (bottom) shows copy numbers in each pixel. c, Spatial distribution of clusters based on copy numbers inferred from spatial Hi-C data. d, Pseudobulk Hi-C map of GBM patient sample NU03747 at a genome-wide scale. e,f, Pseudobulk Hi-C map (top) and the copy number difference between C0 and C1 (bottom) of sample NU03747 from a patient with GBM highlighted (in d) high copy number regions on chr7 (e) and chr12 (f). g, Pseudobulk Hi-C map at EGFR region (top) and heatmap of copy number ratio in each pixel (bottom). h, Spatial distribution (top) and violin plot (bottom) of copy number ratio for EGFR, MDM2 and CDK4 in NU03747. The number of pixels in cluster C0 and C1 are shown in the figure. i, Pseudobulk Hi-C maps (left) and gene activity scores for RNFT2 (right) for different clusters at genomic region chr12: 113,500,000–117,500,000. The number of pixels in cluster C0 and C1 are shown in the figure. j, APA plots for cluster-specific chromatin loops in NU03747. k, GO term enrichment of genes associated with cluster-specific loops in j. The enrichment significance was assessed using Fisher's exact test. Box plots overlaid on violin plots in h and i show the median (center line), the 25th and 75th percentiles (box limits) and whiskers extending to the most extreme data points within 1.5 × IQR of the lower and upper quartiles. Outliers beyond the whiskers are not shown. Statistical significance in h and i was assessed using a two-sided Wilcoxon rank-sum test. P values are shown in the figures.

## Panel-by-Panel 解读

### Panel a — GBM样本H&E染色
**结论**：展示了GBM患者NU03747组织样本的H&E染色图像，以及选定进行空间实验的区域。

**关键数据**：黑色方框标记的空间实验区域。

### Panel b — 拷贝数谱
**结论**：展示了从伪批量空间Hi-C数据推断的GBM样本拷贝数谱，包括chr7和chr12的拷贝数增加。

**关键数据**：已知的GBM基因组改变，包括chr7增益和chr10丢失，以及chr7和chr12上的两个显著局灶性扩增。

### Panel c — 基于拷贝数的聚类空间分布
**结论**：基于拷贝数谱识别出的三个聚类显示出明确的空间分离模式。

**关键数据**：C0和C1聚类显示出清晰的空间分离。

### Panel d — 全基因组Hi-C图谱
**结论**：展示了GBM患者样本NU03747的全基因组伪批量Hi-C图谱。

**关键数据**：chr7和chr12上显示出与全基因组其他区域相互作用的条带状模式，表明高拷贝数。

### Panel e — chr7局灶性扩增
**结论**：展示了chr7上EGFR基因区域的局灶性扩增，C0和C1聚类间存在拷贝数差异。

**关键数据**：EGFR扩增区域包含约80–100个拷贝，C1聚类显示更高的EGFR拷贝数。

### Panel f — chr12局灶性扩增
**结论**：展示了chr12上MDM2和CDK4基因区域的局灶性扩增，C0和C1聚类间存在拷贝数差异。

**关键数据**：C0聚类在CDK4区域显示更高的拷贝数，而C1在MDM2区域显示更高的拷贝数。

### Panel g — EGFR区域单像素拷贝数
**结论**：展示了EGFR扩增区域的单像素分辨率拷贝数分布，揭示了肿瘤异质性。

**关键数据**：高拷贝数像素主要富集在C1聚类中。

### Panel h — EGFR、MDM2、CDK4空间分布和统计
**结论**：展示了三个癌基因的拷贝数比值空间分布和统计比较，证明了肿瘤克隆间的差异。

**关键数据**：EGFR（P < 2.2 × 10−16）、MDM2（P < 2.2 × 10−16）和CDK4（P < 2.2 × 10−16）在C0和C1间存在显著差异。

### Panel i — RNFT2基因区域的3D基因组和基因活性
**结论**：展示了不同聚类在RNFT2基因区域的染色质相互作用和基因活性评分差异。

**关键数据**：C0聚类显示出更高的RNFT2基因活性评分（P < 2.2 × 10−16）。

### Panel j — 聚类特异性染色质环APA分析
**结论**：鉴定了C0和C1聚类特异性的染色质环。

**关键数据**：440个C0特异性环和516个C1特异性环。

### Panel k — 聚类特异性环的GO富集
**结论**：C0和C1特异性环关联的基因显示出不同的功能富集模式。

**关键数据**：C0特异性环富集于自然杀伤细胞介导的免疫和白细胞介导的细胞毒性通路；C1特异性环富集于Wnt信号通路。

## 总体结论
Fig. 5展示了Spatial-ATAC-Hi-C在GBM样本中的临床应用潜力。通过空间分辨的3D基因组和表观基因组共分析，揭示了GBM的复杂基因组改变和肿瘤异质性。技术检测到已知的GBM基因组改变（chr7增益、chr10丢失、EGFR/MDM2/CDK4扩增），并揭示了不同肿瘤克隆间的拷贝数差异和染色质环差异。EGFR、CDK4和MDM2扩增可能是肿瘤异质性的强特征和标记。条带状模式提示这些扩增区域可能位于染色体外DNA（ecDNA）上。

## 关联 Figures / Extended Data
- Supplementary Fig. 3（基于表观遗传特征的聚类分析）
- Supplementary Fig. 4（另一个GBM样本NU03766的验证分析）
- Supplementary Table 10（EagleC软件识别的SV事件）
