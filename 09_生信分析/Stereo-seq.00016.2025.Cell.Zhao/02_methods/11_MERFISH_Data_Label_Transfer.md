# Method: Integrative Cell Type Annotation by Transferring MERFISH Data Labels

## 原文（Methods）
> We performed a cell annotation mapping procedure based on the original expression matrices of our own and MERFISH data. After aligning common genes in the dataset, we summarized gene expression within each cell cluster, which identified by cell segmentation, in the dataset and compared it to the cell clusters in the MERFISH dataset using Spearman rank correlation, thus facilitating the transfer of cell type annotations from the MERFISH dataset to our study. This annotation process was further refined by considering multiple top-ranked MERFISH clusters and manual correction using cluster-specific marker genes.

## 解读

### 意义
通过与MERFISH数据的整合分析，将已注释的MERFISH细胞类型标签映射到Stereo-seq数据。

### 输入
- Stereo-seq单细胞表达矩阵
- MERFISH参考数据集及其细胞类型注释

### 输出
- Stereo-seq数据的细胞类型注释

### 核心步骤
1. 对齐两个数据集的共同基因
2. 汇总每个细胞簇的基因表达
3. 使用Spearman秩相关比较细胞簇
4. 从MERFISH转移细胞类型注释
5. 结合多个top-ranked MERFISH簇和标记基因进行人工校正

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 相关性方法 | Spearman rank correlation | |
| 注释来源 | MERFISH参考数据 | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| MERFISH | Multiplexed Error-robust Fluorescence In Situ Hybridization |
| Spearman correlation | 秩相关分析 |

## 复现
- MERFISH参考数据: https://alleninstitute.github.io/abc_atlas_access/descriptions/Zhuang-ABCA-2.html

## 生物学意义
MERFISH提供了高分辨率的细胞类型注释参考，整合注释可以提高Stereo-seq数据的注释准确性。

## 涉及 Figures
- Fig. 2D (cell type annotation comparison)
