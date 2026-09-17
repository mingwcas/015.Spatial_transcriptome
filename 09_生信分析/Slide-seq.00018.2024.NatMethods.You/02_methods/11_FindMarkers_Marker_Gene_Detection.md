# Method: FindMarkers (Marker Gene Detection)

## 原文（Methods）
> FindMarkers in Seurat was applied to find marker genes between two pairs of cell subsets: 1) lens and melanocytes; 2) pNR4 and pNR1. Genes that exhibited higher expression in the lens and pNR4, with expression levels exceeding 5% of the specific spots, the log-fold-change greater than 0.25, and an adjusted p-value provided by Seurat less than 0.01, were considered as marker genes.

## 解读

### 意义
FindMarkers是Seurat中的差异表达分析方法，用于识别不同细胞类型之间的标记基因。

### 输入
- 聚类后的Seurat对象
- 比较的细胞类型对

### 输出
- 差异表达基因列表
- 统计显著性指标

### 核心步骤
1. 选择待比较的细胞类型对
2. 执行Wilcoxon秩和检验
3. 应用过滤条件
4. 鉴定标记基因

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Test method | Wilcoxon rank-sum test | 统计检验方法 |
| Min. pct. | 0.05 (5%) | 基因表达的最小细胞比例 |
| Log-fold change | > 0.25 | 最小对数倍数变化 |
| Adjusted p-value | < 0.01 | 显著性阈值 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Marker genes | 标记基因，在特定细胞类型中特异表达的基因 |
| Log-fold change | 对数倍数变化 |
| Wilcoxon test | 秩和检验，非参数统计方法 |

## 复现
- 工具/代码/URL：Seurat包内置函数
```r
markers <- FindMarkers(seurat_obj, ident.1 = "cluster1", ident.2 = "cluster2",
                       min.pct = 0.05, logfc.threshold = 0.25, 
                       test.use = "wilcox", padj = 0.01)
```

## 生物学意义
不同平台在标记基因检测方面表现出平台特异性偏好，例如Pax6在不同平台的结果不一致，影响了对神经视网膜发育的解读。

## 涉及 Figures
- **Fig. 4f,g** — 标记基因检测比较
- **Supplementary Table 3** — 完整标记基因列表
