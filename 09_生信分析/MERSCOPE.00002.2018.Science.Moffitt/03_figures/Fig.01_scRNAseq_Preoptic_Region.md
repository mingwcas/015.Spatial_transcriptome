# Fig. 1 — scRNA-seq of the preoptic region in the mouse hypothalamus

## Caption（原文）
> Fig. 1. scRNA-seq of the preoptic region in the mouse hypothalamus. (A) Schematic of the preoptic region of the hypothalamus. Magenta boxes indicate the area dissected for scRNA-seq (Bregma +0.5 to –0.6). (B) t-distributed stochastic neighbor embedding (tSNE) for all cells and inhibitory and excitatory neurons, with cells colored by cluster. Numbers superimposed on the tSNE indicate the cluster ID. Total cell numbers for each tSNE plot are indicated. NFO, newly formed oligodendrocytes; OPC, oligodendrocyte progenitor cells; MO, mature oligodendrocytes. (C) Heat map of z-scores of expression for select genes within inhibitory neuronal clusters. Clusters are organized on the basis of the hierarchical tree constructed with expression in principal component space, with some of the genes differentially expressed between branches indicated (blue). The nomenclature of clusters uses a numeric indicator of excitatory or inhibitory cluster followed by one or two marker genes, with the first marker typically a neuromodulator (29). Inhibitory and excitatory clusters that lack a notable neuromodulator marker gene were designated as Gaba and Glut, respectively, with an additional marker gene to help differentiate among these clusters when possible. Cluster names are colored according to the first gene. Predicted anatomical locations for the clusters are listed on the tree, and the unlabeled lines indicate that such prediction was not possible. Thick black lines underscore clusters grouped by common neuropeptide expression. (D) As in (C) but for excitatory neurons. The hybrid neuronal clusters h1/h2 and h3 are listed in (C) and (D), respectively, because they were initially classified as inhibitory and excitatory, respectively. (E) –log10(P value) for the enrichment of gene categories in differentially expressed genes that mark neuronal clusters calculated based on a gene-set enrichment analysis as shown in fig. S6. *P < 0.05.

## Panel-by-Panel 解读

### Panel A — 视前区解剖与取样范围
**结论**：洋红色框定义了 scRNA-seq 取样的下丘脑视前区。

**关键数据**：组织约 2.5 × 2.5 × 1.1 mm，Bregma +0.5 至 –0.6。

### Panel B — 全细胞及神经元 tSNE
**结论**：无监督降维将主要细胞类和神经元亚群分开。

**关键数据**：总计 31,299 cells；抑制性神经元 15,042 cells；兴奋性神经元 3,511 cells。

### Panel C — 抑制性神经元层级树与 marker 热图
**结论**：抑制性集群常按神经调质/神经肽及其组合 marker 分支，标记为 i1–i45。

**关键数据**：43 个抑制性亚群；示例包括 Gal、Crh、Tac1、Sst、Avp 集群。

### Panel D — 兴奋性神经元层级树与 marker 热图
**结论**：兴奋性集群更多显示与解剖核团相关的分组，标记为 e1–e24，并含 h3。

**关键数据**：23 个兴奋性亚群；混合神经元共 3 个（h1–h3）。

### Panel E — marker 基因类别富集
**结论**：神经肽/神经调质合成与转运基因、转录因子比受体更能区分集群。

**关键数据**：富集以 –log10(P value) 表示，*P < 0.05；受体整体表达更广且更低。

## 总体结论
Fig. 1 建立了视前区单细胞分子分类框架：31,299 个细胞被划分为主要细胞类，并在神经元中解析出约 70 个集群（43 抑制性、23 兴奋性、3 混合性）。集群身份主要由多个神经肽、神经调质通路基因和转录因子的组合定义，而非单一 marker。

## 关联 Figures / Extended Data
- Fig. 2：Gal、Th、Bdnf/Adcyap1 集群的进一步细分
- Fig. 3：将 scRNA-seq marker 转入 MERFISH 空间测量
- fig. S1–S7：解离、聚类及 marker/ISH 支持证据
