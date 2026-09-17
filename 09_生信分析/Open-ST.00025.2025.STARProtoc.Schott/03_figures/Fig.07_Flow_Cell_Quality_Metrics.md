# Fig. 7 — Quality metrics of a barcoded Illumina NovaSeq 6000 S4 flow cell

## Caption（原文）
> (A) Raw and passing filter (PF) cluster density per lane; from the Illumina Sequencing Analysis Viewer (SAV, v.3.0.0).
> (B) Heatmap of sequencing quality score (Q score) per cycle from the Illumina SAV. >Q30 indicates an inferred base call quality of >99.9%.
> (C) Barcode base content (%) per sequencing cycle.

## Panel-by-Panel 解读

### Panel A — Cluster density
**结论**：展示了 S4 flow cell 每个 lane 的原始和通过过滤的簇密度。

**关键数据**：预期 ~85% R Q30，~73% passing filter，~97% clusters occupied。

### Panel B — Quality score heatmap
**结论**：展示了每个测序周期的质量分数热图。

**关键数据**：>Q30 表示碱基识别质量 >99.9%。

### Panel C — Barcode base content
**结论**：展示了每个测序周期的条形码碱基组成。

**关键数据**：碱基组成应遵循 HDMI32 寡核苷酸的设计模式（NNNNNBNNBNNBNNBNNBNNBNNBVNBNNA）。

## 总体结论
Fig. 7 展示了条形码测序 flow cell 的质量指标，这是 Open-ST 捕获区域生成的关键步骤。高质量的 flow cell 应显示高簇密度、高质量分数和正确的条形码碱基组成。这些指标确保捕获区域上的空间条形码质量良好，为空间转录组捕获奠定基础。

## 关联 Figures / Extended Data
- 无直接关联的 Extended Data
