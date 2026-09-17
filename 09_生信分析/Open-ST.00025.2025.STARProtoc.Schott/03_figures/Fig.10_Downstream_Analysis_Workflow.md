# Fig. 10 — Typical downstream analysis workflow for Open-ST data

## Caption（原文）
> (A) Initial data processing steps. The analysis begins with the stitched_segmented.h5ad file, which undergoes metrics calculation per segmented cell and filtering, followed by spatial validation of the data.
> (B) Core analysis pipeline. The workflow continues with gene normalization, dimensionality reduction, and clustering of the data to yield cell types (or regions) in space.
> (C) After clustering, marker gene analysis is performed, including ranking plots and spatial validation of gene expression patterns, which help with the annotation of expression clusters, and lead to the identification of potentially novel disease-relevant candidate genes and gene programs, in space.
> (D) Using ParaView for 3D visualization of spatial gene expression in the histology context allows the validation of the annotations and their spatial patterns.

## Panel-by-Panel 解读

### Panel A — Data preprocessing
**结论**：展示了从分割后 h5ad 文件开始的数据预处理步骤。

**关键数据**：包括细胞过滤、指标计算和空间验证。

### Panel B — Core analysis pipeline
**结论**：展示了基因归一化、降维和聚类的核心分析流程。

**关键数据**：使用 scanpy 进行标准单细胞分析。

### Panel C — Marker gene analysis
**结论**：展示了聚类后的标记基因分析，包括排序图和空间验证。

**关键数据**：差异表达分析识别细胞类型特异的标记基因。

### Panel D — 3D visualization
**结论**：展示了使用 ParaView 进行 3D 可视化的方法。

**关键数据**：可以在组织学背景下可视化基因表达的 3D 模式。

## 总体结论
Fig. 10 展示了 Open-ST 数据的典型下游分析流程。从预处理到 3D 可视化，每个步骤都旨在从空间转录组数据中提取生物学洞见。scanpy 提供了从聚类到差异表达的完整分析工具，而 ParaView 实现了 3D 可视化。这个流程可以揭示细胞异质性、空间组织模式和疾病相关的基因表达变化。

## 关联 Figures / Extended Data
- 无直接关联的 Extended Data
