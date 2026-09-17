# Fig. 6 — Heatmap for Quality Control of DSP Data

## Caption（原文）
> FIGURE 6 | Heatmap of an initial dataset obtained with DSP assay to illustrate the visualization of data as quality control tool. The DSP counts of one region of interest indicated with a black arrow show no or very low DSP counts from all targets of the DSP protein panel, including the housekeeper proteins: GAPDH, Histone3 and S6. The DSP quality control report showed a positive control normalization tag in this specific region of interest.

## Panel-by-Panel 解读

*注：Figure 6 为单一 QC 热图，无独立 panels。以下为整体解读。*

### Heatmap — 初始数据集 QC 热图
**结论**：热图是 DSP 数据集初始 QC 的首选可视化工具，可快速识别异常 AOI（黑箭头所示 ROI 所有靶标包括 housekeeper 蛋白 GAPDH、Histone3 和 S6 均无信号或极低），该 AOI 的 QC 报告显示 positive control normalization 异常。

**关键数据**：
- Housekeeper 蛋白（GAPDH, Histone3, S6）在所有正常 AOI 中均有较高表达
- 异常 AOI（黑箭头）中所有 housekeepers 几乎为零，表明存在技术问题（可能为蒸发损失）
- 热图中的蓝色竖条（低表达）提示该 ROI 存在数据质量问题

## 总体结论
Figure 6 展示了 GeoMx Data Analysis Suite 内置热图在 DSP 质量控制中的核心作用。热图能够将数百个 AOI × 数十个靶标的计数数据以颜色编码方式快速呈现，使研究者能够一眼识别异常模式。该图特别指出了两种 QC 失败类型：（1）所有靶标极低——通常由 oligo 收集过程中的蒸发问题导致；（2）housekeeper 蛋白信号异常——提示该 AOI 的数据不可靠。在实际数据分析中，所有 QC 异常的 AOI 应在病理学家确认后予以排除，以避免下游分析引入假阴性或假阳性结果。

## 关联 Figures / Extended Data
- 与 Methods 06（Data Output and Analysis）和 Methods 08（Data Normalization）直接关联
- 该图的 QC 流程是所有 DSP 研究的必经步骤
