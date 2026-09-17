# Method: Single-Cell Transcriptomic Clustering and Cell Type Annotation

## 原文（Methods）
> For downstream analyses we used the package Seurat (v4.0.4) in R. For each section, we imported 3 matrices containing the gene expression, metadata and positions of segmented cells. We removed the negative probes from the gene expression matrix, deﬁned a unique cell name and created a merged Seurat object with data from all the sections. To identify cell types present in the TME, we adopted a very conservative ﬁltering strategy removing only cells with less than 10 detected genes and removing genes detected in less than 1 cell. We then computed SCT-normalized and scaled gene expression counts and computed the 50 most variable principal components (PCs). We selected the ﬁst 30 PCs to create a shared nearest neighbor graph and to compute a two-dimensional UMAP plot used for data visualization. Finally, we partitioned the shared nearest neighbor graph using a resolution of 0.8 and identiﬁed 24 transcriptomic clusters.

## 解读

### 意义
对CosMx分割后的单细胞基因表达数据进行无监督聚类和细胞类型注释，鉴定肿瘤微环境中18种上皮、基质和免疫细胞类型。

### 输入
- 6张切片的CosMx单细胞基因表达矩阵（960基因）
- 细胞元数据和空间位置信息

### 输出
- 340,644个细胞的聚类结果
- 18种细胞类型注释
- UMAP降维可视化

### 核心步骤
1. 导入6张切片的表达矩阵、元数据和位置矩阵
2. 移除阴性探针，合并为Seurat对象
3. 保守过滤：移除<10基因的细胞和<1细胞检出的基因
4. SCTransform归一化（Hafemeister & Satija, 2019）
5. 计算50个PC，选取前30个PC构建SNN图
6. UMAP降维（分辨率0.8），识别24个转录组聚类
7. 基于标记基因和IF验证注释为18种细胞类型
8. 合并相似聚类（如cluster 0&1→fibroblasts, 2&7→macrophages, 4/5/20/22/23→tumor cells）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 软件 | Seurat v4.0.4, R v4.1 | 单细胞分析框架 |
| 归一化方法 | SCTransform (SCT) | 基于正则化负二项回归的归一化 |
| PC数 | 50（选用前30） | 主成分分析维度 |
| 聚类分辨率 | 0.8 | SNN图聚类的分辨率参数 |
| 初始聚类数 | 24 | 合并前的转录组聚类数 |
| 最终细胞类型 | 18 | 合并后的细胞类型数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SCTransform | 基于正则化负二项回归的单细胞RNA-seq数据归一化和方差稳定方法 |
| SNN图 | 共享最近邻图（Shared Nearest Neighbor），用于聚类 |
| UMAP | 均匀流形近似与投影，用于高维数据降维可视化 |
| PC | 主成分（Principal Component） |
| panCK | 泛细胞角蛋白免疫荧光，用于验证上皮细胞注释 |

## 复现
- Seurat v4.0.4: Stuart et al., 2019 (Cell)
- SCTransform: Hafemeister & Satija, 2019 (Genome Biol)
- UMAP: McInnes et al., 2018 (JOSS)
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
保守的过滤策略和多标记基因验证确保了细胞类型注释的可靠性。18种细胞类型涵盖了TME的主要组成：肿瘤细胞、多种基质细胞（成纤维细胞、内皮细胞、周细胞、平滑肌）和免疫细胞（巨噬细胞、树突状细胞、T细胞等），为下游3D邻域分析和细胞间通讯研究奠定了基础。

## 涉及 Figures
- **Fig. 1C** — UMAP展示18种细胞类型
- **Fig. 1D** — 空间组织学与细胞类型对应
- **Fig. 1E** — 与参考scRNA-seq图谱的label transfer验证
- **Fig. S1E-G** — 聚类结果、标记基因和IF验证
