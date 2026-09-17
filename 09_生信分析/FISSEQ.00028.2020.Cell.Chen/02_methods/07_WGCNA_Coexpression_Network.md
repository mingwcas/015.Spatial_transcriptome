# Method: Weighted Gene Co-expression Network Analysis (WGCNA)

## 原文（Methods）
> WGCNA package in R (Zhang and Horvath, 2005) was used to build signed co-expression networks. The set of genes with the highest 50% standard deviation was selected using the 'varFilter' package from the Bioconductor. Soft power 14 was chosen by WGCNA's 'pickSoftThreshold' function to calculate the adjacency matrix, and the module identification was performed by the 'cutreeDynamic' function by selecting deepSplit = 4. The adjacency matrix is calculated using the 'adjacency.fromsimilary' function using the signed network and soft thresholding power 14. The mean of the connectivity score of a given module is calculated by first taking the row sum of the adjacency matrix as the intra modular connectivity score per gene, and then the average of the intra modular connective score of all genes in the given module was calculated.

## 解读

### 意义
WGCNA是一种无监督的基因共表达网络分析方法，用于识别具有相似表达模式的基因模块，这些模块往往代表共同的生物学功能或调控通路。

### 输入
- 10,327个ST转录组谱
- 变异度最高的50%基因（通过varFilter筛选）

### 输出
- 12个基因共表达模块
- 每个模块的基因列表
- 模块特征基因（module eigengene）
- 基因间连接强度矩阵
- 模块内连接度得分

### 核心步骤
1. 选择变异度最高的50%基因
2. pickSoftThreshold选择soft power = 14
3. 计算邻接矩阵（signed network, soft thresholding）
4. cutreeDynamic（deepSplit = 4）识别模块
5. 提取模块的生物学功能（GOrilla）
6. 计算模块的细胞特征
7. 评估模块与Aβ暴露和基因型的关联

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 网络类型 | Signed | 有符号共表达网络 |
| Soft power | 14 | 软阈值幂次 |
| Gene selection | Top 50% SD | 选择变异度最高的50%基因 |
| deepSplit | 4 | 模块识别的分裂深度 |
| Module count | 12 | 最终识别的模块数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| WGCNA | 加权基因共表达网络分析 |
| Signed network | 有符号网络，考虑正负相关 |
| Soft thresholding | 软阈值，将相关系数转换为邻接值 |
| Adjacency matrix | 邻接矩阵，描述基因间连接强度 |
| Module eigengene | 模块特征基因，模块的第一主成分 |
| Intra-modular connectivity | 模块内连接度，基因与模块内其他基因的连接强度 |
| Hub gene | 枢纽基因，模块内连接度最高的基因 |

## 复现
- 工具/代码/URL
  - WGCNA R package: https://cran.r-project.org/web/packages/WGCNA/index.html
  - Bioconductor varFilter
- 代码片段
```R
library(WGCNA)
# 选择top 50% SD基因
varFilter(exprs, var.cutoff=0.5)
# 选择soft power
sft <- pickSoftThreshold(datExpr, powerVector=1:20)
# 构建网络
net <- blockwiseModules(datExpr, power=14, deepSplit=4, 
                         networkType="signed")
```

## 生物学意义
WGCNA识别了12个基因共表达模块，其中两个最关键的是：紫色模块（PIGs，57个基因）和红色模块（OLIG，165个基因）。PIGs代表了淀粉样斑块诱导的多细胞炎症反应，OLIG代表了少突胶质细胞的髓鞘相关基因响应。模块分析揭示了Aβ病理如何驱动不同细胞类型之间的协调基因表达变化。

## 涉及 Figures
- **Fig. 3** — PIG模块的WGCNA鉴定
- **Fig. 5** — PIG模块随Aβ积累的逐渐共表达
- **Fig. 6** — OLIG模块的分析
- **Figure S3B** — 12个WGCNA模块的总结
