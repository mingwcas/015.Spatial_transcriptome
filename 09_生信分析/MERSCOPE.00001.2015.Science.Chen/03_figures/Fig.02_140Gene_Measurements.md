# Fig. 2 — Simultaneous measurement of 140 RNA species

## Caption（原文）
> Fig. 2. Simultaneous measurement of 140 RNA species in single cells using MERFISH with a 16-bit MHD4 code. (A) Images of RNA molecules in an IMR90 cell after each hybridization round (hyb 1 – hyb 16). The image after photobleaching (bleach 1) demonstrates efficient removal of fluorescent signals between hybridizations. (B) The localizations of all detected single molecules in this cell colored based on their measured binary words. Inset: the composite, false-colored fluorescent image of the 16 hybridization rounds for the boxed sub-region with numbered circles indicating potential RNA molecules. A red circle indicates an unidentifiable molecule, the binary word of which does not match any of the 16-bit MHD4 code words even after error correction. (C) Fluorescent images from each round of hybridization for the boxed sub-region in (B) with circles indicating potential RNA molecules. (D) Corresponding words for the spots identified in (C). Red crosses represent the corrected bits. (E) The RNA copy number for each gene observed without (green) or with (blue) error correction in this cell. (F) The confidence ratio measured for the 130 RNA species (blue) and the 10 misidentification control words (red) normalized to the maximum value observed from the misidentification controls (dashed line). (G) Scatter plot of the average copy number of each RNA species per cell measured with two shuffled codebooks of the MHD4 code. The Pearson correlation coefficient is 0.94 with a p-value of 1x10−53. The dashed line corresponds to the y = x line. (H) Scatter plot of the average copy number of each RNA species per cell versus the abundance determined by bulk sequencing in fragments per kilobase per million reads (FPKM). The Pearson correlation coefficient between the logarithmic abundances of the two measurements was 0.89 with a p-value of 3x10−39.

## Panel-by-Panel 解读

### Panel A — 16 rounds in an IMR90 cell
**结论**：16 轮连续杂交、成像和漂白可以稳定记录单分子信号。

**关键数据**：hyb 1–16；bleach 1 显示漂白有效。约 400 cells 来自 7 个独立实验。

### Panel B — Localizations and binary-word colors
**结论**：把一个细胞中所有检测到的 single molecules 按 measured binary word 着色并定位。

**关键数据**：红圈为即使纠错后也不匹配 16-bit MHD4 code word 的不可识别分子。

### Panel C — Boxed sub-region images
**结论**：同一 boxed 区域的轮次图像展示每个候选 RNA 的 on/off 信号轨迹。

**关键数据**：每个 spot 的跨轮次位置由 fiducial beads 对齐，典型 alignment error ~20 nm。

### Panel D — Corresponding words
**结论**：每个候选分子转换为二进制词；红叉明确显示 MHD4 纠正的错误 bit。

**关键数据**：MHD4 接受 exact match 或 one-bit error-correctable match。

### Panel E — Copy number with/without correction
**结论**：错误纠正显著恢复漏检分子与 RNA species 数量。

**关键数据**：示例细胞纠错后 >1500 molecules，覆盖 87% 的 130 encoded RNA species；分子数约为纠错前 4 倍，species 数约 2 倍。

### Panel F — Confidence ratio
**结论**：真实 RNA words 的可信度高于 misidentification controls，可据此筛除低可信物种。

**关键数据**：91% of 130 RNA species 的 confidence ratio 高于 controls 最大值；95% real words 的计数高于 controls 中位数。

### Panel G — Shuffled codebooks
**结论**：更换并打乱 codebook 后，拷贝数仍高度一致，说明编码方案没有明显技术偏倚。

**关键数据**：Pearson r = 0.94，p = 1×10^−53。

### Panel H — Bulk RNA-seq comparison
**结论**：MERFISH 的平均 RNA 丰度与 bulk sequencing 的相对丰度高度吻合。

**关键数据**：Pearson r = 0.89，p = 3×10^−39；对低至至少 1 copy/cell 的 RNA 仍有灵敏度。

## 总体结论
Fig. 2 首次在单细胞中展示 140-species MERFISH 的完整证据链：多轮图像稳定、MHD4 纠错能显著增加调用、控制词揭示低 misidentification、独立 codebook 重复与 bulk RNA-seq 均验证定量可靠性。15 个基因的 conventional smFISH 进一步给出 MERFISH/smFISH copy ratio = 0.82 ± 0.06，与约 80% calling rate 一致。

## 关联 Figures / Extended Data
- Fig. 1（MHD4 原理）
- Fig. 3（140 基因细胞间共变）
- Fig. S5–S8（纠错、错误率、smFISH 验证）
