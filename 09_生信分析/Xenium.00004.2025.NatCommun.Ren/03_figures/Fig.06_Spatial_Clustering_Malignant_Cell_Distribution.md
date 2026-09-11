# Fig. 6 — Comparison of Spatial Clustering and Malignant Cell Distributions

## Caption（原文）
> Fig. 6 | Comparison of spatial clustering and malignant cell distributions. a Spatial clustering of COAD tissue sections profiled using four ST platforms and adjacent CODEX. Colors represent spatial clusters identified within each dataset. b Pearson correlation between cluster proportions in ST and CODEX data across spatial grids. Hollow circles indicate individual correlation values obtained under different grid sizes (n = 5). Data are presented as mean values +/−SEM. c H&E staining and spatial localization of malignant cells at tumor boundary and core regions, as defined by unsupervised spatial clustering within each ST platform.

## Panel-by-Panel 解读

### Panel a — Spatial Clustering Visualization
**结论**：所有四个ST平台均成功识别了空间聚类，且与CODEX的空间聚类表现出良好的一致性。Stereo-seq v1.3在HCC中一致性较低。
**关键数据**：COAD组织切片的空间聚类结果，各数据集独立聚类

### Panel b — Cluster Proportion Correlation
**结论**：在COAD和OV中，所有ST平台与CODEX的空间聚类比例表现出相当的一致性。Stereo-seq v1.3在HCC中一致性显著较低。
**关键数据**：
- Pearson相关系数（跨空间grid，n=5）
- COAD: 各平台均表现较好
- HCC: Stereo-seq v1.3一致性较低
- OV: 各平台均表现较好

### Panel c — Malignant Cell Localization
**结论**：所有ST平台均成功识别了位于肿瘤核心或边界的恶性细胞。Visium HD FFPE和Xenium 5K勾勒出更连续的肿瘤边界。
**关键数据**：
- H&E染色和恶性细胞空间定位
- 肿瘤边界（tumor boundary）与肿瘤核心（tumor core）的区分
- 各平台对比

## 总体结论
Fig. 6证明了所有ST平台均能成功解析大规模组织结构，但在特定组织类型中平台特定局限性可能影响空间聚类准确性。Xenium 5K和Visium HD FFPE在肿瘤边界描绘方面表现最优，对于肿瘤空间异质性研究具有重要价值。

## 关联 Figures / Extended Data
- **Supplementary Fig. 15a-c** — 空间聚类详细结果
- **Supplementary Fig. 15d** — CD8+ T细胞空间定位分析
- **Supplementary Fig. 16a-k** — 空间通路富集分析
