# Fig. 5 — Comparative Analysis of Cell Clustering, Cell Type Annotation, and Spatial Alignment with Adjacent CODEX

## Caption（原文）
> Fig. 5 | Comparative analysis of cell clustering, cell type annotation, and spatial alignment with adjacent CODEX. a Uniform Manifold Approximation and Projection (UMAP) of scRNA-seq and ST data for COAD samples. Each point represents a single cell (for scRNA-seq, Stereo-seq v1.3, CosMx 6K, and Xenium 5K) or an 8 × 8 μm bin (for Visium HD FFPE). Colors denote clusters identified by unsupervised clustering applied independently to each dataset based solely on transcriptomic profiles. b Average silhouette width (ASW) of unsupervised clustering results across platforms, with higher scores indicating better separation between distinct cell states. c Consistency of automated cell type annotations across five reference-based annotation tools. Bars represent the proportion of cells annotated as the same cell type by one to five tools. d Spatial distribution of annotated cell types in ST and CODEX data. Colors denote major cell types. Each ST platform is compared to its adjacent CODEX section. e, f Spatial correlation between CODEX-inferred and ST-inferred cell counts for different cell types over the spatial grids. Panel e shows the correlations for immune and stromal cells, while panel f shows the correlations for epithelial cells. Pearson correlation coefficients are reported. Hollow circles indicate individual correlation values obtained under different grid sizes (n = 5). Data are presented as mean values +/−SEM. g Representative immune-enriched regions (500 × 500 μm) from COAD sections. H&E staining, ST-derived annotations, CODEX-derived annotations, and multiplexed CODEX staining for CD20, CD8, and CD4 are shown. For ST data, each point represents a single cell (for Stereo-seq v1.3, CosMx 6K, and Xenium 5K) or an 8 × 8 μm bin (for Visium HD FFPE), colored by annotated cell type as shown in the legend. Scale bars, 100 μm.

## Panel-by-Panel 解读

### Panel a — UMAP Visualization
**结论**：scRNA-seq提供了最清晰的细胞群体分离（UMAP上各cluster最分明）。在ST平台中，iST技术（CosMx 6K, Xenium 5K）实现了比sST平台更好的转录组差异解析。
**关键数据**：基于纯转录组特征的无监督聚类（各数据集独立聚类）

### Panel b — Average Silhouette Width (ASW)
**结论**：iST平台在聚类分离度方面优于sST平台，验证了高空间分辨率对细胞异质性解析的优势。
**关键数据**：ASW得分（越接近1越好）

### Panel c — Annotation Consistency Across Tools
**结论**：Xenium 5K在五种注释工具中表现出最高的注释一致性，表明其细胞类型识别稳健性最强。CosMx 6K和Xenium 5K恢复了更多不同的细胞类型。
**关键数据**：被1到5种工具一致注释为同一细胞类型的细胞比例

### Panel d — Spatial Distribution of Annotated Cell Types
**结论**：所有ST平台均与CODEX在空间细胞类型分布上表现出良好的一致性，证明了注释结果的可靠性。
**关键数据**：主要细胞类型的空间分布，每ST平台与其相邻CODEX切片的比较

### Panel e — Immune and Stromal Cell Correlation with CODEX
**结论**：Xenium 5K在免疫和间质细胞与CODEX的空间一致性方面表现最高，证明了其在肿瘤微环境研究中的优势。
**关键数据**：Pearson相关系数（n=5个grid尺寸），COAD、HCC、OV

### Panel f — Epithelial Cell Correlation with CODEX
**结论**：对于上皮细胞，各平台间差异较小，这与上皮细胞分布广泛、丰度高的特点一致。
**关键数据**：Pearson相关系数（n=5个grid尺寸）

### Panel g — Lymphocyte Aggregate Regions
**结论**：Xenium 5K在淋巴细胞富集区域表现出最高的CD4+ T细胞、CD8+ T细胞和B细胞检测准确性。Visium HD FFPE因bin-level分析限制，难以区分重叠的细胞类型。
**关键数据**：
- 区域大小：500 × 500 μm
- 标尺：100 μm
- CODEX验证：CD20, CD8, CD4

## 总体结论
Fig. 5全面评估了细胞聚类、注释和空间对齐能力。iST平台（尤其是Xenium 5K）在所有评估维度上表现最优，证明了高分辨率和多通道染色对空间转录组分析的重要性。

## 关联 Figures / Extended Data
- **Supplementary Fig. 11a-f** — T细胞亚型注释和标记基因表达
- **Supplementary Fig. 12a-c** — 注释细胞类型数和熵评分
- **Supplementary Fig. 14a-e** — 免疫细胞检测详细分析
