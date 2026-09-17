# Method: Whole Transcriptome Sequencing and Analysis

## 原文（Methods）
> RNA libraries were prepared using the TruSeq Stranded Total RNA kit with Ribo-Zero Gold and sequenced on Illumina HiSeq 2500 (2 × 50 bp). Libraries were normalized to 20 pM and sequenced using V3 chemistry. Reads were aligned to the GRCh38 human genome with STAR (v2.6.1) and quantified as TPM using RSEM (v1.3.1), following GTEx guidelines.

## 解读

### 意义
使用链特异性转录组测序技术获取全基因组表达谱，STAR+RSEM流程是RNA-seq标准分析流程。

### 输入
- Total RNA样本
- TruSeq Stranded Total RNA kit with Ribo-Zero Gold（rRNA去除）
- Illumina HiSeq 2500（V3 chemistry，20 pM文库）

### 输出
- 链特异性RNA-seq数据
- GRCh38比对结果（BAM）
- TPM表达矩阵

### 核心步骤
1. TruSeq Stranded Total RNA kit建库（保留链方向性）
2. Ribo-Zero Gold去除rRNA
3. 文库定量至20 pM
4. HiSeq 2500 V3 chemistry测序（2×50 bp）
5. STAR比对至GRCh38（v2.6.1）
6. RSEM定量TPM（v1.3.1）
7. 遵循GTEx分析指南

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 建库试剂盒 | TruSeq Stranded Total RNA + Ribo-Zero Gold | 链特异性 |
| 测序平台 | Illumina HiSeq 2500 | |
| 化学试剂 | V3 | |
| 文库浓度 | 20 pM | |
| 读长 | 2×50 bp | |
| 比对工具 | STAR v2.6.1 | |
| 定量工具 | RSEM v1.3.1 | |
| 参考基因组 | GRCh38 | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| TruSeq Stranded Total RNA | 保留链方向性的建库方案 |
| Ribo-Zero Gold | rRNA去除试剂 |
| TPM | Transcripts Per Million |
| GTEx | 基因型-组织表达项目分析标准 |

## 复现
- 工具：STAR v2.6.1、RSEM v1.3.1
- 遵循GTEx分析规范

## 生物学意义
链特异性建库可以区分正义和反义转录本，提高可变剪接检测准确性，对于理解肿瘤转录组复杂性具有重要价值。

## 涉及 Figures
- **Fig. 2** — 全转录组表达分析
