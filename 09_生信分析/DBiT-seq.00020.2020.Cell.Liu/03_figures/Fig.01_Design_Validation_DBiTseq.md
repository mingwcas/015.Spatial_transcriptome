# Fig. 1 — Design and Validation of DBiT-Seq

## Caption（原文）
> (A) Schematic workflow. A formaldehyde-fixed tissue slide is used as the starting material, which is incubated with a cocktail of antibody-derived DNA tags (ADTs) that recognize a panel of proteins of interest. A custom-designed PDMS microfluidic device with 50 parallel microchannels in the center of the chip is aligned and placed on the tissue slide to introduce the 1st set of barcodes A1 to A50. Each barcode is tethered with a ligation linker and an oligo-dT sequence for binding the poly-A tail of mRNAs or ADTs. Then, reverse transcription (RT) is conducted in situ to yield cDNAs which are covalently linked to barcodes A1–A50. Afterward, this microfluidic chip is removed and another microfluidic chip with 50 parallel microchannels perpendicular to those in the first microfluidic chip is placed on the tissue slide to introduce the 2nd set of DNA barcodes B1–B50. These barcodes contain a ligation linker, a unique molecular identifier (UMI) and a PCR handle. After introducing barcodes B1–B50 and a universal complementary ligation linker through the second microfluidic chip, the barcodes A and B are joined through ligation and then the intersection region of microfluidic channels in the first and second PDMS chips defines a distinct pixel with a unique combination of A and B, giving rise to a 2D array of spatial barcodes AiBj (i = 1–50, j = 1–50). Afterward, the second PDMS chip is removed and the tissue remains intact while spatially barcoded for all mRNAs and the proteins of interest. The barcoded tissue is imaged under an optical or fluorescence microscope to visualize individual pixels. Finally, cDNAs are extracted from the tissue slide, template switched to incorporate another PCR handle, and amplified by PCR for preparation of sequencing library via tagmentation. A paired-end sequencing is performed to read the spatial barcodes (AiBj) and cDNA sequences from mRNAs and ADTs. Computational reconstruction of a spatial mRNA or protein expression map is realized by matching the spatial barcodes AiBj to the corresponding cDNA reads using UMIs. The spatial omics map can be correlated to the tissue image taken during or after microfluidic barcoding to identify the spatial location of individual pixels and the corresponding tissue morphology.
> (B) Microfluidic device used in DBiT-seq. A series of microfluidic chips were fabricated with 50 parallel microfluidic channels in the center that are 50 μm, 25 μm, or 10 μm in width, respectively. The PDMS chip containing 50 parallel channels is placed directly on a tissue slide and the center region is clamped using two acrylic plates and screws to apply the pressing force in a controlled manner. All 50 inlets are open holes (~2 mm in diameter) capable of holding ~13 μL of solution.
> (C) Validation of spatial barcoding using fluorescent DNA probes. The images show parallel lines of Cy3-labeled barcode A (red, left panel) on the tissue slide defined by the first flow, the square pixels of FITC-labeled barcode B (green, right panel) corresponding to the intersection of the first and the second flows, and the overlay of both fluorescence colors (middle). Because barcode B is ligated to the immobilized barcode A in an orthogonal direction, it is detectable only at the intersection of the first set (A1–A50) and the second set (B1–B50) of microchannels. Channel width = 50 μm.
> (D) Validation of leak-free flow barcoding using a layer of cells cultured on a glass slide. HUVECs grown on a glass slide were stained by DAPI (blue) during the 1st flow and anti-human VE-cadherin (red) during the 2nd flow. As shown in the enlarged figures, fluorescence staining was confined within the channels. Scale bar, 20 μm.
> (E) Confocal microscopy image of a tissue slide stained with fluorescent DNA barcode A. The 3D stacked image shows no leakage between adjacent channels throughput the tissue thickness. Scale bar, 20 μm.
> (F) Validation of spatial barcoding for 10 μm pixels. A tissue slide was subjected to spatial barcoding and the resultant pixels were visualized by optical (upper left) and fluorescent imaging (upper right) of the same tissue sample using FITC-labeled barcode B. Pressing microfluidic channels against the tissue section resulted in a slight deformation of the tissue matrix, which allowed for directly visualizing the topography of individual tissue pixels. Enlarged views (low panels) further show discrete barcoded tissue pixels with 10-μm pixel size.
> (G) Qualification of the cross-channel diffusion distance, the measured size of pixels, and the number of cells per pixel. Quantitative analysis of the line profile revealed the diffusion of DNA oligomers through the dense tissue matrix is as small as 0.9 μm, which was obtained with the 10 μm-wide microchannels with the application of an acrylic clamp. The measured pixel size agreed with the microchannel size. Using DAPI, a fluorescent dye for nuclear DNA staining, the number of cells in a pixel can be identified. The average cell number is 1.7 in a 10-μm pixel and 25.1 in a 50-μm pixel.
> (H) Gene and UMI count distribution. DBiT-seq is compared to Slide-seq, ST, and the commercialized ST (Visium) with different spot/pixel sizes. Formaldehyde-fixed mouse embryo tissue slides were used in DBiT-seq. Fresh frozen mouse brain tissues were used in Slide-seq, ST, and Visium.

