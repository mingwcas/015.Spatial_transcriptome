# Method: Data Pre-processing

## 原文（Methods）
> For cDNAs derived from mRNAs, the raw FASTQ file of Read 2 containing the UMI and barcode A and barcode B regions was first reformatted into the standard input format required by ST Pipeline version 1.7.2 using customized Python script. Using recommended ST Pipeline parameters, the Read 1 was STAR mapped to either the mouse genome (GRCm38) or the human genome (GRCh38). The gene expression matrix contains the spatial locations (barcode A × barcode B) of the genes and gene expression levels. For cDNAs derived from ADTs, the raw FASTQ file of Read 2 was reformatted the same way as cDNAs from RNA. Using default settings of CITE-seq-Count 1.4.2, we counted the ADT UMI numbers for each antibody in each spatial location. The protein expression matrix contains the spatial locations (barcode A × barcode B) of the proteins and protein expression levels.

## 解读

### 意义
将原始测序数据转换为带有空间位置信息的基因表达矩阵和蛋白质表达矩阵。

### 输入
- 原始FASTQ文件（Read 1含cDNA序列，Read 2含UMI和Barcode A/B）
- 参考基因组：小鼠GRCm38 / 人GRCh38

### 输出
- 基因表达矩阵（空间位置 × 基因 × 表达量）
- 蛋白质表达矩阵（空间位置 × 蛋白质 × UMI计数）

### 核心步骤
1. mRNA来源cDNA：Read 2重新格式化为ST Pipeline v1.7.2标准输入格式（自定义Python脚本）
2. Read 1使用STAR比对到参考基因组（小鼠GRCm38或人GRCh38）
3. ST Pipeline生成基因表达矩阵（含Barcode A × Barcode B空间位置）
4. ADT来源cDNA：Read 2同样重新格式化
5. 使用CITE-seq-Count v1.4.2（默认参数）统计每个空间位置每个抗体的ADT UMI数
6. 生成蛋白质表达矩阵

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 比对工具 | STAR | RNA-seq读段比对器 |
| ST Pipeline版本 | 1.7.2 | 空间转录组数据处理 |
| CITE-seq-Count版本 | 1.4.2 | ADT计数工具 |
| 小鼠基因组 | GRCm38 | 小鼠参考基因组 |
| 人基因组 | GRCh38 | 人参考基因组 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ST Pipeline | Spatial Transcriptomics Pipeline，空间转录组数据处理流程 |
| CITE-seq-Count | ADT UMI计数工具 |
| STAR | Spliced Transcripts Alignment to a Reference，RNA-seq比对工具 |
| FASTQ | 测序数据标准格式 |
| GRCm38 | 小鼠参考基因组（mm10） |
| GRCh38 | 人参考基因组（hg38） |

## 复现
- 工具/代码/URL
  - ST Pipeline v1.7.2：https://github.com/SpatialTranscriptomicsResearch/st_pipeline
  - CITE-seq-Count v1.4.2：https://github.com/Hoohm/CITE-seq-Count
  - STAR aligner
- 代码片段：
```bash
# mRNA数据处理（概念性命令）
# 1. Reformat Read 2
python3 reformat_barcode.py input_R2.fastq > reformatted_R2.fastq
# 2. STAR比对
STAR --genomeDir GRCh38 --readFilesIn R1.fastq reformatted_R2.fastq
# 3. ST Pipeline处理
st_pipeline_run --expName spatial_rna --genome GRCh38 ...
# 4. ADT计数
CITE-seq-Count -R1 reformatted_R2.fastq -R2 R1.fastq --cbf 1 --cbl 16 ...
```

## 生物学意义
数据预处理将原始测序读段转化为可解读的空间组学数据。ST Pipeline和CITE-seq-Count分别处理转录组和蛋白质组数据，保持空间条码信息的完整性。双端测序设计（Read 1含cDNA序列用于比对，Read 2含条码信息用于空间定位）是该平台的核心数据架构。

## 涉及 Figures
- **Extended Data Fig. 2** — 空间映射的数据质量指标（基因计数、UMI计数等）
- **Extended Data Table 1** — 所有样本的基因和蛋白质计数汇总
