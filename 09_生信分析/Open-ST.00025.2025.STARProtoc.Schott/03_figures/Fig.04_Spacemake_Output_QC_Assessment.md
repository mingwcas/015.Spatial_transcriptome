# Fig. 4 — File structure after running spacemake and first assessment of quality of datasets

## Caption（原文）
> (A) Walkthrough of the folder structure from the spacemake root directory to two key files: the h5ad object containing the spatial cell-by-gene expression matrix, and the QC report in HTML format.
> (B) Mapping statistics for a high quality sample. For samples sequenced at similar depth (~500 M), these numbers are representative of the capabilities of Open-ST. Different values (especially, lower uniquely mapping and higher rRNA), might indicate issues with the tissue.
> (C) Visual validation of spatial mapping. Shown is a high quality sample where, as expected, reads per UMI are uniform in space, and UMI density distinguishes tissue from background.
> (D) Metrics over beads (in this case, each from the default 7 μm-side hexagonal grid). Shown is a "gold standard", i.e., these metrics are expected for a sample with high quality. In particular, PCR bias (# of reads / UMIs) values should tend to 1; lower values are indicative of more complex libraries (desired). The QC reports show all distributions for 7 μm-side hexagons, without filtering, i.e., all pseudocells are included regardless of being in or out of the tissue. These are useful for assessing the background levels (outside of tissue) across all metrics. mLN: human metastatic lymph node.

## Panel-by-Panel 解读

### Panel A — Folder structure
**结论**：展示了 spacemake 输出的文件组织结构，包括 h5ad 对象和 QC 报告。

**关键数据**：主要输出为 h5ad 格式的空间表达矩阵和 HTML 格式的 QC 报告。

### Panel B — Mapping statistics
**结论**：展示了高质量样本的比对统计信息。

**关键数据**：约 75% 唯一比对率，约 7% rRNA 含量，约 11% mt-RNA/细胞。

### Panel C — Spatial mapping validation
**结论**：展示了空间映射的视觉验证，UMI 密度区分组织和背景。

**关键数据**：reads/UMI 在空间上均匀分布，表明无明显技术偏差。

### Panel D — Bead metrics
**结论**：展示了 7 μm 六边形网格的各项质量指标。

**关键数据**：PCR bias（reads/UMI）应接近 1，越低表示文库复杂度越高。

## 总体结论
Fig. 4 展示了 spacemake 流程的输出结构和质量评估方法。QC 报告提供了全面的样本质量指标，包括比对率、rRNA 含量、UMI 和基因检测数量等。视觉验证可以快速识别空间映射问题。高质量样本应显示一致的基因和 UMI 计数、清晰的组织-背景分离，以及接近 1 的 PCR bias 值。这些指标对于评估 Open-ST 实验的成功与否至关重要。

## 关联 Figures / Extended Data
- **Fig. 9** — Quality control assessment of Open-ST data from metastatic lymph node sections
