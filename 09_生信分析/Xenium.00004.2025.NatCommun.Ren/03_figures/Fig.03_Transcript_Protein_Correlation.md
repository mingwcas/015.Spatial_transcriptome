# Fig. 3 — Evaluation of Transcript-Protein Correlation

## Caption（原文）
> Fig. 3 | Evaluation of transcript-protein correlation. a Representative immune-enriched regions (each 500 × 500 μm) from COAD samples profiled using all four ST platforms. Left to right: H&E-stained histology, spatial distribution of transcriptomic signature scores for B cells, CD4+ T cell, and CD8+ T cells derived from ST data, and corresponding CODEX staining images (DAPI, CD20, CD8, CD4). For ST data, color intensity represents the corresponding signature score of each 8 × 8 μm bin. Scale bars, 100 μm. b, c Spatial correlation between CODEX-inferred cell counts and ST-derived signature scores for different cell types over the spatial grids. Panel b shows the correlations for immune and stromal signature scores, while panel c shows the correlations for epithelial signature scores. Pearson correlation coefficients are reported. Hollow circles indicate individual correlation values obtained under different grid sizes (n = 5). Data are presented as mean values +/−SEM.

## Panel-by-Panel 解读

### Panel a — Representative Immune-Enriched Regions
**结论**：在COAD样本的免疫富集区域中，Visium HD FFPE和Xenium 5K与CODEX的B细胞、CD4+ T细胞和CD8+ T细胞标记基因空间分布表现出高度一致性。
**关键数据**：
- 区域大小：500 × 500 μm
- 颜色强度：8 × 8 μm bin水平的signature score
- 标尺：100 μm
- ST平台：B cell signature, CD4+ T cell signature, CD8+ T cell signature
- CODEX验证：DAPI, CD20, CD8, CD4

### Panel b — Immune and Stromal Cell Type Correlation
**结论**：在免疫和间质细胞类型signature scores方面，Visium HD FFPE和Xenium 5K与CODEX表现出最高的空间一致性。
**关键数据**：
- Pearson相关系数（各grid尺寸下的平均值，n=5个grid尺寸）
- COAD、HCC、OV三种癌症类型的相关性
- Visium HD FFPE和Xenium 5K > CosMx 6K和Stereo-seq v1.3

### Panel c — Epithelial Cell Type Correlation
**结论**：对于上皮细胞signature scores，各平台间的差异相对较小，这与上皮细胞分布广泛、丰度高的特点一致。
**关键数据**：
- Pearson相关系数（各grid尺寸下的平均值，n=5）
- 三种癌症类型（COAD、HCC、OV）的相关性
- 平台间差异较小

## 总体结论
Fig. 3证明了基于signature水平的空间相关性分析比单个标记基因更能准确反映细胞类型的空间分布。Visium HD FFPE和Xenium 5K在免疫细胞检测方面与CODEX蛋白表达表现出最强的空间一致性，为肿瘤微环境研究提供了更可靠的空间转录组数据。

## 关联 Figures / Extended Data
- **Supplementary Fig. 7a** — COAD TLS样结构详细分析
- **Supplementary Fig. 7b** — HCC中CD34血管定位分析
- **Supplementary Fig. 7c** — OV中巨噬细胞富集区分析
