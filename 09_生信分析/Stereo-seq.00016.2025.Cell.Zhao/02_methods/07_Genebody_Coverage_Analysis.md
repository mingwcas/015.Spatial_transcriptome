# Method: Quantitative Analysis of Genebody Coverage

## 原文（Methods）
> The raw alignment bam file was first filtered to retain the mapped reads with more than 10 reads by a custom python script. Then RseQC was used to calculate the sequencing depth for each nucleotide position on the genome with the default parameters. Only those reads that align to exons would be used in the calculation and all gene lengths would be scaled to 100 for visualization.

## 解读

### 意义
分析不同空间转录组技术在基因体上的覆盖分布，评估poly(A)捕获 vs 随机引物捕获的偏倚差异。

### 输入
- 比对后的BAM文件
- 参考基因组注释（GTF）

### 输出
- 基因体覆盖深度图
- 5'到3'的覆盖分布曲线

### 核心步骤
1. 过滤：保留MAPQ>10的比对reads
2. 使用RseQC计算每个基因组位置的测序深度
3. 仅使用比对到外显子的reads
4. 将基因长度标准化到100进行可视化比较

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 读数过滤 | MAPQ >10 | 比对质量 |
| 标准化 | 基因长度scale to 100 | 可视化比较 |
| 工具 | RseQC | 测序深度分析 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Gene body coverage | 基因体覆盖深度分布 |
| RseQC | RNA-seq质量控制工具 |
| 3' bias | 3'端覆盖偏倚 |

## 复现
- RseQC: http://rseqc.sourceforge.net/
- 版本：v5.0.1

## 生物学意义
随机引物捕获提供均匀的基因体覆盖，而poly(A)捕获具有3'偏倚。这直接影响对可变剪接、ncRNA等的检测能力。

## 涉及 Figures
- Fig. 3A, 3B (gene body coverage comparison)
