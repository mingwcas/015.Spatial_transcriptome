# Method: Preprocessing Workflow Optimization

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 6 预处理流程分析
> Workflow of the different preprocessing steps and parameters considered in the assessment of the best preprocessing workflow. Preprocessing workflows are sorted from best (bottom) to worst (top) based on their median ARI.

## 解读

### 意义
预处理流程优化是空间转录组数据分析的关键步骤，通过系统性地评估不同归一化方法、高可变基因选择、主成分分析参数和聚类算法的组合，找到最佳分析流程。

### 输入
- Xenium 原始计数矩阵
- 细胞元数据
- 组织类型信息

### 输出
- 优化后的预处理参数组合
- 最佳聚类结果
- 评估指标（ARI, FMI, VI）

### 核心步骤
1. **原始计数数据**：加载 raw counts
2. **高可变基因（HVG）选择**：Yes/No, 阈值优化
3. **归一化方法**：Library-size based (target sum 10/100/1000), SCTransform, None
4. **对数转换**：Yes/No
5. **缩放（Scaling）**：Yes/No
6. **主成分分析（PCA）**：选择 PC 数量
7. **KNN 图构建**：调整邻居数
8. **聚类**：Leiden SLM / Louvain

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| target sum | 10, 100, 1000 | 库大小归一化目标值 |
| HVG | True/False | 是否进行高可变基因选择 |
| log | True/False | 是否进行对数转换 |
| scale | True/False | 是否进行缩放 |
| PCs | 10, 20, 30 | 主成分数量 |
| KNN | 10, 12, 16, 30, 50 | 最近邻数量 |
| clustering | Leiden SLM, Louvain | 聚类算法 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| HVG | Highly Variable Genes，高可变基因 |
| Library-size normalization | 库大小归一化 |
| SCTransform | 正则化负二项回归的归一化方法 |
| PCA | Principal Component Analysis，主成分分析 |
| KNN | K-Nearest Neighbors，K最近邻图 |
| Leiden SLM | Leiden algorithm with Smart Local Moving |
| ARI | Adjusted Rand Index，调整兰德指数 |
| FMI | Fowlkes-Mallows Index |
| VI | Variation of Information |

## 复现
- 工具/代码/URL：https://github.com/Moldia/Xenium_benchmarking v1.2.0
- 代码片段：
```python
# Preprocessing workflow with Scanpy
import scanpy as sc
adata = sc.read_h5ad('input.h5ad')
sc.pp.highly_variable_genes(adata, flavor='seurat', n_top_genes=2000)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.scale(adata)
sc.tl.pca(adata, n_comps=50)
sc.pp.neighbors(adata, n_neighbors=10)
sc.tl.leiden(adata, resolution=1.0)
```

## 生物学意义
预处理流程的优化对于准确恢复细胞类型标签至关重要，不同的组织类型和数据集可能需要不同的预处理参数。系统性的参数评估为空间转录组数据分析提供了最佳实践指南。

## 涉及 Figures
- **ED Fig. 6** — 预处理流程参数优化分析，包含 ARI、FMI、VI 等评估指标
