# Fig. 4 — Neuronal clusters in the preoptic region as revealed with MERFISH

## Caption（原文）
> Fig. 4. Neuronal clusters in the preoptic region as revealed with MERFISH. (A and B) z-scores of expression profiles for (A) inhibitory and (B) excitatory neuronal clusters identified with MERFISH. Depicted are 100 random cells from each cluster. The neuronal clusters are organized on the basis of similarity in their expression profiles, as depicted by the dendrogram. The sizes of red, cyan, and yellow circles indicate the abundance of neuronal clusters, and only clusters with more than 100 cells are depicted. H-1 is grouped with the inhibitory clusters because it was initially classified as inhibitory neurons. (C) The pairwise Pearson correlation coefficients between the expression profile (in z-score) of the MERFISH and scRNA-seq clusters. The order of the clusters in (C) is not the same as in (A) and (B). (D) As in (C) but with only scRNA-seq cluster(s) most similar to each MERFISH cluster shown, identified as the cluster(s) with the highest Pearson correlation coefficient(s) (fig. S14 and table S9) (29). When multiple scRNA-seq clusters show statistically indistinguishable, highest correlation coefficients to a MERFISH cluster (29), all of them are indicated. scRNA-seq clusters outside the region imaged with MERFISH, as assessed by the expression patterns of the marker genes in the Allen Brain Atlas (35) and our own in situ data (fig. S7) (29), are excluded from this analysis (29). (E) Same as (D) but for clusters enriched in galanin (Gal).

## Panel-by-Panel 解读

### Panel A — 抑制性 MERFISH 集群
**结论**：抑制性细胞形成约 40 个 I-集群，表达谱相似性由树状图组织。

**关键数据**：每集群显示 100 个随机细胞；仅绘制细胞数 >100 的集群。

### Panel B — 兴奋性 MERFISH 集群
**结论**：兴奋性细胞形成约 30 个 E-集群，部分集群在 scRNA-seq 中未被同样分辨。

**关键数据**：MERFISH 识别约 30 个 excitatory populations；圆点大小代表集群丰度。

### Panel C — MERFISH 与 scRNA-seq 全集群相关矩阵
**结论**：多数 MERFISH 神经元集群与 scRNA-seq 集群有良好表达相关性。

**关键数据**：指标为 z-score 表达谱的 pairwise Pearson correlation。

### Panel D — 最相似跨平台集群
**结论**：每个 MERFISH 集群可按最高相关系数推断一个或多个 putative scRNA-seq 对应集群。

**关键数据**：多集群最高相关相同或统计不可区分时全部显示；区域外 scRNA-seq 集群排除。

### Panel E — Gal 富集集群对应
**结论**：MERFISH 能把一个 scRNA-seq 集群进一步拆成空间/分子亚群。

**关键数据**：I-14 与 I-16 都对应 scRNA-seq i16，分别为 Calcr/Brs3+ 与 Th+，显示 MERFISH 的亚群解析能力。

## 总体结论
Fig. 4 证明 MERFISH 与 scRNA-seq 在神经元集群层面具有互补而非简单重复的关系：相关性实现跨平台注释，原位测量则可进一步拆分 scRNA-seq 未解析的亚群。约 75 个最富信息基因可恢复约 90% 集群，但 panel 缺失或样本量不足仍会造成部分集群不对应。

## 关联 Figures / Extended Data
- Fig. 3：主要细胞类跨平台相关
- Fig. 5：将 MERFISH 集群放回解剖核团
- fig. S13–S16：基因数、神经网络、Gal 亚群及空间异质性分析
- table S9：MERFISH 与 scRNA-seq 对应关系
