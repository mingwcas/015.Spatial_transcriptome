# Method: snRNA-seq Preprocessing and QC

## 原文（Methods）
> Filtered barcode counts from CellRanger were analyzed using the Seurat package (v. 5.0.1) in R (v. 4.3.2). Cells with at least 200 detected genes and fewer than 20% of reads mapping to mitochondrial genes were retained. To recover neutrophils, the gene threshold was lowered to 100 genes per cell, and cells forming a distinct cluster with high expression of canonical neutrophil markers (that is, FCGR3B, S100A9, IL1R2, CSF3R, FPR1 and NAMPT) were retained.
> Raw counts were normalized using SCTransform, and the top 3,000 variable genes across samples were selected using SelectIntegrationFeatures. Dimensionality reduction was done using principal component analysis (PCA). Clustering was done via Seurat's shared nearest neighbor modularity optimization algorithm (FindNeighbors and FindClusters) using 30 principal components and resolutions between 0.4 and 0.8.
> Clusters were annotated based on the top differentially expressed genes and canonical markers. Significant markers were identified with Seurat::FindAllMarkers() (two-sided Wilcoxon rank sum test, Bonferroni correction, adjusted P < 0.05, log fold change >1). Subclustering enabled finer annotation, resulting in four hierarchical annotation levels.

## 解读

### 意义
snRNA-seq数据作为参考基准，用于Xenium数据的细胞类型注释和质量评估，同时为SPLIT方法提供细胞类型特异性基因表达谱参考。

### 输入
- 10x Chromium平台生成的原始barcode counts数据（CellRanger输出）
- FFPE肿瘤样本（肺癌和乳腺癌各4例）

### 输出
- 质控后的单细胞基因表达矩阵
- 四级层级细胞类型注释（Level 1-4）
- 用于RCTD注释的参考细胞类型图谱

### 核心步骤
1. 质控过滤：≥200基因/细胞，线粒体基因占比<20%
2. 中性粒细胞特殊处理：阈值降至100基因，保留特定标记物高表达 cluster
3. SCTransform标准化
4. 选取3000个高度可变基因
5. PCA降维（30个主成分）
6. SNN聚类（分辨率0.4-0.8）
7. 基于标记物和canonical marker进行细胞类型注释
8. 四级层级注释体系

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| min.genes | 200 | 最小基因数 |
| max.mito.pct | 20% | 线粒体基因最大比例 |
| nFeature_RNA.lower | 100 | 中性粒细胞恢复阈值 |
| nComponents | 30 | PCA主成分数 |
| resolution | 0.4-0.8 | 聚类分辨率范围 |
| FindMarkers参数 | Bonferroni, P<0.05, logFC>1 | 差异表达阈值 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SCTransform | Seurat中的方差稳定化归一化方法 |
| SNN | Shared Nearest Neighbor，共享最近邻 |
| Level 2.1 | 扩展的二级注释，区分CD8+ T细胞，用于IHC验证 |
| UMI | Unique Molecular Identifier，独特分子标签 |

## 复现
- 工具：Seurat v.5.0.1, R v.4.3.2
- 代码参考：https://github.com/bdsc-tds/xenium_analysis_pipeline

## 生物学意义
snRNA-seq作为金标准参考，具有匹配样本来源，可准确注释Xenium数据中的细胞类型，尤其是区分恶性肿瘤细胞的患者特异性转录特征。Level 2.1注释专为IHC验证设计，增强了 Validation的可靠性。

## 涉及 Figures
- **Fig. 1c** — 细胞类型组成在Xenium和Chromium样本中的分布
- **ED Fig. 1** — 使用外部参考的Xenium数据注释
