# Method: Spatial Alternative Splicing Analysis

## 原文（Methods）
> Using a custom Python script, we split the BAM file into region-specific BAM files based on coordinates and deduplicated the BAM file using Picard according to barcode and UMI combinations. Subsequently, in a pseudo-bulk level, we identified differential alternative splicing events between the normal and tumor, as well as between Tumor 1 and Tumor 2. Alternative splicing identification was performed using rMATS-turbo with the parameters "-t single, –readLength 75, –variable-read-length, and –allow-clipping". Events with an FDR ≤0.05 were considered differential alternative splicing events across regions. The expression for junction reads, skipping exon reads, and IR reads were extracted from the BAM file using pysam. Spatial visualization was achieved using scanpy, seaborn, and matplotlib, while RNA track visualization was performed using rmats2sashimiplot.

## 解读

### 意义
利用Stereo-seq V2的全基因体覆盖优势，鉴定肿瘤与正常区域之间的可变剪接(AS)事件。

### 输入
- 空间转录组BAM文件
- 区域注释（肿瘤/正常）
- 参考基因组注释

### 输出
- 可变剪接事件列表（SE, MXE, A3SS, A5SS, RI）
- 差异AS事件（FDR≤0.05）
- 空间可视化

### 核心步骤
1. 按区域分割BAM文件
2. Picard去重（barcode+UMI）
3. 伪bulk水平差异AS分析（rMATS-turbo）
4. FDR≤0.05过滤
5. 提取junction reads, skipping exon reads, IR reads
6. 空间可视化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| rMATS参数 | -t single, –readLength 75 | |
| 参数 | –variable-read-length, –allow-clipping | |
| FDR阈值 | ≤0.05 | 显著AS事件 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SE | Skipped Exon，跳过外显子 |
| MXE | Mutually Exclusive Exon，互斥外显子 |
| A3SS | Alternative 3' Splice Site，3'可变剪接位点 |
| A5SS | Alternative 5' Splice Site，5'可变剪接位点 |
| RI | Retained Intron，内含子保留 |
| rMATS | 检测可变剪接的标准工具 |

## 复现
- rMATS-turbo: https://github.com/Xinglab/rmats-turbo
- Picard: https://broadinstitute.github.io/picard/
- rmats2sashimiplot: https://github.com/Xinglab/rmats2sashimiplot

## 生物学意义
全基因体覆盖使Stereo-seq V2能够分析可变剪接事件，这对于理解肿瘤进展和细胞异质性很重要。

## 涉及 Figures
- Fig. 5 (tumor-associated AS events in TNBC)
