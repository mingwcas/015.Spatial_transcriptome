# Fig. 2 — Xenium 与 Visium 空间表达模式比较

## Caption（原文）
> Figure 2. Comparison of spatial gene expression patterns between Xenium and Visium. (A) Spatial gene expression of MS4A1 overlaid on the corresponding histological images for Xenium and Visium, accompanied by a density plot comparing Xenium vs. Visium MS4A1 expression. The dotted line indicates the identity line (X = Y), and the solid line represents the line of best fit. (B) Gene expression patterns for APOBEC3B: Xenium expression, Visium expression, the aggregated Visium expression combining APOBEC3B and its predicted off-target gene's expression APOBEC3D and APOBEC3F, accompanied by a density plot comparing Xenium vs. Visium APOBEC3B expression. The dotted line indicates the identity line (X = Y), and the solid line represents the line of best fit. (C) Scatterplot of log-transformed total expression counts (with a pseudocount) for 307 genes comparing Visium and Xenium data. The dotted line indicates the identity line (X = Y), and points (genes) are colored by probe information.

## Panel-by-Panel 解读

### Panel A — MS4A1（无预测脱靶）
**结论**：对于无预测脱靶结合的基因 MS4A1，Xenium 与 Visium 的空间模式在视觉上相似，说明两平台在空间对齐后对同一基因的相对表达量有一致性。

**关键数据**：
- RMSE = 3.746（相对 y = x 计算）
- Pearson r = 0.382（中等一致性）

### Panel B — APOBEC3B（有预测脱靶）
**结论**：Xenium 中 APOBEC3B 的空间模式与 Visium 明显不同；但将 Visium 中 APOBEC3B 与其预测脱靶基因 APOBEC3D、APOBEC3F **聚合**后，其空间模式与 Xenium 的 APOBEC3B 更为相似，符合"Xenium 探针脱靶结合到 APOBEC3D/3F"的预测。

**关键数据**：
- 单独 APOBEC3B：RMSE = 5.452，Pearson r = nan（Visium 中不表达）
- 聚合 APOBEC3B+3D+3F：RMSE 降至 4.465，Pearson r = 0.160（非 nan）
- IGV 可视化进一步确认了序列层面的脱靶比对

### Panel C — 307 基因总体一致性
**结论**：两平台总表达量整体呈强正相关，与 Janesick et al. 已发表结果一致；基因按探针信息着色，可直观定位异常基因。

**关键数据**：
- 307/313 基因在两平台共享（6 个基因因 Visium 缺失被排除：AKR1C1、ANGPT2、BTNL9、CD8B、POLR2J3、TPSAB1）
- Visium 原始 4992 spots，取重叠区后为 3958 spots
- Xenium 数据聚合至 ~55 μm × 55 μm 匹配 Visium 分辨率

## 总体结论
Fig. 2 提供了脱靶结合在真实空间数据中的首个实验证据：Xenium 与正交平台 Visium 的差异，可以被"目标基因 + 预测脱靶基因"的聚合表达所解释，说明脱靶结合确实在空间层面扭曲了 Xenium 的表达测量。

## 关联 Figures / Extended Data
- Appendix 1—figure 3 — STalign 结构对齐与分辨率匹配（30 μm 栅格化）
- Appendix 1—figure 7 — TUBB2B / ACTG2 的类似验证
- Appendix 1—figure 12 — ADH1B 案例（脱靶基因不表达时影响甚微）
- Appendix 1—figure 13 — HDC 案例（比对未能发现的非特异信号）
