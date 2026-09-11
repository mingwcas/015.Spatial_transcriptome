# Method: Annotation of scRNA-seq Data

## 原文（Methods）
> Genes detected in fewer than 10 cells were excluded from the analysis. Cells that did not fulfill the following criteria were removed: 1,000 ≤UMI ≤25,000, 500 ≤Gene ≤5,000, and percentage of mitochondrial genes ≤10%. Putative doublets were identified and removed using DoubletFinder (v.2.0.3). A two-round clustering strategy was applied for cell type annotation using Seurat (v.5.1.0). In the first round of clustering, the data were normalized and log-transformed to the same scale. A set of 2000 highly variable genes was identified, followed by scaling of the expression matrix. The top 30 principal components (PCs) were identified to build a nearest-neighbor graph. Clustering was performed using the shared nearest neighbor (SNN) modularity optimization algorithm. We annotated each cluster based on its expression of the following known markers: B cell, CD79A, CD19, and MS4A1; cDC1, XCR1 and CLEC9A; cDC2, CD1C and CLEC10A; mregDC, LAMP3 and CCR7; pDC, LILRA4; macrophage, CD68, C1QC, and SPP1; mast cell, KIT and TPSAB1; monocyte, FCN1; neutrophil, CSF3R and AQP9; endothelial, VWF, CD34, CDH5, and PECAM1; fibroblast, ACTA2, COL1A2, and FAP; SMC, ACTA2 and RGS5; NK cell, FCGR3A, GZMA, and NCAM1; plasma cell, SDC1 and MZB1; CD4+ T cell, CD4, CD3G, CD3D, and CD3E; CD8+ T cell, CD8A, CD8B, CD3G, CD3D, and CD3E; Tprolif, MKI67, CD3G, CD3D, and CD3E; epithelial, EPCAM; hepatocyte, ALB; kupffer cell, CD5L. The subtypes of T cells were annotated after a second round of clustering using a similar approach.

## 解读

### 意义
scRNA-seq数据注释为各ST平台提供可靠的细胞类型参考标签。通过两轮聚类和已知标记基因注释，构建跨平台的细胞类型基准真相，用于评估ST平台的细胞注释准确性。

### 输入
- cellranger v.7.0.0处理的scRNA-seq表达矩阵

### 输出
- 质控后的单细胞表达矩阵
- 细胞类型注释标签（B cell, T cell, epithelial, fibroblast等）
- T细胞亚型注释

### 核心步骤
1. 过滤：排除在<10个细胞中检测到的基因
2. 质控：移除不满足以下条件的细胞：UMI<1,000或>25,000、基因数<500或>5,000、线粒体基因比例>10%
3. DoubletFinder (v.2.0.3)鉴定并移除双细胞
4. 第一轮聚类（Seurat v.5.1.0）：
   - 标准化和log转换
   - 识别2000个高变基因
   - 表达矩阵scale
   - 取前30个PC构建最近邻图
   - SNN模块度优化算法聚类
5. 基于已知标记基因注释各cluster
6. 第二轮聚类：T细胞亚型细分，使用类似方法

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因过滤 | 检测细胞数 < 10 | 排除稀有基因 |
| UMI范围 | 1,000–25,000 |  |
| 基因数范围 | 500–5,000 |  |
| 线粒体基因比例 | ≤10% |  |
| 高变基因数 | 2,000 |  |
| PC数 | 30 |  |
| 聚类算法 | SNN模块度优化 | Leiden算法 |
| 双细胞检测 | DoubletFinder v.2.0.3 |  |
| 分析工具 | Seurat v.5.1.0 |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| UMI | Unique Molecular Identifier，原始分子标签计数 |
| SNN | Shared Nearest Neighbor，共享最近邻 |
| PC | Principal Component，主成分 |
| DoubletFinder | 双细胞检测算法 |
| 高变基因 (HVG) | 在细胞间表达差异较大的基因 |

## 复现
- Seurat: v.5.1.0 (R)
- DoubletFinder: v.2.0.3 (R)
- 标记基因列表见原文

## 生物学意义
scRNA-seq注释提供了本研究所有细胞类型注释的ground truth参考。从matched肿瘤样本生成的注释被转移到各ST数据集，用于评估各平台的细胞类型识别准确性。研究发现scRNA-seq在各平台中始终表现出最高的每细胞转录本/基因检测数。

## 涉及 Figures
- **Fig. 4** — 各平台每细胞转录本/基因数与scRNA-seq比较
- **Supplementary Fig. 8** — 细胞类型标记基因表达
