# Method: Integrative Data Analysis and Cell Type Identification

## 原文（Methods）
> Automatic cell type identification for E11 mouse tail region (Figure 6) was achieved with SingleR (version 1.2.3) (Aran et al., 2019) following standard procedure. Single cell RNA-seq data E10.5 from was used as the reference. The 12 most frequent cell types were shown in the UMAP, and cell types with small size were shown as ''other''.
> Cell type identification for E10 Eye region (Figure 4) was performed through integration with scRNA-seq reference data. We combined DBiT-seq data with scRNA-seq data of mouse embryo E9.5 and E10.5 (Cao et al., 2019) using Seurat V3.2 and did the clustering after ''SCTransform'' procedure. DBiT-seq data showed a similar distribution as scRNA-seq reference data. We then assign each cluster with a cell type using cell type information from the reference data (if two cell types presented in one cluster, we chose the one with higher proportion). The dominant cell type in each pixel was assigned based on the cluster membership and used for spatial cell type mapping.

## 解读

### 意义
该方法通过整合scRNA-seq参考数据实现DBiT-seq像素的自动细胞类型注释，将空间转录组数据转化为空间细胞类型图谱。

### 输入
- DBiT-seq空间转录组数据
- scRNA-seq参考数据（Cao et al., 2019; E9.5, E10.5）
- SingleR v1.2.3
- Seurat V3.2

### 输出
- 每个像素的细胞类型注释
- 空间细胞类型分布图

### 核心步骤
1. E11鼠标尾部样本（Figure 6）：
   - 使用SingleR v1.2.3自动细胞类型鉴定
   - 以E10.5 scRNA-seq数据为参考
   - UMAP展示12个最常见细胞类型
   - 小细胞类型归为"other"
   
2. E10眼部区域（Figure 4）：
   - 使用Seurat V3.2整合DBiT-seq与scRNA-seq E9.5/E10.5数据
   - 执行SCTransform流程
   - 联合聚类
   - 根据参考数据的细胞类型注释每个cluster
   - 如一个cluster含两个细胞类型，选择比例更高的
   - 每个像素根据cluster membership分配主导细胞类型
   - 绘制空间细胞类型映射图

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 细胞类型注释工具 | SingleR v1.2.3 | 自动注释 |
| 参考数据 | E10.5 scRNA-seq (SingleR); E9.5/E10.5 scRNA-seq (Seurat整合) | Cao et al., 2019 |
| 展示细胞类型数 | 12个最常见 | 简化展示 |
| 主导细胞类型判定 | Cluster内最高比例 | 分配到像素 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SingleR | 基于相关性的自动化细胞类型注释工具 |
| scRNA-seq integration | 单细胞与空间转录组数据整合 |
| Cell type mapping | 细胞类型空间分布图 |

## 复现
- 工具/代码/URL：SingleR v1.2.3 (https://github.com/drisso/SingleR)
- scRNA-seq参考数据：Cao et al., 2019 (GEO: GSE109071)
- 代码：https://github.com/rongfan8/DBiT-seq
- 关键调用：NA

## 生物学意义
这是DBiT-seq实现单细胞级别空间分析的关键步骤。通过与scRNA-seq参考数据整合，即使DBiT-seq的10μm像素含有~1.7个细胞，仍可推断每个像素的主导细胞类型。这种整合分析策略充分利用了现有的大规模scRNA-seq数据，使空间组学技术能够直接使用成熟的细胞类型注释。

## 涉及 Figures
- **Fig. 4H-L** — E10眼部区域细胞类型鉴定
- **Fig. 6E-G** — E11尾部区域细胞类型鉴定
