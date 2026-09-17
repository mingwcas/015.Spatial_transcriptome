# Fig. 3 — 分区测序计数分辨率受限的扩增子

## Caption（原文）
> Counting resolution-limited amplicons using partition sequencing. (a) The cDNA or padlock probe template can include three random nucleotides in equal proportions. By controlling the length of the complementary portion of the sequencing primer to the random bases, one can ligate fluorescent probes to different amplicon pools of varying sizes (fibroblasts; scale bars, 1 µm). This scheme works for single-base sequencing-by-ligation, and the SOLiD sequencing chemistry requires additional modifications to the bridge oligonucleotide. C, cytoplasm; N, nucleus. (b) Serial ligation reactions using the sequencing primers with 0–3 complementary bases to the random partitioning bases are analogous to doing a serial dilution experiment. The average count from each primer category can be used to extrapolate and estimate the actual amplicon count, regardless of the limitations in optical microscopy.

## Panel-by-Panel 解读

### Panel a — 分区测序原理
**结论**：通过3个随机核苷酸和不同互补长度的测序引物将扩增子分为64个子集

**关键数据**：
- 25% A:25% G:25% C:25% T 在3个随机位置
- 4³ = 64种可能的条形码路径
- 使用不同互补长度的引物（P1, P2, P3）：
  - P1互补3 bases → 16/64 bins
  - P2互补2 bases → 4/64 bins
  - P3互补1 base → 1/64 bins
- 显示成纤维细胞中的分区效果（比例尺1 µm）

### Panel b — 连续稀释外推法
**结论**：通过不同分区大小的计数外推估计实际扩增子数量

**关键数据**：
- 256：理论最大扩增子数
- 16 bins → 估计总数
- 4 bins → 估计总数
- 1 bin → 估计总数
- 类似于连续稀释实验的外推方法

## 总体结论
Fig. 3展示了一种巧妙的方法来解决FISSEQ中的关键问题：光学分辨率限制下无法区分空间重叠的扩增子。通过在cDNA模板中引入3个随机核苷酸，结合不同互补长度的测序引物，可以将扩增子分区到不同子集进行计数，然后通过外推估计实际数量。此策略使得即使在低分辨率显微镜下也能准确量化扩增子。

## 关联 Figures / Extended Data
- **Fig. 1b** — 扩增子结构
- 论文正文"Partition sequencing"部分
