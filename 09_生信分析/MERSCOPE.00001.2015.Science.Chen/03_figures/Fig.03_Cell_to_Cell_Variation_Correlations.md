# Fig. 3 — Cell-to-cell variations and pairwise correlations

## Caption（原文）
> Fig. 3. Cell-to-cell variations and pairwise correlations for the RNA species determined from the 140 gene-measurements. (A) Comparison of gene expression levels in two individual cells. (B) Fano factors for individual genes. Error bars represent standard error of the mean determined from 7 independent data sets. (C) Z-scores of the expression variations of four example pairs of genes showing correlated (top two) or anti-correlated (bottom two) variation for 100 randomly selected cells. Z-score is defined as the difference from the mean normalized by the standard deviation. (D) Matrix of the pairwise correlation coefficients of the cell-to-cell variation in expression for the measured genes, shown together with the hierarchical clustering tree. The seven groups identified by a specific threshold on the cluster tree (dashed line) are indicated by the black boxes in the matrix and colored lines on the tree, with grey lines on the tree indicating ungrouped genes. Different threshold choices on the cluster tree could be made to select either smaller subgroups with tighter correlations or larger super-groups containing more weakly coupled subgroups. Two of the seven groups are enlarged on the right. (E) Enrichment of 30 selected, statistically significantly enriched GO terms in the seven groups. Enrichment refers to the ratio of the fraction of genes within a group that have the specific GO term to the fraction of all measured genes having that term. Top 10 statistically significantly enriched GO terms for each of the seven groups are shown in table S2. Not all of the GO terms presented here are in the top 10 list.

## Panel-by-Panel 解读

### Panel A — 两个单细胞的表达水平
**结论**：同一批 140 genes 在不同 IMR90 细胞间有显著表达差异，MERFISH 可并行捕获这种自然波动。

**关键数据**：比较两个 individual cells；后续分析覆盖 7 个 independent data sets。

### Panel B — Fano factors
**结论**：许多基因显著偏离 Poisson 预期，且 Fano factor 随平均 RNA 丰度呈上升趋势。

**关键数据**：Poisson 基线 Fano factor = 1；高变异基因包括 SLC5A3、CENPF、MKI67、TNC、KIAA1199。

### Panel C — Correlated / anti-correlated pairs
**结论**：基因对可表现正相关或负相关的 cell-to-cell variation，反映潜在共调控或状态转换。

**关键数据**：展示 4 个 gene pairs、100 个随机细胞；Z-score = (表达 − 均值) / 标准差；顶部两对正相关，底部两对反相关。

### Panel D — Pairwise correlation matrix and tree
**结论**：层次聚类将约 10,000 个 pairwise correlations 组织为 7 个共变基因组。

**关键数据**：7 groups 以黑框/彩色树枝显示；Group 1 为 ECM 相关（FBN1、FBN2、COL5A、COL7A、TNC、VCAN、THBS1），Group 6 富集囊泡运输与细胞运动。

### Panel E — GO enrichment
**结论**：共变基因组具有功能一致的 GO term 富集，支持其共享调控或细胞状态基础。

**关键数据**：30 个 selected statistically significantly enriched GO terms；每组 top 10 见 Table S2。

## 总体结论
Fig. 3 证明 MERFISH 的价值不仅是“多测基因”，还可以利用单细胞自然表达噪声重建共调控网络。ECM 组把未注释 KIAA1199 与 ECM 代谢联系起来，囊泡/运动组把 KIAA1462 与运输联系起来，而细胞周期基因 CENPF/MKI67 的双峰与高 Fano factor 揭示了状态依赖的转录波动。

## 关联 Figures / Extended Data
- Fig. 2（140-gene 计数与质量验证）
- Fig. 6（1001-gene 共变分析）
- Fig. S6–S7（错误率与 codebook 控制）
