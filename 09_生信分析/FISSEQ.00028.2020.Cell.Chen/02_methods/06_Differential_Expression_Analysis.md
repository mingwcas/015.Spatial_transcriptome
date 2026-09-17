# Method: Differential Expression Analysis

## 原文（Methods）
> DE analysis was conducted by fitting two separate generalized linear models (GLM) using Aβ intensity and genotype information respectively. Each GLM model was tested for differential expression by using EdgeR quasi-likelihood F-test which accounts for the uncertainty in dispersion estimation at the age of 3 months and 18 months, separately. The Aβ model represents transcriptional changes under Aβ exposure, which models the log transformed Aβ index as a continuous variable, and its LFC indicates the changes in gene expression per unit change in Aβ index. For a more straightforward interpretation, we multiply all LFC by a constant 4.59 (the difference between the maximum observed Aβ and the minimum observed Aβ index across the database). The genotype model assesses transcriptional changes between WT and TG mice.

## 解读

### 意义
差异表达分析是连接Aβ病理与基因表达变化的核心统计方法，使用两种互补模型区分基因型效应和Aβ暴露效应。

### 输入
- log-CPM标准化矩阵
- Aβ指数（像素强度标准差，log转换）
- 基因型信息（AppNL-G-F vs WT）
- 年龄分组（3月龄和18月龄）

### 输出
- 每个基因的LFC（Log Fold Change）
- 统计显著性p值
- Aβ模型：基因表达随Aβ暴露的变化
- 基因型模型：WT vs TG的差异

### 核心步骤
1. 构建两个独立的广义线性模型（GLM）
   - Aβ模型：log(Aβ index) 作为连续变量
   - 基因型模型：WT vs AppNL-G-F 作为分类变量
2. EdgeR quasi-likelihood F-test检验差异表达
3. LFC乘以常数4.59进行校正（最大-最小Aβ指数差值）
4. 分别在3月龄和18月龄进行分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 统计模型 | GLM (Generalized Linear Model) | 广义线性模型 |
| 检验方法 | EdgeR quasi-likelihood F-test | 准似然F检验 |
| LFC校正常数 | 4.59 | 最大-最小Aβ指数差值 |
| Aβ模型变量 | log(Aβ index) | 连续变量 |
| 年龄分组 | 3月龄、18月龄 | 分别分析 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| LFC (Log Fold Change) | 对数倍数变化 |
| GLM (Generalized Linear Model) | 广义线性模型 |
| Quasi-likelihood F-test | 准似然F检验，考虑离散度估计不确定性 |
| Aβ index | Aβ指数，TD内6E10像素强度的标准差 |
| Genotype model | 基因型模型，比较WT和转基因小鼠 |
| Aβ model | Aβ模型，分析Aβ暴露对基因表达的影响 |

## 复现
- 工具/代码/URL
  - EdgeR: https://bioconductor.org/packages/release/bioc/html/edgeR.html
- 代码片段
```R
# Aβ模型
design_ab <- model.matrix(~log_ab_index)
fit_ab <- glmQLFit(y, design_ab)
qlf_ab <- glmQLFTest(fit_ab, coef=2)

# 基因型模型
design_geno <- model.matrix(~genotype)
fit_geno <- glmQLFit(y, design_geno)
qlf_geno <- glmQLFTest(fit_geno, coef=2)
```

## 生物学意义
双模型设计使研究者能够区分基因型效应（可能是App基因插入本身的影响）和Aβ病理效应。Aβ模型揭示了随Aβ积累逐渐增加的基因表达变化，而基因型模型显示了与WT的总体差异。这种区分对于理解疾病进展机制至关重要。

## 涉及 Figures
- **Fig. 2D-E** — Aβ模型与RNAscope的验证
- **Fig. 3A, E-F** — PIG基因的差异表达
- **Fig. 6A-B** — OLIG基因的差异表达
- **Figure S3A** — GO类别分析
