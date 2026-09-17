# Fig. 6 — Multimodal analysis of tumor neighborhoods identiﬁes an EMT niche at the tumor surface

## Caption（原文）
> (A) 3D neighborhoods reveal numerous stroma-inﬁltrating tumor cells. 3D rendering of the tumor bed highlights tumor cells extending beyond the tumor surface into the surrounding stroma.
> (B) Pseudotime captures tumor epithelial-to-mesenchymal (EMT) dynamics. UMAPs of tumor cell transcriptomic proﬁles colored by pseudotime rank (left) and the SCT-normalized expression of pseudotime-associated EMT marker genes.
> (C) EMT is activated progressively from the tumor core to the desmoplastic stroma. Boxplot of the pseudotime rank of tumor cells in the tumor core, surface, and desmoplastic stroma. ****: t test p values < 0.005, n = 38,804.
> (D) Tumor EMT is upregulated not only in the desmoplastic stroma but already in one region of the tumor surface. Spatial distribution of pseudotime rank scores numerous mesenchymal tumor cells in the EMT niche (black box).
> (E) Inﬁltrating tumor cells are surrounded by a stiff ECM. Spatial plot of collagen ﬁber abundance in tumor cell neighborhoods.
> (F) Matrix stiffness accompanies tumor EMT in the desmoplastic stroma but cannot explain its induction in the EMT niche. Boxplot of collagen ﬁber abundance in tumor cell neighborhoods across the EMT niche and ECM compartments.

## Panel-by-Panel 解读

### Panel A — 肿瘤浸润3D渲染
**结论**：3D渲染显示大量肿瘤细胞（24.0%，>9,000个）延伸到肿瘤表面之外浸润周围基质。

**关键数据**：38,804个肿瘤细胞，24.0%浸润到其他niche。

### Panel B — EMT伪时间
**结论**：伪时间捕获了肿瘤细胞从上皮（CDH1+, EPCAM+高表达）到间充质（ITGB6+, COL3A1+高表达）的表型转变。

**关键数据**：伪时间0=上皮，1=间充质；关键marker基因的动态表达。

### Panel C — EMT空间梯度
**结论**：EMT从肿瘤核心到表面再到促结缔组织增生基质逐步激活。

**关键数据**：伪时间中位数：tumor core 0.39, tumor surface 0.50, desmoplastic stroma 0.85（p<0.05）。

### Panel D — EMT niche鉴定
**结论**：肿瘤表面的一个特定区域（EMT niche）中，mesenchymal-like肿瘤细胞集中分布，这些细胞虽位于肿瘤bed内（early pseudospace）但已显示晚期伪时间（late pseudotime）。

**关键数据**：EMT niche中伪时间密度峰值。

### Panel E-F — ECM与EMT的关系
**结论**：浸润到促结缔组织增生基质的肿瘤细胞确实具有间充质表型，但EMT niche中的肿瘤细胞生活在胶原少的ECM中（类似肿瘤bed其余部分）。因此胶原硬度可以维持浸润细胞的EMT，但不能解释EMT niche中的EMT诱导。

**关键数据**：EMT niche中胶原信号与肿瘤bed其余部分相似，远低于desmoplastic stroma。

## 总体结论
Fig. 6揭示了关键发现：EMT不仅发生在浸润到硬基质的肿瘤细胞中，更早在肿瘤表面的一个特定EMT niche中就已预先激活。该niche中存在独立于ECM硬度的EMT诱导机制，需要进一步寻找触发因素。

## 关联 Figures / Extended Data
- ED Fig. S6A-E — 肿瘤浸润量化、伪时间密度、IF验证CDH1low细胞
