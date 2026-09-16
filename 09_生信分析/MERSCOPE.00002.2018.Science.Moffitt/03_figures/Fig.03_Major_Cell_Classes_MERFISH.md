# Fig. 3 — Major cell classes and their spatial organizations in the preoptic region

## Caption（原文）
> Fig. 3. Major cell classes and their spatial organizations in the preoptic region as revealed with MERFISH. (A) (Left) Schematic of the MERFISH measurements. Combinatorial smFISH imaging was used to identify 135 genes, followed by sequential rounds of two-color FISH to identify 20 additional genes. Total polyadenylated mRNA and nuclei costains then allowed cell boundary segmentation. (Top right) Pseudo-colored dots marking localizations of individual molecules of eight example RNA species, each marking a distinct major cell class, in a 10-mm-thick, 1.8- by 1.8-mm slice. (Bottom right) Magnification of the white boxed region (left) and the total mRNA image and the segmented cell boundaries of the same region (right). The raw and decoded MERFISH images of the same field of view (FOV) for all 135 genes measured by using combinatorial smFISH are shown in fig. S9; the total mRNA and nuclei costain images and segmented cell boundaries for the same FOV are shown in fig. S10. The segmented cell boundaries represent the boundaries of the cell soma (29). A subset of identified RNA molecules fell outside these boundaries and are thus candidates for RNAs in neuronal or glial processes. (B) Expression of all genes measured with MERFISH for ~500,000 cells imaged in multiple naïve animals. Expression for each gene is normalized to the 95% expression quantile for that gene across all cells. Cells are grouped by major classes, and markers of each major cell class are listed on the right. OD, oligodendrocytes. (C) tSNE plot of these cells. (D) Pairwise Pearson correlation coefficients between the average expression profiles (in z-scores) of individual cell classes identified with MERFISH and scRNA-seq. (E) (Top) Spatial distribution of all major cell classes across sections at different anterior-posterior positions from a single female mouse. Cells are marked with cell segmentation boundaries and colored by cell classes as indicated. Six of the twelve 1.8- by 1.8-mm imaged slices are shown. The 0, 100, 200, 300, 400, and 500 mm labels indicate the distance from the anterior position (Bregma +0.26). (Bottom) Enlarged image of the slice at 400 mm from the anterior position (left) and a further magnified image of the region shown in the gray dashed box (right). Scale bars, 500 mm (left), 250 mm (right). (F) Spatial distributions of individual cell classes are shown as colored dots on the background of all cells shown as gray dots. Dashed ovals indicate several specific hypothalamic nuclei and are colored identically to the nuclei abbreviations listed to the right. BNST, bed nucleus of the stria terminalis; MPN, medial preoptic nucleus; MnPO, median preoptic nucleus; Pe, periventricular hypothalamic nucleus; AvPe, anteroventral periventricular nucleus; VMPO, ventromedial preoptic nucleus; VLPO, ventrolateral preoptic nucleus; PVA, paraventricular thalamic nucleus; PaAP, paraventricular hypothalamic nucleus, anterior parvicellular.

## Panel-by-Panel 解读

### Panel A — MERFISH 流程、RNA 定位与细胞分割
**结论**：组合 smFISH、顺序 FISH 和总 mRNA/DAPI 共染共同实现单分子识别与细胞体边界分割。

**关键数据**：155 genes；135 组合基因 + 20 顺序基因；成像区 1.8 × 1.8 mm；原文 caption 标为 10-mm-thick slice。

### Panel B — 主要细胞类表达热图
**结论**：155 基因表达矩阵可区分神经元、胶质和血管相关主要细胞类。

**关键数据**：约 500,000 个 naïve 细胞；每个基因按全细胞第 95% 分位数归一化。

### Panel C — MERFISH tSNE
**结论**：原位细胞按转录表达形成可分离的主要细胞类。

**关键数据**：识别 inhibitory、excitatory、OD、astrocyte、microglia、ependymal、endothelial、mural 等类别。

### Panel D — 跨平台细胞类相关性
**结论**：MERFISH 与 scRNA-seq 的平均细胞类表达谱具有高 Pearson 相关。

**关键数据**：相关性在 z-score 平均表达谱之间计算；scRNA-seq 中 astrocytes/endothelial/ependymal 相对耗竭。

### Panel E — 沿前后轴的空间分布
**结论**：不同细胞类在前后轴和核团中呈现明显空间组织。

**关键数据**：12 个成像切片中展示 6 个；位置标签为距 Bregma +0.26 的 0–500 μm。

### Panel F — 细胞类与核团对应
**结论**：抑制性神经元广泛分布并富集后部 BNST/MPN，兴奋性神经元前部富集、后部弥散。

**关键数据**：PVA/BAC 主要为兴奋性；BNST-p/BNST-mv 主要为抑制性。

## 总体结论
Fig. 3 展示 MERFISH 如何在完整组织中同时读取 RNA、分割细胞并重建主要细胞类的空间图谱。它不仅复现 scRNA-seq 的分子类别，还揭示了解离测序无法看到的核团定位、细胞类比例与空间差异。

## 关联 Figures / Extended Data
- Fig. 4：神经元集群级别跨平台整合
- Fig. 5：神经元集群空间组织与邻域分析
- fig. S9–S12：图像、分割、重复性、灵敏度与 bulk RNA-seq 对照
