# Method: Downstream Analysis with Scanpy and ParaView

## 原文（Methods）
> This exploratory analysis workflow consists of several key steps: data preprocessing, gene expression normalization, dimensionality reduction, clustering, marker gene identification, spatial gene expression analysis, and 3D visualization. Data preprocessing involves filtering the cells with too low or too high counts and genes, by assessing the distribution of unique counts and genes per cell.

## 解读

### 意义
对空间转录组数据进行下游分析，包括预处理、聚类、差异表达和 3D 可视化，揭示细胞异质性和空间组织模式。

### 输入
- 分割后的 h5ad 文件（stitched_segmented.h5ad）
- scanpy 工具包
- ParaView 软件（用于 3D 可视化）

### 输出
- 细胞聚类结果
- 差异表达基因列表
- 空间基因表达可视化
- 3D 组织可视化

### 核心步骤
1. 数据预处理：过滤低质量和高质量异常细胞
2. 基因表达归一化：按细胞测序深度归一化，校正中位数深度
3. 对数转换
4. PCA 降维
5. Leiden 聚类识别细胞群
6. 差异表达分析识别标记基因
7. 空间基因表达可视化
8. 使用 ParaView 进行 3D 可视化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 聚类算法 | Leiden | 基于图的聚类算法 |
| 降维方法 | PCA | 主成分分析 |
| 归一化方法 | 深度归一化 + 对数转换 | 标准 scRNA-seq 归一化 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| scanpy | Python 单细胞分析工具包 |
| Leiden clustering | Leiden 聚类算法，基于模块度优化 |
| PCA | Principal Component Analysis，主成分分析 |
| Marker genes | 标记基因，特定细胞类型高表达的基因 |
| ParaView | 开源 3D 数据可视化软件 |

## 复现
- 工具/代码/URL：
  - scanpy: https://github.com/scverse/scanpy
  - ParaView: https://www.paraview.org
  - 教程：https://rajewsky-lab.github.io/openst
- 代码片段：
```python
import scanpy as sc

# 读取数据
adata = sc.read_h5ad('stitched_segmented.h5ad')

# 预处理
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# 归一化
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# 高变基因
sc.pp.highly_variable_genes(adata)

# PCA
sc.tl.pca(adata)

# 聚类
sc.pp.neighbors(adata)
sc.tl.leiden(adata)

# 差异表达
sc.tl.rank_genes_groups(adata, 'leiden')

# 可视化
sc.pl.spatial(adata, color='leiden')
```

## 生物学意义
下游分析是将空间转录组数据转化为生物学洞见的关键步骤。scanpy 提供了从预处理到可视化的完整分析流程。Leiden 聚类可以识别空间中的细胞群，差异表达分析可以发现细胞类型特异的标记基因。空间可视化可以揭示基因表达的空间模式，如区域特异性表达、梯度分布等。ParaView 的 3D 可视化功能使得研究者可以在三维空间中探索组织结构和基因表达模式，这对于理解复杂组织（如脑、肿瘤）的空间组织尤为重要。

## 涉及 Figures
- **Fig. 10** — Typical downstream analysis workflow for Open-ST data
