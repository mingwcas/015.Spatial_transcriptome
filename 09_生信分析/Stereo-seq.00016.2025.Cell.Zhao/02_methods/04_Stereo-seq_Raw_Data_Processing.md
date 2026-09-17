# Method: Stereo-seq Raw Data Processing (SAW Pipeline)

## 原文（Methods）
> The raw fastq sequencing files generated via Stereo-seq V2 assays were processed with the SAW pipeline. Briefly, read 1 contains the coordination identity (CID) and Unique molecular identifiers (UMI) sequences. CID sequences were mapped to the coordinates of Stereo-seq V2 capturing chip, allowing 1 base mismatch. UMIs having either N bases or more than 2 bases with quality score less than 10 were filtered out. Then associated read 2 was aligned to reference genome (mm10 for mouse data, hg38 for human data) using STAR, and only reads with MAPQ >10 were kept. UMIs of the same CID and the same gene were collapsed with one mismatch allowed for PCR or sequencing errors. The gene expression counts were aggregated to generate a profile matrix with spatial coordinates.

## 解读

### 意义
SAW pipeline是Stereo-seq的标准数据分析流程，将原始测序数据转化为带有空间坐标的基因表达矩阵。

### 输入
- 原始Fastq文件（Read 1: CID+UMI; Read 2: 序列）
- 参考基因组 (mm10/hg38)

### 输出
- 空间基因表达矩阵（每spot的基因计数）
- BAM文件

### 核心步骤
1. Read 1解析：提取CID和UMI序列
2. CID比对到芯片坐标（允许1个错配）
3. UMI质量过滤：去除含N或>2个Q<10的碱基的UMI
4. Read 2比对到参考基因组（STAR）
5. MAPQ>10过滤
6. 相同CID和基因的UMI去重（允许1个错配）
7. 汇总为空间表达矩阵

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| CID比对错配 | ≤1 | |
| UMI质量过滤 | 无N碱基，≤2个Q<10的碱基 | |
| 比对软件 | STAR | |
| MAPQ阈值 | >10 | |
| 去重允许错配 | 1 | PCR/测序错误 |
| 参考基因组 | mm10 (小鼠), hg38 (人) | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SAW | Stereo-seq Analysis Workflow |
| CID | Coordinate Identity，空间坐标条码 |
| UMI | Unique Molecular Identifier，唯一分子标签 |
| MAPQ | Mapping Quality，比对质量分数 |

## 复现
- 工具：SAW pipeline (STOmics)
- 比对软件：STAR
- 网址：https://github.com/STOmics/SAW

## 生物学意义
这是空间转录组数据分析的基础，将原始测序数据转化为可进行后续分析的空间表达矩阵。

## 涉及 Figures
- 支撑所有figures的基础数据分析
