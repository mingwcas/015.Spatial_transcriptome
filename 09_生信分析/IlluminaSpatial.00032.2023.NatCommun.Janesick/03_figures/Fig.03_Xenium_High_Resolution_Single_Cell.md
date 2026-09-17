# Fig. 3 — Xenium data provide high-resolution single-cell information with spatial localization

## Caption（原文）
> a Maximum intensity projection of RNA fluorescence signal in Cycle 1 from a 5 μm FFPE section. Fifteen of such images (unprojected, original z-stacks), one per cycle, were input into the on-instrument pipeline to decode 313 genes. Scale bar = 1 mm. b Selected genes representing major cell types are shown: stromal (POSTN, yellow), lymphocytes (IL7R, blue), macrophage (ITGAX, turquoise), myoepithelial (ACTA2, KRT15, green), endothelial (VWF, dark blue), DCIS (CEACAM6, pink), and invasive tumor (FASN, red). c H&E staining performed post-Xenium workflow, highlighting the minimal impact of the Xenium assay on tissue integrity. d Deep learning-based cell segmentation assigns individual transcripts to cells. Scale bar = 0.1 mm. e Histogram showing the distribution of transcripts per cell (Q ≥20). Dotted lines: 10th percentile = 61 and 90th percentile = 372 median transcripts per cell. Solid line: 50th percentile = 166 median transcripts per cell. f Log10(transcripts per cell) across the entire section. g, h Bar plots showing the number of genes detected per cell for scFFPE-seq (downsampled to the 313 genes on the Xenium panel) compared to Xenium. i t-SNE projection of scFFPE-seq data using all 17,696 genes (left) then down-selected to 313 genes (right). j t-SNE projection of Xenium cells annotated using supervised labels derived from scFFPE-seq data. Cells which were not unambiguously identified in the Xenium data (<50% of the nearest neighbors coming from one cell type) were unlabeled (~14% of cells). j′ t-SNE projection of Xenium cells annotated using unsupervised labels, agnostic to the scFFPE-seq data. k Heatmap representation of the t-SNE j showing the relative expression of genes across different cell types found in the Xenium data. Scale bar is a z-score computed across cell types for each gene by subtracting the mean and dividing by the standard deviation. See Supp. Figure 3 for the corresponding scFFPE-seq heatmap. l Spatial plot with cell type labels transferred. The Xenium experiment was performed in replicate on two serial sections, with one representative section shown here. The scFFPE-seq data is N = 1 due to inherent limitations in using a single block for multiple technologies (see "Methods").

## Panel-by-Panel 解读

### Panel a — Cycle 1 RNA 荧光信号最大强度投影
**结论**：展示了 Xenium 第一轮解码循环的 RNA 荧光信号最大强度投影，清晰呈现了 5 μm FFPE 切片的组织结构细节。

**关键数据**：15 张图像（每轮一张）输入仪器 pipeline 解码 313 个基因；比例尺 = 1 mm。

### Panel b — 主要细胞类型标记基因空间分布
**结论**：选定的标记基因成功标识了主要细胞类型的空间定位，包括基质细胞（POSTN）、淋巴细胞（IL7R）、巨噬细胞（ITGAX）、肌上皮细胞（ACTA2, KRT15）、内皮细胞（VWF）、DCIS（CEACAM6）和侵袭性肿瘤（FASN）。

**关键数据**：7 种主要细胞类型的标记基因空间分布。

### Panel c — Xenium 后 H&E 染色
**结论**：Xenium 工作流程后进行的 H&E 染色保持了高质量的组织形态学，证明 Xenium 分析对组织完整性的影响极小。

**关键数据**：后 Xenium H&E 染色质量与标准 H&E 可比。

### Panel d — 深度学习细胞分割
**结论**：基于深度学习的细胞分割将单个转录本分配到细胞中，实现了亚细胞分辨率的空间转录组分析。

**关键数据**：比例尺 = 0.1 mm。

### Panel e, f — 每细胞转录本分布
**结论**：转录本/细胞的分布呈典型的右偏分布，中位数为 166 个转录本/细胞。

**关键数据**：167,885 个总细胞；36,944,521 个总转录本（Q score ≥20）；中位数 166 转录本/细胞；第 10 百分位 = 61；第 90 百分位 = 372。

### Panel g, h — scFFPE-seq 与 Xenium 基因检测数比较
**结论**：在相同的 313 基因面板下，Xenium 每细胞检测到的基因数（中位数 62）高于 scFFPE-seq（中位数 34），体现了 Xenium 的高灵敏度。

**关键数据**：scFFPE-seq 下采样至 313 基因后中位数 34 基因/细胞；Xenium 中位数 62 基因/细胞。

### Panel i — scFFPE-seq t-SNE（全基因 vs 313 基因）
**结论**：scFFPE-seq 数据从全部 17,696 个基因下选至 313 个 Xenium 面板基因后，仍能识别相同的细胞类型群体，验证了 Xenium 乳腺面板忠实捕捉生物异质性。

**关键数据**：17,696 个全基因 → 313 个基因（仅占全转录组的 1.8%）。

### Panel j, j′ — 监督标注与非监督标注比较
**结论**：监督标注（基于 scFFPE-seq 标签转移）识别了 86% 的细胞为单一细胞类型；非监督标注产生了类似的细胞类型注释，但未能区分 DCIS 亚型和增殖性肿瘤细胞，突出了整合分析的价值。

**关键数据**：86% 的细胞被明确识别为单一细胞类型；~14% 的细胞未标记。

### Panel k — Xenium 热图
**结论**：热图展示了 Xenium 数据中不同细胞类型间基因的相对表达模式，证实了细胞类型特异性标记基因的正确表达。

**关键数据**：z-score 标准化的基因表达热图。

### Panel l — 空间细胞类型图
**结论**：将细胞类型标签映射到空间位置，生成完整的 Xenium 空间细胞类型图谱，可视化了整个组织切片中各类细胞的分布。

**关键数据**：技术重复在两个连续切片上进行，结果一致。

## 总体结论
该图全面展示了 Xenium In Situ 技术在 FFPE 乳腺癌样本上的性能：313 基因靶向面板能够以亚细胞分辨率检测空间定位的基因表达，每细胞中位数 166 个转录本和 62 个基因。通过与 scFFPE-seq 数据的整合（监督标注），86% 的细胞被明确识别为单一细胞类型。Xenium 面板仅占全转录组的 1.8%，但忠实地捕捉了主要的生物异质性。非监督和监督标注的互补使用进一步丰富了细胞类型注释信息。

## 关联 Figures / Extended Data
- Fig. 2（scFFPE-seq 和 Visium 表征）
- Supp. Figure 2（复杂度和阴性对照）
- Supp. Figure 3（scFFPE-seq 热图）
- Supp. Figure 4（完整空间图）
- Supp. Figure 5（重复性验证）
- Supp. Figure 6（脂肪细胞分析）
- Supp. Figure 7（灵敏度基准比较）
- Supp. Figure 8（Visium-Xenium 比较）
- Supp. Figure 9（免疫荧光验证）
