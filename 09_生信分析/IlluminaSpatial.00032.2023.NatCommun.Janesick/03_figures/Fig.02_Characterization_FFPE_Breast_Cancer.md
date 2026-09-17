# Fig. 2 — Characterization of FFPE breast cancer sample using whole transcriptome single cell and spatial technologies

## Caption（原文）
> A human breast cancer sample was obtained as an FFPE block (annotated by pathologist as invasive ductal carcinoma) and processed for single cell analysis and spatial transcriptomics as described in Fig. 1. a Dimension reduction of the scFFPE-seq data yielded a t-SNE projection with 17 unsupervised clusters. Each point represents a cell and the colors/labels show annotated cell types. Macrophages 1 cluster is marked by LYZ, IFI30, and ITGAX. Macrophages 2 cluster is marked by SELENOP, F13A1, and RNASE1. b t-SNE projection of Visium spots also identifies 17 clusters. Based on differential gene expression analysis, ten clusters could be unequivocally assigned to cell types, while the others were mixtures of cell types. c H&E staining conducted pre-CytAssist is shown for reference alongside the spatial distribution of clusters in (b). Scale bar = 1 mm. Cell type-specific marker genes are expressed as log2(normalized UMI counts). The Visium data elucidated the spatial location of two molecularly distinct DCIS and invasive subtypes and the general locations of immune, myoepithelial, adipocytes, and stromal cells. Additionally, Visium features mitochondrial probes (e.g., MT-ND1), and their spatial distribution correlates with the invasive region of the tissue section. This experiment was performed in replicate on two serial sections, with one representative section shown here.

## Panel-by-Panel 解读

### Panel a — scFFPE-seq t-SNE 投影
**结论**：scFFPE-seq 数据的无监督聚类产生 17 个聚类，涵盖多种细胞类型，包括两种不同的巨噬细胞亚群。

**关键数据**：17 个无监督聚类；Macrophages 1 标记基因：LYZ、IFI30、ITGAX；Macrophages 2 标记基因：SELENOP、F13A1、RNASE1。

### Panel b — Visium t-SNE 投影
**结论**：Visium 数据同样产生 17 个聚类，其中 10 个可明确归属为单一细胞类型，其余 7 个为混合细胞类型组成。

**关键数据**：17 个空间聚类；10 个可明确注释的聚类；7 个混合组成聚类。

### Panel c — H&E 染色与空间聚类分布
**结论**：Visium 数据揭示了两个分子层面不同的 DCIS 亚型（DCIS #1 和 DCIS #2）和侵袭性肿瘤的空间位置，同时描绘了免疫细胞、肌上皮细胞、脂肪细胞和基质细胞的大致分布区域。

**关键数据**：三个肿瘤亚域的空间分离；MT-ND1（线粒体探针）的分布与侵袭区域相关；比例尺 = 1 mm。

## 总体结论
该图展示了 scFFPE-seq 和 Visium 两种全转录组技术对 FFPE 乳腺癌样本的互补表征。scFFPE-seq 在单细胞水平揭示了 17 个细胞类型聚类（包括两种不同的巨噬细胞亚群），而 Visium 提供了这些细胞类型的空间分布信息，成功区分了两个分子上不同的 DCIS 亚型和侵袭性肿瘤区域。两种技术的整合为后续 Xenium 高分辨率分析奠定了基础，也揭示了脂肪细胞等脆弱细胞类型的空间信息——这类细胞在单细胞解离过程中容易丢失。

## 关联 Figures / Extended Data
- Fig. 1（实验设计）
- Supp. Figure 1a（两个巨噬细胞群的差异表达基因）
- Supp. Figure 10（Visium spot 解卷积）
