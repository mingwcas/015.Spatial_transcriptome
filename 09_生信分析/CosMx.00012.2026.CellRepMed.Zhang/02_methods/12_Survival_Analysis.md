# Method: Survival Analysis

## 原文（Methods）
> To assess the association between CN abundance and patient survival, the patients were stratified into 'high' or 'low' groups for each CN, based on whether their sample level was above or below the median value across the entire cohort. To validate the spatial gene signature, the top 20 DEGs defining the prognostically favorable Pan-immune hotspot-1 (PIHs-1) were used to create a gene signature. A single-sample gene set enrichment analysis (ssGSEA) score for this signature was computed for each sample in the independent bulk RNA-seq cohorts using the 'GSVA' package (v2.0.7). The cohorts were dichotomized into PIHs-1 high/low groups based on the median ssGSEA score for survival analysis. Survival differences were evaluated using the Kaplan-Meier method and the log rank test. Univariable and multivariable Cox proportional hazards models were constructed using the 'survival' R package (v3.5-7). Hazard ratios (HR) and 95% confidence intervals (CI) are reported.

## 解读

### 意义
生存分析评估空间细胞结构（CN abundance和PIHs-1 signature）与患者预后（OS和DFS）的关联，为发现临床可应用的预后生物标志物提供证据。

### 输入
- 患者临床预后数据（OS、DFS）
- CN丰度数据
- PIHs-1的20个特征基因列表
- GSVA包 (v2.0.7)
- Survival包

### 输出
- Kaplan-Meier生存曲线
- Log rank检验p值
- 单变量和多变量Cox回归HR和95% CI
- ssGSEA评分

### 核心步骤
1. 基于中位数将患者分为高/低CN丰度组
2. 使用PIHs-1的top 20 DEGs创建基因signature
3. GSVA计算单样本GSEA评分（ssGSEA）
4. 基于中位ssGSEA评分分组
5. Kaplan-Meier生存曲线和log rank检验
6. 单变量和多变量Cox回归

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 分组方法 | 中位数分割 | high vs low |
| PIHs-1基因数 | 20 | 预后signature |
| GSVA版本 | v2.0.7 | ssGSEA分析 |
| Survival版本 | v3.5-7 | 生存分析 |
| 统计软件 | R v4.3.0 | 分析环境 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| OS | Overall survival，总生存期 |
| DFS | Disease-free survival，无病生存期 |
| HR | Hazard ratio，风险比 |
| CI | Confidence interval，置信区间 |
| ssGSEA | single-sample gene set enrichment analysis，单样本基因集富集分析 |
| PIHs-1 | Pan-immune hotspot-1，泛免疫热点-1 |

## 复现
- 工具/代码/URL：
  - GSVA: https://new.bioconductor.org/packages/devel/bioc/html/GSVA.html
  - Survival: https://cran.r-project.org/web/packages/survival/index.html
- 代码片段：
```r
library(GSVA)
library(survival)
# ssGSEA score calculation
gsva_scores <- gsva(expr_data, gene_sets, method = "ssgsea")
# Kaplan-Meier analysis
fit <- survfit(Surv(time, status) ~ group, data = clinical_data)
ggsurvplot(fit, data = clinical_data)
# Cox regression
coxph(Surv(time, status) ~ variable, data = clinical_data)
```

## 生物学意义
生存分析证明PIHs-1是独立预后因素（OS: HR=4.418, p=0.011; DFS: HR=2.195, p=0.052），且其预后价值独立于任何单一免疫细胞类型的丰度。这表明空间组织架构本身而非细胞组成决定临床预后，为空间生物标志物的临床转化奠定基础。

## 涉及 Figures
- **Fig. 5D, 5E** — CN丰度与生存关联、PIHs-1 Kaplan-Meier曲线
- **Fig. S12A, S12B, S12C** — 扩展生存分析
