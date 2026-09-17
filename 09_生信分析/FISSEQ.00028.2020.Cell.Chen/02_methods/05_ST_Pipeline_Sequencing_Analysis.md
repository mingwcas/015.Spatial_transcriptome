# Method: ST Pipeline Sequencing Data Analysis

## 原文（Methods）
> Sequencing data were pre-processed with the ST pipeline (Navarro et al., 2017), which filtered low quality bases, mapped against the mouse genome (Ensembl 88), and generated a count matrix. The count matrix was further filtered by removing spots with tissue coverage less than 30% in the HE image. The EdgeR 'cpm' function was used for library size normalization and the output log-cpm matrix was used for the rest of the analyses.

## 解读

### 意义
ST Pipeline是ST测序数据的标准预处理流程，将原始测序数据转换为可用于下游分析的基因表达计数矩阵。

### 输入
- Illumina NextSeq500双端测序原始数据（FASTQ）
- 空间条形码阵列ID文件
- 小鼠基因组参考（Ensembl 88）

### 输出
- 原始计数矩阵（spots × genes）
- 过滤后的计数矩阵（组织覆盖度>30%）
- log-CPM标准化矩阵

### 核心步骤
1. ST pipeline过滤低质量碱基
2. 比对到小鼠基因组（Ensembl 88）
3. 生成计数矩阵
4. 过滤组织覆盖度<30%的spots
5. EdgeR 'cpm'函数进行文库大小标准化
6. 输出log-CPM矩阵用于下游分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 参考基因组 | Ensembl 88 | 小鼠基因组版本 |
| 组织覆盖度阈值 | 30% | TD质量过滤标准 |
| 标准化方法 | EdgeR cpm | 计数/百万标准化 |
| 输出格式 | log-CPM | 对数转换的CPM值 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ST pipeline | 空间转录组学数据预处理自动化流程 |
| CPM (Counts Per Million) | 每百万计数，文库大小标准化方法 |
| log-CPM | CPM值的对数转换 |
| Count matrix | 计数矩阵，行为spots，列为基因 |
| Ensembl 88 | 小鼠基因组注释版本 |

## 复现
- 工具/代码/URL
  - ST pipeline: https://github.com/SpatialTranscriptomicsResearch/st_pipeline
  - EdgeR: https://bioconductor.org/packages/release/bioc/html/edgeR.html
- 代码片段
```R
# EdgeR标准化
library(edgeR)
dge <- DGEList(counts=count_matrix)
dge <- calcNormFactors(dge)
logcpm <- cpm(dge, log=TRUE)
```

## 生物学意义
ST pipeline的标准化确保了不同样本间基因表达的可比性。30%组织覆盖度阈值过滤掉了可能包含非特异性信号的spots，保证了数据质量。每个TD平均检测到31,283 ± 7,441个UMI和6,578 ± 987个基因，证明了该方法的高灵敏度。

## 涉及 Figures
- **Figure S1B-C** — 每个TD的基因和reads分布
- **Figure S1D-E** — 全数据库基因和TD的reads分布
