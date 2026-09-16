# Method: Seurat整合、聚类与细胞类型注释

## 原文（Methods）
> The filtered gene matrices from each sample were normalized using the NormalizeData function. To identify highly variable genes, we used FindVariableFeatures, which models the mean-variance relationship ... and identified 5,000 genes per sample. We further identified anchors using FindIntegrationAnchors ... dims = 20, k.filter = 30, anchor.features = 3000 and k.score = 30 ... For the major cell type and nucleus clustering, the first 20 principal components were used ... resolution = 0.2 ... and for nuclei the resolution = 0.3.

## 解读
### 意义
跨患者/样本校正批次并识别主要细胞类型与低维结构。
### 输入
质控后的scRNA/snRNA表达矩阵。
### 输出
整合表达矩阵、PCA/UMAP、21个初始簇及最终10个细胞和11个细胞核主类型簇。
### 核心步骤
1. NormalizeData；每样本FindVariableFeatures选5,000基因。
2. FindIntegrationAnchors识别锚点，IntegrateData整合患者。
3. ScaleData、RunPCA、ElbowPlot确定PC；FindNeighbors/FindClusters聚类；RunUMAP可视化。
4. 以质量指标、差异基因和canonical markers排除异常簇。
5. FindAllMarkers（Wilcoxon）结合SingleR和marker人工审核完成注释。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| integration dims | 20 | CCA锚点与整合维度 |
| k.filter/k.score | 30/30 | 锚点过滤与评分 |
| anchor.features | 3,000 | 整合特征数 |
| variable genes | 5,000/样本 | 高变基因 |
| clustering resolution | 0.2（细胞）；0.3（细胞核） | 主类型聚类 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| CCA | canonical correlation analysis，跨样本整合方法 |
| Anchor | Seurat用于匹配样本细胞状态的对应关系 |
| UMAP | 非线性降维可视化 |

## 复现
- Seurat v3.2.3；SingleR。
- 关键调用：`FindIntegrationAnchors(object.list, dims=1:20, k.filter=30, anchor.features=3000, k.score=30)`；`FindClusters(resolution=0.2)`。

## 生物学意义
整合使126位女性样本中的共享细胞谱系可比较；过度校正可能削弱真实患者差异。

## 涉及 Figures
- **Fig. 1c–f** — 主类型UMAP与marker热图。
- **Fig. 3b–c、4f–j、5b、6b/e/j** — 各谱系聚类。
