# Method: Gene-wise Expression Correlation Between ST and scRNA-seq Data

## 原文（Methods）
> The total transcript count of each gene was log10-transformed, and gene-wise correlations between ST and scRNA-seq expression profiles were computed. For CosMx 6K, transcript calls were ranked according to their probability of representing random signals. We then stepwise extracted the top percentages of high-quality calls—specifically at 50%, 62.5%, 75%, and 87.5%—and assessed the gene-wise expression correlations with scRNA-seq data.

## 解读

### 意义
通过计算每个基因在ST平台和scRNA-seq之间的表达相关性，评估各ST平台的基因检测准确性。scRNA-seq作为无空间信息的参考，用于验证ST平台的全转录组捕获保真度。

### 输入
- 各ST平台处理后的表达矩阵
- matched scRNA-seq表达矩阵
- CosMx 6K的转录本call概率

### 输出
- 各基因的Pearson相关系数
- CosMx 6K不同质控阈值下的相关性对比

### 核心步骤
1. 计算每个基因在所有癌症类型中的总转录本数，取log10转换
2. 计算ST与scRNA-seq之间的基因水平Pearson相关系数
3. CosMx 6K额外分析：
   - 按随机信号概率排序calls
   - 逐步提取top 50%、62.5%、75%、87.5%高质量calls
   - 分别计算与scRNA-seq的相关性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 相关性指标 | Pearson相关系数 |  |
| log转换 | log10(total transcript count per gene) |  |
| CosMx质控阈值 | 50%, 62.5%, 75%, 87.5% | 高质量calls比例 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 基因水平相关性 | 每个基因在ST和scRNA-seq之间的表达相关性 |
| Pearson相关系数 | 衡量两个变量线性相关性的指标 |

## 复现
- 纯数学计算，无需特殊工具
- 统计软件：Python (numpy, scipy, pandas)

## 生物学意义
研究发现Stereo-seq v1.3、Visium HD FFPE和Xenium 5K与scRNA-seq表现出高相关性，而CosMx 6K尽管检测到更多总转录本，其基因水平计数与scRNA-seq存在显著偏差，且提高质控阈值未能显著改善相关性。

## 涉及 Figures
- **Fig. 1d** — 各平台与scRNA-seq的基因表达相关性
- **Supplementary Fig. 3c, d** — CosMx 6K不同质控阈值下的相关性
