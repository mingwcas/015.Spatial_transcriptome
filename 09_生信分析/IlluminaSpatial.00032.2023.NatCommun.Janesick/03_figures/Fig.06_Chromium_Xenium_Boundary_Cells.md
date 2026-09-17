# Fig. 6 — Chromium and Xenium integration derive differentially expressed genes in a rare cell type

## Caption（原文）
> a Xenium UMAP for a different biological section (different donor) of invasive ductal carcinoma (Sample #2). Most cell types are driven by a single marker (Supp. Fig. 12). TAFs = Tumor-Associated Fibroblasts. When subclustering the epithelial and myoepithelial populations, we noticed a group of cells situated between tumor and DST+ cells, which we label "boundary" and color red. a′ Zoomed-in view of UMAP from (a) showing myoepithelial and epithelial cell subtypes. b DCIS ROI containing these cells which are viewed close-up in (b′), along with markers for both tumor (purple) and myoepithelial (green) cells. c and c′ Corresponding H&E images. Scale bar = 200 µm in c and 10 µm in (c′). d Normal duct ROI containing myoepithelial and epithelial cells in closer proximity. d′ Zoomed in region of (d) showing minimal comingling of transcripts representing each cell type: myoepithelial (dark green) and epithelial (light green). Scale bar = 50 µm. e Heatmap representation of the UMAP showing relative expression for selected features. HVGs = highly variable genes. Scale bar is a z-score computed across cell types for each gene. Red box highlights that these rare boundary cells express both tumor and myoepithelial markers. The Xenium experiment was performed in replicate on two serial sections, with one representative section shown here. f Using the gene expression profile of the rare boundary cells shown in (e), we identified this cell type (~283 cells) in the scFFPE-seq data of Sample #1 shown in Figs. 1–5. We conducted a differential gene expression analysis of these cells compared to tumor and myoepithelial cells and validated that these cells express both myoepithelial (MYLK) and tumor (ABCC11) markers. We further derived genes CX3CL1, CCL28, PROM1, and KLK5 which are differentially expressed in the boundary cells. Differential expression was performed in Loupe Browser (see "Methods") which performs a variant of the negative binomial exact test (for small gene counts), or a fast asymptotic beta test derived from edgeR (for large gene counts). P-values are adjusted for multiple testing using the Benjamini–Hochberg procedure to control for the false discovery rate.

## Panel-by-Panel 解读

### Panel a, a′ — Sample #2 Xenium UMAP
**结论**：对来自不同供体的侵袭性导管癌样本（Sample #2）进行 Xenium 分析，UMAP 展示了免疫、肌上皮、上皮和肿瘤细胞群。在对上皮和肌上皮群体进行亚聚类分析时，发现了一组位于肿瘤和 DST+ 细胞之间的"边界细胞"。

**关键数据**：TAFs = 肿瘤相关成纤维细胞；边界细胞共表达肿瘤标记（ERBB2、ABCC11）和肌上皮标记（MYLK、DST）。

### Panel b, b′ — DCIS ROI 中的边界细胞
**结论**：高倍镜检查确认了在肌上皮边界退化的 DCIS 区域中，这些细胞同时表达肿瘤（紫色）和肌上皮（绿色）标记。

**关键数据**：ERBB2（肿瘤标记，紫色）和 MYLK/DST（肌上皮标记，绿色）共表达。

### Panel c, c′ — 对应 H&E 图像
**结论**：H&E 染色显示了 DCIS 区域的形态学特征，与分子数据相对应。

**关键数据**：比例尺 = 200 µm（c）和 10 µm（c′）。

### Panel d, d′ — 正常导管对照
**结论**：作为对照，正常导管中肌上皮和上皮细胞虽然紧密相邻，但细胞类型特异性标记没有混合，排除了分割伪影的可能性。

**关键数据**：比例尺 = 50 µm；正常导管中细胞类型标记未混杂。

### Panel e — UMAP 热图（边界细胞标记）
**结论**：热图展示了边界细胞（红色框）同时表达肿瘤和肌上皮标记的特征，证实了这些稀有细胞的存在。

**关键数据**：边界细胞共表达 ERBB2、ABCC11（肿瘤标记）和 MYLK、DST（肌上皮标记）。

### Panel f — scFFPE-seq 差异表达分析
**结论**：利用 Xenium 数据中边界细胞的基因表达谱，在 Sample #1 的 scFFPE-seq 数据中找到了约 283 个对应细胞（约 1%），并进行了差异表达分析。发现了 CX3CL1、CCL28、PROM1 和 KLK5 四个在边界细胞中高表达的基因。

**关键数据**：约 283 个边界细胞（~1% 的 scFFPE-seq 细胞）；差异表达基因：CX3CL1（促进乳腺癌转移）、CCL28（上皮致瘤性细胞因子）、PROM1（CD133，癌症干细胞标记）、KLK5；差异表达使用负二项精确检验或 edgeR 衍生的渐近 beta 检验；p 值经 Benjamini-Hochberg 校正。

## 总体结论
该图展示了如何通过 Xenium 和 Chromium scFFPE-seq 数据整合发现和表征一种稀有的"边界细胞"群体。这些细胞位于肌上皮边界，共表达肿瘤（ERBB2、ABCC11）和肌上皮（MYLK、DST）标记，可能代表了 DCIS 向侵袭性转变过程中的过渡态细胞。通过在 Sample #2 的 Xenium 数据中发现这些细胞，再在 Sample #1 的 scFFPE-seq 数据中匹配其表达谱并获取全转录组信息，鉴定出 CX3CL1、CCL28、PROM1 和 KLK5 为边界细胞特异性差异表达基因。这一发现为理解 DCIS-侵袭性转变的分子机制提供了新的线索。

## 关联 Figures / Extended Data
- Fig. 4（DCIS 亚型和侵袭性肿瘤的细胞组成）
- Supp. Figure 12（Sample #2 所有细胞亚型）
- Supp. Figure 13（形态学与分子数据的对应）
