# Method: PRECAST v1.6.2 (Spatial Clustering)

## 原文（Methods）
> PRECAST was applied with the number of clusters specified as 10 and using the SelectModel function to reorganize the fitting results within PRECASTObj.

## 解读

### 意义
PRECAST (Probabilistic Embedding, Clustering, and Alignment for Integrating Spatial Transcriptomics Data)是一种空间转录组数据整合分析方法。

### 输入
- Seurat处理后的标准化数据
- 空间坐标信息

### 输出
- 整合空间信息的聚类结果

### 核心步骤
1. 概率嵌入
2. 空间感知聚类
3. 模型选择和结果优化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| PRECAST version | v1.6.2 | 空间整合分析方法版本 |
| number of clusters | 10 | 预设聚类数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Probabilistic embedding | 概率嵌入，将数据映射到低维空间 |

## 复现
- 工具/代码/URL：PRECAST R包

## 生物学意义
与DR.SC类似，PRECAST在特定数据集上有效，但并不总是优于传统Seurat聚类方法。

## 涉及 Figures
- **Fig. 4** — 下游性能比较
