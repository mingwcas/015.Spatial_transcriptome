# Method: Integration analysis with single-cell ATAC-seq data

## 原文（Methods）
> We used the gene raw count matrix from similar coronal slices for the integration analysis. Specifically, for mouse brain R6 sample, the scATAC-seq data from slice 6 was used; and for mouse brain R8 sample, the scATAC-seq data from slice 8 and 9 was used as a reference. To integrate our spatial data with the single-cell ATAC-seq data from adult mouse brain, we first generated the gene count matrix from the corresponding slices using the same strategy as the spatial data. The integration was then performed using Seurat R package, which basically consisted of three major steps to align the spatial gene count matrices and the single-cell gene count matrices onto the same space: (1) using dimension reduction to derive embeddings of the two datasets; (2) applying canonical component analysis (CCA) to identify transferable anchors; and (3) aligning the low-dimensional representation of the two datasets together with the anchors using MapQuery. It is difficult to scale up to millions of cells using the CCA framework of Seurat due to the memory limitations. To address this, we randomly selected ~10% of cells from the original scATAC-seq datasets as the reference.

## 解读

### 意义
将Spatial-ATAC-Hi-C数据与单细胞ATAC-seq数据整合，利用已有的单细胞参考数据注释空间数据的细胞类型

### 输入
- Spatial-ATAC-Hi-C基因计数矩阵（GAS）
- 单细胞ATAC-seq基因计数矩阵（参考数据）
  - 小鼠脑R6样本：使用slice 6的scATAC-seq数据
  - 小鼠脑R8样本：使用slice 8和9的scATAC-seq数据

### 输出
- 整合后的低维表示
- 细胞类型注释和转移标签
- 空间数据与单细胞数据的对齐结果

### 核心步骤
1. **数据准备**：
   - 从空间数据生成基因计数矩阵（GAS）
   - 从对应切片的scATAC-seq数据生成基因计数矩阵
   - 使用相同策略确保数据可比性

2. **Seurat整合流程**：
   - 步骤1：降维获取两个数据集的嵌入
   - 步骤2：应用典型成分分析（CCA）识别可转移锚点
   - 步骤3：使用MapQuery将两个数据集的低维表示与锚点对齐

3. **内存优化**：
   - 由于Seurat CCA框架内存限制，无法处理百万级细胞
   - 解决方案：从原始scATAC-seq数据集中随机选择~10%细胞作为参考

4. **细胞类型注释转移**：
   - 利用锚点将参考数据的细胞类型标签转移到空间数据
   - 生成空间分布的细胞类型图谱

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 整合方法 | Seurat CCA | 典型成分分析整合方法 |
| 参考数据选择 | 随机选择~10%细胞 | 解决内存限制的策略 |
| 参考数据来源 | 对应切片的scATAC-seq数据 | 确保空间和参考数据的生物学一致性 |
| 锚点识别 | CCA | 识别两个数据集之间的可转移特征 |
| 对齐方法 | MapQuery | 使用锚点对齐低维表示 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| scATAC-seq | 单细胞ATAC-seq，单细胞水平的染色质可及性分析 |
| CCA | Canonical Component Analysis，典型成分分析，用于多数据集整合 |
| 锚点 | Anchors，两个数据集之间可转移的特征对 |
| MapQuery | Seurat函数，使用锚点对齐和整合数据集 |
| GAS | Gene Activity Score，基因活性分数，用于整合分析的基因表达估计 |

## 复现
- 工具/代码/URL
  - Seurat: https://github.com/satijalab/seurat
  - 整合教程：https://satijalab.org/seurat/articles/integration_introduction.html
  - scATAC-seq数据：GEO accession GSE246791 (BICCN数据)
- 代码片段
  ```bash
  # Seurat整合流程（R）
  library(Seurat)
  
  # 1. 创建Seurat对象
  spatial_obj <- CreateSeuratObject(counts = spatial_counts)
  reference_obj <- CreateSeuratObject(counts = reference_counts)
  
  # 2. 数据预处理
  spatial_obj <- NormalizeData(spatial_obj)
  reference_obj <- NormalizeData(reference_obj)
  
  # 3. 识别锚点
  anchors <- FindTransferAnchors(
    reference = reference_obj,
    query = spatial_obj,
    reduction = "cca"
  )
  
  # 4. 转移标签
  spatial_obj <- TransferData(
    anchorset = anchors,
    reference = reference_obj,
    refdata = "cell_type"
  )
  
  # 5. 对齐数据
  spatial_obj <- MapQuery(
    anchorset = anchors,
    reference = reference_obj,
    query = spatial_obj
  )
  ```

## 生物学意义
数据整合分析在Spatial-ATAC-Hi-C中具有重要价值：

**细胞类型注释**：
- 利用已有的单细胞参考数据注释空间数据
- 提高细胞类型识别的准确性
- 建立空间数据与单细胞图谱的联系

**跨平台验证**：
- 验证Spatial-ATAC-Hi-C数据的质量
- 与独立的单细胞技术比较，评估技术一致性
- 发现技术偏差和批次效应

**生物学发现**：
- 揭示细胞类型的空间分布模式
- 发现新的细胞状态和亚型
- 理解组织微环境的细胞组成

该整合方法的优势：
- 利用成熟的Seurat整合框架
- CCA方法对批次效应有较好的校正能力
- 标准化流程便于应用和比较

局限性：
- 内存限制需要随机采样参考数据，可能丢失信息
- 整合质量依赖于参考数据的质量和覆盖度
- CCA方法可能过度校正真实的生物学差异
- 需要仔细选择参考数据以确保相关性

## 涉及 Figures
- **Fig. 3** — 空间数据与单细胞数据整合分析
- **Fig. 4** — 细胞类型注释和空间分布
- **Extended Data Fig. 7** — 整合质量评估和锚点验证
