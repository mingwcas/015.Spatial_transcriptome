# Method: Specificity and Contamination Assessment

## 原文（Methods）
> For each pair of distinct cell types, denoted as the target cell type i and the potential contaminating cell type j, cells annotated as type i were assigned a binary label: 1 for those spatially adjacent (based on centroid distance ≤15 µm) to at least one cell of type j, and 0 for those not adjacent to any cell of type j. We then trained a logistic regression model to predict, based on the gene expression profile of a cell of type i, whether it is adjacent to a cell of type j.
> For each sample after QC filtering, input features were z-scored log-normalized expression levels of all genes for cells of type i. We used the implementation from scikit-learn with default parameters, except for max_iter, which was increased to 500 and class_weight set to 'balanced'. Genes were ranked by the magnitude of their coefficients to assess their potential association with signal contamination from cell type j within cell type i. To evaluate whether these ranked gene lists were enriched for markers of cell type j, we counted the number of markers present in the top 20 ranks.

## 解读

### 意义
评估转录本污染程度：检验目标细胞类型中是否富集了邻近污染细胞的标记基因，是衡量信号纯度的关键指标。

### 输入
- 细胞类型注释
- 细胞空间坐标
- 原始或校正后的表达矩阵
- 各细胞类型的标记基因列表

### 输出
- Logistic回归系数（基因重要性排名）
- Top 20中污染细胞类型标记基因的数量
- GSEA富集分析结果

### 核心步骤
1. 定义空间邻近关系（质心距离≤15µm）
2. 对每对细胞类型(i, j)，将细胞i分为邻近j vs 不邻近j
3. 用基因表达谱训练Logistic回归预测邻近关系
4. 根据系数排序基因
5. 统计top 20中细胞类型j标记基因的数量
6. 运行GSEA分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| spatial_distance | ≤15µm | 空间邻近定义 |
| max_iter | 500 | Logistic回归最大迭代 |
| class_weight | balanced | 类别平衡 |
| top_n_markers | 20 | 评估标记基因富集的数量 |
| permutation_n | 1000 | 置换检验次数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Contamination index | Top 20中污染标记基因数量 |
| Logistic regression | 预测细胞空间邻近关系 |
| GSEA | 基因集富集分析 |
| NES | Normalized Enrichment Score |

## 复现
- 工具：scikit-learn, scipy
- 代码：https://github.com/bdsc-tds/xenium_analysis_pipeline
- 参考方法：Mitchel et al., Nature Genetics 2026

## 生物学意义
该方法直接衡量污染程度：如果T细胞邻近恶性细胞，其top基因中应包含更少恶性标记。SPLIT校正后，恶性标记显著减少，而T细胞标记得以保留或增强。

## 涉及 Figures
- **Fig. 4e-g** — T细胞被恶性细胞污染的评估
- **ED Fig. 10** — 不同分割方法下预测T细胞接近恶性细胞的top基因
