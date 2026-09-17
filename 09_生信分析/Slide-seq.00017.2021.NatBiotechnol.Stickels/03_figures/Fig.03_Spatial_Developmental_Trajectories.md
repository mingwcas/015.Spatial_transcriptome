# Fig. 3 — Slide-seqV2 of developing mouse cortex reconstructs spatial developmental trajectories

## Caption（原文）
> Fig. 3 | Slide-seqV2 of developing mouse cortex reconstructs spatial developmental trajectories. a, Left, unsupervised cluster analysis of Slide-seqV2 data obtained from a section of E15 mouse brain. The black box delineates the region used in the analysis. Scale bar, 200 μm. ML, medial–lateral axis; DV, dorsal–ventral axis. Right, beads present within the black box colored by their annotated cluster identities and subsetted by clusters of cortical identity. Red, VZ; blue and purple, SVZ and IZ, respectively; green and orange, CP and L5/6, respectively; pink, CR cells. These reflect the layers present in the mouse cortex at this time point. Scale bar, 200 µm. b, Beads within the anatomical region of developing cortex colored by their assigned LT metric from scVelo. Arrow size and direction correspond to the direction and magnitude of the spatial derivative of the LT in physical space. Scale bar, 200 µm. c, Expression profiles of sample genes jointly identified by Slide-seqV2, scVelo and Monocle3 across the Slide-seqV2-generated spatial LT axis. d, Two-dimensional (2D) density plot quantifying the relationship between a gene's correlation with scVelo LT (x axis) and spatial significance (permutation test, one-sided, y axis; Methods). Each square is colored by the number of genes found in that bin. e, Stacked histogram of the number of genes associated with the developmental trajectory by Monocle3 (blue), scVelo (yellow) and spatial LT (red) binned by expression level. f, Left, density plot of all spatial LT genes (SV) compared to DD LT genes (DD) across mean-expressed LT value; right, density plot of all spatial LT genes (SV) compared to DD LT genes (DD) for summed gene expression across array. g, Slide-seqV2 reconstruction images of metagenes associated with each spatial cluster of DD genes Scale bar, 200 µm. h, GO classifications using over-representation analysis (Methods) for biological process terms for each spatial cluster in g (hypergeometric test, FDR-corrected P value).

## Panel-by-Panel 解读

### Panel a — Unsupervised clustering of E15 cortex
**结论**: Slide-seqV2 可识别 E15 mouse cortex 的主要发育区域

**关键数据**:
- VZ (red), SVZ/IZ (blue/purple), CP/L5/6 (green/orange), CR cells (pink)
- Scale bar = 200 μm

### Panel b — Latent time projection
**结论**: scVelo LT 成功重现皮层径向发育轴 (VZ → SVZ/IZ → CP)

**关键数据**:
- Arrow direction = developmental direction
- Arrow magnitude = rate of differentiation
- 发育早期变化速率最快

### Panel c — Sample trajectory genes
**结论**: Sema5b, Ephb1, Nrp1 等发育相关基因与 spatial LT 高度相关

**关键数据**:
- 与 axonal guidance 相关 (已知发育基因)

### Panel d — 2D density of correlation vs significance
**结论**: 1,043 / 1,349 spatially varying genes 与 LT 显著相关

**关键数据**:
- pFDR < 0.005
- 非空间变异基因很少显示 LT 相关性

### Panel e — Gene overlap across methods
**结论**: Spatial LT 与 scVelo/Monocle3 高度重叠 (76.5%, 75.6%)

**关键数据**:
- scVelo: 179 genes (137 overlapped)
- Monocle3: 377 genes (285 overlapped)
- 跨越所有表达水平

### Panel f — Developmental disorder (DD) genes
**结论**: DD genes 在 spatial LT 上富集 (74/299, 1.87-fold, P=3.2×10^-8)

**关键数据**:
- DD genes 表达更晚 (higher LT)
- 分为 5 个 spatial clusters

### Panel g — DD gene spatial clusters
**结论**: 每个 cluster 代表不同发育过程

**关键数据**:
- Cluster 1: chromatin modification
- Cluster 2-5: various developmental processes

### Panel h — GO enrichment
**结论**: 不同 spatial clusters 富集不同功能类别

**关键数据**:
- Histone modification, axonogenesis, forebrain development 等

## 总体结论

Fig. 3 证明 Slide-seqV2 可重建发育中的大脑皮层空间发育轨迹。通过整合 scVelo RNA velocity 与空间信息，成功识别了 1,043 个沿发育轨迹的基因，显著富集发育障碍相关基因 (DD genes)，揭示了皮层发育的分子空间特征。

## 关联 Figures / Extended Data
- **Supplementary Fig. 7a,b** — Additional cortex analysis
- **Supplementary Fig. 7d,e** — Eye development trajectory
- **Supplementary Fig. 7f,g** — Eye spatial LT genes
- **Supplementary Fig. 8** — Method comparisons
- **Supplementary Table 4, 5** — Gene lists
