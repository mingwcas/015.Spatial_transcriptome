# Fig. 2 — Stereo-seq V2 dissects the adult mouse brain with single-cell resolution

## Caption（原文）
> (A) Left: spatial visualization of the intronic read signals on an FFPE adult coronal mouse hemibrain section. Middle: magnification showing the intronic read signals from the region squared in left. Right: outlines of all segmented cells in the squared region from the middle panel.
> (B) The Venn diagram at the top shows the confluence and variance in gene capture efficiency between Visium FFPE and Stereo-seq V2. The pie chart at the bottom left categorizes the spectrum of gene types designed in the Visium FFPE probe set. The pie chart at the bottom right enumerates the gene types captured by Stereo-seq V2.
> (C) Spatial visualization of specific gene expression in Stereo-seq V2, Visium FFPE, and ISH (Allen Brain Atlas [ABA]) data.
> (D) Left: spatial clustering result of Visium FFPE mouse hemibrain data. Right: spatial visualization of unsupervised cell clustering result of segmented cells on Stereo-seq V2 sections. Regions and cells are colored by their annotation. [extensive list of abbreviations]
> (E) Magnified visualization showing cell-type composition in the regions squared in (D). This includes the PIR, AMY, and HY regions as identified by Visium FFPE and Stereo-seq V2. The corresponding dot plots illustrate differential gene expression in cell populations contained within the selected areas on Stereo-seq V2 data.
> See also Figure S2.

## Panel-by-Panel 解读

### Panel A — Cell Segmentation
**结论**：Stereo-seq V2实现了FFPE样本的单细胞分割，分辨率达到单细胞水平。

**关键数据**：通过unspliced RNA信号实现细胞分割。

### Panel B — Gene Capture Comparison
**结论**：V2检测到42,440个基因，包括Visium FFPE未覆盖的23,459个基因，且V2覆盖了96.6%的Visium探针集。

**关键数据**：V2额外检测到3,351个蛋白编码基因和3,895个ncRNA；Visium探针集仅含19,593个蛋白编码基因。

### Panel C — Spatial Gene Expression
**结论**：V2与ISH数据高度一致，验证了空间表达模式的准确性。

**关键数据**：Etv1和Vsnl1等标记基因在相应脑区高表达。

### Panel D — Spatial Clustering
**结论**：V2识别出34种细胞类型，涵盖17个脑区，分辨率远超Visium。

**关键数据**：Leiden聚类识别34个细胞类型簇。

### Panel E — Cell Type Composition
**结论**：V2揭示了复杂脑区的细胞组成，如GABAergic神经元(STR-PAL Chst9 Gaba)高表达Erbb4。

**关键数据**：Piriform cortex和hypothalamus区域显示复杂细胞组成。

## 总体结论
Stereo-seq V2能够在FFPE样本上实现单细胞分辨率的全转录组空间分析，显著优于探针-based的Visium FFPE。

## 关联 Figures / Extended Data
- ED Fig. S2 (Spatial clustering comparison with MERFISH)
