# Method: Tumor Sample Collection and RNA Sequencing

## 原文（Methods）
> Tumor specimens from surgical resections or biopsies with ≥20% tumor content were processed for RNA extraction (QIAamp Mini Kit). RNA-seq libraries were prepared using Illumina TruSeq kits and sequenced on the HiSeq 2500 platform (2×50 bp). Reads were aligned to the GRCh38 genome using STAR (v2.6.1) and quantified as TPM using RSEM (v1.3.1), following GTEx-recommended parameters.

## 解读

### 意义
描述Bulk RNA-seq的实验流程和生物信息学分析标准流程，用于获取各转移灶的全局基因表达谱。

### 输入
- 手术切除或活检组织样本（肿瘤含量≥20%）
- QIAamp Mini Kit（RNA提取）
- Illumina TruSeq建库试剂盒
- HiSeq 2500测序平台

### 输出
- Raw reads（FASTQ格式）
- 比对结果（BAM格式）
- 基因表达矩阵（TPM值）

### 核心步骤
1. 组织样本RNA提取（QIAamp Mini Kit）
2. Illumina TruSeq文库构建
3. HiSeq 2500测序（2×50 bp双端）
4. STAR比对至GRCh38基因组（v2.6.1）
5. RSEM定量TPM值（v1.3.1）
6. 遵循GTEx推荐参数

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 肿瘤含量阈值 | ≥20% | 样本筛选标准 |
| 测序平台 | HiSeq 2500 | Illumina |
| 读长 | 2×50 bp | 双端测序 |
| 比对工具 | STAR v2.6.1 | |
| 定量工具 | RSEM v1.3.1 | |
| 表达量单位 | TPM | |
| 参考基因组 | GRCh38 | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| TPM | Transcripts Per Million，标准化表达量单位 |
| STAR | Spliced Transcripts Alignment to a Reference，快速RNA-seq比对工具 |
| RSEM | RNA-Seq by Expectation-Maximization，基因表达定量工具 |
| GTEx | Genotype-Tissue Expression project，组织特异性基因表达参考数据库 |

## 复现
- 工具/代码/URL：
  - STAR: https://github.com/alexdobin/STAR
  - RSEM: https://github.com/deweylab/RSEM
- 代码片段（关键调用，≤10行）：
```
STAR --genomeDir GRCh38 --readFilesIn R1.fastq R2.fastq
rsem-calculate-expression --paired-end --alignments -p 8 input.bam GRCh38 output
```

## 生物学意义
Bulk RNA-seq提供了各转移灶的整体转录组特征，是后续免疫浸润分析（GSEA、EPIC反卷积）和样本分群（PCA）的基础。

## 涉及 Figures
- **Fig. 2** — 功能转录组学分析，免疫浸润状态分层
- **Supplementary Figure S2** — EPIC细胞类型反卷积分析
