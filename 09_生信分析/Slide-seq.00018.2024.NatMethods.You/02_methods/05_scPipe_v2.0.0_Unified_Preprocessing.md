# Method: scPipe v2.0.0 (Unified Preprocessing)

## 原文（Methods）
> We preprocessed fastq files from multiple platforms using their respective preprocessing pipeline (where provided) and updated scPipe to allow sample processing with unified functions for data from different sST technologies starting from fastq files. Mouse GRCm39 was used as a reference for alignment in each of the pipelines for locally generated data. DBiT-seq data underwent initial filtering using a predefined barcode list, and subsequently, fastq file 1 was restructured to adopt the format of spatial barcodes followed by UMIs. The processed data were further analyzed using scPipe (v2.0.0) to generate spot-by-gene count matrices.

## 解读

### 意义
scPipe是一个统一的空间转录组数据预处理管道，本研究对其进行了更新以支持多种sST技术的数据处理，便于进行公平比较。

### 输入
- 多种平台的原始FASTQ文件
- 空间条码信息
- 参考基因组（Mouse GRCm39）

### 输出
- 统一的spot-by-gene计数矩阵
- downsampled数据用于标准化比较

### 核心步骤
1. 解析不同平台的空间条码格式
2. 将reads比对到GRCm39基因组
3. 生成统一的计数矩阵
4. 支持downsampling以标准化测序深度

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| scPipe version | v2.0.0 | 统一预处理管道 |
| reference genome | Mouse GRCm39 | 小鼠参考基因组 |
| downsampling | 等量reads抽样 | 用于标准化不同平台的测序深度 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Downsampling | 向下抽样，将不同样本统一到相同reads数量 |
| Unified preprocessing | 统一预处理流程 |

## 复现
- 工具/代码/URL：https://github.com/YOU-k/cadasSTre (cadasSTre分析脚本)
- scPipe包：https://bioconductor.org/packages/release/bioc/html/scPipe.html

## 生物学意义
scPipe的更新使得跨平台比较成为可能，对推动空间转录组领域的方法标准化具有重要意义。

## 涉及 Figures
- **Fig. 1** — 实验设计和数据处理流程概述
- **Fig. 2-4** — 所有下游分析均基于scPipe处理的数据
