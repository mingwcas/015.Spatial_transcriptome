# Fig. 7 — Stereo-seq V2 reveals the BCR clone dynamics in response to Mtb infection

## Caption（原文）
> (A) Comparison of reads aligned to IGH gene regions between Visium, Stereo-seq V1, and Stereo-seq V2. Ductal carcinoma in situ (DCIS) from public data was a representative of the 10× spatial transcriptome. Both colon adenocarcinoma (COAD) and liver cancer (LC) were the representatives of Stereo-seq V1. The peak value of gene track represents the relative RPKM value of that position in the genome. The locations of C and V region are distinguished by red and yellow, respectively.
> (B) Spatially resolved density distribution of Mtb RNAs and BCR clones. Visualized in kernel density estimation (KDE).
> (C) Spatial visualization of the total count of unique BCR clonotypes and the CDR3 mutation counts.
> (D) Scatterplot showing BCR clonotype counts and CDR3 mutation counts against the distance to Mtb-infected areas. The distance interval is 5 μm. R represents the Pearson correlation coefficient.
> (E) Venn plot showing the intersection of IGK clones identified in our Stereo-seq and public RNA-seq data.
> (F) Dendrogram showing the hierarchical clustering results of IGK BCR clones. The outer circle shows the data source and the inner circle shows the clusters.
> (G) Top: consensus protein sequences for clones from our data (8 weeks PI) and public RNA-seq data (PMC10100962) in IGK cluster 7, respectively. Bottom: KDE visualization of the spatial distribution density of the corresponding clones in the top panel.
> (H) From left to right: acid-fast staining of human tuberculous lung sections; Mtb staining signal within red dashed boxes identified using U-Net model; total UMI signals of Mtb transcriptome detected by Stereo-seq V2 in similar regions on nearby sections; merged image of staining and UMI signals. The numbers indicate the section orders.
> (I) Spatial visualization of total UMI counts (left) and CDR3 mutation frequency (right) in human lung tissue. Black lines demarcate the boundary of the necrotic regions.
> (J) Scatterplot showing CDR3 mutation frequency against the distance to the Mtb-infected area. The distance interval is 50 μm. Correlation coefficients were determined by the Pearson correlation coefficient.
> (K) Venn plot showing the intersection of BCR clones across 3 patients. Bottom: 16 clones shared in multiple patients; different non-black colors indicate unified CDR3 clusters.
> (L) Consensus protein sequences for clusters containing recurrent clones in (K).
> (M) Consensus protein sequences for similar clusters in public RNA-seq data (GEO: GSE107995).
> (N) Boxplot showing frequencies of clones in cluster 9/14 CDR3s among active TB patients and healthy controls (GEO: GSE107995). p value is determined using t test.
> See also Figures S6 and S7.

## Panel-by-Panel 解读

### Panel A — V Region Coverage
**结论**：V2在BCR V区域的覆盖显著优于V1和Visium。

**关键数据**：V2的V region覆盖更完整。

### Panel B — Density Distribution
**结论**：BCR克隆在Mtb感染区域及周围富集。

**关键数据**：KDE可视化显示克隆密度分布。

### Panel C — Clonotype and Mutation
**结论**：独特BCR克隆型和CDR3突变计数在感染区域空间可视化。

**关键数据**：克隆型数量和突变频率空间分布。

### Panel D — Distance Correlation
**结论**：距感染区域越近，BCR克隆多样性越高，突变频率越高。

**关键数据**：距离间隔5μm；R = Pearson相关系数。

### Panel E — Clone Intersection
**结论**：V2与公共RNA-seq数据共享25个IGK克隆。

**关键数据**：25 shared IGK clones between Stereo-seq V2 and public data。

### Panel F and G — CDR3 Clustering
**结论**：CDR3序列相似性聚类识别96个IGH簇和36个IGK簇。

**关键数据**：距离阈值<7；Consensus序列高度相似。

### Panel H — Human Lung Validation
**结论**：U-Net识别人类肺结核样本的Mtb信号与V2的UMI信号一致。

**关键数据**：抗酸染色与UMI信号Merge图像。

### Panel I and J — Human Necrotic Regions
**结论**：人类肺组织中BCR克隆多样性和突变频率随距坏死区距离增加。

**关键数据**：距离间隔50μm；坏死边界黑线标注。

### Panel K — Recurrent Clones
**结论**：3例患者共享16个BCR克隆（15 IGK + 1 IGL）。

**关键数据**：16 recurrent clones。

### Panel L-N — Shared Clone Validation
**结论**：共享克隆在活动性TB患者中频率显著高于健康对照。

**关键数据**：cluster 9/14 CDR3s在TB患者中显著富集(p < 0.05)。

## 总体结论
V2揭示了Mtb感染中BCR克隆的动态变化，发现了Mtb特异性的共享BCR克隆，为理解体液免疫应答提供空间分辨率的证据。

## 关联 Figures / Extended Data
- ED Fig. S6 (BCR dynamics in mouse model)
- ED Fig. S7 (Human TB lung analysis)
