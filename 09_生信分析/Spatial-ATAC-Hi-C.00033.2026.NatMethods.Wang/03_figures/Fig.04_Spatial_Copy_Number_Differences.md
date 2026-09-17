# Fig. 4 — Spatial-ATAC-Hi-C can faithfully capture spatial copy number differences

## Caption（原文）
> a, Schematic workflow of the experimental design. b, Spatial location of the two tumor samples NU04707 (in blue) and NU04741 (in orange), which were stitched together onto one slide. c, Copy number profiles for NU04707 and NU04741 from Spatial-ATAC-Hi-C data and WGS data (top) and zoomed-in profiles on chr9 and chr12 (bottom). The copy number profiles for Spatial-ATAC-Hi-C data were generated based on the pseudobulk of the pixels from NU04707 and NU04741 samples on each side of the stitched slide. The copy number profiles for WGS experiments were generated from the adjacent tissue section of these two patients separately. d, UMAP embedding of the clustering analysis based on single-pixel copy number profiles at 5-Mb resolution. e, Spatial distribution of the clusters in d. f, Heatmap showing the whole-genome copy number in each pixel. Panel a created in BioRender; Wang, P. https://biorender.com/e8huh87 (2026).

## Panel-by-Panel 解读

### Panel a — 实验设计示意图
**结论**：展示了将两个肿瘤样本（GBM和星形细胞瘤）放置在同一玻片上进行Spatial-ATAC-Hi-C实验的设计方案。

**关键数据**：两个样本分别为GBM患者NU04741和星形细胞瘤患者NU04707。

### Panel b — 肿瘤样本空间位置
**结论**：展示了两个肿瘤样本在玻片上的空间位置，NU04707（蓝色）和NU04741（橙色）拼接在同一玻片上。

**关键数据**：两个样本的空间位置分布。

### Panel c — 拷贝数谱比较
**结论**：Spatial-ATAC-Hi-C推断的拷贝数谱与WGS数据高度一致，证明技术能够准确捕获拷贝数变异。

**关键数据**：展示了chr9上CDKN2A和CDKN2B基因的拷贝数丢失（星形细胞瘤样本），以及chr12上CDK4基因的拷贝数增加（GBM样本），两种方法结果高度一致。

### Panel d — 基于拷贝数的聚类UMAP
**结论**：基于单像素拷贝数谱（5-Mb分辨率）的聚类分析识别出5个不同的肿瘤克隆。

**关键数据**：5个聚类（C0–C4），C0主要来自星形细胞瘤患者NU04707，C1、C2、C3主要来自GBM患者NU04741。

### Panel e — 聚类空间分布
**结论**：展示了基于拷贝数谱的聚类在组织中的空间分布，揭示了肿瘤克隆的空间异质性。

**关键数据**：不同聚类显示出明确的空间分离模式。

### Panel f — 全基因组拷贝数热图
**结论**：展示了每个像素的全基因组拷贝数热图，揭示了不同聚类间的拷贝数差异。

**关键数据**：chr12p和chr11q等区域在不同聚类间显示出拷贝数差异。

## 总体结论
Fig. 4证明Spatial-ATAC-Hi-C能够准确捕获肿瘤样本的空间拷贝数差异。通过将GBM和星形细胞瘤样本放置在同一玻片上进行实验，并与WGS数据进行系统比较，验证了技术在CNV检测方面的可靠性。基于单像素拷贝数谱的聚类分析揭示了5个不同的肿瘤克隆，展示了肿瘤的空间异质性。该技术能够同时在同一组织切片上检测两个不同肿瘤样本的拷贝数变异。

## 关联 Figures / Extended Data
- Extended Data Fig. 7（SV检测的详细验证，包括chr2/chr5易位和ADAM23::CTNND2融合事件）
- Supplementary Table 10（EagleC软件识别的SV事件）
