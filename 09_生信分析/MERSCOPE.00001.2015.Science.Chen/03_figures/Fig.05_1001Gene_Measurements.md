# Fig. 5 — Simultaneous measurement of 1001 RNA species

## Caption（原文）
> Fig. 5. Simultaneous measurements of 1001 RNA species in single cells using MERFISH with a 14-bit MHD2 code. (A) The localizations of all detected single molecules in a cell colored based on their measured binary words. Inset: the composite, false-colored fluorescent image of the 14 hybridization rounds for the boxed sub-region with numbered circles indicating potential RNA molecules. Red circles indicate unidentifiable molecules, the binary words of which do not match any of the 14-bit MHD2 code words. Images of individual hybridization round are shown in fig. S9A. (B) Scatter plot of the average copy number per cell measured in the 1001-gene experiments versus the abundance measured via bulk sequencing. The black symbols are for the 73% of genes detected with confidence ratios higher than the maximum ratio observed for the misidentification controls. The Pearson correlation coefficient is 0.76 with a P value of 3x10−133. The red symbols are for the remaining 27% of genes. The Pearson correlation coefficient is 0.65 with a P value of 3x10−33. (C) Scatter plot of the average copy number for the 107 genes shared in both the 1001-gene measurement with the MHD2 code and the 140-gene measurement with the MHD4 code. The Pearson correlation coefficient is 0.89 with a P value of 9x10−30. The dashed line is correspond to the y = x line.

## Panel-by-Panel 解读

### Panel A — 1001-gene molecule localizations
**结论**：即使 MHD2 没有纠错，14 轮成像仍能在单细胞中同时读取数百 RNA species。

**关键数据**：一个细胞检测到 430 RNA species；约 200 cells、3 个独立实验复现；红圈为不匹配任何 14-bit MHD2 code word 的分子。

### Panel B — MERFISH vs bulk RNA-seq
**结论**：高置信基因的 MERFISH copy number 与 bulk abundance 保持良好线性相关，低置信基因相关性稍弱但仍可用。

**关键数据**：73% genes：Pearson r = 0.76，P = 3×10^−133；其余 27%：r = 0.65，P = 3×10^−33。

### Panel C — Shared genes and MHD4 comparison
**结论**：同一批 shared genes 在 MHD2 与 MHD4 实验中的相对丰度仍高度一致，说明无纠错主要降低检测效率而非改变排序。

**关键数据**：107 个 shared genes；Pearson r = 0.89，P = 9×10^−30；总 counts 约为 140-gene 实验的 1/3，calling rate 约下降 3-fold。

## 总体结论
Fig. 5 展示 MERFISH 通过牺牲纠错能力换取通量的工程折中：14-bit MHD2 用约 94 probes/gene 与 14 轮杂交扩展到 1001 个 code words，实际细胞中检测到 430 RNA species。MHD2 的 calling rate 约为 MHD4 的 1/3、misidentification 更高（real words 高于 control 中位数的比例由 95% 降至 77%），但相对丰度仍可由 bulk RNA-seq 与 shared-gene 对照验证。

## 关联 Figures / Extended Data
- Fig. 1（MHD2/MHD4 编码原理与通量预测）
- Fig. 2（140-gene MHD4 基准）
- Fig. 6（1001-gene 共变分析）
- Fig. S8、S9（smFISH 与逐轮成像补充验证）
