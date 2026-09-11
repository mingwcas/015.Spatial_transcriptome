# ED Fig. 3 — Cross-Panel Consistency

## Caption（原文）
> Extended Data Fig. 3 | Cross-panel consistency across Xenium and Chromium. a, Spearman correlation of mean gene counts across technical replicates in targeted panels. Each dot represents a gene. b-c, Correlation of gene expression between Custom IO and (b) Prime 5K and (c) Lung panels in matched samples. d-g, Scatterplots of RCTD-inferred cell-type compositions across matched samples profiled with different panels. h, UMAPs of matched Chromium data using only genes in the corresponding targeted panels.

## Panel-by-Panel 解读

### Panel a — 技术重复相关性
**结论**：靶向面板的技术重复间高度一致，验证平台可重复性。

**关键数据**：
- Spearman R高
- 散点集中于对角线

### Panel b,c — Custom IO与5K/Lung的表达相关性
**结论**：Custom IO panel与5K和Lung panel均显示良好基因表达相关性。

**关键数据**：
- Custom IO vs 5K: R = 0.73-0.88
- Custom IO vs Lung: R高

### Panel d-g — 细胞类型组成一致性
**结论**：不同面板的细胞类型组成高度一致，尽管基因内容不同。

**关键数据**：
- 各面板组合R值均高

### Panel h — Chromium限制基因集UMAP
**结论**：Chromium数据即使限制在Xenium面板基因集内，也能清晰分离细胞类型。

**关键数据**：UMAP cluster清晰

## 总体结论
ED Fig. 3证明Xenium平台跨面板和跨技术的高度一致性，以及Chromium作为参考的可靠性。

## 关联 Figures / Extended Data
- **Fig. 2d** — 细胞类型组成散点图
