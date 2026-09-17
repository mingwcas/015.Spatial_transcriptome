# Method: Downstream Analysis & Integration

## 原文（Methods）
> The 3′, 5′, and scFFPE-seq data were filtered with scanpy 1.19. Cell filtering parameters included largest gene fraction ≤0.2, mitochondrial fraction ≤0.15, and number of genes observed ≥500. We performed t-distributed stochastic neighbor embedding (t-SNE) on Chromium and Xenium data using the monet package v0.3.2. A principal component analysis (PCA) was performed on the feature-cell matrix, and the top 50 components were input to the t-SNE. We subsampled the whole transcriptome Chromium and Visium data to only the 313 genes used in the Xenium panel. The Xenium t-SNE coordinates were initialized with the scFFPE-seq cluster centers. The Visium t-SNE was generated in Loupe, and expression is either reported as log2(counts) when shown stand-alone, or as raw counts when comparing directly with Xenium transcript counts.

> We annotated the scFFPE-seq data by first conducting a differential gene expression (DGE) analysis across unsupervised clusters in Loupe. Annotations were built upon this DGE analysis, and literature review, and pre-CytAssist H&E staining. We assigned labels DCIS #1 and DCIS #2 according to transcriptional similarity between the scFFPE-seq and Visium platforms. We performed a log-normalization step of the data, and then calculated a z-score across cells. A PCA was performed and the top 50 PCs were selected. From the in situ data, we determined the 30 nearest neighbors for each cell after normalization and projection into PC space, and if at least 50% were one cell type, then that is the cell type that was assigned. If that criteria was not met, then the cell was classified as "unlabeled".

> For Sample #2 (Fig. 6 and Supp. Fig. 13), we used the Seurat vignette as guide to load and analyze the Xenium data with the development branch of Seurat 5. We identified 14 clusters (resolution = 0.3), and further subclustered the epithelial and macrophage clusters to increase resolution of the cell types within. Annotations were aided by single cell atlas data. Cropped FOV images with segmentation were generated with the ImageFeaturePlot function, and a custom ggplot2 script was used to plot individual transcripts on top of the segmented cells.

> Cell Ranger, Space Ranger, and Loupe Browser test, for each gene and each cluster, whether the in-cluster mean differs from the out-of-cluster mean using one of two methods. When gene counts are small, the quick and simple method, a version of the negative binomial exact test was used. For larger counts, a modified version of the fast asymptotic beta test was used. For the differential gene expression analysis shown in Fig. 6, we created a heatmap in Seurat v4.3 and obtained variable features using the vst selection method. These features were used to define a gene expression profile for tumor, myoepithelial, and rare boundary cells. We then used the Filter function in Loupe Browser v6.4.1 to threshold marker genes and assign identities (tumor, myoepithelial, and boundary) to barcodes in the scFFPE-seq data. We then performed a locally distinguishing feature comparison to find novel differentially expressed genes in the rare boundary cells. We visualized these genes using VlnPlot in Seurat v4.3.

> Using spot interpolation (see Supp. Fig. 10), we derived information about the cell composition of the triple positive region (ERBB2+/ESR1+/PGR+). Using Loupe Browser v6.4.1, we lassoed around the spots within the triple positive domain that were predominantly composed of the DCIS cell type. We then conducted a global differential gene expression analysis to derive genes featured in Fig. 5j. For the gene ontology analysis, we used Loupe to lasso around PGR− DCIS #1 and PGR− DCIS #2 cells, and compared them to the triple positive region (PGR+). We then took the differentially expressed genes and inputted them into Enrichr to obtain the ontology information shown in Supplemental Fig. 11.

> We drew a region of interest (ROI), a polygon around morphological features (individual cells, groups of cells, etc.) and performed DGE across these ROIs with scanpy v1.19. ROI selection was performed in the Xenium Explorer software (development version, 10x Genomics), and significance was assessed with the Wilcoxon test on log-normalized count data. The DGE was performed for each cell type across ROIs.

> The Xenium assay's sensitivity is unique for each gene. Therefore, we designed probes to estimate the effective sensitivity of the assay for each gene, and we describe the effective sensitivity as an average or median gene sensitivity. Because mean sensitivity is biased by high expressors, we calculated median gene sensitivity by first computing the sensitivity of each gene separately (the mean of the counts per cell), then calculating the median across all genes. Because sensitivity is dependent on sequencing saturation, the 3′ and 5′ GEX data were downsampled to 10,000 mean reads per cell to match the sequencing depth of 10,000 reads per cell (the recommended depth) for scFFPE-seq, and 20,000 mean reads per cell (the recommended sequencing depth for the 3′ and 5′ assays). The 3′ and 5′ GEX data were also downsampled to only the genes on the RTL scFFPE-seq probe set.

