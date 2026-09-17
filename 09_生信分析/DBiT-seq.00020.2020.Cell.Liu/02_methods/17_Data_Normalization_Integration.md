# Method: Data Normalization and Integration

## 原文（Methods）
> Normalization and variance stabilization of transcriptome data for each pixel with regularized negative binomial regression was performed using ''SCTransform,'' a module in Seurat V3.2. The process is similar to that widely used for scRNA-seq data normalization, with each ''pixel'' treated as a ''single cell.'' The expression matrix of all pixels was SCTransformed (''NormalizeData,'' ''ScaleData'' and ''FindVariableFeatures''). The integration of scRNA-seq reference data and spatial transcriptome data was conducted using Seurat V3.2 with the ''SCTransform'' module. Normalization of gene data was completed through Scran (V3.11) following a standard protocol as recommended in Seurat package.

## 解读

### 意义
该方法使用scRNA-seq领域的标准标准化方法SCTransform对空间转录组数据进行标准化和方差稳定，使下游分析更准确。

### 输入
- 原始表达矩阵（pixels × genes）
- Seurat V3.2
- Scran V3.11

### 输出
- SCTransform标准化后的表达矩阵
- 稳定方差的表达数据
- 变量基因列表

### 核心步骤
1. 使用Seurat V3.2的SCTransform模块
2. 每个"pixel"被视为一个"single cell"
3. SCTransform执行：NormalizeData + ScaleData + FindVariableFeatures
4. 使用regularized negative binomial regression进行标准化和方差稳定
5. 如需整合scRNA-seq数据，使用Seurat V3.2的SCTransform进行整合
6. 可选：使用Scran V3.11进行补充标准化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 标准化方法 | SCTransform (Seurat V3.2) | 正则化负二项回归 |
| 整合方法 | Seurat V3.2 SCTransform | 单细胞与空间数据整合 |
| 辅助标准化 | Scran V3.11 | 补充标准化 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SCTransform | Seurat中的正则化泊松/负二项回归标准化方法，比log标准化更准确 |
| Regularized negative binomial regression | 正则化负二项回归，估计基因特异性校正因子 |
| Scran | 单细胞RNA-seq标准化包 |

## 复现
- 工具/代码/URL：Seurat V3.2 (https://satijalab.org/seurat/); Scran V3.11
- 关键代码：NA

## 生物学意义
SCTransform已成为scRNA-seq数据分析的标准方法，通过建模技术消除了文库大小效应，使基因表达比较更加准确。将像素视为单细胞进行处理，使得空间转录组数据能够直接复用成熟的单细胞分析工具，为后续聚类和细胞类型注释奠定基础。

## 涉及 Figures
- 无直接关联（下游分析基础）
