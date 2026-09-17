# Method: Statistical Analysis

## 原文（Methods）
> Statistical analyses were performed in R (v4.1.1). Continuous variables were compared using the Wilcoxon signed-rank test or one-way ANOVA, as appropriate. Trend analyses were conducted using linear regression-based trend tests (and ANOVA-based trend assessment where applicable). Two-sided P-values < .05 were considered statistically significant.

## 解读

### 意义
统计检验是验证生物学发现可靠性的基础，本研究采用非参数和参数检验相结合的方式控制I类错误。

### 输入
- 连续型变量数据（表达量、评分、距离等）
- 分组变量（敏感vs抵抗、转移部位等）
- R v4.1.1环境

### 输出
- 组间比较P值
- 显著性判断（阈值：P < 0.05）

### 核心步骤
1. 数据分布检验（正态性/方差齐性）
2. 连续变量比较：
   - 两组：Wilcoxon符号秩检验（或Mann-Whitney U检验）
   - 多组：单因素方差分析（ANOVA）
3. 趋势分析：
   - 线性回归趋势检验
   - ANOVA趋势评估（如适用）
4. 双侧P值 < 0.05判定为统计显著

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 统计软件 | R v4.1.1 | |
| 两组比较 | Wilcoxon signed-rank test | 非参数检验 |
| 多组比较 | one-way ANOVA | 参数检验 |
| 趋势检验 | 线性回归趋势检验 + ANOVA趋势评估 | |
| 显著性阈值 | P < 0.05（双侧） | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Wilcoxon signed-rank test | 非参数配对检验，适用于配对样本 |
| ANOVA | Analysis of Variance，方差分析 |
| P-value | 统计显著性概率值 |
| 双侧检验 | Two-sided test，考虑方向性的检验 |

## 复现
- 工具：R v4.1.1
- 内置统计函数或以下扩展包：
```R
# 基本用法
wilcox.test(group1, group2, paired = FALSE)
aov(expression ~ group, data = df)
summary(lm(expression ~ trend_variable, data = df))
```

## 生物学意义
严格的统计检验确保了报告中生物学差异的可靠性。Wilcoxon检验对非正态分布数据更稳健，ANOVA则适用于多组同时比较。

## 涉及 Figures
- 所有包含统计显著性标注的图表
- **Fig. 4d** — 细胞毒性评分比较（P = .007）
- **Fig. 4h** — M1/M2极化评分比较（P = 9.35e-36, P = 6.30e-19）