> For registration of IF images to the Xenium morphology images, which are both DAPI images, we used a SIFT registration with the cv2 4.5.4 package in python v3.9.7, which produces the transformation between IF and Xenium. For registration of Visium to Xenium data, serial sections were rotated 2.58 degrees relative to each other, then a manual-defined keypoint registration between the corresponding H&E images (serial sections) was used. Over 100 landmark features were identified on commonly shared microstructures. Using RANSAC, we determined the subset of coordinates that matched, and performed the transformation between coordinates with the FindHomography() function in the cv2 package.

> Using the registration of Xenium to Visium, we binned cells (by centroid) and transcripts from Xenium into the Visium spots. This was done by proximity. The closest spot to a cell or transcript was identified as the spot a cell or transcript lies within. Robust Cell Type Decomposition (RCTD) with spacexr 2.0.1 in R was used to deconvolve Visium spots into cell types using the unsupervised scFFPE-seq reference.

## 解读

### 意义
整合三种技术平台的数据，实现细胞类型注释、差异基因表达分析、空间反卷积和跨平台图像配准，从多个维度揭示肿瘤微环境的分子和空间异质性

### 输入
- scFFPE-seq基因-细胞矩阵
- Visium空间基因表达数据
- Xenium转录本列表和细胞边界
- H&E和IF图像

### 输出
- 标注的细胞类型（监督和非监督）
- 差异表达基因列表
- 基因本体富集分析结果
- 空间注册的多平台叠加数据
- Spot反卷积的细胞类型比例

### 核心步骤

#### Chromium & Visium Post-processing
1. 使用scanpy 1.19过滤细胞：最大基因比例≤0.2，线粒体比例≤0.15，检测基因数≥500
2. 使用monet v0.3.2进行PCA（前50个主成分）+ t-SNE降维
3. 将全转录组Chromium和Visium数据下采样至Xenium面板的313个基因
4. Xenium t-SNE坐标以scFFPE-seq聚类中心初始化
5. Visium t-SNE在Loupe中生成

#### Supervised Labeling & Label Transfer
6. 在Loupe中对scFFPE-seq无监督聚类进行DGE分析
7. 基于DGE、文献综述和H&E染色注释细胞类型
8. 根据scFFPE-seq与Visium的转录相似性分配DCIS #1和DCIS #2标签
9. 对数据进行log归一化和z-score计算
10. PCA取前50个PC
11. 在PC空间中确定每个细胞的30个最近邻
12. 若≥50%的最近邻为同一细胞类型，则分配该标签；否则标记为"unlabeled"

#### Unsupervised Labeling and Subclustering
13. 使用Seurat 5开发分支加载和分析Xenium数据（Sample #2）
14. 识别14个聚类（resolution = 0.3）
15. 对上皮和巨噬细胞聚类进行亚聚类以提高分辨率
16. 使用ImageFeaturePlot生成分割FOV图像
17. 使用自定义ggplot2脚本绘制分割细胞上的单个转录本

#### Chromium and Visium DGE
18. Cell Ranger/Space Ranger/Loupe Browser使用两种方法进行DGE：负二项精确检验（小计数）或快速渐近beta检验（大计数）
19. Seurat v4.3创建热图，使用vst方法获取高变特征
20. Loupe Browser v6.4.1 Filter功能阈值标记基因并分配细胞身份
21. 进行局部区分特征比较以发现罕见边界细胞的差异表达基因

#### Gene Ontology Analysis
22. 使用Spot interpolation确定三阳性区域的细胞组成
23. Loupe Browser中lasso选择三阳性区域的DCIS spots
24. 进行全局DGE分析
25. 将差异表达基因输入Enrichr获取基因本体信息（BioPlanet和Reactome数据库）

#### Xenium DGE
26. 在Xenium Explorer中绘制ROI（多边形）
27. 使用scanpy v1.19对log归一化计数数据进行Wilcoxon检验
28. 对每个细胞类型跨ROI进行DGE

#### Benchmarking Sensitivity
29. 计算每个基因的灵敏度（每细胞计数均值）
30. 计算所有基因的中位基因灵敏度（避免高表达基因偏差）
31. 将3′/5′ GEX数据下采样至10,000 reads/cell匹配scFFPE-seq深度
32. 将3′/5′ GEX数据下采样至RTL探针集基因

#### Image Registration
33. IF到Xenium：使用SIFT配准（cv2 4.5.4，Python v3.9.7），基于DAPI图像
34. Visium到Xenium：旋转校正2.58°，手动关键点配准（>100个地标），RANSAC + FindHomography()

