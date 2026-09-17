# Fig. 2 — Spatial co-mapping of gene expression and RNA processing in the mouse brain

## Caption（原文）
> (A) Patho-DBiT profiling of a mouse brain section. Left: H&E of an adjacent section. Middle: tissue scanning. Right: spatial pan-mRNA and UMI count maps.
> (B) Unsupervised clustering. The distribution aligned with the region annotation from the Allen Brain Atlas.
> (C) Integration of spatial data with scRNA-seq dataset.
> (D) Anatomical brain region labeling in the Patho-DBiT dataset.
> (E) Number of significant differentially spliced events and parental genes between brain region pairs under different read count thresholds.
> (F) Top-ranked 12 genes exhibiting significant regional differences in exon inclusion levels.
> (G and H) Junction read coverage of Myl6 (G) and Ppp3ca (H) splicing event in specific brain regions.
> (I) Left: spatial variations in A-to-I RNA editing. Right: distribution of editing ratio across all editing sites and the expression level of ADAR-encoding genes in different brain regions.
> (J) Left: spatial Adarb1 expression. Right: correlation between the Adarb1 expression and the average regional editing ratio across various brain regions, with the Spearman coefficient indicated.
> (K) Editing ratio correlation between 259 sites commonly detected by Patho-DBiT and long-read nanopore sequencing, as reported in the reference literature, with the Pearson coefficient indicated.

## Panel-by-Panel 解读

### Panel A — Mouse brain profiling
**结论**：Patho-DBiT成功应用于小鼠脑组织
**关键数据**：H&E、组织扫描和空间表达图谱一致

### Panel B — Unsupervised clustering
**结论**：无监督聚类与Allen脑图谱注释一致
**关键数据**：15个解剖学聚类

### Panel C — Integration with scRNA-seq
**结论**：空间数据与单细胞数据整合良好
**关键数据**：细胞类型注释一致

### Panel D — Anatomical labeling
**结论**：精确标注脑区解剖结构
**关键数据**：脑区边界清晰

### Panel E — Differentially spliced events
**结论**：不同脑区间存在大量差异剪接事件
**关键数据**：3,879个可变剪接事件，2,368个基因

### Panel F — Regional isoform switching
**结论**：12个基因显示显著的区域异构体转换
**关键数据**：外显子包含水平的区域差异

### Panel G — Myl6 splicing
**结论**：Myl6剪接在特定脑区特异性发生
**关键数据**：CA1区域特异性剪接

### Panel H — Ppp3ca splicing
**结论**：Ppp3ca剪接与阿尔茨海默病风险相关
**关键数据**：海马区域特异性剪接

### Panel I — A-to-I editing
**结论**：A-to-I编辑在不同脑区间存在显著差异
**关键数据**：丘脑显示高编辑比率

### Panel J — Adarb1 expression
**结论**：Adarb1表达与编辑比率相关
**关键数据**：Spearman相关系数显著

### Panel K — Editing ratio correlation
**结论**：Patho-DBiT与纳米孔测序编辑比率一致
**关键数据**：259个共同检测位点，Pearson相关系数高

## 总体结论
Fig. 2展示了Patho-DBiT在小鼠脑组织中同时分析基因表达和RNA加工的能力，揭示了可变剪接和RNA编辑的空间模式，证明了该技术在研究RNA生物学复杂性方面的强大功能。

## 关联 Figures / Extended Data
- ED Fig. S2 — 补充分析数据
- Table S1 — 差异剪接事件列表
