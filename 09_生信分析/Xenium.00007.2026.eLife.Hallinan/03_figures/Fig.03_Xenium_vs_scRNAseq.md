# Fig. 3 — Xenium 与 scRNA-seq 单细胞表达模式比较

## Caption（原文）
> Figure 3. Comparison of single-cell gene expression patterns between Xenium and single-cell RNA sequencing (scRNA-seq). (A) Harmonized Uniform Manifold Approximation and Projection (UMAP) visualization of MS4A1 expression for Xenium and scRNA-seq data, accompanied by a scatterplot comparing Xenium vs. scRNA-seq MS4A1 cluster expression. The dotted line indicates the identity line (X = Y), and the solid line represents the line of best fit. (B) Comparison of APOBEC3B expression patterns on harmonized UMAP: Xenium expression, scRNA-seq expression, an aggregated scRNA-seq profile combining APOBEC3B and its predicted off-target genes' expression APOBEC3D and APOBEC3F, and scRNA-seq expression of APOBEC3B's predicted off-targets APOBEC3D and APOBEC3F. Two scatterplots are shown: one comparing Xenium vs. scRNA-seq for APOBEC3B cluster expression alone, and one comparing Xenium vs. the aggregated scRNA-seq cluster expression of APOBEC3B and its predicted off-targets. The dotted line indicates the identity line (X = Y), and the solid line represents the line of best fit. (C) Scatterplot of log-transformed total expression counts (with a pseudocount) for 313 genes between Visium and scRNA-seq data. The dotted line indicates the identity line (X = Y), and points (genes) are colored by probe information.

## Panel-by-Panel 解读

### Panel A — MS4A1 的跨技术整合 UMAP
**结论**：经 Harmony 校正批次效应后，Xenium 与 scRNA-seq 在同一 UMAP 嵌入中表达模式一致，无预测脱靶的基因在两技术间可比较。

**关键数据**：
- Harmony v1.2.3，top 30 PCs，theta = 8
- CPM + log(x+1) 归一化，pseudocount = 1

### Panel B — APOBEC3B 及其预测脱靶基因
**结论**：Xenium 的 APOBEC3B 表达更接近 scRNA-seq 中"APOBEC3B + APOBEC3D + APOBEC3F"的**聚合**表达，而非 APOBEC3B 单独表达，进一步证实脱靶结合。

**关键数据**：
- APOBEC3B 单独：Xenium vs scRNA-seq Pearson r = 0.653
- 聚合 APOBEC3B+ACTB+POTEM+POTEE+POTEF+POTEI+POTEJ+ACTA1 等脱靶后：r 提升至 0.813
- TUBB2B：单独 r = 0.015 → 加入 TUBB2A 后 r = 0.793（最显著的提升案例）

### Panel C — 313 基因总体一致性
**结论**：两技术总表达量整体强正相关，与 Visium 比较结果一致，说明平台间差异是局部（特定位点）而非全局的。

**关键数据**：
- scRNA-seq：12,388 个细胞，36,601 个基因
- 全部 313 个 Xenium 基因均存在于 scRNA-seq 数据中
- Leiden 聚类分辨率 = 1.0；少于 10 个细胞的簇被排除

## 总体结论
Fig. 3 用单细胞分辨率数据独立验证了 Fig. 2 的空间结论：对 TUBB2B 而言，加入脱靶基因后相关性从 r = 0.015 跃升至 0.793，这是脱靶结合最有力的定量证据。该图表明脱靶效应对部分基因可造成近乎彻底的表达模式扭曲。

## 关联 Figures / Extended Data
- Appendix 1—figure 5 — 跨技术共享 UMAP 嵌入
- Appendix 1—figure 8 — ACTG2 / TUBB2B 的 scRNA-seq 验证
- Appendix 1—figure 11 — 脱靶基因是否表达对结果影响的分析
