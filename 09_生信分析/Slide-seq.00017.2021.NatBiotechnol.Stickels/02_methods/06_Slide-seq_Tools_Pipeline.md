# Method: Slide-seq Tools Pipeline

## 原文（Methods）
> We developed the Slide-seq tools pipeline for processing Slide-seq data. The scripts, documentation and example data are available at https://github.com/MacoskoLab/slideseq-tools. The Slide-seq tools included several analysis steps...

## 解读

### 意义
Slide-seq Tools是处理Slide-seq数据的完整pipeline，将原始BCL文件转换为标准化digital gene expression (DGE)矩阵。

### 输入
- Illumina BCL files (原始图像数据)
- Bead barcode annotations (from PuckCaller)
- Reference genome (GRCm38.81)

### 输出
- Digital gene expression (DGE) matrix
- 质量报告 (mapping rate, UMI counts, Hamming distance等)
- Barcode匹配结果

### 核心步骤
1. **Extract Illumina barcodes**: run_barcodes2sam.py + Picard ExtractIlluminaBarcodes
2. **Convert to BAM**: Picard IlluminaBasecallsToSam (demultiplex, sort by barcode)
3. **Pre-alignment**: Drop-seq tools - 标记barcode (XC), 过滤低质量reads, 切除starting sequence和poly(A)
4. **Align to genome**: STAR aligner (GRCm38.81)
5. **Post-alignment**: Picard SortSam/MergeBamAlignment + Drop-seq TagReadWithInterval/GeneFunction
6. **Generate reports**: Picard CollectRnaSeqMetrics + Drop-seq BamTagHistogram等
7. **Select top cells**: Drop-seq SelectCellsByNumTranscripts
8. **Match barcodes**: cmatcher.cpp计算Illumina barcode与bead barcode的Hamming距离 (≤1)
9. **Final reports**: DigitalExpression生成DGE矩阵

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因组 | GRCm38.81 | Mouse reference |
| Read quality cutoff | ≥10 | 最低质量分数 |
| Min transcripts per cell | 用户指定 | 细胞筛选阈值 |
| Hamming distance | ≤1 | barcode匹配容错 |
| Reads per bead | ~3,000 | 测序深度 |
| 总reads per puck | ~200 million | 每个puck测序量 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DGE matrix | Digital Gene Expression matrix，每行gene每列barcode的UMI计数 |
| UMI | Unique Molecular Identifier，区分原始分子 |
| XC tag | BAM tag for bead barcode |
| XM tag | BAM tag for molecular barcode (UMI) |
| Hamming distance | 两字符串对应位置不同字符的数目 |
| Drop-seq tools | Broad Institute开发的单细胞RNA-seq分析工具 |
| Picard | Broad Institute开发的基因组学工具包 |

## 复现
- **URL**: https://github.com/MacoskoLab/slideseq-tools
- **依赖工具**:
  - Picard: https://broadinstitute.github.io/picard/ (picard-2.18.14)
  - Drop-seq: https://github.com/broadinstitute/Drop-seq (v2.3.0)
  - STAR: https://github.com/alexdobin/STAR (v2.5.2a)
- **代码片段**:
```bash
# Step 1: Extract barcodes
python run_barcodes2sam.py
java -jar Picard ExtractIlluminaBarcodes

# Step 2: Align
python run_alignment.py
STAR --genomeDir GRCm38 --readFilesIn reads.fastq

# Step 8: Match barcodes
cmatcher.cpp -i illumina_barcodes.txt -b bead_barcodes.txt -o matches.txt
```

## 生物学意义
Slide-seq Tools实现了从原始测序数据到空间基因表达矩阵的自动化转换，是Slide-seq技术可重复使用的关键。该pipeline的开源使其他实验室能够处理自己的数据。

## 涉及 Figures
- **Supplementary Fig. 9** — Complete pipeline workflow diagram
- **Fig. 1** — All figures use data processed by this pipeline
