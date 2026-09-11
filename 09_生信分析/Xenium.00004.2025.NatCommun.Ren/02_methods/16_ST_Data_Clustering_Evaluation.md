# Method: Evaluation of Clustering of ST Data Based on Transcriptomic Profiles

## 原文（Methods）
> Genes detected in fewer than 100 bins or cells were filtered out. Bin-level data demonstrated lower quality than cell-level data due to the retention of non-cellular regions that would be excluded after cell segmentation. To address this, we applied a more stringent cutoff to filter out the low-quality bins. For Visium HD FFPE, bins with total counts below the 20th percentile of all bins were excluded. For cell-level data from Stereo-seq v1.3, CosMx 6K, and Xenium 5K, we filtered out low-quality cells with total counts below the 10th percentile of all cells. We further utilized the Python package scanpy (v.1.10.3) to perform clustering. Data were normalized and log-transformed to the same scale. The top 10% of genes with the highest variance were defined as highly variable genes. The top 30 principal components were computed to build neighborhood graphs. Data were embedded using Uniform Manifold Approximation and Projection (UMAP) for further dimensionality reduction and visualization. Clustering was performed using the Leiden algorithm with default resolution settings. The silhouette_score function from the Python package scikit-learn was used to assess the clustering quality. This score evaluates cluster separation by comparing intra-cluster and inter-cluster distances, with a value approaching 1 indicating better-defined clusters.

## 解读

### 意义
通过无监督聚类评估各ST平台解析细胞异质性的能力。使用轮廓宽度（silhouette score）量化聚类质量，比较scRNA-seq与各ST平台在区分不同细胞状态方面的表现。

### 输入
- 各ST平台过滤后的表达矩阵
- 质控后的bin-level (Visium HD FFPE)或cell-level数据

### 输出
- UMAP降维可视化
- Leiden算法聚类结果
- 轮廓宽度评分（聚类质量指标）

### 核心步骤
1. 过滤：在<100个bins/cells中检测到的基因被排除
2. 质控过滤：
   - Visium HD FFPE：排除总计数<第20百分位的bins
   - Stereo-seq v1.3, CosMx 6K, Xenium 5K：排除总计数<第10百分位的cells
3. 使用scanpy (v.1.10.3)进行聚类：
   - 标准化和log转换
   - 定义高变基因（top 10%方差最高）
   - 计算前30个PC构建邻域图
   - UMAP降维
   - Leiden算法聚类（默认分辨率）
4. 使用scikit-learn的silhouette_score评估聚类质量

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因过滤 | 检测bins/cells < 100 | 排除稀有基因 |
| Visium HD FFPE质控 | <第20百分位排除 | bin-level |
| 细胞水平质控 | <第10百分位排除 | Stereo-seq/CosMx/Xenium |
| 高变基因 | 方差top 10% |  |
| PC数 | 30 |  |
| 降维 | UMAP |  |
| 聚类算法 | Leiden | 默认分辨率 |
| 评估指标 | Silhouette score | 越接近1越好 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Silhouette score | 轮廓宽度，评估聚类分离度，范围[-1, 1] |
| Leiden算法 | 社区检测/聚类算法，比Louvain更高效 |
| UMAP | Uniform Manifold Approximation and Projection，统一流形近似与投影 |
| 高变基因 (HVG) | 在细胞间高度变异的基因 |

## 复现
- scanpy: v.1.10.3 (Python)
- scikit-learn: silhouette_score函数
- Leiden: scanpy默认实现

## 生物学意义
研究发现scRNA-seq提供最有效的细胞群体分离。在ST平台中，iST技术（CosMx 6K, Xenium 5K）因更高的空间分辨率而在解析细胞转录组差异方面表现更好，突显了高分辨率对细胞异质性研究的优势。

## 涉及 Figures
- **Fig. 5a, b** — UMAP和轮廓宽度比较
