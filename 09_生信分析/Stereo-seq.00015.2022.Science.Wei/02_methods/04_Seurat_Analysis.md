# Method: Seurat Analysis for Cell Type Annotation

## 原文（Methods）
> To dissect cell type composition, we next conducted unsupervised clustering analysis by Seurat based solely on gene expression. This analysis identified 16 cell clusters, which were further mapped to the section according to their spatial information. Referring to established cell marker genes, such as excitatory neuron marker Neurod6, inhibitory neuron marker Gad1, and EGC marker Gfap, we determined the identity of each cell cluster.

## 解读

### 意义
Seurat是单细胞RNA-seq数据分析的标准工具，通过无监督聚类识别细胞群，并结合已知标记基因进行细胞类型注释，实现细胞类型的系统鉴定。

### 输入
- 单细胞表达矩阵（UMI counts）
- 每个细胞的spatial坐标
- 已知细胞类型标记基因列表

### 输出
- 细胞聚类结果
- 细胞类型注释
- 每个聚类的marker genes
- 空间映射的细胞类型分布

### 核心步骤
1. 质量控制：过滤低质量细胞
2. SCTransform normalization：使用SCTransform进行标准化
3. 降维：PCA降维
4. 聚类：FindNeighbors + FindClusters进行无监督聚类
5. Marker基因鉴定：FindAllMarkers识别每个聚类的marker genes
6. 细胞类型注释：基于已知标记基因和marker genes确定细胞类型
7. 空间映射：将聚类结果映射回空间位置

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 成年蝾螈细胞簇数 | 16个 | unsupervised clustering结果 |
| 发育阶段细胞类型 | 33种 | 包括13种 immature/intermediate types |
| 再生阶段细胞类型 | 28种 | 包括8种发育阶段未发现的类型 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SCTransform | 单细胞转录组标准化方法 |
| PCA | Principal Component Analysis，主成分分析 |
| UMAP | Uniform Manifold Approximation and Projection |
| Marker genes | 细胞类型特异性基因 |
| EGC | Ependymoglial cell，室管膜胶质细胞 |

## 复现
- **工具/代码/URL**: 
  - Seurat: https://satijalab.org/seurat/
  - 参考文献: Hao et al., Cell 2021 (doi: 10.1016/j.cell.2021.04.048)
- **代码片段**:
```r
# Seurat standard workflow
obj <- SCTransform(obj, vars.to.regress = "percent.mt")
obj <- RunPCA(obj)
obj <- FindNeighbors(obj, dims = 1:30)
obj <- FindClusters(obj, resolution = 0.8)
obj <- RunUMAP(obj, dims = 1:30)
```

## 生物学意义
Seurat分析实现了蝾螈端脑细胞类型的系统鉴定，识别出包括兴奋性神经元、抑制性神经元、室管膜胶质细胞(EGC)等多种细胞类型。这些发现为理解脑发育和再生的细胞基础提供了全面的转录组视角。

## 涉及Figures
- **Fig. 1C-D** — 细胞类型注释和标记基因验证
- **Fig. 2A** — 发育阶段细胞类型聚类
- **Fig. 3B** — 再生阶段细胞类型分布
