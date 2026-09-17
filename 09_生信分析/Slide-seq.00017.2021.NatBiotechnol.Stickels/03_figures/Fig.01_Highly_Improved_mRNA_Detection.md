# Fig. 1 — Highly improved mRNA detection sensitivity in Slide-seqV2

## Caption（原文）
> Fig. 1 | Highly improved mRNA detection sensitivity in Slide-seqV2. a, Overview of the Slide-seq method. An example array is shown of mouse hippocampus generated with Slide-seqV2 in which each bead is colored by the number of UMIs. BC, barcode. b, Histogram of the number of UMIs per bead for Slide-seq (red) versus Slide-seqV2 (blue) on serial mouse embryo sections. c, Images of hippocampus marker genes in Slide-seqV2 (left) versus hybridization chain reaction (HCR) FISH images (right). Data represent n = 1 HCR experiment on a serial section of Slide-seq. d, Comparison of marker gene counts in the mouse hippocampus CA1 across four modalities (n = 6 measurements per modality; mean ± s.d. data are reported in Supplementary Table 2). For smFISH, Slide-seqV2 and Slide-seq, all transcript counts within a fixed area of the CA1 were summed together. For scRNA-seq, we summed the counts for the number of CA1 pyramidal cells counted within this area. Scale bars, 500 μm.

## Panel-by-Panel 解读

### Panel a — Overview of the Slide-seq method
**结论**: 展示了Slide-seqV2的完整工作流程，从bead synthesis到array generation到spatial RNA profiling

**关键数据**: 
- 10 μm bead size
- 每个bead uniquely indexed by barcode
- BC = barcode

### Panel b — UMI counts per bead comparison
**结论**: Slide-seqV2相比原始Slide-seq，UMI counts提升约9倍

**关键数据**:
- Slide-seqV2 median UMIs = 550
- Slide-seq median UMIs = 59
- Fold change ≈ 9.3x (E12.5 mouse embryos)

### Panel c — Marker gene imaging vs HCR FISH
**结论**: Slide-seqV2的空间表达模式与HCR FISH高度一致

**关键数据**: 
- n = 1 HCR experiment on serial section
- Atp2b1, Ociad2, Slc17a7 三个CA1 marker genes

### Panel d — Cross-modality comparison
**结论**: Slide-seqV2的检测效率接近droplet-based scRNA-seq (约44%)，远超原始Slide-seq

**关键数据** (n=6, mean±s.d.):
- scRNA-seq: Atp2b1=33.5±1.4, Ociad2=2.1±1.5, Slc17a7=1.2±1.5
- Slide-seqV2: Atp2b1=15.7±1.5, Ociad2=2.3±2.4, Slc17a7=1.9±2.6

## 总体结论

Fig. 1 证明了Slide-seqV2相比原始Slide-seq在mRNA检测灵敏度上提升了约9倍（median UMIs从59提升到550），达到单细胞RNA-seq约44%的检测效率，与HCR FISH空间模式高度一致。这一灵敏度提升使得检测低丰度转录本（如dendritic mRNAs）成为可能。

## 关联 Figures / Extended Data
- **Supplementary Fig. 3a-d** — Comparison with 10x Visium
- **Supplementary Fig. 3e,f** — Comparison with HDST
- **Supplementary Fig. 4, 5a** — smFISH validation
- **Supplementary Fig. 5b,c** — Sensitivity and reproducibility
