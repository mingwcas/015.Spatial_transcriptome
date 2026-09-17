# Method: Preprocessing Workflow Optimization

## 原文（Methods）
> The optimal preprocessing workflow was identified by systematically evaluating different preprocessing steps including normalization, feature selection, dimensionality reduction, and clustering parameters. The Adjusted Rand Index (ARI) between clusters derived from different preprocessing workflows and ground truth cell type labels was used as the primary evaluation metric.

## 解读

### 意义
建立标准化的Xenium数据预处理流程，确保从原始空间转录组数据到可靠的细胞类型聚类结果的分析可重复性。

### 输入
- Xenium 处理后的细胞×基因表达矩阵
- 地面真值细胞类型标签（ground truth）

### 输出
- 最优预处理流程参数组合
- 各步骤对聚类结果影响的敏感性分析

### 核心步骤
1. 系统评估各预处理步骤：标准化、特征选择、降维、聚类
2. 对每个步骤测试不同算法和超参数组合
3. 使用ARI评估各工作流与地面真值标签的一致性
4. 使用Fowlkes-Mallows Index (FMI) 和 Variability Index (VI) 进行补充评估
5. 通过敏感性分析确定各参数对最终结果的影响程度
6. 在多个Xenium数据集上验证最优流程的泛化能力

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 评估指标 | ARI, FMI, VI | 聚类一致性评估指标 |
| 数据集数量 | 多个Xenium数据集 | 验证流程泛化性 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ARI (Adjusted Rand Index) | 调整兰德指数，聚类结果与真值的一致性度量 |
| FMI (Fowlkes-Mallows Index) | Fowlkes-Mallows指数，另一种聚类相似性度量 |
| VI (Variability Index) | 变异性指数，衡量聚类结果间的差异程度 |
| Ground truth labels | 手动注释或已知的细胞类型标签 |

## 复现
- 工具/代码：Scanpy (Python), 标准空间转录组预处理流程
- 代码片段：
```python
import scanpy as sc
sc.pp.normalize_total(adata)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.leiden(adata)
```

## 生物学意义
预处理参数的选择直接影响细胞类型鉴定的准确性。不同的标准化方法和聚类参数可能导致截然不同的细胞类型注释结果，进而影响对组织微环境组成的理解。

## 涉及 Figures
- **Fig. 4** — 预处理优化主要结果
- **Extended Data Fig. 6** — 扩展预处理分析
