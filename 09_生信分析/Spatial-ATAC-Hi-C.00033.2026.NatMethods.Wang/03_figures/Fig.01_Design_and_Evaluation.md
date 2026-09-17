# Fig. 1 — Design and evaluation of Spatial-ATAC-Hi-C data

## Caption（原文）
> a, Schematic workflow. b, Imputed single-pixel Hi-C map at 25-kb resolution in mouse brain R6 sample at genomic region chr2: 106–118 Mb. Spatial locations for each pixel and the selected single pixels are highlighted in red (left). Corresponding Hi-C maps of the three selected pixels (right). c, Hi-C maps (top) and PC1 value tracks (bottom) of Spatial-ATAC-Hi-C in mouse brain R8 sample, in situ Hi-C and Spatial-ATAC-Hi-C without barcoding (Spatial-no-barcoding) from adjacent mouse R8 tissues at chr2 regions. d, Comparison of aggregated chromatin accessibility profiles of Spatial-ATAC-Hi-C in mouse brain R6 sample with bulk ATAC-seq from adjacent mouse brain R6 tissue and the ATAC-seq profiles in the forebrain, midbrain and hindbrain of E16.5 mouse embryos from ENCODE consortium at genomic region chr7: 19.57–19.78 Mb. e, Violin plot showing the number of unique total contacts in each sample at log10 scale. The number of pixels in each sample is n = 2,500. f, Violin plot showing the fraction of long-range (≥10 kb) contacts over the unique intra-chromosomal contacts. The number of pixels in each sample is n = 2,500. g, Enrichment of spatial sequencing reads around TSSs in each sample. Box plots overlaid on violin plots in e and f show the median (center line), the 25th and 75th percentiles (box limits) and whiskers extending to the most extreme data points within 1.5 × IQR of the lower and upper quartiles. Outliers beyond the whiskers are not shown. Panel a created in BioRender; Wang, P. https://biorender.com/jp386u0 (2026).

## Panel-by-Panel 解读

### Panel a — 技术流程示意图
**结论**：展示了Spatial-ATAC-Hi-C的完整实验流程，包括组织固定、核透化、酶切消化、原位连接、Tn5转座、空间条形码标记、测序和数据分析等步骤。

**关键数据**：技术采用微流控条形码系统，水平条形码A（A1–A50）和垂直条形码B（B1–B50）依次递送到组织表面，创建二维空间条形码组织像素网格（n=2,500）。

### Panel b — 单像素Hi-C图谱
**结论**：展示了在25-kb分辨率下单像素水平的Hi-C接触图谱，证明技术能够在单像素水平捕获染色质相互作用。

**关键数据**：基因组区域chr2: 106–118 Mb，展示了三个选定像素（Pixel_23_13, Pixel_28_17, Pixel_23_34）的Hi-C图谱。

### Panel c — 技术验证：与in situ Hi-C比较
**结论**：Spatial-ATAC-Hi-C与in situ Hi-C及无条形码对照组在Hi-C接触图谱和PC1值上高度一致，证明条形码步骤不影响3D基因组架构的捕获。

**关键数据**：三组数据集（Spatial-ATAC-Hi-C、in situ Hi-C、Spatial-no-barcoding）在chr2区域的PC1值和绝缘分数高度一致。

### Panel d — 染色质可及性验证
**结论**：Spatial-ATAC-Hi-C的ATAC-seq数据与批量ATAC-seq及ENCODE数据高度一致，证明技术能够准确捕获染色质可及性信息。

**关键数据**：基因组区域chr7: 19.57–19.78 Mb，展示了与邻近组织批量ATAC-seq及ENCODE前脑、中脑、后脑数据的比较。

### Panel e — 唯一总接触数
**结论**：不同样本中每个像素的唯一总接触数分布，展示了技术的测序深度。

**关键数据**：中位数25,343–58,403个总接触/像素，每个像素平均包含约3–21个细胞。

### Panel f — 长程接触比例
**结论**：长程接触（≥10 kb）在所有样本中的比例为24–33.3%，与单细胞Hi-C方法（Droplet Hi-C、single-cell Hi-C、sciHi-C）相当。

**关键数据**：88.1–90.3%的接触为染色体内接触，24–33.3%为长程相互作用（>10 kb）。

### Panel g — TSS富集
**结论**：ATAC-seq信号在TSS周围显示出清晰的富集峰和核小体周期性模式，确认了ATAC-seq数据的质量。

**关键数据**：TSS富集模式与已发表的空间ATAC-seq数据相当。

## 总体结论
Fig. 1全面展示了Spatial-ATAC-Hi-C技术的设计原理、实验流程和数据质量评估。通过与批量Hi-C、ATAC-seq及ENCODE数据的系统比较，证明该技术能够准确捕获3D基因组架构和染色质可及性信息，且条形码步骤不引入显著偏差。技术在多个样本中均表现出稳定的测序深度和高质量的数据产出。

## 关联 Figures / Extended Data
- Extended Data Fig. 1（Hi-C接触图谱、PC1值和绝缘分数的详细比较）
- Extended Data Fig. 2（ATAC-seq数据的详细验证）
- Extended Data Fig. 3（Hi-C读段在开放染色质区域的富集分析）
- Extended Data Fig. 4（测序质量指标和与其他单细胞Hi-C方法的比较）
