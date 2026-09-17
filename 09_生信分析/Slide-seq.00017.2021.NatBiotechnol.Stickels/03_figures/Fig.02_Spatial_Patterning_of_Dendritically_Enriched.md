# Fig. 2 — Slide-seqV2 reveals spatial patterning of dendritically enriched mRNAs

## Caption（原文）
> Fig. 2 | Slide-seqV2 reveals spatial patterning of dendritically enriched mRNAs. a, Spatial heat map of the number of UMIs for a hippocampal Slide-seqV2 dataset. b, Top, schematic of linear spatial profiling across CA1 soma and dendrites. Bottom, spatial profiles of a CA1 marker (Hpca, red) and a classically dendritically localized gene (Camk2a, blue). c, Differentially expressed genes in the soma versus proximal dendrites. Two-tailed, two-sample t-tests were performed (n = 5 tissue sections), and genes with a false discovery rate (FDR)-corrected P value of <0.05 and a fold change >2 are highlighted. Several classically known dendritically expressed genes are circled. Camk2a, FDR-adjusted P = 2.8 × 10−3, yellow; Ef1a, FDR-adjusted P = 5 × 10−4, green; Prkcz, FDR-adjusted P = 0.034, red; Map2, FDR-adjusted P = 1.7 × 10−4, teal; and Ddn, FDR-adjusted P = 2 × 10−5, purple. d, Expression heat map of 237 dendritically enriched RNAs across the neuronal profile axis. Genes are shown clustered by their spatial profile (k-means clustering, four clusters). Rows are normalized and summed to 1. e, Average spatial expression profile of each of the four gene clusters identified in d across the CA1. f, Slide-seqV2 reconstruction images of one synaptic protein-encoding gene from each of the four clusters in d. Scale bars, 500 μm for all Slide-seqV2 reconstructions. The color bar represents the total number of UMIs detected for a gene. g, Quantile–quantile plot of the log2 fold change (log2 FC) between CA1 and CA3/dentate pyramidal cell types (defined by scRNA-seq12) of dendritic (x axis) compared to somatic (y axis) gene sets defined by the analysis in c. h, Ratio of expression between CA3 and CA1 regions in the soma and dendrites for Slide-seqV2 data. Linear fit is shown in red (slope = 0.22, R2 = 0.13).

## Panel-by-Panel 解读

### Panel a — Spatial UMI heat map
**结论**: 展示了全 hippocampus 的 UMI 空间分布，SOMA层信号最强

**关键数据**: 
- n = 4 sections
- CA1 pyramidal layer 可见高密度信号

### Panel b — Linear spatial profiling
**结论**: Hpca (soma marker) 富集于 pyramidal layer，而 Camk2a (dendritic marker) 在 neuropil 区域信号最强

**关键数据**:
- Spatial profile 从 stratum oriens → stratum pyramidale → stratum radiatum
- 1D profile 可视化基因空间分布

### Panel c — Differential expression soma vs dendrites
**结论**: 鉴定出 213 个显著 dendritically enriched genes (FC>2, q<0.05)

**关键数据**:
- n = 5 tissue sections
- 经典 dendritic genes: Camk2a, Map2, Ddn, Ef1a, Prkcz 均被检出
- P < 10^-16 与 previous studies 重叠

### Panel d — Expression heat map with clustering
**结论**: 237 个 dendritic genes 可分为 4 个空间表达 cluster

**关键数据**:
- k-means clustering, k=4
- Gap-statistic 用于确定最优 k

### Panel e — Cluster average profiles
**结论**: 4 个 cluster 显示不同 degree of dendritic enrichment

**关键数据**:
- Cluster 1-4 逐渐增加 dendritic enrichment
- Cluster 3,4 富集 ribosomal subunits

### Panel f — Example genes per cluster
**结论**: 每个 cluster 的代表性基因可重建空间分布

**关键数据**:
- Synaptic 和 cytoskeletal genes 各有代表
- Scale bar = 500 μm

### Panel g — Cell-type specificity (QQ plot)
**结论**: Dendritic genes 比 somatic genes 更少细胞类型特异性

**关键数据**:
- Wilcoxon rank-sum test, P < 0.05
- Dendritic genes 更倾向于 broadly expressed

### Panel h — CA3 vs CA1 fold change
**结论**: Dendritic expression 相对 buffered from soma changes

**关键数据**:
- Two-sample F-test, P = 3×10^-9
- Soma fold change only explains 13% variance in dendritic expression

## 总体结论

Fig. 2 展示了 Slide-seqV2 鉴定 dendritically enriched mRNAs 的能力。通过利用 CA1 的极化结构，鉴定出 213 个显著 dendritic genes，分为 4 个功能 cluster。关键发现：dendritic mRNAs 更倾向于 broadly expressed（而非 cell type specific），且 dendritic compartment 相对 buffered from transcriptional changes，暗示存在独立的调控机制。

## 关联 Figures / Extended Data
- **Supplementary Fig. 6a** — Overlap with previous studies
- **Supplementary Fig. 6b** — GO enrichment per cluster
- **Supplementary Table 3** — Gene lists
- **Supplementary Dataset 1** — All 213 genes spatial reconstructions
