# ED Fig. 8 — Doublets and Specific Phenotypes

## Caption（原文）
> Extended Data Fig. 8 | Doublets and specific phenotypes. a, IHC and morphology image highlighting cells identified as malignant (primary) with cycling lymphocytes (secondary). b-e, UMAPs of the same Xenium sample: (b) computed on raw data; (c) subset to doublets; (d) computed on data purified using the default SPLIT; (e) computed on data purified with the neighborhood-aware SPLIT.

## Panel-by-Panel 解读

### Panel a — IHC验证
**结论**：IHC确认恶性细胞被cycling lymphocytes污染的情况，白色箭头标记的细胞显示primary为恶性但secondary为cycling lymphocytes。

**关键数据**：
- DAPI: 细胞核
- panCK: 恶性细胞
- 恶性转录本（棕色），cycling lymphocytes转录本（青色）

### Panel b — Raw数据UMAP
**结论**：Raw数据显示混合信号，cycling cells分散在malignant cluster中。

**关键数据**：多个cluster混合

### Panel c — Doublets子集UMAP
**结论**：仅看doublets时，可以看到被cycling lymphocytes污染的malignant cells。

**关键数据**：Doublets揭示污染结构

### Panel d — 默认SPLIT校正UMAP
**结论**：默认SPLIT有效纯化信号，但cycling cells被错误分类。

**关键数据**：部分cycling cells被误判

### Panel e — 邻域感知SPLIT校正UMAP
**结论**：邻域感知SPLIT保留cycling表型，因为它检测到这些细胞被错误分类。

**关键数据**：
- Proliferation signature保留
- 更准确的表型鉴定

## 总体结论
ED Fig. 8展示SPLIT如何处理复杂情况，特别是邻域感知SPLIT如何避免过度校正代表真实生物学异质性的细胞。

## 关联 Figures / Extended Data
- **ED Fig. 7c** — SPLIT-shift示意图
- **Fig. 3h** — SPLIT原理
