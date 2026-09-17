# Fig. 2 — 3D neighborhoods identify multicellular niches in the TME

## Caption（原文）
> (A) Airways cross multiple sections in 3D. 3D plot of the 6 CosMx sections after registration with STIM. Green: respiratory epithelium cells, gray: other cell types. Axes are scaled to the same length for visualization purposes.
> (B) Design and analysis of 3D cellular neighborhoods. Left: exemplary 3D neighborhood. Red: center cell, dark green: tumor cells, orange: ﬁbroblasts, gray: other cell types. Right: quantiﬁcation of cell types in 3D neighborhoods is used to build the 3D neighborhood matrix.
> (C) The TME is formed by lung-resident, tumor, stromal, and immune multicellular niches. UMAP of 3D cellular neighborhoods colored by 3D niche assignments. Cells are grouped based on their 3D neighborhood composition, regardless of their gene expression.
> (D) The composition of 3D neighborhoods guides multicellular niche annotation. Heatmap of niche-speciﬁc average cell type counts in 3D neighborhoods. Color scale is clipped to 30 for visualization purposes.
> (E) 3D multicellular niches capture the spatial organization of the TME. Comparison of 3D niche spatial localization (left, section 10) with pathologist manual annotations of H&E tissue domains (right, section 3).

## Panel-by-Panel 解读

### Panel A — 3D配准验证
**结论**：STIM配准后呼吸道上皮细胞在3D中呈现连续的管腔结构，验证了3D对齐的准确性。

**关键数据**：6张CosMx切片的3D图；中位细胞位移42μm。

### Panel B — 3D邻域设计
**结论**：展示了3D细胞邻域的概念设计：以中心细胞为圆心，50μm半径内的所有细胞构成邻域，量化18种细胞类型计数构建邻域矩阵。

**关键数据**：3D邻域面积比2D大2.28倍；中位71个细胞/9种细胞类型/邻域。

### Panel C — 多细胞niche UMAP
**结论**：无监督聚类识别出10种多细胞niche，涵盖肺组织固有结构和TME特有结构。

**关键数据**：10种niche：tumor core, tumor surface, airways, alveoli, desmoplastic stroma, vascular stroma, smooth muscle, macrophage niche, dendritic cell niche, T cell niche。

### Panel D — Niche组成热图
**结论**：每种niche有特征性的细胞类型组成模式。Tumor core以肿瘤细胞为主，desmoplastic stroma富含成纤维细胞和浆细胞，immune niches以特定免疫细胞为主。

**关键数据**：热图显示niche特异性的平均细胞类型计数，色阶截断为30。

### Panel E — Niche与病理学标注对应
**结论**：3D多细胞niche与病理学家手动H&E标注高度一致，包括气道、肺泡、淋巴细胞聚集、纤维化和大血管平滑肌。

**关键数据**：niche提供了比手动标注更精细的肿瘤、免疫和基质niche分类。

## 总体结论
Fig. 2是本文的核心分析之一，展示了3D细胞邻域如何将TME解构为10种空间有序的多细胞niche。niche注释与病理学家标注一致但更为精细，证明了3D邻域分析在捕获TME空间组织方面的强大能力。

## 关联 Figures / Extended Data
- ED Fig. S2 — 3D配准变换量化、聚类结果和细胞多样性
