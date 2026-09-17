# Fig. 5 — Tumor Heterogeneity and Communication Signatures

## Caption（原文）
> (A) Spatial and transcriptomic heterogeneity of tumor cells across the primary tumor tissue.
> (B) As in (A), but in the metastatic tissue.
> (C) Spatial neighborhood enrichment of tumor and stroma populations.
> (D) Normalized enrichment score in the tumor subclusters highlights differentially active gene programs.
> (E) Cell-cell communication is organized as spatial motifs discovered with non-negative matrix factorization.

## Panel-by-Panel 解读

### Panel A — 原发肿瘤异质性
**结论**：原发肿瘤中肿瘤状态组织成连续的空间域

**关键数据**：10个转录组状态(T1-T10)，每个状态在特定区域富集

### Panel B — 转移性肿瘤异质性
**结论**：转移性肿瘤中肿瘤状态更加混合

**关键数据**：肿瘤状态没有明确边界，与原发肿瘤形成对比

### Panel C — 邻域富集分析
**结论**：细胞类型空间相互作用在原发和转移肿瘤中不同

**关键数据**：置换检验p值<0.05的显著空间相互作用

### Panel D — 基因程序活性
**结论**：不同肿瘤亚簇具有不同的活性基因程序

**关键数据**：NES>1且FDR调整p值<0.05的程序

### Panel E — 通讯热点
**结论**：细胞间通讯组织成空间因子，对应肿瘤异质性

**关键数据**：4个NMF因子：炎症(F1)、基质硬度(F2)、粘附(F3)、ECM重塑(F4)

## 总体结论
Fig. 5揭示了原发和转移HNSCC中肿瘤细胞状态的空间组织，以及这些状态与细胞间通讯热点的紧密关联，为理解肿瘤微环境提供新视角。

## 关联 Figures / Extended Data
- Fig. S6 — 肿瘤亚簇与基因程序活性
