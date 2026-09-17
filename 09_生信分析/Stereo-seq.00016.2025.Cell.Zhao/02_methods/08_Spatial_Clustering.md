# Method: Spatial Clustering

## 原文（Methods）
> We adopted the methods of He et al. and Shi et al., replacing the high-dimensional gene expression matrix with a feature matrix generated via the scVI method, to reduce batch effects. We then created smoothed feature vectors for each cell by concatenating the vectors of its 30 nearest spatial neighbors, including the cell itself. All cells' spatially smoothed feature matrices were combined into one dataset for Principal Component Analysis (PCA). Using the Leiden algorithm, we clustered these data to identify spatial domains. These domains were annotated based on the anatomical structures in the Allen Mouse Brain Atlas and markers reported by Shi et al.

## 解读

### 意义
基于空间转录组数据进行空间域识别和聚类分析，用于揭示组织内的空间异质性。

### 输入
- 空间转录组表达矩阵
- 空间坐标信息
- 细胞分割结果

### 输出
- 空间聚类结果
- 空间域注释

### 核心步骤
1. 使用scVI降低批次效应
2. 对每个细胞，取30个最近邻（包括自身）
3. 拼接空间平滑特征向量
4. PCA降维
5. Leiden算法聚类
6. 基于Allen Mouse Brain Atlas和标记基因注释空间域

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 最近邻数 | 30 | 空间平滑 |
| 降维方法 | PCA | |
| 聚类算法 | Leiden | |
| 注释参考 | Allen Mouse Brain Atlas | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| scVI | single-cell Variational Inference，降维方法 |
| Leiden算法 | 图聚类算法 |
| 空间域 | Spatial domain |

## 复现
- scVI: https://scvi-tools.org/
- Scanpy: Python单细胞分析库
- Leiden聚类: scanpy.tl.leiden

## 生物学意义
空间聚类揭示了组织内不同区域的分子特征，对于理解组织结构和功能区室至关重要。

## 涉及 Figures
- Fig. 2D (spatial clustering of mouse brain)
- Fig. 6D (spatial clustering of Mtb-infected lungs)
