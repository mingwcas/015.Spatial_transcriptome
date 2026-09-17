# Method: Spatially Constrained Clustering Analysis

## 原文（Methods）
> To acquire a global picture of cell clusters spatially assigned onto the section, we performed the spatially constrained clustering analysis. In total, we obtained six clusters of cells separated into previously defined anatomical regions of the axolotl telencephalon, including the VZ, dorsal pallium, medial pallium, lateral pallium, striatum, and septum.

## 解读

### 意义
空间约束聚类分析结合细胞的空间位置信息和基因表达谱，能够在保持空间连续性的同时识别具有相似表达模式的细胞群，从而揭示组织结构与细胞类型的关系。

### 输入
- 单细胞分割后的表达矩阵
- 每个细胞的空间坐标（x, y）
- 基因表达数据

### 输出
- 空间聚类结果
- 解剖区域注释（VZ、背侧皮层、内侧皮层、外侧皮层、纹状体、隔膜）
- 细胞类型空间分布图

### 核心步骤
1. 构建空间邻域图：基于空间距离确定细胞间的邻域关系
2. 空间约束聚类：在聚类过程中加入空间约束，确保同簇细胞在空间上邻近
3. 结合形态学信息：整合解剖学形态定义脑区
4. 多截面整合：沿前后轴的多个截面通过CCA算法整合

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 聚类数目（成年阶段） | 16个细胞簇 | 基于基因表达的 unsupervised clustering |
| 解剖区域数 | 6个 | VZ、背侧皮层、内侧皮层、外侧皮层、纹状体、隔膜 |
| 发育阶段分析 | 33种细胞类型 | 包含13种 immature/intermediate cell types |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Spatially constrained clustering | 空间约束聚类 |
| VZ | Ventricular Zone，脑室区 |
| CCA | Canonical Correlation Analysis，典型相关分析 |
| Anatomical regions | 解剖区域 |

## 复现
- **工具/代码/URL**: 
  - Seurat包: https://satijalab.org/seurat/
  - 空间约束聚类方法（自定义实现）
- **代码片段**: 无特定代码（Seura包的标准功能）

## 生物学意义
空间约束聚类能够识别在空间上连续分布且具有相似转录组的细胞群，这对于定义组织特异性的细胞类型至关重要。在蝾螈端脑中，这种分析揭示了不同脑区的细胞类型组成差异，为理解脑发育和再生的空间组织提供了基础。

## 涉及Figures
- **Fig. 1C** — 空间聚类识别解剖区域和细胞类型
- **Fig. 3B** — 再生过程中空间细胞类型分布
