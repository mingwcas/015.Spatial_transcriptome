# Method: Cell-Cell Interaction/Avoidance Analysis

## 原文（Methods）
> Pairwise spatial interactions were assessed using a permutation-based method. Two cells were considered to be 'interacting' if their centroids were within a 6 μm radius. For each sample, we calculated the observed frequency of interaction for every pairwise combination of cell types. To determine whether the observed frequency deviated significantly from a random spatial arrangement, we generated a null distribution through spatial permutation. For each of 1,000 permutations per sample, the x and y coordinates of all cells were randomized while preserving the overall cell density and sample boundaries. The p-value for an observed interaction (or avoidance) frequency was calculated as the proportion of permutations where the randomized frequency was greater than or equal to (or less than or equal to, for avoidance) the observed frequency. p-values from individual samples within the same group were combined using Fisher's combined probability test. A combined p-value of less than 0.05 was considered statistically significant, indicating non-random spatial association (interaction) or dissociation (avoidance). The analysis assumed symmetry in pairwise relationships. Potential ligand-receptor interactions were inferred using the 'CellChat' R package (v1.6.1), which models communication probability based on the expression of ligands and receptors and their published interaction databases. Significant ligand-receptor pairs were identified using a permutation test within the 'CellChat' framework (p < 0.01).

## 解读

### 意义
细胞间相互作用/回避分析在单细胞空间分辨率下量化不同细胞类型之间的空间共定位关系，揭示肿瘤微环境中的细胞间通信网络。

### 输入
- 细胞分割后的空间坐标（x, y）
- 细胞类型注释
- CellChat配体-受体数据库

### 输出
- 细胞类型pairwise相互作用/回避热图
- 统计显著性p值（Fisher combined probability test）
- CellChat推断的配体-受体相互作用对

### 核心步骤
1. 定义"相互作用"：细胞质心距离<6μm
2. 计算每样本每对细胞类型的观察相互作用频率
3. 空间置换检验（每样本1,000次置换）
4. 置换检验p值计算
5. Fisher联合概率检验合并p值
6. CellChat分析配体-受体通信

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 相互作用距离阈值 | 6 μm | 细胞质心距离 |
| 置换次数 | 1,000次/样本 | 构建零分布 |
| 显著性阈值 | combined p < 0.05 | 统计显著 |
| CellChat版本 | v1.6.1 | 配体-受体分析 |
| CellChat显著性 | p < 0.01 | 置换检验 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 相互作用 | 细胞质心距离<6μm的空间共定位 |
| 回避 | 细胞间距离显著大于随机预期的空间分离 |
| Fisher combined probability test | 合并多个独立检验p值的方法 |
| CellChat | 基于配体-受体表达推断细胞间通信的工具 |

## 复现
- 工具/代码/URL：
  - CellChat: https://github.com/jinworks/CellChat.git
  - 空间置换方法来自Karimi et al., Nature 2023 (https://doi.org/10.1038/s41586-022-05680-3)
- 代码片段：
```r
# Spatial interaction analysis
# CellChat analysis
library(CellChat)
cellchat <- createCellChat(object = data, group.by = "cell_type")
cellchat <- subsetData(cellchat)
cellchat <- identifyOverExpressedGenes(cellchat)
cellchat <- identifyOverExpressedInteractions(cellchat)
cellchat <- computeCommunProb(cellchat)
cellchat <- filterCommunication(cellchat, min.cells = 10)
```

## 生物学意义
该分析揭示了恶性细胞与免疫细胞之间的空间回避行为（C5、C6、C9亚群表现出免疫排除特征），以及内皮细胞与多种免疫细胞类型（巨噬细胞、效应T细胞、B细胞）之间的正向空间关联。这表明淋巴结转移过程中血管-免疫 niche被动态重编程。

## 涉及 Figures
- **Fig. 4A, 4B, 4C** — 细胞间相互作用/回避热图和相关性
- **Fig. S7, S8, S9, S10** — Extended interaction analysis
