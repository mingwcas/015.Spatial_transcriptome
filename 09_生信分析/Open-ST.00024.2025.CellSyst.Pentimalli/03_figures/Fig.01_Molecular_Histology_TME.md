# Fig. 1 — Molecular histology of the TME at single-cell resolution

## Caption（原文）
> (A) Experimental design for the 3D reconstruction and multimodal proﬁling of cellular neighborhoods. 34 consecutive 5 μm sections were cut from one non-small cell lung cancer (NSCLC) tumor block. Second harmonic imaging (SHG, quantiﬁes collagen and elastin), hematoxylin and eosin (H&E, detects tissue morphology), ST (1000-plex RNA in situ hybridization with CosMx), and immunoﬂuorescence (IF) were combined for multimodal spatial proﬁling. Gray: sections collected on a glass slide but not processed.
> (B) Deep learning-based identiﬁcation of a tumor and stroma-rich region of interest (ROI, black square). Semantic segmentation of the whole-slide H&E image in carcinoma (red), stroma (orange), and normal lung (not colored) regions.
> (C) 18 epithelial, stromal, and immune cell types compose the TME. UMAP of cellular gene expression colored by cell type identity (CosMx data generated in this study).
> (D) Molecular histology matches tissue morphology. Top left and bottom right: H&E staining (section 3). Top right and bottom left: CosMx cells colored by their assigned cell types (section 4).
> (E) Congruence of gene expression proﬁles in segmented cells with single-cell RNA sequencing references. UMAPs of cellular gene expression colored by label transfer scores from healthy and tumor published atlases.

## Panel-by-Panel 解读

### Panel A — 实验设计
**结论**：展示了3D多模态分析的实验设计：从1个FFPE肿瘤block切取34张连续5μm切片，交替用于SHG、H&E、CosMx ST和IF分析。

**关键数据**：34张连续切片，CosMx分析每6张取1张（sections 4, 10, 16, 22, 28, 34），切片间距30μm。

### Panel B — ROI选择
**结论**：深度学习H&E语义分割自动识别肿瘤（红）和基质（橙）丰富区域，选择16mm²的ROI用于ST分析。

**关键数据**：深度学习分割模型F1≈0.93；ROI选择包含肿瘤和癌相关基质共存区域。

### Panel C — 细胞类型UMAP
**结论**：无监督聚类和标记基因注释鉴定出TME中18种上皮、基质和免疫细胞类型。

**关键数据**：18种细胞类型；340,644个细胞；中位101个基因/细胞，198个转录本/细胞。

### Panel D — 分子组织学与形态学对应
**结论**：CosMx细胞类型分布与H&E组织形态学高度一致。

**关键数据**：section 3的H&E与section 4的CosMx细胞类型空间对应。

### Panel E — 参考图谱验证
**结论**：CosMx基因表达与已发表的健康肺和NSCLC scRNA-seq图谱高度一致，验证了细胞类型注释的准确性。

**关键数据**：label transfer score显示与两个独立参考图谱的一致性。

## 总体结论
Fig. 1建立了研究的实验基础：展示了从FFPE临床样本到单细胞分辨率3D分子图谱的完整工作流程，生成了包含340,000+细胞、18种细胞类型的高质量空间转录组数据集。

## 关联 Figures / Extended Data
- ED Fig. S1 — 数据质量评估（阴性探针、转录本计数相关性、聚类结果、标记基因）
