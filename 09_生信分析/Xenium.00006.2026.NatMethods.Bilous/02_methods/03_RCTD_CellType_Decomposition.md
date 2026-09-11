# Method: RCTD Cell-Type Decomposition

## 原文（Methods）
> RCTD is a computational method for deconvolving spatial transcriptomics data using single-cell RNA-seq references. It uses a Poisson regression model to represent each spatial unit (spot or segmented cell) as a mixture of cell-type-specific profiles, assigning weights that capture the contribution of each type. In doublet mode, RCTD restricts the decomposition to two cell types, assigning w1 to the primary type and w2 to the secondary type. In our analysis, we interpret the primary cell type as the cell's true underlying identity, whereas the secondary type and its weight w2 are treated as indicative of contaminating signal and its magnitude.
> We performed cell-type annotation of Xenium data using the RCTD algorithm in doublet mode, leveraging both matched snRNA-seq and external scRNA-seq references. Reference datasets were filtered to remove cells with fewer than 10 or more than 2,000 UMIs, and cell types represented by fewer than 25 cells were excluded. RCTD was run on raw UMI count data from both the reference and Xenium data. Due to the inherently lower UMI counts in single-cell resolution Xenium data, we applied a more permissive filtering strategy: cells with fewer than 10 total UMIs were excluded and the UMI_min_sigma parameter was reduced to 100.

## 解读

### 意义
RCTD通过单细胞参考图谱对Xenium空间转录组数据进行细胞类型解卷积，同时识别混合信号（污染），为后续SPLIT校正提供基础。

### 输入
- Xenium分割后的单细胞表达矩阵（原始UMI counts）
- snRNA-seq参考图谱（匹配或外部）
- 参考数据集（UMI 10-2000，细胞类型≥25 cells）

### 输出
- 每个细胞的primary和secondary细胞类型标签
- 权重w1（主类型比例）和w2（次类型比例）
- 细胞分类：singlet, doublet_certain, doublet_uncertain, reject

### 核心步骤
1. 准备参考scRNA-seq图谱
2. 参考数据质控过滤（UMI 10-2000，类型≥25 cells）
3. RCTD双细胞类型模式运行
4. 获取每个细胞的w1/w2权重
5. 基于权重差阈值判断singlet/doublet状态
6. 可选：外部参考进行注释验证

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| mode | doublet | 双类型分解模式 |
| UMI_min | 10 | 最小UMI数 |
| UMI_max | 2000 | 最大UMI数 |
| UMI_min_sigma | 100 | Xenium专用降低阈值 |
| class_df | 自定义 | 细胞类型分组以提高特异性 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| w1 | 主细胞类型权重 |
| w2 | 次（污染）细胞类型权重 |
| doublet_certain | 自信的双细胞混合类型 |
| doublet_uncertain | 主类型确定但污染源不明确 |
| singlet | 单一细胞类型 |

## 复现
- 工具：RCTD (https://github.com/dmcable/RCTD)
- 参考代码：https://github.com/bdsc-tds/xenium_analysis_pipeline
- 相关文献：Cable et al., Nature Biotechnology 2022

## 生物学意义
RCTD的双细胞模式能够识别转录本污染：w2高表示该细胞受到邻近其他类型细胞的转录本污染。这对于T细胞等低RNA含量细胞尤为重要，因为它们容易被高RNA含量的恶性细胞污染。

## 涉及 Figures
- **Fig. 3a,b,h** — RCTD双细胞模式示意和SPLIT原理
- **ED Fig. 7** — SPLIT校正后的UMAP
