# Method: 视前区 Droplet-based scRNA-seq（31,299 细胞）

## 原文（Methods）
> We dissected a rostral part of the mouse hypothalamus that contains the preoptic region (Fig. 1A)—the medial preoptic area (MPOA) and surrounding nuclei (~2.5 by 2.5 by 1.1 mm, Bregma +0.5 to –0.6)—from adult female and male brains and dissociated the tissue using a custom protocol that improved cell survival and capture (fig. S1). We collected scRNA-seq profiles from 31,299 cells across three replicates of each sex using droplet-based scRNA-seq (27–29).
> scRNA-seq of the preoptic region was performed by using protocols modified from (70) to increase neuronal survival.

**来源**：正文 Results "scRNA-seq of the preoptic region"（PDF p.2）与 Methods summary（PDF p.12）。注意：本文详细 Methods 位于 Supplementary Materials，正文 PDF 仅含 Methods summary。

## 解读

### 意义
用全转录组、无偏的方式对视前区所有细胞做分子普查，解决"该区域到底有多少种细胞类型"这一根本问题，并为后续 MERFISH 基因 panel 提供标记基因来源。

### 输入
- 成年雌雄小鼠脑组织（含 MPOA 及周边核团）
- 解剖坐标：Bregma +0.5 至 –0.6，组织块 ~2.5 × 2.5 × 1.1 mm
- 改良的解离协议（提高神经元存活率与捕获率）
- droplet-based scRNA-seq 平台（Drop-seq 型，参考文献 27–29）

### 输出
- 31,299 个细胞的表达矩阵（雌雄各 3 个生物学重复）
- 主要细胞类注释：抑制性神经元、兴奋性神经元、microglia、astrocytes、immature OD（NFO/OPC）、mature OD、ependymal、endothelial、fibroblasts、macrophages、mural cells
- 神经元亚群：抑制性 15,042 细胞、兴奋性 3,511 细胞
- 后续用于 MERFISH panel 设计的差异表达基因清单

### 核心步骤
1. 解剖含视前区的小鼠下丘脑前部组织块（Bregma +0.5 至 –0.6）
2. 用自定义改良协议解离组织，提高神经元存活与捕获
3. 对雌雄各 3 个重复样本做 droplet-based scRNA-seq
4. 质控与合并，共获得 31,299 个细胞表达谱
5. 输出表达矩阵供下游无监督聚类（见 `02_scRNAseq_Clustering_Annotation.md`）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 细胞总数 | 31,299 cells | 最终通过质控的 scRNA-seq 细胞数 |
| 生物学重复 | 3 replicates / sex | 每个性别 3 个独立动物样本 |
| 组织尺寸 | ~2.5 × 2.5 × 1.1 mm | 解剖的视前区组织块体积 |
| 解剖坐标 | Bregma +0.5 to –0.6 | 前后轴范围 |
| 平台 | droplet-based scRNA-seq | 基于液滴分隔的单细胞测序 |
| 神经元数 | inhibitory 15,042 / excitatory 3,511 | 用于二次聚类的神经元细胞数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| MPOA | medial preoptic area，内侧视前区，视前区核心核团 |
| scRNA-seq | single-cell RNA sequencing，单细胞转录组测序 |
| droplet-based | 液滴微流控分隔单细胞并加条形码的技术路线 |
| NFO | newly formed oligodendrocytes，新形成少突胶质细胞 |
| OPC | oligodendrocyte progenitor cells，少突胶质前体细胞 |
| MO | mature oligodendrocytes，成熟少突胶质细胞 |
| Bregma | 小鼠颅骨前囟，立体定位坐标零点 |

## 复现
- 数据：GEO **GSE113576**（scRNA-seq 原始数据）
- 分析代码：https://github.com/ZhuangLab/MERFISH_analysis
- 解离协议参考：(70) Campbell et al., Nat. Neurosci. 20, 484–496 (2017) 并做改良

```r
# 概念性流程：读入表达矩阵 → QC → 归一化
mat <- Read10X("GSE113576/filtered_feature_bc_matrix")
mat <- mat[, Matrix::colSums(mat) > 0]     # 去除空液滴
# 解离改良重点：提高神经元存活率（降低解离温度/时间，加保护剂）
```

## 生物学意义
该步骤首次以全转录组精度刻画视前区的细胞组成，证明该区域神经元多样性远超"少数几种功能细胞"的传统认知（最终收敛为 ~70 个神经元集群）。局限：需解离组织，**丢失空间信息**；astrocytes、endothelial、ependymal 因解离丢失而在 scRNA-seq 中比例偏低，必须由 MERFISH 原位数据补足。

## 涉及 Figures
- **Fig. 1A** — 解剖区域示意（洋红色框标记 Bregma +0.5 至 –0.6）
- **Fig. 1B** — 全部细胞 / 抑制性 / 兴奋性神经元的 tSNE（31,299 / 15,042 / 3,511 cells）
- **fig. S1** — 改良解离协议对细胞存活与捕获的提升
