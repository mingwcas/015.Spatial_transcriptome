# Method: Seurat v4.3.0 (Clustering Analysis)

## 原文（Methods）
> Low-quality spots with total counts below 30% of the first quantile of total counts are filtered out before normalization, which was carried out using the median number of total counts from each platform as the scaling factor. Subsequently, the top 2,000 highly variable genes were identified using the FindVariableFeatures function and used to scale the data through the ScaleData function. A total of 20 principal components (PCs) were then calculated using RunPCA. To categorize spots in each eye sample, we employed 3 distinct methods, including Seurat (v4.3.0), DR.SC (v3.3), and PRECAST (v1.6.2). Seurat initially identified neighbors based on 20 PCs, with a k-value of 5 chosen for the k-nearest neighbor algorithm in FindNeighbors. FindClusters was subsequently applied with various physical resolutions to group known cell-type spots.

## 解读

### 意义
Seurat是用于单细胞和空间转录组数据整合分析的主流工具，本研究使用其进行聚类分析和细胞类型注释。

### 输入
- scPipe处理后的spot-by-gene计数矩阵
- 空间坐标信息

### 输出
- 细胞类型注释结果
- 聚类标签
- 差异表达基因列表

### 核心步骤
1. 过滤低质量spots（total counts < 30% of first quantile）
2. 标准化（median scaling）
3. 鉴定2,000个高变基因
4. 缩放数据（ScaleData）
5. PCA降维（20 PCs）
6. KNN聚类（k=5）
7. 聚类分析（FindClusters）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Seurat version | v4.3.0 | 分析工具版本 |
| k-value | 5 | KNN算法中最近邻数量 |
| PCs | 20 | PCA降维主成分数 |
| HVG | 2,000 | 高变基因数量 |
| filter threshold | 30% of first quantile | 低质量spots过滤阈值 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| PCA | 主成分分析，用于降维 |
| KNN | K近邻算法 |
| HVG | Highly Variable Genes，高变基因 |
| ECA | Entropy of Clustering Accuracy，聚类准确性熵 |
| ECP | Entropy of Clustering Purity，聚类纯度熵 |

## 复现
- 工具/代码/URL：Seurat v4.3.0 (https://satijalab.org/seurat/)
- 代码：
```r
data <- NormalizeData(data)
data <- FindVariableFeatures(data, nfeatures = 2000)
data <- ScaleData(data)
data <- RunPCA(data, npcs = 20)
data <- FindNeighbors(data, k.param = 5, dims = 1:20)
data <- FindClusters(data, resolution = 0.8)
```

## 生物学意义
Seurat在三种聚类方法中表现最稳定和鲁棒，能可靠地识别预期的细胞亚群。尽管空间感知方法（DR.SC、PRECAST）在某些数据集上表现良好，但并不总是优于仅依赖基因表达的方法。

## 涉及 Figures
- **Fig. 4** — 下游性能比较：聚类结果和细胞注释
- **Supplementary Figure 12-13** — 聚类方法比较
