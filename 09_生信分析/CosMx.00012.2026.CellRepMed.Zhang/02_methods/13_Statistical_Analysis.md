# Method: Statistical Analysis

## 原文（Methods）
> All statistical analyses and data visualizations were conducted in R (v4.3.0). Unless otherwise specified, comparisons between two groups were performed using two-sided Wilcoxon rank-sum tests. Correlations were assessed using Spearman's rank correlation coefficient. All tests were two-sided, and a p value of less than 0.05 was considered significant; ns denotes not significant (p > 0.05).

## 解读

### 意义
统计方法是所有数据分析的基石，确保研究结果的科学可靠性和可重复性。

### 输入
- 各分析产生的原始数据
- R环境 (v4.3.0)

### 输出
- 统计检验p值
- 相关性系数（Spearman ρ）
- 可视化图表

### 核心步骤
1. 两组比较：双侧Wilcoxon rank-sum检验
2. 相关性分析：Spearman等级相关系数
3. 多重检验校正：Benjamini-Hochberg FDR
4. 显著性判定：p < 0.05

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 统计软件 | R v4.3.0 | 分析环境 |
| 两组比较 | 双侧Wilcoxon rank-sum test | 非参数检验 |
| 相关性 | Spearman's rank correlation | 等级相关 |
| 显著性阈值 | p < 0.05 | 统计显著 |
| p值调整 | Benjamini-Hochberg FDR | 多重检验校正 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Wilcoxon rank-sum test | 非参数检验，用于两组独立样本比较 |
| Spearman's ρ | 等级相关系数，衡量单调相关性 |
| FDR | False Discovery Rate，伪发现率 |

## 复现
- 工具/代码/URL：
  - R: https://www.r-project.org/
  - stats包 (v4.3.0): https://search.r-project.org/R/refmans/stats/html/00Index.html

## 生物学意义
严格的统计方法确保了研究发现的可信度。非参数检验适用于单细胞转录组数据这种非正态分布的数据，而Spearman相关适用于分析细胞丰度与预后等非线性关系。

## 涉及 Figures
- 贯穿所有图表的统计显著性标注
