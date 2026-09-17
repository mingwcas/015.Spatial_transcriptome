# Method: Tissue Distribution Preference (Ro/e Analysis)

## 原文（Methods）
> The enrichment or depletion of cell subsets across sample types was quantified using the ratio of observed to expected (Ro/e) calculation. Statistical significance was assessed using a two-sided Fisher's exact test. A Ro/e value greater than 1 indicates significant enrichment in a given tissue context, while a Ro/e value between 0 and 0.2 indicates significant depletion.

## 解读

### 意义
Ro/e分析量化细胞亚群在不同组织类型（PT、PT-LNM、LNMT）中的富集或 depletion程度，识别与淋巴结转移相关的特定细胞亚群。

### 输入
- 细胞类型注释结果
- 样本分组信息（PT、PT-LNM、LNMT）
- 每个细胞亚群在各样本类型中的细胞数

### 输出
- Ro/e值：观察值/期望值比值
- Fisher精确检验p值
- 富集（Ro/e>1）或depletion（Ro/e<0.2）的细胞亚群列表

### 核心步骤
1. 计算每个细胞亚群在每个组织类型中的observed count
2. 计算expected count（基于总细胞比例）
3. Ro/e = observed/expected
4. Fisher精确检验统计显著性
5. 设定阈值：Ro/e>1为富集，Ro/e<0.2为depletion

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 富集阈值 | Ro/e > 1 | 显著富集 |
| Depletion阈值 | Ro/e < 0.2 | 显著缺失 |
| 统计检验 | Two-sided Fisher's exact test | 显著性检验 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Ro/e | Ratio of observed to expected，观察值/期望值比值 |
| Fisher's exact test | 精确概率检验，用于离散数据的独立性检验 |

## 复现
- 工具/代码/URL：Ro/e方法来自Zhang et al., Nature 2018 (https://doi.org/10.1038/s41586-018-0694-x)
- 代码片段：
```r
# Ro/e calculation
observed <- table(cell_type, tissue_type)
expected <- outer(rowSums(observed), colSums(observed)) / sum(observed)
roe <- observed / expected
# Fisher's exact test for each cell type
fisher.test(observed[,c(1,2)])$p.value
```

## 生物学意义
Ro/e分析揭示了C5、C6、C9三个恶性细胞亚群特异性地富集于有淋巴结转移的样本（PT-LNM和LNMT），在无转移的PT中几乎不存在。这表明这些亚群可能代表淋巴结转移相关的适应性程序。

## 涉及 Figures
- **Fig. 2B** — C5、C6、C9在LNMT和PT-LNM中富集的热图
- **Fig. S2C, S2D** — 细胞组成的组织分布偏好
