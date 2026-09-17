# Method: R语言数据分析

## 原文（Methods）
> Data analysis can be done on any software package, but R is convenient for interactive analysis and high-quality graphs. Find the HISTORY tab on the upper right console window, and double-click on individual commands in order to re-execute the previous R session and learn how to: import and filter data using a specific criterion (i.e., cluster size); plot a distribution of reads by a specific criterion (i.e., RNA classes and strands); convert a table of reads into a table of gene expression level; correlate gene expression from different images; and find statistically enriched genes in different regions.

## 解读

### 意义
对FISSEQ测序结果进行统计分析，包括数据过滤、基因表达量化、空间富集分析等

### 输入
- results.tsv（空间聚类结果）

### 输出
- 基因表达矩阵
- 空间富集分析结果
- 质控图表

### 核心步骤
1. 导入results.tsv数据
2. 按聚类大小过滤（推荐cluster size >5）
3. 绘制RNA类别和链方向分布图
4. 将读取表转换为基因表达水平表
5. 比较不同图像间的基因表达相关性
6. 使用Fisher精确检验等方法找空间富集基因

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 聚类大小阈值 | >5 | 过滤低质量读取 |
| 正义链比例 | >90% | 预期正义链读取比例 |
| rRNA比例 | 50-80% | 预期rRNA读取比例 |
| 每FOV读取数 | 10,000-50,000 | 典型数据量 |
| 每区域细胞数 | ~30-50 | 典型FOV |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Cluster size | 聚类中的像素数，反映扩增子大小 |
| Sense/antisense reads | 正义/反义链读取 |
| RNA classes | RNA分类（mRNA, rRNA, tRNA等） |
| Fisher's exact test | 用于空间富集分析的统计检验 |

## 复现
- 工具：R + RStudio, ggplot2, data.table包
- 示例数据和R session文件：http://arep.med.harvard.edu/FISSEQ_Nature_Protocols_2014/
- 推荐：创建B&W图像掩膜基于细胞形态、DAPI染色等进行区域比较

## 生物学意义
R数据分析是将FISSEQ测序数据转化为生物学知识的关键步骤。通过空间富集分析可以发现细胞类型特异性基因、亚细胞RNA定位模式等。FISSEQ的独特优势是其读取富含细胞类型特异性基因而非管家基因，使其特别适合细胞类型鉴定。

## 涉及 Figures
- **Fig. 2** — FISSEQ与单细胞RNA-seq比较（基因表达相关性）
- **Fig. 6** — 数据分析步骤50-51
- **Supplementary Fig. 6** — RStudio数据分析界面
