# Method: Clustering Analysis and Cell Typing

## 原文（Methods）
> We performed cell type annotation by following standard practices for single-cell analysis and by using scanpy. Data preprocessing involved applying UMI thresholds per segmented cell (at least 250, at most 10,000), mitochondrial count filtering (at most 10% for mouse, 20% for human), and retaining genes expressed in a minimum of 10 cells.

## 解读

### 意义
无监督聚类和细胞类型注释是揭示组织异质性和空间细胞组成的核心分析步骤。

### 输入
- 细胞×基因表达矩阵
- 参考数据集（可选）

### 输出
- 细胞类型注释
- 标记基因列表
- UMAP可视化

### 核心步骤
1. 质量控制过滤（UMI阈值、线粒体比例）
2. 标准化（总计数归一化、对数转换）
3. 高变基因选择（前2000个）
4. PCA降维（前30个主成分）
5. 最近邻图构建
6. Leiden聚类
7. 标记基因鉴定（Wilcoxon方法）
8. 基于标记基因和文献的细胞类型注释
9. 使用scVI/scANVI进行参考数据集标签转移（可选）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 最小UMI数 | 250 (mouse) / 500 (human) | 细胞质量过滤阈值 |
| 最大UMI数 | 10,000 | 避免双细胞 |
| 最大线粒体比例 | 10% (mouse) / 20% (human) | 细胞质量过滤 |
| 最小基因表达细胞数 | 10 | 基因过滤阈值 |
| PCA维度 | 30 | 降维维度 |
| 高变基因数 | 2,000 | 用于降维的基因数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Leiden聚类 | 基于图的社区检测算法 |
| UMAP | 统一流形近似和投影，用于降维可视化 |
| scVI | 单细胞变分推断，用于批次校正和标签转移 |
| 标记基因 | 特定细胞类型中高表达的基因 |

## 复现
- 工具/代码/URL: https://github.com/scverse/scanpy
- 代码片段:
```python
import scanpy as sc
sc.pp.normalize_total(adata)
sc.pp.log1p(adata)
sc.tl.leiden(adata)
sc.tl.rank_genes_groups(adata, 'leiden')
```

## 生物学意义
聚类分析揭示了组织中的细胞类型多样性，包括肿瘤、免疫和基质细胞群。结合空间信息，可以研究细胞类型的空间分布和相互作用。

## 涉及 Figures
- **Fig. 3** — 小鼠胚胎头部细胞类型
- **Fig. 4** — 人类原发性组织细胞类型复杂性
