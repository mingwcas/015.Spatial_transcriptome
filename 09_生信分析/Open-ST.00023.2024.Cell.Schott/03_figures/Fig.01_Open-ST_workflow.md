# Fig. 1 — Open-ST Workflow for High-Resolution Spatial Transcriptomics

## Caption（原文）
> (A) All experimental and computational resources are open-source and available under https://rajewsky-lab.github.io/openst.
> (B) Sequencing designed oligos in patterned Illumina flow cells allows barcode registration in regularly spaced spots. Oligonucleotides are processed to allow capture of polyadenylated RNA.
> (C) Our custom 3D-printable device guides cutting into capture areas of desired size.
> (D) Transcriptomic and H&E imaging data are generated from the same fresh-frozen tissue section.
> (E) Tissue morphological information is integrated with ST data with our open-source openst package, including automatic cell segmentation, pairwise alignment of modalities, and quantification of transcripts in segmented cells.
> (F) Serial sections can be used for three-dimensional reconstruction of tissue histology and transcriptome, using STIM.

## Panel-by-Panel 解读

### Panel A — 开放资源
**结论**：Open-ST提供完整的开源实验和计算资源

**关键数据**：所有协议和软件在 https://rajewsky-lab.github.io/openst 可用

### Panel B — 条形码注册
**结论**：利用Illumina patterned flow cell技术生成密集条形码阵列

**关键数据**：捕获点分辨率约0.6 μm，使用NovaSeq6000 S4 flow cell

### Panel C — 捕获区域制备
**结论**：3D打印切割指南实现精确的捕获区域制备

**关键数据**：最大捕获区域6.3×89 mm，3×4 mm区域可制备约360个

### Panel D — 多模态数据生成
**结论**：同一冷冻切片同时获取转录组和H&E成像数据

**关键数据**：单次文库制备成本<€130/12 mm²

### Panel E — 单细胞整合
**结论**：openst包实现自动化细胞分割和多模态数据整合

**关键数据**：配准精度约1 μm

### Panel F — 3D重建
**结论**：连续切片可重建3D虚拟组织块

**关键数据**：19个切片跨越350 μm组织深度

## 总体结论
Fig. 1展示了Open-ST的完整工作流程，从捕获区域制备到3D重建，提供了一个端到端、开源、经济高效的空间转录组学解决方案。

## 关联 Figures / Extended Data
- Fig. S1 — 质量控制和图像处理
