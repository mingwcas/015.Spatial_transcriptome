# ED Fig. 7 — SPLIT and SPLIT-shift

## Caption（原文）
> Extended Data Fig. 7 | SPLIT. a-b, Integrated UMAPs of SPLIT-corrected cells using matched (a) and external (b) scRNA-seq data as reference, grouped by panel. c, Schematic of the SPLIT-shift procedure.

## Panel-by-Panel 解读

### Panel a — 匹配参考的SPLIT校正UMAP
**结论**：SPLIT校正后，使用匹配参考的各面板数据显示更好的细胞类型分离。

**关键数据**：
- 匹配参考产生更紧凑的cluster
- 面板间一致性良好

### Panel b — 外部参考的SPLIT校正UMAP
**结论**：即使使用外部参考，SPLIT仍能有效改善细胞类型分离。

**关键数据**：
- 外部参考效果略逊于匹配参考
- 整体分离仍显著改善

### Panel c — SPLIT-shift示意图
**结论**：当转录组学邻域显示细胞被错误分配primary/secondary时，SPLIT-shift交换标签并重新纯化。

**关键数据**：
- 如果邻域主要是ct2但标签为ct1
- 则交换并使用ct2作为primary

## 总体结论
ED Fig. 7证明SPLIT兼容匹配和外部参考，且SPLIT-shift处理标签交换问题。

## 关联 Figures / Extended Data
- **Fig. 3h** — SPLIT原理
- **ED Fig. 8** — SPLIT处理doublets和特异表型
