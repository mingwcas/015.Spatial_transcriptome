# Method: Clustering and Visualization

## 原文（Methods）
> The clusters of RNA and protein expression matrix was generated using Seurat version 3.2. The transcriptome data were normalized using the 'SCTransform' function. Normalized data were then clustered and UMAP was built with the dimensions set to 30, and cluster resolution was set to 0.5. Protein data were normalized using the centered log ratio (CLR) transformation method in Seurat version 3.2. All heat maps were plotted using ggplot2. Weighted nearest neighbor analysis were conducted using Seurat version 3.2 following default settings.

## 解读

### 意义
对空间蛋白质组和转录组数据进行无监督聚类和可视化，识别组织中的空间域。

### 输入
- 基因表达矩阵（空间位置 × 基因）
- 蛋白质表达矩阵（空间位置 × 蛋白质）

### 输出
- 蛋白质聚类结果和UMAP
- 转录组聚类结果和UMAP
- 差异表达蛋白/基因热图
- 空间聚类分布图

### 核心步骤
1. 转录组数据标准化：使用Seurat v3.2的SCTransform函数
2. 转录组聚类：UMAP维度=30，聚类分辨率=0.5
3. 蛋白质数据标准化：使用centered log ratio (CLR)变换
4. 蛋白质聚类：同样使用Seurat v3.2
5. 热图绘制：使用ggplot2
6. 加权最近邻分析：Seurat v3.2默认参数，整合RNA和蛋白质模态

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Seurat版本 | 3.2 | 单细胞分析R包 |
| 转录组标准化 | SCTransform | 基于负二项分布的标准化 |
| UMAP维度 | 30 | 降维使用的主成分数 |
| 聚类分辨率 | 0.5 | Louvain聚类分辨率参数 |
| 蛋白质标准化 | CLR | Centered Log Ratio变换 |
| 绘图工具 | ggplot2 | R绑图包 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SCTransform | Seurat的正则化负二项回归标准化方法 |
| CLR | Centered Log Ratio，居中对数比变换，用于组成数据标准化 |
| UMAP | Uniform Manifold Approximation and Projection，非线性降维 |
| Louvain | 基于图的社区检测聚类算法 |
| Weighted Nearest Neighbor (WNN) | Seurat的多模态数据整合方法 |

## 复现
- 工具/代码/URL
  - Seurat v3.2：https://satijalab.org/seurat/
  - ggplot2
- 代码片段：
```r
# 转录组聚类（概念性代码）
library(Seurat)
obj <- CreateSeuratObject(counts = gene_matrix)
obj <- SCTransform(obj)
obj <- RunPCA(obj)
obj <- FindNeighbors(obj, dims = 1:30)
obj <- FindClusters(obj, resolution = 0.5)
obj <- RunUMAP(obj, dims = 1:30)

# 蛋白质聚类
obj_protein <- CreateAssayObject(counts = protein_matrix)
obj_protein <- NormalizeData(obj_protein, normalization.method = "CLR")
```

## 生物学意义
蛋白质聚类和转录组聚类的比较是本文的核心发现之一。结果显示，基于273种蛋白质的无监督聚类能够清晰地分辨扁桃体中的生发中心明区/暗区、T细胞区、隐窝等解剖结构，且比转录组聚类更精确、噪声更少。这证明了高plex蛋白质组在组织空间域识别中的优越性。

## 涉及 Figures
- **Fig. 1e-h** — 人扁桃体蛋白质和转录组的UMAP聚类及空间分布
- **Fig. 1i** — 差异表达蛋白热图
- **Fig. 2c-f** — 皮肤活检的转录组和蛋白质聚类
- **Extended Data Fig. 7a** — 加权最近邻分析的模态权重
