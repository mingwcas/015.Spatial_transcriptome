# Method: Sequence Alignment and Expression Matrix Generation

## 原文（Methods）
> Sequence alignment and generation of mRNA expression matrix. Computational innovations to decode rich RNA biology inherent in FFPE samples.

## 解读

### 意义
将测序数据转化为可用的表达矩阵，进行下游分析

### 输入
- 原始测序数据（FASTQ文件）
- 参考基因组
- 基因注释文件

### 输出
- mRNA表达矩阵
- 空间表达图谱
- 变异检测结果

### 核心步骤
1. 测序数据质量控制
2. 序列比对到参考基因组
3. 基因表达定量
4. 空间表达矩阵生成
5. 变异检测（SNV分析）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 参考基因组 | 小鼠/人类基因组 | 比对参考 |
| 比对工具 | STAR/HISAT2 | 序列比对 |
| 定量方法 | 特异性定量 | 准确计数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 表达矩阵 | 基因×空间位置的计数矩阵 |
| SNV | 单核苷酸变异 |
| 空间表达图谱 | 基因表达的空间分布 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
计算分析流程将原始测序数据转化为生物学见解，是连接实验和生物学发现的关键环节。

## 涉及 Figures
- **Fig. 1** — Patho-DBiT workflow and spatial whole transcriptome mapping of mouse embryo
- **Fig. 2** — Spatial co-mapping of gene expression and RNA processing in the mouse brain