## Panel-by-Panel 解读

### Panel A — Schematic Workflow
**结论**：DBiT-seq通过两步微流控条码实现组织像素的二维空间编码
**关键数据**：第一套Barcode A (A1-A50) + 第二套Barcode B (B1-B50) = 2500个独特空间条码(AiBj)

### Panel B — Microfluidic Device
**结论**：三种通道宽度(10/25/50μm)的微流控芯片满足不同分辨率需求
**关键数据**：入口孔径~2mm，可容纳~13μL溶液；亚克力夹具提供受控压力

### Panel C — Validation with Fluorescent Probes
**结论**：正交条码连接成功形成二维像素阵列
**关键数据**：红色Cy3标记Barcode A条纹，绿色FITC标记Barcode B像素，通道宽度50μm

### Panel D — Leak-free Validation
**结论**：微流控通道密封良好，无跨通道泄漏
**关键数据**：HUVECs培养层中，DAPI(蓝色)和抗VE-cadherin(红色)染色均被限制在通道内

### Panel E — 3D Confocal Validation
**结论**：整个组织厚度内无相邻通道间泄漏
**关键数据**：3D堆叠图像证实无通道间泄漏

### Panel F — 10μm Pixel Validation
**结论**：10μm通道可形成清晰的离散像素阵列
**关键数据**：光学和荧光成像均可见10μm像素；组织在通道壁下轻微形变

### Panel G — Diffusion Distance & Cell Count
**结论**：10μm通道扩散距离仅0.9μm，10μm像素含~1.7个细胞
**关键数据**：10μm通道+夹具：扩散距离0.9±0.2μm；50μm通道无夹具：扩散距离4.5±1μm；平均细胞数：10μm像素1.7个，50μm像素25.1个

### Panel H — Gene/UMI Count Comparison
**结论**：DBiT-seq在相同像素大小下检测效率显著高于其他技术
**关键数据**：DBiT-seq 10μm像素：平均~2,068 genes/pixel；Slide-seq 10μm：~150 genes/pixel；ST 100μm：类似DBiT-seq但像素大100倍

## 总体结论
Fig. 1 证明了DBiT-seq技术的可行性：微流控芯片实现无泄漏的空间条码递送，10μm像素达到单细胞级别（~1.7细胞/像素），检测效率比Slide-seq高出一个数量级，且兼容甲醛固定组织。

## 关联 Figures / Extended Data
- **ED Fig. S1** — 补充验证数据（芯片设计、泄漏测试等）
- **ED Fig. S2** — 数据质量评估（cDNA大小分布、饱和曲线等）
