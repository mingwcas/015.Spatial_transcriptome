# Method: GO-term Enrichment Analysis

## 原文（Methods）
> We used Metascape for GO-term enrichment analysis. Genes of interest were uploaded to Metascape website (https://metascape.org/gp/index.html), and analyzed for the enriched biological processes with default parameters.

## 解读

### 意义
对Mtb相关基因模块进行Gene Ontology功能富集分析，揭示感染相关的生物学通路。

### 输入
- 目的基因列表（如Mtb相关基因）

### 输出
- GO富集结果
- 生物学通路列表

### 核心步骤
1. 将基因列表上传到Metascape
2. 使用默认参数进行富集分析
3. 提取显著富集的生物学过程

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 工具 | Metascape | |
| 参数 | 默认参数 | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| GO | Gene Ontology，基因本体论 |
| Metascape | 在线富集分析工具 |

## 复现
- Metascape: https://metascape.org/gp/index.html

## 生物学意义
GO富集分析揭示了差异表达基因的生物学功能，帮助理解感染和免疫应答的分子机制。

## 涉及 Figures
- Fig. 6H, 6I (GO enrichment of Mtb-associated genes)
