# Method: Dimensionality Reduction and Clustering

## 原文（Methods）
> For the integrated CosMx SMI dataset, highly variable genes were identified using the FindVariableFeatures function in Seurat (v5.1.0). Principal component analysis (PCA) was performed using all 1,000 profiled genes. The top 50 principal components, which captured the majority of biological variance, were used for downstream analysis. A shared nearest neighbor graph was constructed using FindNeighbors, and unsupervised graph-based clustering was performed with FindClusters at a resolution of 0.8. For visualization, Uniform Manifold Approximation and Projection (UMAP) was applied to the Harmony-corrected principal components (dims = 1:20) using the RunUMAP function (umap.method = 'uwot'). This clustering process was repeated iteratively on subsets of cells to define finer subpopulations.

## 解读

### 意义
通过无监督聚类分析将CosMx数据中的细胞按照转录组相似性分组，识别不同的细胞类型和亚群，是单细胞数据分析的核心步骤。

### 输入
- Harmony校正后的表达矩阵（50个PCs）
- 全部1,000个基因的表达数据

### 输出
- 细胞聚类结果（cluster IDs）
- UMAP降维可视化坐标
- 每个聚类的差异表达基因列表

### 核心步骤
1. 使用FindVariableFeatures识别高变基因
2. 对所有1,000基因进行PCA
3. 取top 50 PCs用于下游分析
4. 构建共享最近邻图（FindNeighbors）
5. 图聚类（FindClusters, resolution=0.8）
6. Harmony校正后的PCs进行UMAP可视化（dims 1:20, umap.method='uwot'）
7. 对细胞子集迭代聚类以定义更细的亚群

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| FindVariableFeatures | Seurat默认参数 | 识别高变基因 |
| PCA基因数 | 1,000 | 全部探针基因 |
| 用于下游的PCs | top 50 | 捕获大部分生物学变异 |
| 聚类分辨率 | 0.8 | 图聚类分辨率 |
| UMAP dims | 1:20 | Harmony校正后PCs |
| UMAP method | 'uwot' | UMAP算法实现 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| PCA | Principal Component Analysis，主成分分析 |
| UMAP | Uniform Manifold Approximation and Projection，非线性降维方法 |
| PCs | Principal Components，主成分 |
| Harmony | 批次效应校正工具 |

## 复现
- 工具/代码/URL：
  - Seurat v5.1.0: https://cran.r-project.org/web/packages/Seurat/index.html
  - Harmony v1.0: https://cran.r-project.org/web/packages/harmony/index.html
- 代码片段：
```r
# Dimensionality reduction and clustering
pbmc <- FindVariableFeatures(pbmc)
pbmc <- RunPCA(pbmc, npcs = 50)
pbmc <- RunHarmony(pbmc, group.by.vars = "sample", dims.use = 1:50)
pbmc <- FindNeighbors(pbmc, dims = 1:50)
pbmc <- FindClusters(pbmc, resolution = 0.8)
pbmc <- RunUMAP(pbmc, dims = 1:20, umap.method = 'uwot')
```

## 生物学意义
该分析流程将604,230个单细胞分成不同的转录组学群组，首次在单细胞分辨率下系统性地描绘了SCLC原发肿瘤和淋巴结转移的肿瘤微环境细胞组成。聚类结果后续用于细胞类型注释，识别出13个恶性细胞亚群和多种免疫细胞亚型。

## 涉及 Figures
- **Fig. 1B, 1C** — 全局细胞组成的UMAP可视化
- **Fig. 2A** — 353,268个恶性细胞的13个亚群UMAP
- **Fig. 3A, 3B** — T细胞和B细胞亚群的UMAP
