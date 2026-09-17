# Fig. 1 — Spatial transcriptome of axolotl telencephalon by Stereo-seq

## Caption（原文）
> (A) Schematic diagram of Stereo-seq for the axolotl telencephalon. Step 1: sample collection and frozen section preparation of the adult axolotl telencephalon. Step 2: in situ RNA capture of tissue loaded onto the Stereo-seq chip. Step 3: cDNA amplification, library construction, and sequencing.
> (B) Spatially assigned spliced (purple) and unspliced transcripts (blue) (bottom left) and corresponding nucleus areas represented by single-stranded DNA staining (gray) (top left). Single-cell segmentations were performed by watershed algorithm (right).
> (C) Stereo-seq identified anatomical regions (top left) and cell types (right) of axolotl telencephalon. DP, dorsal pallium; MP, medial pallium; LP, lateral pallium; VZ, ventricular zone; cckIN, Cck+ inhibitory neuron; CMPN, cholinergic, monoaminergic, and peptidergic neuron; CP, choroid plexus; dpEX, dorsal pallium excitatory neuron; mpEX, medial pallium excitatory neuron; mpIN, medial pallium inhibitory neuron; MSN, medium spiny neuron; nptxEX, Nptx+ lateral pallium excitatory neuron; ntng1IN, Ntng1+ inhibitory neuron; ribEGC, ribosomal EGC; scgnIN, Scgn+ inhibitory neuron; sfrpEGC, Sfrp+ EGC; sstIN, Sst+ inhibitory neuron; tlNBL, telencephalon neuroblast; VLMC, vascular leptomeningeal cell; wntEGC, Wnt+ EGC.
> (D) Spatial visualization of the expression of selected genes on Stereo-seq maps (left) and corresponding RNA ISH images (right).
> (E) Distribution of the sstIN in the medial pallium region of the adult axolotl telencephalon. Annotated sstIN in green (left) and cells expressing high levels of the Sst gene (right) are indicated by white arrows.
> (F) The distribution of three subtypes of EGCs (left). The expression of marker genes for the selected EGC subtype is shown (right).
> (G) Violin plot showing the expression level of neural stem cell markers (Sox2, Vim, Slc1a3, and Gfap) in three types of EGCs.
> (H) Bubble plot showing the expression level of specific markers of various biological functions in each EGC subtype.

## Panel-by-Panel 解读

### Panel A — Stereo-seq Workflow Schematic
**结论**：Stereo-seq 技术流程包含三个核心步骤：样本收集与冰冻切片制备、原位RNA捕获、cDNA扩增与测序。

**关键数据**：成年蝾螈脑室管膜厚度为20 µm，以实现单细胞层捕获；DNA纳米球（DNB）直径220 nm，中心间距500或715 nm，实现亚细胞分辨率。

### Panel B — Single-Cell Transcriptome Segmentation
**结论**：Stereo-seq 可实现空间定位的单细胞转录组分析 spliced 和 unspliced 转录本，并通过watershed算法进行单细胞分割。

**关键数据**：每个细胞区域包含约850个DNB位点，平均检测到6291个独特分子标签（UMI）和1680个基因。

### Panel C — Anatomical Regions and Cell Types Identification
**结论**：Stereo-seq 鉴定出蝾螈脑室的6个解剖区域（VZ、dorsal pallium、medial pallium、lateral pallium、striatum、septum）和16种细胞类型。

**关键数据**：通过Seurat无监督聚类分析鉴定16个细胞簇，并映射回空间位置；兴奋性神经元富集于pallium，抑制性神经元富集于striatum、medial pallium和septum区域。

### Panel D — Validation of Gene Expression by RNA ISH
**结论**：Stereo-seq 的基因表达空间模式与RNA原位杂交（ISH）结果高度一致，验证了该技术的可靠性。

**关键数据**：Gad2和Sst转录本在连续切片上的分布模式相似；Stereo-seq估算的Sst+抑制性神经元比例与RNA ISH结果相当。

### Panel E — Sst+ Inhibitory Neuron Distribution
**结论**：Sst+抑制性神经元稀疏分布于pallium区域，RNA扩散效应在细胞边界外迅速下降。

**关键数据**：Sst和Gad2在Sst+抑制性神经元中的平均转录水平显著高于邻近细胞。

### Panel F — Three EGC Subtypes Distribution
**结论**：鉴定出三种EGC亚型（wntEGC、sfrpEGC、ribEGC），各自位于脑室区不同位置并表达特异性标记基因。

**关键数据**：wntEGC表达Wnt8b，sfrpEGC表达Sfrp1，ribEGC表达核糖体相关基因。

### Panel G — Neural Stem Cell Markers in EGCs
**结论**：三种EGC亚型均表达神经干性标记基因（Sox2、Vim、Slc1a3、Gfap），但表达水平存在差异。

**关键数据**：Sox2、Vim、Slc1a3、Gfap在三种EGC类型中的表达水平通过小提琴图展示。

### Panel H — Biological Function Markers in EGC Subtypes
**结论**：各EGC亚型具有不同的生物学功能特征：ribEGC高表达细胞周期和翻译相关基因，提示其活跃增殖特性。

**关键数据**：Gene Ontology分析显示ribEGC富集细胞周期和翻译相关基因；其他EGC亚型分别富集Wnt/BMP/Notch信号调控和神经突生长相关功能。

## 总体结论

本图展示了Stereo-seq技术应用于蝾螈脑室单细胞空间转录组分析的核心结果。通过20 µm厚度冰冻切片实现单细胞层捕获，结合DNB测序和watershed算法分割，获得高分辨率空间转录组数据。鉴定出6个解剖区域和16种细胞类型，包括三种EGC亚型（wntEGC、sfrpEGC、ribEGC），其中ribEGC具有活跃增殖特性。Stereo-seq与RNA ISH验证结果高度一致，证明该技术可准确揭示脑室的空间细胞类型分布和基因表达模式。

## 关联 Figures / Extended Data
- ED Fig. 1（补充Fig. S1-S5 相关方法验证）
