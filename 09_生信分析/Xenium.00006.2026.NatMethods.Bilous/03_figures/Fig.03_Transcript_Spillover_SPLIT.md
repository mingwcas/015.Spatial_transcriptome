# Fig. 3 — Transcript Spillover and SPLIT Purification

## Caption（原文）
> Fig. 3 | Transcript spillover in Xenium data and the SPLIT purification approach. a, Section of a Xenium sample showing cell segmentation overlaid with RCTD-derived cell-type annotations. Border colors indicate the primary cell type assigned to each cell. Pie charts represent RCTD-computed cell-type compositions, where sector size corresponds to the proportion of each cell type and color denotes identity. Small dots represent transcripts specific to tumor cells (brown: MUC1, F3, FASN, KRT7 and EPCAM) and CD8+ T cells (blue: CD8A). b, Schematic illustrating the definition of a cell's neighborhood (top) and its neighborhood composition (bottom). c, Cosine similarity between a cell's secondary cell-type weight (w2) and the average proportion of the same cell type in its neighborhood, across all cells and samples. d, Cell-type spillover index. e, Spearman correlation between w2 and the proportion of malignant signal in spatial neighborhood of tumor-exposed cells. f,g, IHC validation showing cells misannotated due to tumor transcript spillover (f) and residual tumor transcripts in correctly annotated CD8+ T cells (g). h, Schematic of the RCTD cell-type annotation in doublet mode and SPLIT decomposition.

## Panel-by-Panel 解读

### Panel a — 分割与RCTD注释可视化
**结论**：直接展示转录本溢实现象：肿瘤特异性转录本（棕色点）出现在CD8+ T细胞边界内。

**关键数据**：
- 5µm扩展分割边界
- Pie chart显示w1/w2混合比例

### Panel b — 邻域定义示意图
**结论**：细胞邻域定义为15µm半径内最近的20个细胞，邻域组成是各细胞类型的加权比例。

**关键数据**：
- Neighborhood radius: 15µm
- Max neighbors: 20

### Panel c — w2与邻域组成的余弦相似度
**结论**：w2与邻域中同细胞类型比例呈强正相关，证实转录本溢出的空间依赖性。

**关键数据**：
- 所有panel显示显著正相关
- Breast: R ≈ 0.56
- Lung: R ≈ 0.48

### Panel d — 细胞类型溢出指数
**结论**：恶性细胞具有最高溢出指数，是最主要的污染源；T细胞等低RNA含量细胞更易被污染。

**关键数据**：
- Malignant cell溢出指数最高
- More abundant cell types显示更高溢出

### Panel e — 恶性细胞邻近与污染的相关性
**结论**：所有暴露于肿瘤的细胞类型中，w2与邻域恶性信号比例显著正相关。

**关键数据**：
- Macrophage: R = 0.51
- T cell: R = 0.42
- 其他细胞类型：R = 0.29-0.47

### Panel f,g — IHC验证
**结论**：IHC确认转录本溢出导致的注释错误：CD8+ T细胞被误判为肿瘤细胞（f），或保留残余肿瘤转录本（g）。

**关键数据**：
- IHC: CD8蛋白（粉色），panCK恶性细胞（红色）
- 转录本：肿瘤（棕色），CD8+ T（蓝色）

### Panel h — SPLIT原理示意图
**结论**：SPLIT利用RCTD权重(w1, w2)和参考图谱重新分配转录本，保留主细胞类型表达谱。

**关键数据**：
- xdoublet-SPLIT = (w1×ref1)/(w1×ref1 + w2×ref2) ⊙ xobserved

## 总体结论
Fig. 3是本文核心发现：转录本溢出是Xenium数据的主要噪声源，具有空间依赖性，SPLIT通过解卷积有效校正。

## 关联 Figures / Extended Data
- ED Fig. 5, 6 — 各panel溢出指数详细分布
- ED Fig. 7, 8 — SPLIT校正效果
