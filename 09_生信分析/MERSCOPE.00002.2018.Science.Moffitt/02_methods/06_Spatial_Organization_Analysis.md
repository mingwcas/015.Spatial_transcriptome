# Method: 空间分布与邻域复杂度/纯度分析

## 原文（Methods）
> Next, we examined the spatial distributions of individual neuronal clusters (Fig. 5A and figs. S17 and S18) within the framework of major anatomically defined nuclei of the preoptic region as depicted in Fig. 5B (45). About 30% of the MERFISH clusters were enriched primarily in a single nucleus (Fig. 5C, pink shading)... whereas approximately half of the clusters were distributed over a few (two to four), often physically contiguous nuclei (Fig. 5C, unshaded clusters)... By contrast, a small fraction of the neuronal clusters were dispersed and not enriched in any given nucleus, such as I-21 and E-22 (Fig. 5A).
> To quantify the degree of intermixing, we calculated the neighborhood composition for each neuron. This analysis showed that each neighborhood contained multiple clusters and was typically not dominated by a single cell population (Fig. 5, D and E).

**来源**：正文 Results "Spatial organization of specific neuronal cell types"（PDF p.7–8）。

## 解读

### 意义
把"细胞类型"与"解剖核团"两套体系对接起来：回答某个分子定义的细胞类型是否等同于一个核团，以及不同细胞类型在组织中是分层聚居还是高度混居。

### 输入
- MERFISH 细胞分割边界 + 细胞类/集群标签 + 三维坐标（12 层切片）
- 参考脑图谱核团边界：Paxinos & Franklin, The Mouse Brain in Stereotaxic Coordinates（文献 45）
- 对齐地标：anterior commissure、fornix、ventricle

### 输出
- 各神经元集群的空间分布图（局部型 vs 弥散型）
- 集群 × 核团富集矩阵（哪些核团只含抑制性或只含兴奋性集群）
- 每个神经元的 100 μm 半径邻域复杂度分布（**复杂度** = 邻域内出现的不同集群数）
- 每个神经元的 100 μm 半径邻域纯度分布（**纯度** = 邻域内最丰富集群占全部细胞的比例）
- 基于解剖的分类命名（弥散型集群仍按 marker 基因命名）

### 核心步骤
1. 把 12 层成像切片按地标对齐到参考脑图谱的核团边界
2. 统计各集群在每个核团内的富集情况，判定"单核团 / 数核团 / 弥散"
3. 标注只含兴奋性或只含抑制性集群的核团
4. 对每个神经元取半径 100 μm 的邻域，统计其中的集群种类数（复杂度）
5. 计算该邻域内最丰富集群所占比例（纯度）
6. 绘制复杂度与纯度的概率分布，量化局部混居程度
7. 结合解剖位置给集群命名，并用 MERFISH↔scRNA-seq 对应关系回推 scRNA-seq 集群的位置

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 邻域半径 | 100 μm | 计算复杂度/纯度的空间尺度 |
| 复杂度定义 | 邻域内不同神经元集群的数目 | 局部细胞类型多样性 |
| 纯度定义 | 邻域内最丰富集群占全部细胞的比例 | 局部细胞类型均一程度 |
| 单核团集群 | ~30% of clusters | 主要局限在一个核团 |
| 跨 2–4 核团集群 | ~half of clusters | 常为物理上相邻的核团 |
| 纯兴奋性核团 | PVA, BAC | 仅含兴奋性集群 |
| 纯抑制性核团 | BNST-p, BNST-mv | 仅含抑制性集群 |
| 弥散型示例 | I-21, E-22 | 不富集于任何核团 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Neighborhood complexity | 邻域复杂度，半径 100 μm 内不同集群的种类数 |
| Neighborhood purity | 邻域纯度，邻域内最丰富集群的细胞占比 |
| Nucleus enrichment | 集群在特定核团内的相对富集 |
| Dispersed cluster | 弥散型集群，无核团偏好 |
| Paxinos atlas | 小鼠脑立体定位坐标图谱，核团边界来源 |
| BNST / MPN / VLPO / PVA / BAC | 见 Fig. 3F 与 Fig. 5B 的核团缩写表 |

## 复现
- 代码：https://github.com/ZhuangLab/MERFISH_analysis
- 核团边界：Paxinos & Franklin (2007) 第 3 版图谱（文献 45）

```python
# 概念性流程
for neuron in cells:
    nb = neighbors_within(neuron, r=100)          # 100 μm 邻域
    complexity[neuron] = len(unique_clusters(nb))
    purity[neuron]     = max_cluster_fraction(nb)
# 核团归属与富集
enrich = cluster_by_nucleus(cells.cluster, cells.nucleus_label)
```

## 生物学意义
该分析揭示视前区神经元集群的空间组织高度多样：既有"一个集群 ≈ 一个核团"的紧密对应（如 I-5 主要位于 VLPO、E-9 位于 PVA），也有跨多个相邻核团的同一细胞类型——可能反映同一功能在不同核团中的复用，或发育上的亲缘关系。同时，任一核团内部都由多个集群混居，**单一集群很少主导某个邻域**，说明"核团"与"细胞类型"不是同一层级的组织单位。局限：集群与核团的对应建立在参考图谱边界对齐之上，存在配准误差；scRNA-seq 集群的推定位置依赖较粗糙的原位杂交图谱，只是近似。

## 涉及 Figures
- **Fig. 5A** — 局部型与弥散型神经元集群的空间分布示例
- **Fig. 5B** — 成像范围内主要下丘脑核团示意图（含 Bregma 位置）
- **Fig. 5C** — 抑制性/兴奋性集群富集核团汇总（粉色竖条标单一核团集群）
- **Fig. 5D / 5E** — 100 μm 邻域复杂度与纯度的概率分布
- **fig. S17 / S18** — 其余集群的空间分布
- **table S9** — 集群的解剖命名与对应关系
