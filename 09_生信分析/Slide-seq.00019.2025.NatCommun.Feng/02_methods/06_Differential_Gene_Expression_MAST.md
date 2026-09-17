# Method: Differential Gene Expression Analysis (MAST)

## 原文（Methods）
> DGE analysis was performed using the MAST framework, applying two-sided tests and using biological replicate identity as a covariate to minimize inter-sample variability and improve detection of condition-specific transcriptional changes. FDR correction was applied using the BH method across all datasets. Genes expressed in at least 5% of nuclei within each cell subtype were retained. For the human snRNA-seq dataset, raw UMI counts were extracted from the "RNA assay" of the Seurat object and normalized. For the human snRNA-seq dataset, genes with a |log2FC| > 0 and FDR ≤0.05 were considered statistically significant. A |log2FC| > 0 and FDR ≤0.05 were used for the MERFISH datasets.

## 解读

### 意义
差异基因表达（DGE）分析识别DS与整倍体对照之间细胞类型特异性基因表达变化，是揭示DS神经发育异常分子机制的核心分析。

### 输入
- Seurat对象中的raw UMI counts
- 细胞类型注释
- 样本批次信息（作为协变量）

### 输出
- 差异表达基因列表（log2FC, FDR）
- 火山图
- 热图

### 核心步骤
1. 从Seurat对象提取每个细胞亚型的raw UMI counts
2. 筛选在≥5%细胞中表达的基因
3. 使用MAST框架进行双侧检验
4. 以生物重复身份为协变量控制样本间变异
5. Benjamini-Hochberg (BH)方法进行FDR校正
6. 设定显著性阈值：|log2FC| > 0, FDR ≤ 0.05

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 检验方法 | MAST (双侧) | 适合单细胞RNA-seq的差异分析 |
| 表达阈值 | ≥5% nuclei | 基因必须在≥5%细胞中表达 |
| log2FC阈值 | > 0 | 差异表达基因阈值 |
| FDR阈值 | ≤0.05 | 多重检验校正 |
| 协变量 | 生物重复身份 | 控制样本间变异 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| MAST | Model-based Analysis of Single-cell Transcriptomics |
| FDR | False Discovery Rate，错误发现率 |
| BH method | Benjamini-Hochberg多重检验校正方法 |
| log2FC | log2转化后的倍数变化 |
| UMI | Unique Molecular Identifier，唯一分子标识符 |

## 复现
- R包：MAST
- 参考：https://github.com/RGLab/MAST
- Python：scVelo用于MERFISH数据分析

## 生物学意义
DGE分析揭示了DS脑中广泛的下调通路，包括细胞周期相关通路（CDK1, CDK4, CCND2）、翻译相关通路（EIF3F, EEF1A1）以及DNA修复通路，同时也发现了特定基因的上调（如DSCAM, APP, DYRK1A），这些发现为理解DS神经发育异常提供了分子层面的证据。

## 涉及 Figures
- **Fig. 2** — Transcriptional dysregulation in NPCs
- **Fig. 3** — Transcriptional signatures in neurons and glia
- **Fig. 6** — DEGs in trisomic mouse brain
