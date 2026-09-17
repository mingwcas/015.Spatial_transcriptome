# Method: scRNA-seq and Spatial Data Integration

## 原文（Methods）
> The cell types of skin biopsy section were annotated through integration analysis using the matched scRNA-seq data as the reference. The two datasets were normalized with the 'SCTransform' function in Seurat version 3.2 and then integrated into one dataset. After clustering, the spatial pixel data conformed well with the scRNA-seq data, and, thus, the cell types were assigned based on the scRNA-seq cell type annotation for each cluster (if two cell types presented in one cluster, the major cell types were assigned). SPOTlight was used to deconvolve the spatial spots.

## 解读

### 意义
将spatial-CITE-seq数据与配对的scRNA-seq数据整合，实现空间像素的细胞类型注释和去卷积。

### 输入
- Spatial-CITE-seq转录组数据
- 配对的scRNA-seq数据（同一皮肤活检样本）

### 输出
- 空间像素的细胞类型注释
- SPOTlight去卷积结果（空间细胞比例）

### 核心步骤
1. 两个数据集分别使用SCTransform标准化
2. Seurat v3.2整合分析，将空间像素数据和scRNA-seq数据合并
3. 聚类分析，验证空间像素数据与scRNA-seq数据的一致性
4. 基于scRNA-seq的细胞类型注释为每个空间聚类分配细胞类型
5. 使用SPOTlight包对空间spots进行去卷积分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 整合方法 | Seurat SCTransform + Integration | 标准化后整合 |
| 去卷积工具 | SPOTlight | 基于NMF回归的去卷积 |
| 参考数据 | 配对scRNA-seq | 同一组织样本的单细胞数据 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Label transfer | 标签转移，将参考数据集的细胞类型注释转移到查询数据集 |
| SPOTlight | Seeded NMF regression，基于种子非负矩阵分解的空间去卷积方法 |
| Deconvolution | 去卷积，推断每个空间spot中不同细胞类型的比例 |
| Integration | 整合，将不同数据集对齐到共同的低维空间 |

## 复现
- 工具/代码/URL
  - Seurat v3.2：https://satijalab.org/seurat/
  - SPOTlight：https://github.com/MarcElosua/SPOTlight
- 代码片段：
```r
# 整合分析（概念性代码）
library(Seurat)
# 标准化
spatial <- SCTransform(spatial)
scRNA <- SCTransform(scRNA)
# 整合
anchors <- FindIntegrationAnchors(list(spatial, scRNA))
integrated <- IntegrateData(anchors)
# 聚类和注释
integrated <- FindClusters(integrated)

# SPOTlight去卷积
library(SPOTlight)
spotlight <- spotlight_deconvolution(
  se_sc = scRNA_ref,
  counts_spatial = spatial_counts,
  clust_vr = "cell_type"
)
```

## 生物学意义
空间-单细胞数据整合是将细胞类型映射到组织空间位置的关键步骤。通过label transfer，研究者发现COVID-19疫苗注射部位存在大量Tph（外周辅助T）细胞，这些细胞表达LAG3、PD-1和CXCR6等激活标志物。SPOTlight去卷积进一步确认了角质形成细胞和成纤维细胞为主要细胞类型，与scRNA-seq数据一致。

## 涉及 Figures
- **Fig. 2g** — 整合分析的UMAP（空间像素与scRNA-seq数据）
- **Fig. 2h** — Label transfer后的细胞类型空间分布
- **Extended Data Fig. 7b** — SPOTlight去卷积的饼图结果
