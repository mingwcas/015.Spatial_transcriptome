# Fig. 2 — scRNA-seq identifies subdivisions of previously defined marker populations

## Caption（原文）
> Fig. 2. scRNA-seq identifies subdivisions of cells that express markers previously associated with single neuronal populations. (A to C) Expression distributions of selected marker genes and genes of interest in all neuronal clusters that are statistically enriched [Model-based Analysis of Single-cell Transcriptomics (MAST) (75), false discovery rate <0.01] in (A) galanin (Gal), (B) tyrosine hydroxylase (Th), or (C) Bdnf and Adcyap1. Gene names in black indicate differentially expressed genes for each selected neuronal cluster. Gene names in blue indicate inhibitory (Gad1, Gad2, Slc32a1) and excitatory (Slc17a6) neuronal markers, as well as dopaminergic markers (Ddc, Slc6a3, and Slc18a2). Gene names in green indicate sex hormone receptors. The y axis on each violin plot depicts the log transformed counts with the range set to the 95% expression quantile of the cluster with the highest expression (29). The sizes of red, cyan, and yellow circles correspond to the cell abundance of the inhibitory, excitatory, and hybrid clusters, respectively.

## Panel-by-Panel 解读

### Panel A — Galanin（Gal）细分
**结论**：Gal 阳性细胞不是单一类型，而是 7 个具有不同 marker 与激素受体谱的集群。

**关键数据**：7 个 Gal-enriched clusters；示例 i20:Gal/Moxd1 与 e24:Gal/Rxfp1 的性激素受体谱明显不同。

### Panel B — Tyrosine hydroxylase（Th）细分
**结论**：Th 细胞被分成多个分子群，只有部分具备完整多巴胺合成/转运程序。

**关键数据**：6 个 Th-enriched clusters；仅 i16:Gal/Th 与 i38:Kiss1/Th 同时表达 Ddc 与 Slc18a2/Vmat2。

### Panel C — Bdnf/Adcyap1 细分
**结论**：所谓 warm-sensitive 神经元标记 Bdnf/Adcyap1 覆盖多个兴奋性或混合集群，而不是单一细胞群。

**关键数据**：9 个 Adcyap1/Bdnf-enriched clusters；均表达 Gad2 与 Slc17a6，仅 1 个表达 Slc32a1。

## 总体结论
Fig. 2 证明传统上按单个 marker 定义的 Gal、Th 和 Bdnf/Adcyap1 细胞群内部存在显著分子异质性。MAST FDR < 0.01 的 marker 分布、抑制/兴奋标志及性激素受体共同显示，功能研究必须采用 marker 组合而非单基因定义细胞类型。

## 关联 Figures / Extended Data
- Fig. 1C–D：神经元集群的整体层级结构
- Fig. 7：Gal 与 Adcyap1 集群的 MERFISH 空间细分
- fig. S7：双色 ISH marker 验证
