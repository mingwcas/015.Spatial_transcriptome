# Method: Evaluation Metrics (ARI, NMI, FMI, VI)

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 4-7 评估指标
> Ranked performance of different algorithms in identifying tissue domains in mouse brain sections, using the manually segmented domains as a reference.

## 解读

### 意义
评估指标是量化分割、聚类和空间分析方法性能的标准化度量，用于客观比较不同方法的准确性和一致性。

### 输入
- 预测结果（分割掩膜、聚类标签、domains）
- 参考/真实标签（ground truth）

### 输出
- 量化评分（0-1 范围，越高越好，除了 VI）
- 方法排序

### 核心步骤
1. 计算预测标签和真实标签之间的匹配
2. 计算各种评估指标
3. 汇总统计（median ARI 等）
4. 方法排序和比较

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| ARI | 0-1 | Adjusted Rand Index，调整兰德指数 |
| NMI | 0-1 | Normalized Mutual Information，标准化互信息 |
| FMI | 0-1 | Fowlkes-Mallows Index |
| VI | 0-1 | Variation of Information，变异信息 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ARI | Adjusted Rand Index，衡量两个聚类分配之间的相似度，1=完美匹配 |
| NMI | Normalized Mutual Information，衡量两个聚类之间的互信息，1=完美匹配 |
| FMI | Fowlkes-Mallows Index，衡量两个聚类之间的一致性，1=完美匹配 |
| VI | Variation of Information，衡量两个聚类之间的信息差异，越低越好 |
| Ground truth | 参考标准，手动注释的真实标签 |

## 复现
- 工具/代码/URL：scikit-learn, sklearn.metrics
- Python 包：adjustized_rand_score, normalized_mutual_info_score, fowlkes_mallows_score, variation_of_information
- 代码片段：
```python
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from sklearn.metrics import fowlkes_mallows_score, variation_of_information

# Calculate evaluation metrics
ari = adjusted_rand_score(labels_pred, labels_true)
nmi = normalized_mutual_info_score(labels_pred, labels_true)
fmi = fowlkes_mallows_score(labels_pred, labels_true)
vi = variation_of_information(labels_pred, labels_true)
```

## 生物学意义
标准化的评估指标使得不同方法之间的比较成为可能，为方法选择和优化提供了客观依据，有助于推动空间转录组分析方法的标准化。

## 涉及 Figures
- **ED Fig. 4** — NCP (Negative Coexpression Purity) 评估
- **ED Fig. 5** — ARI 分割指标评估
- **ED Fig. 6** — ARI, FMI, VI 聚类评估
- **ED Fig. 7** — ARI, NMI, FMI, VI SVF 算法评估
