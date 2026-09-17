# Method: Spatial Clustering of Dendritically Enriched Genes

## 原文（Methods）
> For the 213 genes identified to be dendritically enriched, we clustered genes by their spatial profile along the CA1–neuropil axis via k-means clustering. The gap-statistic was used to determine the optimal number of clusters (k = 4).

## 解读

### 意义
Spatial clustering将具有相似dendritic localization模式的基因分组，揭示不同功能类别基因的空间分布特征。

### 输入
- 213 dendritically enriched genes
- 1D spatial expression profiles along CA1 neuropil axis
- Normalized expression values per gene

### 输出
- 4 spatial clusters of dendritic genes
- Cluster average expression profiles
- GO enrichment results per cluster

### 核心步骤
1. **Normalize profiles**: Each gene's spatial profile normalized to sum to 1
2. **K-means clustering**: k=4 (determined by gap-statistic)
3. **ClusterProfiler analysis**: GO cellular component enrichment
4. **Visualization**: Heatmap and average profile plots

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Clustering method | k-means | 标准方法 |
| Number of clusters | k=4 | Gap-statistic确定 |
| Normalization | Row sum to 1 | 标准化表达谱 |
| GO database | org.Mm.eg.db | Mouse genome annotation |
| P-value cutoff | q < 0.05 | FDR校正 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Gap-statistic | 估计最优cluster数目的统计量 |
| K-means clustering | 将数据划分为k个cluster的迭代算法 |
| GO cellular component | 基因本体论细胞组分分类 |
| ClusterProfiler | Yu et al.开发的GO分析R包 |

## 复现
- **工具**: R clusterProfiler package
- **URL**: http://bioconductor.org/packages/release/data/annotation/html/org.Mm.eg.db.html
- **代码**: 
```R
library(clusterProfiler)
library(org.Mm.eg.db)
go_results <- enrichGO(gene = cluster_genes, 
                       OrgDb = org.Mm.eg.db,
                       ont = "CC",
                       pvalueCutoff = 0.05)
```

## 生物学意义
不同cluster的基因富集于不同功能类别（线粒体、ribosome、ubiquitin ligases等），表明dendritic mRNA运输具有功能选择性，特定类别的蛋白质在突触区域需要局部合成。

## 涉及 Figures
- **Fig. 2d** — Expression heatmap of 237 genes across CA1
- **Fig. 2e** — Average spatial profile of 4 clusters
- **Supplementary Fig. 6b** — GO enrichment per cluster
