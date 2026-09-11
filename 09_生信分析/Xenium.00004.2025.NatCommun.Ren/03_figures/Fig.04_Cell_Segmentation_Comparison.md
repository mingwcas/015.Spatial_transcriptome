# Fig. 4 — Comparison of Cell Segmentation

## Caption（原文）
> Fig. 4 | Comparison of cell segmentation. a Comparison of platform-derived automatic cell segmentation and manual nuclear segmentation across Stereo-seq v1.3, CosMx 6K, and Xenium 5K HCC sections. For each platform, a 250 × 250 μm region is shown. H&E staining for Stereo-seq v1.3 and multi-channel immunofluorescent staining for CosMx 6K and Xenium 5K are shown. Left column, automatically segmented cell boundaries. Middle column, manually segmented nuclear boundaries. Right column, overlay of automatic and manual segmentations, where white polygons denote automatic segmentations, and blue-filled masks in Stereo-seq v1.3 and yellow polygons in CosMx 6K and Xenium 5K indicate manual segmentations. Scale bars, 50 μm. b Number of automatically segmented cells and manually segmented nuclei per 100 × 100 μm bin across platforms (n = 125 bins per platform per cancer type). Each data point represents one bin. Center lines indicate the median value, and lower and upper hinges represent the 25th and 75th percentiles, respectively. The whiskers denote 1.5× the interquartile range. c Log2-transformed transcript and gene counts per cell across platforms. For ST platforms, the platform-derived automatic segmentations were used. Left: all detected genes included. Right: only retained genes shared across scRNA-seq, CosMx 6K, and Xenium 5K. Each data point represents one cell. Center lines indicate the median value, and lower and upper hinges represent the 25th and 75th percentiles, respectively. The whiskers denote 1.5× the interquartile range. d Joint density plots showing the expression of exclusive marker pairs within cells in COAD. Only cells with ≥1 transcript of either marker gene were included. Color intensity indicates the density of cells. e Expression correlation of 36 gene pairs expected to be exclusively expressed in distinct major lineages. Pearson correlation was computed across either cells or 8 × 8 μm bins. Each data point represents one marker pair (n = 36). Lower values indicate better separation of marker pairs. Center lines indicate the median value, and lower and upper hinges represent the 25th and 75th percentiles, respectively. The whiskers denote 1.5× the interquartile range.

## Panel-by-Panel 解读

### Panel a — Segmentation Visualization
**结论**：CosMx 6K和Xenium 5K的自动分割与手动核分割高度吻合，而Stereo-seq v1.3因染色伪影导致分割准确性较低。
**关键数据**：250 × 250 μm区域，标尺50 μm

### Panel b — Cell Count Comparison
**结论**：CosMx 6K和Xenium 5K的自动分割细胞数与手动分割核数高度一致，证明了分割的准确性和可靠性。Stereo-seq v1.3一致性较低。
**关键数据**：每100 × 100 μm bin的细胞/核数（n=125 bins × 3种癌症类型）

### Panel c — Transcript and Gene Counts Per Cell
**结论**：在所有检测基因中，scRNA-seq检测到最多的每细胞转录本和基因。但当限制于2,522个共有基因时，iST平台表现出与scRNA-seq相当的检测能力。
**关键数据**：
- 左图（所有基因）：scRNA-seq > 各ST平台
- 右图（共有基因）：CosMx 6K和Xenium 5K与scRNA-seq可比

### Panel d — Co-expression of Exclusive Marker Pairs
**结论**：ST数据中观察到显著的EPCAM与CD3E/CD68共表达（预期应互斥），高于scRNA-seq中的共表达水平，表明细胞分割不准确导致转录本分配错误。
**关键数据**：COAD样本中互斥标记基因对（EPCAM与CD3E/CD68）的联合密度

### Panel e — Marker Pair Correlation Analysis
**结论**：Xenium 5K在细胞水平上表现出最低的互斥标记基因对相关性，提示其单细胞分割最准确。分割后ST平台的标记分离均优于bin-level分析。
**关键数据**：
- 36对互斥标记基因的Pearson相关性
- Bin-level vs Cell-level比较
- Xenium 5K最佳分离效果

## 总体结论
Fig. 4系统评估了细胞分割准确性。Xenium 5K凭借多通道染色支持的全细胞分割实现了最准确的单细胞边界划定，有效减少了转录本跨细胞泄漏，为下游细胞类型注释和空间分析提供了高质量的分割基础。

## 关联 Figures / Extended Data
- **Supplementary Fig. 9a-d** — 形态学指标（solidity, circularity, aspect ratio, cell size）比较
- **Supplementary Fig. 9e-g** — 手动分割区域和细胞数比较
- **Supplementary Fig. 10a-d** — 转录本保留和共表达详细分析
- **Supplementary Fig. 13** — 多核细胞和肝细胞分割案例
