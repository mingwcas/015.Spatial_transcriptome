# Method: Sequence Alignment and Generation of Gene Expression Matrix

## 原文（Methods）
> To obtain transcriptomics data, the Read 2 was processed by extracting the UMI, Barcode A and Barcode B. The processed read 1 was trimmed, mapped against the mouse genome (GRCh38), demultiplexed and annotated (Gencode release M11) using the ST pipeline v1.7.2 (Navarro et al., 2017), which generated the digital gene expression matrix for down-stream analysis. The rows of the gene matrix correspond to pixels, defined by their location info (barcode A x barcode B) and columns correspond to genes. For proteomics data, the Read 2 was processed by extracting the antibody-derived barcode, spatial Barcode A and Barcode B. The processed read was trimmed, demultiplexed using the ST pipeline v1.7.2 (Navarro et al., 2017), which generated the gene protein matrix for down-stream analysis. Similar to the gene expression matrix, the rows correspond to pixels, defined by (barcode A x barcode B) and columns correspond to proteins.
> The pan-mRNA and pan-protein heatmap plots in Figure 2A were generated using raw UMI counts without normalization.

## 解读

### 意义
这是DBiT-seq数据分析的核心步骤，将原始测序数据转化为像素×基因的表达矩阵，是所有下游分析的基础。

### 输入
- 原始测序数据（FASTQ）
- 小鼠基因组（GRCh38）
- 基因注释（Gencode release M11）
- ST pipeline v1.7.2

### 输出
- 数字基因表达矩阵（行=pixels, 列=genes）
- 蛋白质表达矩阵（行=pixels, 列=proteins）
- 原始UMI counts

### 核心步骤
1. 从Read 2提取UMI、Barcode A、Barcode B
2. Read 1进行trimming
3. 使用ST pipeline v1.7.2比对到小鼠基因组GRCh38
4. Demultiplex和注释
5. 生成pixels × genes表达矩阵
6. 蛋白数据类似处理（提取抗体条码、空间条码A和B）
7. 生成pixels × proteins表达矩阵
8. 图2A使用原始UMI counts（未标准化）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因组版本 | GRCh38 | 小鼠参考基因组 |
| 基因注释 | Gencode release M11 | 完整注释 |
| Pipeline | ST pipeline v1.7.2 | 空间转录组标准分析流程 |
| 矩阵结构 | 像素(barcode A × barcode B) × 基因/蛋白 | 二维空间坐标 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ST pipeline | Spatial Transcriptomics pipeline，空间转录组标准分析流程 |
| Demultiplex | 分流，将测序数据按条码分类 |
| UMI | Unique Molecular Identifier，唯一分子标识符 |
| Digital gene expression matrix | 数字基因表达矩阵，行列分别为像素和基因 |

## 复现
- 工具/代码/URL：ST pipeline v1.7.2 (https://github.com/SpatialTranscriptomicsResearch/st_pipeline)
- 代码：https://github.com/rongfan8/DBiT-seq
- 关键调用：NA

## 生物学意义
这是连接实验与数据分析的关键步骤。ST pipeline是空间转录组领域的标准分析工具，被广泛用于Slide-seq和Visium等平台的数据处理。通过从Read 2解析空间条码并与Read 1的转录本序列关联，实现了每个像素的空间转录组定量。

## 涉及 Figures
- **Fig. 2A** — Pan-mRNA和pan-protein heatmap使用原始UMI counts
- **Fig. 1H** — 基因和UMI count分布比较
