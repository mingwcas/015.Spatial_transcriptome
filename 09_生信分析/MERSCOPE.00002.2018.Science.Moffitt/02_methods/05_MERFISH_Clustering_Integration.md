# Method: MERFISH 聚类与跨平台整合（与 scRNA-seq 对应）

## 原文（Methods）
> We used an unsupervised, community-detection–based clustering approach similar to that applied to scRNA-seq data to identify transcriptionally distinct cell populations in MERFISH data (Fig. 3, B and C, and table S7) (29).
> Clustering analyses of inhibitory neurons and excitatory neurons separately identified ~40 inhibitory and ~30 excitatory neuronal populations (Fig. 4, A and B, and tables S7 and S8). We investigated the impact of the number of genes used to cluster cells in MERFISH data and found that ~90% of the identified neuronal clusters were recovered by using the ~75 genes that were most informative among the 155 (fig. S13).
> The expression profiles of most neuronal clusters determined with MERFISH correlated well with those of scRNA-seq clusters (Fig. 4C and fig. S14, A and B). This observation allowed us to infer, for each MERFISH cluster, the putative corresponding or most similar scRNA-seq cluster(s), defined as the cluster(s) with the highest correlation coefficient(s) (Fig. 4D, fig. S14C, and table S9) (29).

**来源**：正文 Results（PDF p.6–7）。

## 解读

### 意义
把 MERFISH 的 100 万个原位细胞压缩成可与 scRNA-seq 对齐的细胞类型体系，从而同时获得"全转录组分子定义"与"原位空间定位"两种信息。

### 输入
- MERFISH 细胞 × 155 基因矩阵（naïve 动物 ~500,000 细胞）
- scRNA-seq 集群表达谱（43 抑制性 + 23 兴奋性 + 3 混合）
- 155 基因中各基因的信息量排序（fig. S13）

### 输出
- MERFISH 主要细胞类聚类（table S7）
- ~40 个抑制性（I-1, I-2, …）与 ~30 个兴奋性（E-1, E-2, …）神经元集群 + 1 个混合集群 H-1
- MERFISH ↔ scRNA-seq 集群的 Pearson 相关矩阵与"最相似集群"对应表（table S9）
- 基于解剖位置与 marker 基因的集群命名体系

### 核心步骤
1. 对 MERFISH 数据施加与 scRNA-seq 相似的无监督社区发现聚类，得到主要细胞类
2. 分别对抑制性与兴奋性神经元二次聚类，得到 ~40 I- 与 ~30 E- 集群
3. 用 155 基因中最富信息的 ~75 个基因做敏感性分析（集群恢复率）
4. 计算 MERFISH 与 scRNA-seq 集群表达谱（z-score）的两两 Pearson 相关
5. 对每个 MERFISH 集群取相关系数最高的 scRNA-seq 集群作为"推定对应"
6. 用神经网络分类器做独立验证；用 bootstrap 重复估计相关性的上限基线
7. 结合解剖位置（Fig. 5B 核团图）与 marker 基因给出集群命名

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| MERFISH 抑制性集群 | ~40 (I-1, I-2, …) | 抑制性神经元集群数 |
| MERFISH 兴奋性集群 | ~30 (E-1, E-2, …) | 兴奋性神经元集群数 |
| MERFISH 混合集群 | 1 (H-1) | 初判为抑制性 |
| 主要细胞类 | 除 macrophages/fibroblasts 外全部 | 后两者 marker 未入 panel |
| 基因敏感性 | ~75 genes → ~90% clusters | 最富信息基因的恢复率 |
| 相关性指标 | Pearson correlation（z-score） | 跨平台集群对应依据 |
| 独立验证 | 神经网络分类器 | 与相关分析相互印证 |
| 神经元采样比 | scRNA-seq ≈ MERFISH 的 4% | 解释部分集群无法对应 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| I-n / E-n / H-n | MERFISH 命名的抑制性 / 兴奋性 / 混合集群 |
| i-n / e-n / h-n | scRNA-seq 命名的对应集群 |
| Putative correspondence | 用最高相关系数推断的跨平台集群对应关系 |
| Cluster recovery | 用子集基因仍能重现的集群比例 |
| fig. S16 | 同一集群内仍存在的空间相关异质性 |

## 复现
- 代码：https://github.com/ZhuangLab/MERFISH_analysis
- 对应关系表：table S9；集群表达谱：tables S7、S8

```python
# 概念性流程
clusters = louvain_cluster(merfish_expr, genes="all155")
top75    = rank_genes_by_information(merfish_expr)[:75]
recovery = louvain_cluster(merfish_expr, genes=top75)   # ~90% 集群可恢复
corr     = pearson_z(merfish_centroids, scrna_centroids)
best     = corr.idxmax(axis=1)                          # 推定对应
```

## 生物学意义
MERFISH 与 scRNA-seq 高度互证，且**互补**：scRNA-seq 测得基因更多、定义了 marker；MERFISH 提供空间语境并更可靠地定量低表达基因（如受体）。MERFISH 还**分辨出 scRNA-seq 无法区分的亚群**——例如 I-14 与 I-16 同源于 i16，但 Calcr/Brs3+ 的 I-14 与 Th+ 的 I-16 在不同社会行为中差异激活。局限：对应关系是**推断**而非直接配对验证（两种数据并非来自同一张切片）；一小部分 MERFISH 集群与任何 scRNA-seq 集群都无显著相关；部分集群内部仍残留与空间位置相关的异质性（fig. S16）。

## 涉及 Figures
- **Fig. 3B / 3C** — MERFISH 主要细胞类聚类热图与 tSNE
- **Fig. 3D** — MERFISH 与 scRNA-seq 细胞类的 Pearson 相关矩阵
- **Fig. 4A / 4B** — 抑制性 / 兴奋性 MERFISH 集群 z-score 热图与树状图
- **Fig. 4C / 4D** — 全集群相关矩阵与"最相似集群"对应（含 Gal 富集群版本 Fig. 4E）
- **fig. S13 / S14 / S15** — 基因数敏感性、神经网络验证、Gal 集群细分
