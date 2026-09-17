# Method: Identification of Spatially Auto-correlated Gene Modules

## 原文（Methods）
> Spatially auto-correlated gene modules were identified using Hotspot algorithm. The raw count matrix of all genes was used as the input. For the gene modules, a k-nearest neighbor (knn) graph of genes was created using the create_knn_graph function with the parameters: "n_neighbors = 30, weighted_graph=True". Genes with significant spatial autocorrelation (FDR < 0.01) were kept for building spatial gene modules. The modules were identified using a umi-adjusted negative binomial model via the create_modules function with the parameters: "min_gene_threshold = 20, core_only=False, fdr_threshold = 0.01". Genes classified in the same module with M. tb RNAs (Rvnr01, Rvnr02) were regarded as M. tb-correlated genes.

## 解读

### 意义
鉴定与Mtb感染区域空间共表达的基因模块，用于揭示感染相关的宿主基因表达变化。

### 输入
- 原始计数矩阵（所有基因）
- 空间坐标信息

### 输出
- 空间自相关基因模块
- Mtb相关基因列表

### 核心步骤
1. 输入原始计数矩阵
2. 使用Hotspot创建基因kNN图（n_neighbors=30）
3. FDR<0.01过滤显著空间自相关基因
4. 使用UMI调整的负二项模型构建模块
5. 鉴定与Mtb RNA共模块的基因

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| n_neighbors | 30 | kNN图构建 |
| weighted_graph | True | 加权图 |
| min_gene_threshold | 20 | 模块最小基因数 |
| fdr_threshold | 0.01 | 显著模块 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Hotspot | 空间自相关基因模块鉴定算法 |
| Spatial autocorrelation | 空间自相关 |
| knn | k-nearest neighbor |

## 复现
- Hotspot: https://github.com/willtownes/hotspot
- 使用UMI调整的负二项模型

## 生物学意义
空间自相关分析揭示了组织内基因表达的空间组织规律，对于理解感染和组织微环境至关重要。

## 涉及 Figures
- Fig. 6G, 6H (Mtb-associated gene modules)
