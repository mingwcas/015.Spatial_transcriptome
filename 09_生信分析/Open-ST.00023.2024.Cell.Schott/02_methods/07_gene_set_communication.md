# Method: Gene Set and Communication Analysis

## 原文（Methods）
> We explored gene programs and cell-cell communication within the primary HNSCC, healthy, and metastatic lymph nodes starting from a Differential Gene Expression (DGE) analysis. The identified differentially expressed genes per cluster underwent Gene Set Enrichment Analysis (GSEA) using the Reactome pathway gene set signatures.

## 解读

### 意义
基因集分析和细胞间通讯预测揭示了肿瘤微环境中的功能程序和信号网络。

### 输入
- 细胞类型注释和标记基因
- 配体-受体数据库

### 输出
- 富集的通路和基因程序
- 空间通讯热点
- 配体-受体相互作用网络

### 核心步骤
1. 伪批量差异基因表达分析（pydeseq2）
2. 基因集富集分析（GSEA，Reactome通路）
3. AUCell评分计算基因程序空间活性
4. 使用liana-py进行空间配体-受体分析
5. 非负矩阵分解（NMF）发现空间通讯热点
6. 使用肘部法确定最优因子数

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| log2FC阈值 | >0.5 | 差异表达基因筛选 |
| 调整p值 | <0.05 | 统计显著性阈值 |
| NES阈值 | >1 | 标准化富集分数 |
| FDR阈值 | <0.05 | 错误发现率 |
| 通讯距离 | 50 μm | 配体-受体分析的空间距离 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| GSEA | 基因集富集分析 |
| AUCell | 基因集活性评分方法 |
| NMF | 非负矩阵分解，用于发现空间模式 |
| NES | 标准化富集分数 |

## 复现
- 工具/代码/URL: https://github.com/saezlab/liana-py
- 代码片段:
```python
import liana as li
li.mt.rank_aggregate(adata, groupby='cell_type', resource_name='consensus')
```

## 生物学意义
基因集和通讯分析揭示了肿瘤微环境中的功能异质性，特别是炎症、基质硬度、粘附和细胞外基质重塑等通讯热点，这些与肿瘤进展和转移密切相关。

## 涉及 Figures
- **Fig. 5** — 肿瘤异质性和通讯特征
- **Fig. S6** — 肿瘤亚簇的基因程序活性
