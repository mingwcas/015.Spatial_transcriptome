# Method: CNV Clustering

## 原文（Methods）
> To classify spatial spots and delineate malignant tumor regions, PCA dimension reduction was applied to the CNV score matrix. The cnv.pp.neighbors function computes correlations between all chromosomal regions within the PCA space with default parameters. Finally, the cnv.tl.leiden function was used to cluster all spots, with the resolution of Leiden adjusted based on the visualization of CNV using a chromosome heatmap to distinguish between malignant tumors and normal cells.

## 解读

### 意义
基于CNV评分对空间spots进行聚类，区分恶性肿瘤和正常细胞区域。

### 输入
- CNV评分矩阵（来自inferCNV）
- 空间坐标

### 输出
- 恶性/正常spot分类
- CNV聚类结果

### 核心步骤
1. PCA降维CNV评分矩阵
2. 计算染色体区域间相关性
3. Leiden聚类
4. 调整分辨率优化可视化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 降维 | PCA | |
| 聚类算法 | Leiden | |
| 分辨率 | 调整 | 可视化优化 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CNV clustering | 基于拷贝数变异的聚类 |

## 复现
- infercnvpy: https://github.com/icbi-lab/infercnvpy

## 生物学意义
CNV聚类可以区分恶性肿瘤和正常细胞，为肿瘤微环境分析提供基础。

## 涉及 Figures
- Fig. 4I, 4J (tumor subtypes based on CNV)
