# Fig. 3 — Heterogeneity of T and B cell landscapes in SCLC lymph node metastasis

## Caption（原文）
> (A and B) UMAP plots visualizing the annotated subsets of (A) T cells (n = 38,149) and (B) B cells (n = 9,678) across PT, PT-LNM, and LNMT samples. Each dot represents a single cell, colored by its respective subtype. (C) Stacked bar plots showing the relative proportions of T cell (top) and B cell (bottom) subsets across PT, PT-LNM, and LNMT. (D) Lollipop plot illustrating the log2 fold change (FC) in the proportion of each T cell and B cell subset for the comparisons PT-LNM vs. PT, LNMT vs. PT, and LNMT vs. PT-LNM. (E) Lollipop plot showing the number of DEGs identified in each immune cell type for the three comparisons. (F) Scatterplots demonstrating the correlation between the log2FC values of DEGs across the indicated pairwise comparisons. Spearman's correlation coefficient (ρ) and p value are shown. (G) Conserved transcriptional trends and pathway activation. (Left) Venn diagram identifying 11 DEGs with a monotonic increase from PT to PT-LNM to LNMT. (Middle) Heatmap showing the scaled expression of these 11 DEGs across sample types. (Right) Bar plots of the top KEGG pathways enriched for the shared up-regulated DEGs.

## Panel-by-Panel 解读

### Panel A — T细胞亚群UMAP
**结论**：38,149个T细胞分为6个亚群：效应CD4+ T细胞、效应CD8+ T细胞、炎症Tregs、耗竭Tregs、双阴性T细胞(DNTs)、耗竭CD8+ T细胞
**关键数据**：6个T细胞亚型

### Panel B — B细胞亚群UMAP
**结论**：9,678个B细胞分为4个亚群：记忆B细胞、增殖B细胞、初始B细胞、过渡B细胞
**关键数据**：4个B细胞亚型

### Panel C — T/B细胞组成变化
**结论**：PT富集效应CD4+和CD8+ T细胞；PT-LNM和LNMT中耗竭Tregs和炎症Tregs比例升高；LNMT中初始B细胞占主导，过渡B细胞和增殖B细胞增加
**关键数据**：免疫抑制性TME重编程

### Panel D — 各亚群比例变化
**结论**：各T/B细胞亚型的比例在PT→PT-LNM→LNMT过程中呈现方向性变化，反映免疫微环境的动态演化
**关键数据**：log2FC量化变化

### Panel E — 差异基因数量
**结论**：不同免疫细胞类型在LNMT vs PT比较中表现出最大数量的差异基因
**关键数据**：DEG数量统计

### Panel F — 转录组变化相关性
**结论**：LNMT vs PT的基因表达变化与PT-LNM vs PT高度相关(ρ=0.73)，LNMT vs PT-LNM也高度相关(ρ=0.79)，表明从PT到LNMT存在连续的转录组演变
**关键数据**：Spearman ρ = 0.73 (p < 2.2×10⁻¹⁶); ρ = 0.79 (p < 2.2×10⁻¹⁶)

### Panel G — 保守转录趋势
**结论**：识别出11个在PT→PT-LNM→LNMT过程中单调上调的共享DEG，涉及趋化因子信号、细胞因子-受体相互作用、NF-κB和TNF信号通路
**关键数据**：11个共享DEG；富集通路包括CCL21/CCL19/VCAM1等

## 总体结论
Fig. 3揭示了SCLC淋巴结转移过程中T细胞和B细胞景观的动态重编程，从效应T细胞主导的免疫激活状态转变为免疫抑制状态，为理解转移微环境的免疫逃逸机制提供重要见解。

## 关联 Figures / Extended Data
- **Fig. S5** — T/B细胞亚群的详细注释标记物
- **Fig. S6** — 保守转录趋势的详细分析
