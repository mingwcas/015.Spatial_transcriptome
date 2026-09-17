# Method: GOrilla Functional Enrichment Analysis

## 原文（Methods）
> Functional annotation of the DE analysis was performed by GOrilla using the 'Single ranked list of genes' model. For each DE analysis, two ranks are generated using LFCs, one from the most negative to most positive, and vice versa. The software will search for GO terms that are enriched in the top of the list compared to the rest of the list using the mHG statistics. Total of 8 GOrilla analyses were performed for each age group (3 months and 18 months) and Genotype and Plaque, respectively. Bonferroni correction was performed on all GOrilla analyses based on the total number of comparisons (21825 GO terms × 8 ranks = 174600). Functional annotation of each module was performed by GOrilla using the 'Two unranked lists of genes' model. Each module is used as the target list and the total of 36715 genes expressed in our dataset were used as the background set. To merge similar GO terms into cluster, we first generated a similarity matrix between all significantly enriched GO terms based on the number of the genes overlapping between two GO terms. Next, we performed hierarchical clustering using the complete linkage method, with tree height 3.3 which grouped all significant GO terms into 12 functionally overlapping clusters.

## 解读

### 意义
GOrilla功能富集分析用于从差异表达结果和WGCNA模块中提取生物学功能信息，识别显著富集的Gene Ontology (GO) 术语。

### 输入
- 差异表达基因排序列表（按LFC排序）
- WGCNA模块基因列表
- 背景基因集（36,715个表达基因）

### 输出
- 显著富集的GO术语
- 13个功能超级类别
- 12个功能聚类
- 每个WGCNA模块的功能注释

### 核心步骤
1. 差异表达分析的GO富集（Single ranked list模型）
   - 每个DE分析生成两个排序（正向和反向）
   - 使用mHG统计量检测富集
   - 共8个GOrilla分析（2年龄×2模型×2方向）
2. WGCNA模块的功能注释（Two unranked lists模型）
   - 模块作为目标列表
   - 36,715个基因作为背景集
   - 使用超几何统计量
3. Bonferroni校正（21825 GO terms × 8 = 174600比较）
4. GO术语相似性矩阵和层次聚类（complete linkage, height 3.3）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| DE分析模型 | Single ranked list | 单排序列表模型 |
| 模块分析模型 | Two unranked lists | 双非排序列表模型 |
| 统计量 | mHG (minimum Hypergeometric) | 最小超几何统计量 |
| 多重校正 | Bonferroni | 校正174600次比较 |
| 聚类方法 | Complete linkage | 完全连接层次聚类 |
| 聚类高度 | 3.3 | GO术语聚类阈值 |
| 功能聚类数 | 12 | 最终功能聚类数 |
| 超级类别数 | 13 | 13个功能超级类别 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| GOrilla | Gene Ontology enRIchment anaLysis and visuaLizAtion tool |
| GO (Gene Ontology) | 基因本体论，基因功能标准化注释系统 |
| mHG | 最小超几何统计量 |
| Bonferroni correction | Bonferroni多重比较校正 |
| Functional supercategory | 功能超级类别，相关GO术语的聚类 |
| Enrichment | 富集，目标基因集中某功能的过表达 |

## 复现
- 工具/代码/URL
  - GOrilla: http://cbl-gorilla.cs.technion.ac.il/
- 代码片段
```
# GOrilla是在线工具，无需本地代码
# DE分析: 输入排序基因列表
# 模块分析: 输入目标基因列表和背景列表
# 输出: 显著富集的GO术语列表
```

## 生物学意义
GOrilla分析识别了13个功能超级类别，包括抗原加工、趋化性、溶酶体降解和炎症等在18月龄Aβ和基因型轴上显著上调的功能。有趣的是，髓鞘类别在3月龄上调但在18月龄下调，反映了OLIG模块的双相响应。12个功能聚类为WGCNA模块提供了生物学解释。

## 涉及 Figures
- **Figure S3A** — 13个功能超级类别的GO分析总结
- **Table S4** — 每个WGCNA模块的GO功能注释
