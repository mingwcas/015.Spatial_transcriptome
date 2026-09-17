# Fig. 9 — Quality control assessment of Open-ST data from metastatic lymph node sections

## Caption（原文）
> (A) Barplots displaying key metrics across all processed sections, including total reads, uniquely mapped reads, rRNA mapped reads, median mt-RNA percentage per cell, number of cells, median PCR bias, median UMI, and median genes detected. Red dashed lines indicate median values, while blue and green dotted lines represent the first (Q1) and third (Q3) quartiles, respectively.
> (B) Spatial plots of UMI per cell (top row) and PCR bias (bottom row) for six representative sections. Here, a regular grid of 7 μm hexagons is used instead of cell segmentation for the first QC of the data. Only cells passing a cutoff of 250 UMIs are displayed. UMI counts show clear spatial correlation with tissue structure, while PCR bias remains relatively uniform across the tissue, as expected for high-quality data. Color scales are consistent across all sections for each metric, facilitating direct comparisons. In (B), only the first 60 μm across the Z-axis (out of 350 μm) are shown for illustrative purposes. Note that some spatial artifacts are visible, such as higher UMI content in one swath of section #3, and incomplete coverage in sections 6-7. These issues were identified in this early experiment, leading to the discovery of 1.5 cm blind spots at the flow cell ends, which are now accounted for in the protocol.

## Panel-by-Panel 解读

### Panel A — Cross-section metrics
**结论**：展示了所有处理切片的关键质量指标。

**关键数据**：约 75% 唯一比对率，约 7% rRNA，约 11% mt-RNA/细胞，中位数 ~800 UMIs/细胞。

### Panel B — Spatial QC plots
**结论**：展示了 6 个代表性切片的 UMI 和 PCR bias 空间分布。

**关键数据**：UMI 与组织结构空间相关，PCR bias 在组织上均匀分布。部分切片可见空间伪影。

## 总体结论
Fig. 9 展示了 Open-ST 数据的全面质量控制评估。跨切片的质量指标显示一致的性能，表明方法的可重复性。空间 QC 图可以快速识别技术问题，如 UMI 分布不均或 PCR bias 异常。部分切片显示的空间伪影（如 swath 间差异、不完整覆盖）已被识别并在后续协议中改进。这些 QC 指标对于评估实验成功与否至关重要。

## 关联 Figures / Extended Data
- **Fig. 4** — File structure and QC assessment
