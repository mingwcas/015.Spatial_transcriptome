# Fig. 2 — Spatial Multi-Omics Mapping of Whole Mouse Embryos

## Caption（原文）
> (A) Pan-mRNA and pan-protein-panel spatial expression maps (pixel size, 50 μm) reconstructed from DBiT-seq, alongside the H&E image from an adjacent tissue section. Whole transcriptome pan-mRNA map correlated with anatomic tissue morphology and density.
> (B) Comparison to ''pseudo bulk'' RNA-seq data. Four embryo samples (E10) analyzed by DBiT-seq correctly situated in the UMAP in relation to those analyzed by single-cell RNA-seq (Cao et al., 2019) in terms of the developmental stage.
> (C) Unsupervised clustering analysis and spatial pattern. Left: UMAP showing the clusters of tissue pixel transcriptomes. Middle: spatial distribution of the clusters. Right: overlay of spatial cluster map and tissue image(H&E). Because the H&E staining was conducted on an adjacent tissue section, minor differences were anticipated.
> (D) Gene Ontology (GO) analysis of all 11 clusters. Selected GO terms are highlighted.
> (E) Anatomic annotation of major tissue regions based on the H&E image.
> (F) Correlation between mRNAs and proteins in each of the anatomically annotated tissue regions. The average expression levels of individual mRNAs and cognate proteins are compared.

## Panel-by-Panel 解读

### Panel A — Spatial Expression Maps
**结论**：DBiT-seq成功绘制全胚胎mRNA和蛋白质空间表达图谱
**关键数据**：50μm像素；每个像素检测到12,314 mRNA UMIs和~3,038蛋白UMIs（22种蛋白）；平均4,170 genes/pixel

### Panel B — Pseudo-bulk Comparison
**结论**：DBiT-seq数据在发育时间轴上与scRNA-seq参考数据一致
**关键数据**：4个E10 DBiT-seq样本位于E9.5和E10.5 scRNA-seq样本之间

### Panel C — Clustering Analysis
**结论**：无监督聚类识别出11个主要组织clusters，与解剖学注释一致
**关键数据**：11个clusters通过NMF鉴定；UMAP显示clusters分布；空间映射与H&E图像重叠

### Panel D — GO Analysis
**结论**：每个cluster富集不同的生物学过程
**关键数据**：GO分析揭示telencephalon、mesencephalon、rhombencephalon、branchial arches、spinal neural tube、heart、limb bud等组织类型

### Panel E — Anatomic Annotation
**结论**：基于H&E图像手动注释13个主要组织区域
**关键数据**：9个GO分析识别的组织类型与手动注释一致

### Panel F — mRNA-Protein Correlation
**结论**：mRNA与蛋白表达在大多数组织区域呈正相关
**关键数据**：15对mRNA-蛋白平均Pearson相关系数~0.28；Notch1、CD63、PECA、EpCAM、ITGA4等在特定组织高表达

## 总体结论
Fig. 2 展示了DBiT-seq在全胚胎尺度上进行空间多组学映射的能力。通过50μm像素成功识别出主要组织类型（大脑、心脏、神经管等），且mRNA-蛋白联合分析揭示了转录后调控的存在。

## 关联 Figures / Extended Data
- **ED Fig. S3** — Hox基因空间表达、mRNA-蛋白详细对比、免疫荧光验证
