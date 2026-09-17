# Method: Gene Length Bias Analysis

## 原文（Methods）
> Gene length bias is well understood in bulk RNA-seq data. We further analyzed our DBiT-seq data and ST data using reference package GeneLengthBias for RNaseq data (Phipson et al., 2017) following standard protocols.

## 解读

### 意义
该方法评估DBiT-seq数据中是否存在基因长度偏倚，这是RNA-seq数据分析中需要关注的技术效应。

### 输入
- DBiT-seq表达矩阵
- ST (Spatial Transcriptomics)数据
- GeneLengthBias R包

### 输出
- 基因长度与检测效率的关系分析

### 核心步骤
1. 使用GeneLengthBias包分析DBiT-seq数据
2. 使用相同流程分析ST数据作为对照
3. 评估基因长度对表达量检测的影响
4. 比较两种技术间的偏倚差异

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 分析工具 | GeneLengthBias (Phipson et al., 2017) | 基因长度偏倚分析 |
| 对照技术 | ST (Spatial Transcriptomics) | 空间转录组对照 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Gene length bias | 基因长度偏倚，长基因更容易被检测到的现象 |
| GeneLengthBias | 检测基因长度对RNA-seq影响的方法 |

## 复现
- 工具/代码/URL：GeneLengthBias R包 (Phipson et al., 2017)
- 关键调用：NA

## 生物学意义
基因长度偏倚是RNA-seq技术中的常见问题，长基因更容易被检测到。分析表明DBiT-seq与ST数据存在类似的基因长度依赖性，这是预期的技术效应，不影响相对表达比较。理解这种偏倚有助于正确解释数据。

## 涉及 Figures
- **Fig. S2E** — 基因长度偏倚分析
