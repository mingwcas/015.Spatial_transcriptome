# Method: Cellular Neighborhood (CN) Identification

## 原文（Methods）
> The local microenvironment for each cell was characterized by the cell-type composition of its 10 nearest neighbors. All of these local composition vectors were then aggregated and clustered using the MiniBatchKMeans function in the 'ClusterR' package (v1.3.3), with the batch_size parameter set to 100 and the initializer parameter set to 'kmeans++'. The optimal number of clusters (k) was determined by evaluating the average silhouette score across a range of k values and selecting the k that maximized this metric. The resulting clusters were defined as distinct CNs. To characterize each CN, we calculated the enrichment of specific cell types within it relative to their global abundance, using normalized odds ratios (OR). Statistical significance of enrichment was assessed via a two-sided Fisher's exact test, with p-values adjusted for multiple testing using the false discovery rate (FDR) method. An adjusted p-value of less than 0.05 was considered significant.

## 解读

### 意义
Cellular neighborhood (CN)分析通过定义每个细胞周围10个最近邻的细胞类型组成，将组织划分为不同的空间微环境结构，揭示多细胞空间组织模式的生物学意义。

### 输入
- 细胞空间坐标（x, y）
- 细胞类型注释
- ClusterR包 (v1.3.3)

### 输出
- 每个细胞的CN归属
- CN数量（PT: 11, PT-LNM: 13, LNMT: 15）
- 每种CN的细胞类型富集情况（odds ratios）
- 6种主要空间结构：肿瘤compartment、exhausted niche、PIHs-1、PIHs-2、B cell-enriched niche、vascular niche

### 核心步骤
1. 对每个细胞识别其10个最近邻
2. 计算每个细胞的局部细胞类型组成向量
3. MiniBatchKMeans聚类所有组成向量
4. 通过silhouette score确定最优k值
5. 计算每种CN内各细胞类型的富集odds ratio
6. Fisher精确检验显著性，FDR校正

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 最近邻数量 | 10 | 局部微环境定义 |
| 聚类方法 | MiniBatchKMeans | 大规模数据高效聚类 |
| ClusterR版本 | v1.3.3 | 聚类工具 |
| batch_size | 100 | 批处理大小 |
| initializer | 'kmeans++' | 初始化方法 |
| 显著性阈值 | FDR < 0.05 | 多重检验校正 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CN | Cellular neighborhood，细胞邻里 |
| Odds ratio (OR) | 优势比，用于量化富集程度 |
| Silhouette score | 聚类质量评估指标 |
| MiniBatchKMeans | 迷你批处理K均值聚类算法 |

## 复现
- 工具/代码/URL：ClusterR: https://cran.r-project.org/web/packages/ClusterR/index.html
- 代码片段：
```r
library(ClusterR)
# Determine optimal k using silhouette score
silhouette_scores <- c()
for(k in 2:20){
  km <- MiniBatchKMeans( compositions, clusters = k,
                         batch_size = 100,
                         initializer = 'kmeans++')
  sil <- mean(silhouette(km$clusters))
  silhouette_scores <- c(silhouette_scores, sil)
}
optimal_k <- which.max(silhouette_scores) + 1
```

## 生物学意义
CN分析揭示了SCLC淋巴结转移过程中空间组织结构的动态变化。PIHs-1在PT中最高，LNMT中最低，与良好预后相关；而exhausted niche在PT-LNM中富集。该分析表明空间架构而非单纯的细胞组成决定临床预后。

## 涉及 Figures
- **Fig. 5A, 5B, 5C** — CN identification and distribution
- **Fig. S11** — CN与空间热点验证
