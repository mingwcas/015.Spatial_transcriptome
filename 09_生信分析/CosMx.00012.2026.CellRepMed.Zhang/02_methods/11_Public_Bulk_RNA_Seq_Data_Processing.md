# Method: Public Bulk RNA-Seq Data Processing

## 原文（Methods）
> Two independent published SCLC bulk RNA-seq cohorts were obtained from George's study and Jiang's study. Raw RNA-seq data from George cohort were processed and normalized to Fragments Per Kilobase Million (FPKM). The count expression profiles from the Jiang cohort were normalized using a log2 (count+1) transformation.

## 解读

### 意义
利用两个独立的公共bulk RNA-seq队列验证PIHs-1基因signature的预后价值，确保发现的生物学意义和临床应用潜力具有普遍性。

### 输入
- George et al. SCLC bulk RNA-seq数据（Nature 2015）
- Jiang et al. SCLC bulk RNA-seq数据（GEO: GSE60052）

### 输出
- 标准化后的表达矩阵
- PIHs-1 signature评分
- 高/低PIHs-1组的生存差异验证

### 核心步骤
1. 获取两个公共队列的表达数据
2. George队列：FPKM标准化
3. Jiang队列：log2(count+1)转换
4. 用于后续PIHs-1 signature验证

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| George队列标准化 | FPKM | Fragments Per Kilobase Million |
| Jiang队列标准化 | log2(count+1) | 对数转换 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| FPKM | Fragments Per Kilobase Million，每千碱基百万片段数 |
| PIHs-1 | Pan-immune hotspot-1，泛免疫热点-1 |

## 复现
- 工具/代码/URL：
  - George et al. Nature 2015: https://doi.org/10.1038/nature14664
  - Jiang et al. GEO GSE60052: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60052

## 生物学意义
通过在两个独立的bulk RNA-seq队列中验证PIHs-1 signature的预后价值，证明了该空间生物学发现可以转化为临床适用的转录组生物标志物，用于患者分层。

## 涉及 Figures
- **Fig. S12D** — PIHs-1 signature在独立队列中的预后验证
