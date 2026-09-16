# Fig. 6 — Co-variation analysis of the 1001-gene measurements

## Caption（原文）
> Fig. 6. Co-variation analysis of the RNA species measured in the 1001-gene measurements. (A) Matrix of all pairwise correlation coefficients of the cell-to-cell variation in expression for the measured genes shown with the hierarchical clustering tree. The ~100 identified groups of correlated genes are indicated by color on the tree. Zoom in of four of the groups described in the text are shown on the right. (B) Enrichment of 20 selected, statistically significantly enriched GO terms in the four groups. The statistically most significantly enriched GO terms (maximum 10) for each of the ~100 groups are shown in table S4.

## Panel-by-Panel 解读

### Panel A — 1001-gene correlation matrix and tree
**结论**：把 1001-gene measurement 的 cell-to-cell expression variation 组织成约 100 个相关基因组，显著扩展了可探索的调控网络空间。

**关键数据**：矩阵包含所有 pairwise correlation coefficients；tree 上以颜色标示 ~100 groups，并放大正文讨论的 4 个 group。

### Panel B — GO enrichment
**结论**：绝大多数共变 group 都有统计显著的功能相关 GO term 富集，说明表达共变具有生物学而非纯技术基础。

**关键数据**：图中展示 4 个 group 的 20 个 selected significantly enriched GO terms；约 100 组中每组最多 10 个最显著 term 见 Table S4。

## 总体结论
Fig. 6 证明 MERFISH 的大规模并行读出可把单细胞转录噪声转化为系统的功能网络资源：1001-gene 实验约 200 cells、3 个独立实验中获得约 100 个共变模块，几乎每组都有 GO 富集，并为 46 个未注释 RNA 和 61 个转录因子/部分注释蛋白提出功能假设。由于 MHD2 无纠错且调用率低，模块解释应依赖独立验证，不能把相关性直接等同于因果调控。

## 关联 Figures / Extended Data
- Fig. 3（140-gene 的 7 个共变 group 与 Fano factor 基线）
- Fig. 5（1001-gene 测量质量与 shared-gene r = 0.89）
- Table S4（~100 groups 的完整 GO 富集与 p-values）