#### Spot Interpolation/Deconvolution
35. 将Xenium细胞（按质心）和转录本按最近邻原则分配到Visium spots
36. 使用RCTD（spacexr 2.0.1，R）以scFFPE-seq为参考对Visium spots进行细胞类型反卷积

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 细胞过滤：最大基因比例 | ≤0.2 | 排除双细胞或低质量细胞 |
| 细胞过滤：线粒体比例 | ≤0.15 | 排除死细胞或损伤细胞 |
| 细胞过滤：最小基因数 | ≥500 | 排除低质量细胞 |
| PCA主成分数 | 50 | 降维输入维度 |
| t-SNE工具 | monet v0.3.2 | PCA-based t-SNE |
| 最近邻数（label transfer） | 30 | 用于监督标记的KNN |
| 标记分配阈值 | ≥50%最近邻为同一类型 | 超过阈值分配标签，否则"unlabeled" |
| Seurat聚类分辨率 | 0.3 | 控制聚类粒度 |
| DGE方法（小计数） | 负二项精确检验 | 小基因计数的差异检验 |
| DGE方法（大计数） | 快速渐近beta检验（edgeR衍生） | 大基因计数的差异检验 |
| Visium-Xenium旋转校正 | 2.58° | 连续切片间的旋转差异 |
| RANSAC配准地标数 | >100 | 手动标注的共同微结构特征 |
| RCTD工具 | spacexr 2.0.1 (R) | 空间转录组细胞类型反卷积 |
| 变异特征选择方法 | vst（Seurat） | 方差稳定变换选择高变基因 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| t-SNE | t-分布随机邻域嵌入，一种非线性降维可视化方法 |
| PCA | 主成分分析，线性降维方法 |
| DGE | 差异基因表达分析（Differential Gene Expression） |
| 监督标记（supervised labeling） | 利用已知参考数据（scFFPE-seq）指导细胞类型注释 |
| 非监督标记（unsupervised labeling） | 不依赖参考数据，基于数据内在结构的聚类和注释 |
| spot interpolation | 将Xenium转录本和细胞按最近邻原则分配到Visium spots的方法 |
| RCTD | Robust Cell Type Decomposition，空间转录组细胞类型反卷积算法 |
| SIFT | Scale-Invariant Feature Transform，尺度不变特征变换，用于图像配准 |
| RANSAC | Random Sample Consensus，随机抽样一致性算法，用于鲁棒图像配准 |
| Enrichr | 在线基因本体富集分析工具 |
| BioPlanet/Reactome | 通路和基因本体数据库 |
| vst | variance stabilizing transformation，方差稳定变换，用于高变基因选择 |

## 复现
- 工具/代码/URL：
  - scanpy v1.19：`pip install scanpy`
  - monet v0.3.2：PCA-based t-SNE
  - Seurat v5（开发分支）：`https://github.com/satijalab/seurat/tree/develop`
  - Loupe Browser v6.4.1：10x Genomics商业软件
  - Xenium Explorer（开发版本）：10x Genomics
  - spacexr v2.0.1：`install.packages("spacexr")`
  - Enrichr：`https://maayanlab.cloud/Enrichr/`
  - cv2 v4.5.4：`pip install opencv-python`
  - Spot interpolation代码：`https://github.com/10XGenomics/janesick_nature_comms_2023_companion`
- 代码片段：
```python
# scanpy细胞过滤
import scanpy as sc
adata = sc.read_h5ad("input.h5ad")
sc.pp.filter_cells(adata, min_genes=500)
adata = adata[adata.obs.pct_counts_mt <= 15]
adata = adata[adata.obs.gene_frac <= 0.2]

# Xenium DGE (scanpy)
sc.tl.rank_genes_groups(adata, groupby='roi', method='wilcoxon')
```

```r
# RCTD反卷积
library(spacexr)
reference <- Reference(counts_ref, cell_types_ref)
query <- SpatialRNA(coords, counts_spatial)
RCTD <- create.RCTD(query, reference, max_cores=4)
RCTD <- run.RCTD(RCTD, doublet_mode="doublet")
```

## 生物学意义
下游分析与整合是本研究将三种互补技术转化为生物学发现的核心环节。通过监督和非监督标记的互补使用，作者既利用了scFFPE-seq的全转录组信息进行精确注释，又通过非监督方法发现了监督方法未能识别的细胞亚群。Spot interpolation方法巧妙地将Xenium的单细胞分辨率空间信息与Visium的全转录组信息结合，使得三阳性受体区域（仅5-6个Visium spots）的全转录组DGE成为可能。跨平台图像配准确保了不同技术检测结果的空间对齐，是数据整合的基础。该整合分析范式展示了多技术联合分析在揭示肿瘤异质性方面的独特优势——任何单一技术都无法独立完成这些发现。

## 涉及 Figures
- **Fig. 2** — scFFPE-seq和Visium的聚类与注释
- **Fig. 3j, j′, k** — Xenium监督和非监督标记的比较
- **Fig. 4b, d** — ROI选择和跨区域DGE
- **Fig. 5i, j** — Spot interpolation和三阳性区域DGE
- **Fig. 6e, f** — 边界细胞DGE
- **Supp. Fig. 7** — 灵敏度基准比较
- **Supp. Fig. 8** — Visium与Xenium定量比较
- **Supp. Fig. 10** — Spot interpolation方法详细说明
- **Supp. Fig. 11** — 基因本体富集分析
- **Supp. Fig. 12-13** — Sample #2亚聚类和分子发现
