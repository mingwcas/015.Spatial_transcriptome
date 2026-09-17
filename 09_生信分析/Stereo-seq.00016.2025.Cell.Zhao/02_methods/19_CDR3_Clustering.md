# Method: CDR3 Clustering and Consensus Sequence Analysis

## 原文（Methods）
> Besides identical BCR clones, we also noticed that some BCR clones shared similar complementarity-determining region 3 (CDR3) sequences, suggesting similar target antigen epitopes. To explore this, we computed the pairwise Levenshtein distance across all CDR3 sequences of IGH and IGK and then performed hierarchical clustering on BCR clones. We partitioned BCR clones with distances shorter than 7 into a cluster and classified the BCR clones into 36 IGK and 96 IGH clusters. Then, we constructed consensus sequences for clusters with more than three clones each from RNA-seq data and Stereo-seq V2 data.

## 解读

### 意义
通过CDR3序列相似性聚类，识别具有相似抗原表位的BCR克隆群。

### 输入
- BCR克隆的CDR3氨基酸序列
- IGH和IGK克隆型

### 输出
- CDR3聚类结果
- 共有序列(consensus sequences)

### 核心步骤
1. 计算所有CDR3序列两两之间的Levenshtein距离
2. 层次聚类
3. 距离<7的克隆归为一个簇
4. 构建共有序列（≥3个克隆的簇）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 距离阈值 | <7 | 聚类阈值 |
| 最小克隆数 | ≥3 | 构建consensus |
| 聚类数 | 36 IGK + 96 IGH | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CDR3 | Complementarity Determining Region 3 |
| Levenshtein距离 | 编辑距离 |
| Consensus sequence | 共有序列 |

## 复现
- Levenshtein: https://rapidfuzz.github.io/Levenshtein/
- ClustalW: http://www.clustal.org/clustal2/
- 版本：2.1

## 生物学意义
具有相似CDR3的克隆可能靶向相同抗原表位，聚类分析有助于发现Mtb特异性BCR克隆。

## 涉及 Figures
- Fig. 7F, 7G (CDR3 clustering and consensus sequences)
