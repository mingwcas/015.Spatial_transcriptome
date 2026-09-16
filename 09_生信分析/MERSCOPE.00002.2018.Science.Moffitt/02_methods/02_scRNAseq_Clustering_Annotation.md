# Method: Louvain 聚类与神经元集群注释（43 抑制性 i1–i45 / 23 兴奋性 e1–e24 / 3 混合性 h1–h3）

## 原文（Methods）
> We used unsupervised, graph-based, community-detection methods (28, 30, 31) modified by us (fig. S2) to cluster cells (29). This led to the delineation of major cell classes... Further clustering of inhibitory neurons (15,042 cells) and excitatory neurons (3511 cells) separately revealed 43 and 23 subpopulations, respectively... Cells in two neuronal clusters originally designated as inhibitory and one originally designated as excitatory coexpressed Slc17a6 (or Slc17a8, vGlut3) and Slc32a1... We denote these clusters as h1, h2, and h3.
> Cell clusters were identified by using Louvain community detection on a nearest-neighbor graph built on the statistically significant principle components of gene expression (28, 31, 73) modified to allow an optimized choice of the number of nearest neighbors in the graph.

**来源**：正文 Results（PDF p.2–3）与 Methods summary（PDF p.12）。

## 解读

### 意义
把 3 万余个细胞的表达矩阵转化为有限个可命名、可复用的"细胞类型"，并用层级树揭示这些类型之间的分子亲缘关系。

### 输入
- 31,299 细胞 × 全转录组表达矩阵
- 细胞类标签（抑制性 / 兴奋性 / 非神经元）
- 统计显著主成分（statistically significant PCs）

### 输出
- 主要细胞类划分（神经元 + 9 类非神经元）
- 抑制性亚群 43 个（i1–i45）、兴奋性亚群 23 个（e1–e24）、混合亚群 3 个（h1–h3）
- 每个集群的前 5 个差异表达基因与 marker 命名（如 i16:Gal/Th）
- 层级树与预测解剖位置

### 核心步骤
1. 在显著主成分上构建 k 近邻图（k 值可优化选择）
2. 在近邻图上运行 Louvain community detection
3. 得到主要细胞类；对抑制性与兴奋性神经元**分别**再次聚类
4. 用 Slc17a6 / Slc32a1 判别兴奋性 vs 抑制性；识别同时共表达二者的混合集群
5. 取各集群 top 差异表达基因，按"编号 + 标记基因"命名（首个 marker 通常为神经调质）
6. 在 PCA 空间构建层级树，并做基因类别富集分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 聚类算法 | Louvain community detection | 基于图的社区发现 |
| 图构建 | nearest-neighbor graph on significant PCs | 在显著主成分上建近邻图 |
| 抑制性亚群 | 43 clusters（i1–i45） | 抑制性神经元细分数 |
| 兴奋性亚群 | 23 clusters（e1–e24） | 兴奋性神经元细分数 |
| 混合亚群 | 3 clusters（h1, h2, h3） | 共表达 Slc17a6/Slc32a1 的集群 |
| 判别基因 | Slc17a6 vs Slc32a1 | 比 Gad1/Gad2 更可靠的兴奋/抑制判别子 |
| 差异表达检验 | MAST，FDR < 0.01 | Fig. 2 标记基因富集统计 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Louvain | 基于模块度优化的图社区发现算法 |
| tSNE | t-distributed stochastic neighbor embedding，降维可视化 |
| h1/h2/h3 | hybrid 集群，疑似 GABA/谷氨酸共释放神经元 |
| Slc17a6 / Slc32a1 | 编码 Vglut2 / Vgat，兴奋性 / 抑制性神经元判别基因 |
| MAST | Model-based Analysis of Single-cell Transcriptomics，差异表达检验框架 |
| GSEA | gene-set enrichment analysis，基因类别富集分析 |

## 复现
- 工具：Louvain（文献 28 路线）、Seurat/Scanpy 生态、MAST（文献 75）
- 代码：https://github.com/ZhuangLab/MERFISH_analysis

```r
# 概念性流程
pcs <- significant_pcs(expr)                 # 统计显著主成分
g   <- build_knn(pcs, k = optimized_k)       # k 可优化
clu <- louvain(g, resolution = res)          # community detection
de  <- MAST::zlm(~cluster, expr); de <- de[de$fdr < 0.01, ]
```

## 生物学意义
聚类结果显示神经元集群**主要靠神经肽、神经调质合成/转运基因与转录因子**区分，而神经调质受体表达广泛且水平低、判别力弱——这对后续用受体基因做功能研究是重要警示。层级树上，抑制性集群常按共有神经调质聚集（如 Avp/Gal/Crh/Tac1/Sst），而兴奋性集群更多按解剖核团聚集（如 e4/e2/e21/h3/e17 位于 PVN 及邻近核团）。局限：转录组相似 ≠ 功能相同；少数极低丰度集群可能并非真实细胞类型。

## 涉及 Figures
- **Fig. 1B** — 细胞类与神经元亚群的 tSNE
- **Fig. 1C / 1D** — 抑制性 / 兴奋性集群的 z-score 热图与层级树
- **Fig. 1E** — 基因类别在差异表达基因中的富集（*P < 0.05）
- **fig. S2–S5** — 聚类改良、GABA/谷氨酸判别、marker 与神经肽表达
