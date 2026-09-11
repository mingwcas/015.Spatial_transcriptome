# Method: Alternative Count Correction Methods

## 原文（Methods）
> ResolVI is a probabilistic model that refines spatial transcriptomic data by resolving cell-type mixtures using variational inference. In this study, we applied ResolVI using default parameters, with models trained either in an unsupervised manner or supervised using Level 2.1 cell-type labels, with T cell subtypes and malignant cell subtypes each grouped into one category.
> Ovrlpy combines a vertical subslicing strategy with an unsupervised, segmentation-free analysis of spatial transcriptomics data to identify and correct for potential spatial doublets. In this study, we applied ovrlpy with default parameters, with a threshold of either 0.5 or 0.7 applied to the pixel signal integrity map.

## 解读

### 意义
ResolVI和ovrlpy是SPLIT之前开发的两种替代校正方法，用于与SPLIT进行性能比较，评估不同校正策略对空间转录组数据质量的影响。

### 输入
- 原始或分割后的Xenium表达矩阵
- （ResolVI）细胞类型注释标签
- （ovrlpy）原始像素信号完整性图

### 输出
- ResolVI：变分推断校正后的表达矩阵
- ovrlpy：垂直切片策略校正后的空间 doublet校正

### 核心步骤
**ResolVI:**
1. 使用变分推断解析细胞类型混合物
2. 可选择监督模式（使用Level 2.1注释）或无监督模式
3. 将T细胞亚型和恶性细胞亚型各自归为一类

**ovrlpy:**
1. 垂直切片策略分析
2. 无分割的空间转录组分析
3. 应用像素信号完整性阈值（0.5或0.7）
4. 识别并校正潜在空间doublet

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| ResolVI模式 | unsupervised/supervised | 无监督或监督训练 |
| Ovrlpy阈值 | 0.5/0.7 | 像素信号完整性阈值 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ResolVI | 基于变分推理的概率模型（Ergen & Yosef, 2025） |
| ovrlpy | 垂直切片策略的空间doublet校正方法（Tiesmeyer et al., 2025） |
| Variational inference | 变分推断，概率近似推理方法 |

## 复现
- ResolVI：https://github.com/bdsc-tds/xenium_analysis_pipeline (issues/83)
- ovrlpy：https://github.com/HiDiHlabs/ovrl.py (issues/40)

## 生物学意义
ResolVI和ovrlpy都能减少转录本污染，但本文显示它们可能显著降低基因计数，导致大量空或近空细胞。SPLIT作为参考基础的方法，在保持基因检测水平方面表现更优。

## 涉及 Figures
- **Fig. 4b-f** — SPLIT、ResolVI、ovrlpy的比较
- **ED Fig. 9b-h** — 乳腺癌panel的比较结果
