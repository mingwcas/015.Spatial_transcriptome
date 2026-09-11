# Fig. 1 — Experimental Design and Key Metrics

## Caption（原文）
> Fig. 1 | Experimental design and key metrics. a, Experiment names correspond to the profiling technology and panel used, with the number in parentheses indicating the panel size. Each sample is represented as a tile, and replicate experiments are marked with 'x2' or 'x3' within the tile to refer to the number of replicates. Columns group samples originating from the same donor. b, Density distributions of the number of transcripts per cell and the number of detected genes per cell for each sample, along with the number of cells per sample, color-coded by panel and assay type. c, Cell-type composition of all Xenium and Chromium samples, grouped by donor and colored by cell type. The colored strip alongside each row indicates the corresponding panel or assay. d, Integrated UMAPs grouped by panel and assay. Cells are colored by cell type as assigned by RCTD using matched Chromium reference at Level 2.1 annotation.

## Panel-by-Panel 解读

### Panel a — 实验设计概览
**结论**：展示了41个组织切片的完整实验设计，包括19个乳腺癌样本和22个肺癌样本，使用多种基因面板进行Xenium分析。

**关键数据**：
- 乳腺癌：17 donors × 1-3 sections， Breast panel (280 genes)
- 肺癌：10 donors × 1-3 sections，Lung panel, Custom IO, 5K PRIME
- 匹配snRNA-seq和IHC数据

### Panel b — 质控指标分布
**结论**：所有样本产生高质量数据，单细胞水平有稳健的转录本和基因检测。

**关键数据**：
- 转录本/cell：各样本差异较大，但均>10
- 基因/cell：各panel差异明显
- 细胞数/样本：100-100,000范围

### Panel c — 细胞类型组成
**结论**：技术重复间强可重复性，但患者间和技术间（Chromium vs Xenium）有实质性差异。

**关键数据**：
- 主要细胞类型：Malignant cell, Fibroblast, Macrophage, T cell等
- Chromium解离细胞与Xenium空间细胞的组成差异

### Panel d — UMAP可视化
**结论**：非恶性细胞群体在个体间一致对齐，恶性细胞按患者特异性聚集，表明Xenium数据质量高、批次效应低。

**关键数据**：
- 无需批次校正或数据整合（Seurat log normalization除外）
- 批次整合指标（iLISI, Silhouette Batch）确认强一致性

## 总体结论
Fig. 1建立了本文的数据资源基础：41个Xenium样本+匹配snRNA-seq，证明了Xenium平台的高质量和可重复性。

## 关联 Figures / Extended Data
- ED Fig. 1 — 外部参考的注释验证
- ED Fig. 2 — 批次整合评分
- ED Fig. 3 — 技术重复相关性
