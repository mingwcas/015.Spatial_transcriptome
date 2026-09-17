# Method: Data Analysis with Single-Cell RNA-seq Analysis Workflow

## 原文（Methods）
> The data analysis of E10-E12 tissue sections was carried out with Seurat V3.2 (Butler et al., 2018; Stuart et al., 2019) following standard procedures. In short, data normalization, transformation, and selection of variable genes were performed using the SCTransform function with default settings. Principal component analysis (PCA) was performed on the top 3,000 variable genes using the RunPCA function, and the first 30 principal components were used for Shared Nearest Neighbor (SNN) graph construction using the FindNeighbors function. Clusters were then identified using the FindClusters function. We used Uniform Manifold Approximation and Projection (UMAP) to visualize DBiT-seq data in a reduced two-dimensional space (McInnes et al., 2018). To identify differentially expressed genes for every cluster, pairwise comparisons of cells in individual clusters against all remaining cells were performed using the FindAllMarkers function (settings: min.pct = 0.25, logfc.threshold = 0.25). Expression heatmap was then generated using top 10 differentially expressed genes in each cluster.

## 解读

### 意义
该方法将标准的scRNA-seq分析流程应用于DBiT-seq空间转录组数据，实现聚类、降维和差异表达分析。

### 输入
- SCTransform标准化后的DBiT-seq数据
- Seurat V3.2

### 输出
- PCA降维结果（top 3000 variable genes, top 30 PCs）
- SNN图
- 聚类结果
- UMAP可视化
- 差异表达基因列表
- 表达热图

### 核心步骤
1. SCTransform标准化（默认参数）
2. 选择top 3000 variable genes
3. RunPCA执行PCA降维
4. 使用前30个PCs构建SNN图（FindNeighbors）
5. FindClusters识别clusters
6. UMAP降维可视化
7. FindAllMarkers找差异表达基因（min.pct=0.25, logfc.threshold=0.25）
8. 每个cluster top 10差异基因绘制热图

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 变量基因数 | Top 3000 | 降维输入 |
| PCA主成分数 | 30 | SNN图构建 |
| 差异表达阈值 | min.pct=0.25, logfc.threshold=0.25 | 显著性标准 |
| 热图基因数 | Top 10/cluster | 展示用 |
| 可视化方法 | UMAP | 优于tSNE的全局结构保持 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| PCA | Principal Component Analysis，主成分分析，线性降维 |
| SNN graph | Shared Nearest Neighbor graph，共享最近邻图 |
| UMAP | Uniform Manifold Approximation and Projection，比tSNE更好的全局结构保持 |
| FindAllMarkers | Seurat中差异表达分析函数 |

## 复现
- 工具/代码/URL：Seurat V3.2 (https://satijalab.org/seurat/)
- 代码：https://github.com/rongfan8/DBiT-seq
- 关键调用：NA

## 生物学意义
Seurat是scRNA-seq数据分析的标准工具，将其应用于DBiT-seq数据证明了空间转录组与单细胞技术的兼容性。UMAP可视化比tSNE更好地保留了全局结构，对于理解组织内不同区域的关系很重要。前30个PCs的选择平衡了信息保留和噪声过滤。

## 涉及 Figures
- **Fig. 2B** — UMAP与scRNA-seq数据对比
- **Fig. 4H** — scRNA-seq与DBiT-seq联合UMAP
- **Fig. 5A-D** — 11个胚胎样本的tSNE/UMAP分析
