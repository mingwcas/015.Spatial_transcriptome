# Method: SVF Identification Algorithms

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 7 SVF 识别算法比较
> Extended exploration of the SVF identification brain section (ROI2) and the domains identified by different algorithms. Ranked performance of different algorithms in identifying tissue domains.

## 解读

### 意义
空间可变特征（SVF, Spatial Variable Feature）识别是空间转录组数据分析的核心任务，用于识别具有空间分布特征的基因或特征，对于理解组织微环境和细胞间相互作用至关重要。

### 输入
- 空间转录组计数矩阵
- 细胞空间坐标
- 组织注释信息

### 输出
- 空间可变基因列表
- 组织 domains/regions 划分
- 算法性能评估

### 核心步骤
1. 加载空间转录组数据
2. 应用不同 SVF 识别算法
3. 比较算法性能（ARI, NMI, FMI, VI）
4. 评估不同 domain 数量下的表现
5. 分析算法运行时间

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| SPACEL | SVF identification | 基于层次聚类的空间变量特征识别 |
| SpaGCN | SVF identification | 图卷积网络方法 |
| STAGATE | SVF identification | 图注意力网络方法 |
| deepST | SVF identification | 深度学习方法 |
| N° pred. domains | 5, 6, 10, 14, 16 | 预测的 domain 数量 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SVF | Spatial Variable Feature，空间可变特征 |
| SPACEL | 基于层次聚类的 SVF 识别算法 |
| SpaGCN | Spatial Gene Expression using Graph Convolutional Networks |
| STAGATE | Spatial Transcriptome analysis using GAT |
| deepST | 深度学习空间转录组分析 |
| ARI | Adjusted Rand Index |
| NMI | Normalized Mutual Information |
| FMI | Fowlkes-Mallows Index |
| VI | Variation of Information |

## 复现
- 工具/代码/URL：https://github.com/Moldia/Xenium_benchmarking v1.2.0
- Python 包：squidpy, SPACEL, SpaGCN, STAGATE, deepST
- 代码片段：
```python
# SVF identification using different algorithms
# SPACEL
from spacel import SPACEL
spacel = SPACEL()
spacel.fit(adata)

# SpaGCN
from spagcn import SpaGCN
spagcn = SpaGCN()
spagcn.fit(adata)

# STAGATE
from stagate import STAGATE
stagate = STAGATE()
stagate.fit(adata)
```

## 生物学意义
SVF 识别算法能够揭示基因的空间表达模式，帮助理解组织结构和细胞功能分区。不同算法有不同的优势和适用范围，选择合适的算法对于准确识别组织微环境至关重要。

## 涉及 Figures
- **ED Fig. 7** — SVF 识别算法比较，包含运行时间和性能评估
