# Fig. 4 — 3D neighborhoods identify niche-speciﬁc interactions and unravel immune inhibitory crosstalk in dendritic cell niches

## Caption（原文）
> (A) 3D neighborhoods enable the spatial analysis of cellular interactions. The sensitive co-detection of ligands and their receptors in 3D cellular neighborhoods is leveraged to quantify ligand 3D spatial activity scores in each receiver cell.
> (B) 3D communication analysis identiﬁes niche-speciﬁc ligands. Heatmap of spatial activity z-scores for the top 5 enriched ligand per niche.
> (C–E) Ligand spatial activities mark the location of speciﬁc niches in the TME. 3D volumetric rendering of ligand spatial activity densities for PDGFB (vascular niches), AREG (tumor core and surface), and CCL19 (T and dendritic cell niches).
> (F) Cellular and molecular players of the dendritic cell niche signaling network. Dotplot of receptor-ligand interactions enriched in dendritic cell niches. Dot size: cell type-speciﬁc percentage of sender and recipient cells, dot color: cell type-speciﬁc scaled average interaction scores.
> (G) Immune checkpoint interactions suppress local anti-tumoral immune responses. Summary scheme of selected cellular and molecular interactions in dendritic cell niches, revealing mechanism-based personalized targets for cancer interception. The pill symbol indicates druggable interactions.

## Panel-by-Panel 解读

### Panel A — 通讯分析流程
**结论**：基于3D邻域中受体和配体的共检测，量化每个接收细胞的配体3D空间活性评分。

**关键数据**：480对受体-配体对，165个配体轴。

### Panel B — Niche特异性配体
**结论**：96个配体在至少1个niche中富集（log2FC>0.5），包括已知的niche特异性通讯分子。

**关键数据**：热图显示每个niche的top 5富集配体的空间活性z-score。

### Panel C-E — 配体活性3D渲染
**结论**：PDGFB限于血管niche，AREG限于肿瘤bed，CCL19标记树突状细胞和T细胞niche。配体活性的3D密度分布精确标记了niche的空间位置。

**关键数据**：配体活性密度的3D体积渲染。

### Panel F — 树突状细胞niche通讯网络
**结论**：映射了树突状细胞niche中15对受体-配体相互作用的细胞间通讯网络。成纤维细胞是CCL19-CCR7的主要发送方，淋巴内皮细胞发送CCL21；肿瘤细胞发送MIF，不接收趋化因子信号。

**关键数据**：免疫检查点：PD-L1/PD-1, Galectin-9/Tim-3, CD80-CTLA4。

### Panel G — 免疫检查点示意图
**结论**：树突状细胞niche中存在多条免疫抑制轴：DC直接通过PD-L1/PD-1和Galectin-9/Tim-3抑制CTL，间接通过CD80/CTLA4促进Treg。同时CTL在T细胞和树突状细胞niche中富集但无法浸润肿瘤核心。

**关键数据**：CTL log2FC：T cell niche 1.52, dendritic cell niche 0.43, tumor core -2.74。

## 总体结论
Fig. 4展示了3D邻域约束的通讯分析如何揭示niche特异性的细胞间通讯网络，并在树突状细胞niche中鉴定出多条免疫检查点相互作用。这些发现为免疫检查点抑制剂（nivolumab, ipilimumab）的使用提供了该患者的分子依据。

## 关联 Figures / Extended Data
- ED Fig. S4 — 通讯分析细节、Treg富集、niche特异性配体
