# Fig. 6 — Mapping Internal Organs in a E11 Mouse Embryo

## Caption（原文）
> (A) Enlarged view of UMAP clustering of Figure 5D with a specific focus on the E11 embryo lower body sample.
> (B) Spatial expression of four select clusters indicated in (A).
> (C) UMAP showing the clustering analysis of the E11 embryo lower body sample only. The tissue pixels from four major clusters shown in (A) and (B) are circled in this UMAP with more sub-clusters identified.
> (D) Spatial map of all the clusters shown in (C).
> (E) Cell type annotation (SingleR) using scRNA-seq reference data from E10.5 mouse embryo (Cao et al., 2019).
> (F) Spatial expression maps of individual genes.
> (G) Tissue types identified for clusters a, b, c, and d indicated in (A) overlaid onto the tissue image. Major organs such as heart (atrium and ventricle), liver, and neutral tube were identified, in agreement with the tissue anatomy. Erythrocyte coagulation was detected by DBiT-seq, for example, within the dorsal aorta and the atrial chamber. Scale bar, 250 μm.

## Panel-by-Panel 解读

### Panel A — E11 Lower Body UMAP
**结论**：E11胚胎下半身样本显示多个明显分离的sub-clusters
**关键数据**：四个主要clusters (a,b,c,d)对应不同组织类型

### Panel B — Spatial Expression of Selected Clusters
**结论**：四个选定clusters显示独特的空间分布模式
**关键数据**：clusters a,b,c,d分别对应不同解剖结构

### Panel C — E11 Lower Body Detailed Clustering
**结论**：E11下半身样本细分出13个clusters
**关键数据**：比全局分析更细致的组织分类

### Panel D — Spatial Cluster Map
**结论**：13个clusters清晰映射到组织空间位置
**关键数据**：展示了组织内不同区域的转录组异质性

### Panel E — SingleR Cell Type Annotation
**结论**：使用SingleR自动鉴定细胞类型
**关键数据**：12个最常见细胞类型展示在UMAP上

### Panel F — Individual Gene Spatial Maps
**结论**：8个代表性marker基因显示特异的组织表达模式
**关键数据**：Myh6(心房)、Myh7(心室)、Pax6(神经管)、Car3(脊索)、Apoa2(肝脏)、Hba.a2(红细胞)、Col4a1(血管内皮)、Actb(广泛表达)

### Panel G — Tissue Type Identification
**结论**：Cluster a-d分别对应liver、neural tube、heart(dorsal aorta/atrium/ventricle)、blood vessels with coagulated erythrocytes
**关键数据**：DBiT-seq准确识别心房vs心室、肝脏、神经管等结构；Hba.a2检测到血凝块中的红细胞

## 总体结论
Fig. 6 证明了DBiT-seq在亚器官级别分辨率下的空间细胞类型映射能力。通过SingleR自动化注释和marker基因空间表达验证，成功识别了心房vs心室、肝脏、神经管、背主动脉等精细结构，甚至检测到血凝块中的红细胞。

## 关联 Figures / Extended Data
- **ED Fig. S6** — DBiT-seq与ENCODE bulk RNA-seq对比（r=0.8）
