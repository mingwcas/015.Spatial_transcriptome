# Method: DR.SC v3.3 (Spatial Clustering)

## 原文（Methods）
> DR.SC was applied by setting K (the number of clusters) as 10.

## 解读

### 意义
DR.SC (Dimension Reduction and Spatial Clustering)是一种结合空间信息与基因表达数据的聚类方法。

### 输入
- Seurat处理后的标准化数据
- 空间坐标信息

### 输出
- 整合空间信息的聚类结果

### 核心步骤
1. 将空间坐标信息纳入模型
2. 联合降维和聚类
3. 输出细胞类型注释

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| DR.SC version | v3.3 | 空间聚类方法版本 |
| K | 10 | 预设聚类数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Spatial clustering | 空间聚类，将空间位置信息纳入聚类 |

## 复现
- 工具/代码/URL：DR.SC Bioconductor包

## 生物学意义
DR.SC等空间感知方法在特定数据集上表现良好，但在本研究的比较中并未一致性地优于仅依赖转录组数据的Seurat方法。

## 涉及 Figures
- **Fig. 4** — 下游性能比较
- **Supplementary Figure 12** — 聚类方法比较
