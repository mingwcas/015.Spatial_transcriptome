# Method: Inferred Copy Number Variation (inferCNV) Analysis

## 原文（Methods）
> The raw expression matrix of spatial transcriptomics data was filtered preliminarily by scanpy to retain spots with a minimum of 500 genes, and genes present in at least 50 cells. The filtered matrix was then used as input for inferCNV algorithm. Simultaneously, chromosomal positions for all genes are annotated by searching the GTF file, which also serves as input for inferCNV. The cnv.tl.infercnv function was set with parameters: lfc_clip = 3, window_size = 250, and exclude_chromosomes=('chrX','chrY'). The immune cell cluster were identified by integrating the RNA clustering results and evaluating markers such as PTPRC and CD3 gene in each cluster. These immune cell clusters were selected as normal references for inferCNV analysis.

## 解读

### 意义
从空间转录组数据推断拷贝数变异(CNV)，用于区分恶性肿瘤和正常细胞。

### 输入
- 空间转录组表达矩阵
- 参考基因组注释文件（GTF）

### 输出
- 全基因组CNV热图
- 恶性/正常区域分类

### 核心步骤
1. Scanpy预处理：过滤<500基因的spots和<50细胞的基因
2. 输入inferCNV算法
3. 染色体位置注释
4. 设置参数：lfc_clip=3, window_size=250
5. 排除性染色体
6. 使用免疫细胞簇作为正常参考
7. Leiden聚类结合CNV结果

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因过滤 | ≥50 cells | |
| Spot过滤 | ≥500 genes | |
| lfc_clip | 3 | log fold change截断 |
| window_size | 250 | 滑动窗口大小 |
| 排除染色体 | chrX, chrY | 性别染色体 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| inferCNV | 拷贝数变异推断工具 |
| CNV | Copy Number Variation，拷贝数变异 |
| lfc_clip | log fold change截断值 |

## 复现
- inferCNVpy: https://github.com/icbi-lab/infercnvpy
- Trinity CTAT Project: https://github.com/broadinstitute/inferCNV

## 生物学意义
CNV分析可以区分恶性肿瘤和正常细胞，在肿瘤微环境中识别克隆进化和区域异质性。

## 涉及 Figures
- Fig. 4I, 4J (CNV analysis of TNBC sample)
