# Fig. 4 — Spatial Gene Expression Mapping of Early Eye Development

## Caption（原文）
> (A) Bright-field image of a whole mouse embryo tissue section (E10). Red indicates pan-mRNA signal in a region of interest (ROI) analyzed by DBiT-seq (10-μm pixel size). Scale bar, 500 μm (left panel); 200 μm (right panel).
> (B) H&E staining performed on an adjacent tissue section. Scale bar, 200 μm.
> (C) Overlay of spatial expression maps for selected genes. It revealed spatial correlation of different genes with high accuracy. For example, Pax6 is expressed in whole optic vesicle including a single-cell-layer of melanocytes marked by Pmel and the optical nerve fiber bundle on the left. Six6 is expressed within the optic vesicle but does not overlap significantly with the melanocyte layer although they are in proximity. Scale bar, 100 μm.
> (D) Pmel, Pax6, and Six6 spatial expression superimposed onto the dark-field tissue images of the mouse embryo samples E10 and E11 (pixel size, 10 μm). These genes are implicated in early stage embryonic eye development. Pmel was detected in a layer of melanocytes lining the optical vesicle. Pax6 and Six6 were mainly detected inside the optical vesicle but also seen in other regions mapped in this data.
> (E) Spatial expression of Aldh1a1 and Aldh1a3. Aldh1a1 is expressed in dorsal retina of early embryo, and meanwhile, Adlh1a3 is mainly expressed in retinal pigmented epithelium and in ventral retina.
> (F) Spatial expression of Msx1. It is mainly enriched in the ciliary body of an eye, including the ciliary muscle and the ciliary epithelium, which produces the aqueous humor.
> (G) Spatial expression of Gata3. It is essential for lens development and mainly expressed in posterior lens fiber cells during embryogenesis.
> (H) Integration of scRNA-seq (Cao et al., 2019) and DBiT-seq data (10-μm pixel size). The combined data were analyzed with unsupervised clustering and visualized with different colors for different samples. It revealed that DBiT-seq pixels conformed into the clusters of scRNA-seq data.
> (I) Clustering analysis of the combined dataset (scRNA-seq and DBiT-seq) revealed 25 major clusters.
> (J) Spatial pattern of select clusters (0, 2, 4, 6, 7, 8, 14, 19, 20, and 22) identified in UMAP (I).
> (K) Cell types (different colors) identified by scRNA-seq and comparison with DBiT-seq pixels (black).
> (L–N) Spatial expression pattern of DBiT-seq pixels from select clusters (I) in relation to cell types identified (K).

## Panel-by-Panel 解读

### Panel A — Bright-field with ROI
**结论**：E10全胚胎明场图像，标注了DBiT-seq分析的ROI
**关键数据**：10μm像素，500μm和200μm标尺

### Panel B — H&E Adjacent Section
**结论**：相邻组织切片H&E染色
**关键数据**：200μm标尺

### Panel C — Gene Overlay
**结论**：10μm像素高分辨率揭示Pax6、Pmel、Six6等基因的空间相关性
**关键数据**：Pax6在视杯和黑色素细胞层表达；Six6在视杯内部特异表达，不与黑色素细胞层重叠

### Panel D — Time Course (E10 vs E11)
**结论**：E10到E11发育过程中Pmel、Pax6、Six6空间模式动态变化
**关键数据**：Pmel在光杯周围的黑色素细胞层表达；E11时视杯开始形成视杯杯状结构

### Panel E — Aldh1a1/Aldh1a3
**结论**：Aldh1a1和Aldh1a3在视网膜背腹轴差异化表达
**关键数据**：Aldh1a1在背侧视网膜高表达；Aldh1a3在腹侧和RPE高表达

### Panel F — Msx1
**结论**：Msx1在睫状体特异表达
**关键数据**：睫状肌和睫状上皮

### Panel G — Gata3
**结论**：Gata3在晶状体后部纤维细胞特异表达
**关键数据**：对晶状体发育至关重要

### Panel H — scRNA-seq Integration
**结论**：DBiT-seq像素（红色）完美嵌入scRNA-seq clusters（蓝色/灰色）
**关键数据**：联合分析显示10μm像素接近单细胞水平

### Panel I — 25 Clusters
**结论**：联合数据集鉴定出25个主要clusters
**关键数据**：DBiT-seq像素与scRNA-seq数据整合良好

### Panel J — Spatial Cluster Maps
**结论**：选定clusters显示清晰的空间分布模式
**关键数据**：clusters 0,2,4,6,7,8,14,19,20,22

### Panel K — Cell Type Assignment
**结论**：scRNA-seq鉴定的细胞类型可直接映射到DBiT-seq像素
**关键数据**：黑色为DBiT-seq像素，彩色为scRNA-seq细胞类型

### Panel L-N — Cell Type Spatial Mapping
**结论**：不同cluster对应不同细胞类型和空间位置
**关键数据**：Cluster 2,8,22对应retina trajectory/epithelium/oligodendrocyte定位于optic vesicle；Cluster 14,16对应erythroid/endothelial cells定位于微血管和血凝块

## 总体结论
Fig. 4 证明了DBiT-seq的10μm像素可实现单细胞级别的空间转录组分析。通过与scRNA-seq参考数据整合，成功鉴定了早期眼部发育中的多种细胞类型及其空间分布，包括视杯、视网膜色素上皮、睫状体和晶状体等结构。

## 关联 Figures / Extended Data
- **ED Fig. S5** — 19个top基因空间表达、GO分析
