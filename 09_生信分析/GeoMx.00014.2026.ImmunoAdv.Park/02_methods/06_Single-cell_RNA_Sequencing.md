# Method: Single-cell RNA Sequencing and Analysis

## 原文（Methods）
> Tumor tissues were dissociated using the gentleMACS system and cryopreserved. Single-cell libraries were prepared using the 10 × Genomics Chromium 5′ V(D)J platform and sequenced on NovaSeq 6000 (∼50 000 reads/cell). Reads were mapped to GRCh38 with CellRanger (v5.0). Analysis was conducted in R (v4.1) using Seurat (v4.0). Low-quality cells (<300 genes or >40% mitochondrial content) were excluded. Normalization, scaling, and clustering were performed with batch correction using Harmony. Cell types were annotated based on canonical markers using the FindAllMarkers function.

## 解读

### 意义
10× Genomics单细胞RNA测序技术解析肿瘤微环境中每个细胞的转录组，结合Harmony批次校正和Seurat聚类，实现细胞类型精准注释。

### 输入
- 新鲜肿瘤组织
- gentleMACS系统（组织解离）
- 10× Genomics Chromium 5′ V(D)J平台
- NovaSeq 6000测序（~50,000 reads/cell）
- CellRanger v5.0、Cell hashed或类似样本标签
- R v4.1、Seurat v4.0、Harmony

### 输出
- 单细胞转录组表达矩阵（UMI counts）
- 细胞注释结果（各类群T细胞、NK细胞、巨噬细胞、B细胞等）
- UMAP/t-SNE降维可视化

### 核心步骤
1. gentleMACS系统解离肿瘤组织
2. 低温保存处理后的单细胞悬液
3. 10× Genomics Chromium 5′ V(D)J文库构建
4. NovaSeq 6000测序（~50K reads/cell）
5. CellRanger v5.0比对至GRCh38
6. R v4.1 + Seurat v4.0分析：
   - 质控：剔除<300基因或>40%线粒体含量的细胞
   - 标准化、Scale、Harmony批次校正
   - 聚类分析
   - FindAllMarkers进行细胞类型注释

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织解离 | gentleMACS | |
| 单细胞平台 | 10× Chromium 5′ V(D)J | |
| 测序深度 | ~50,000 reads/cell | |
| 比对工具 | CellRanger v5.0 | |
| 分析语言 | R v4.1 | |
| 分析工具 | Seurat v4.0 | |
| 批次校正 | Harmony | |
| 质控标准 | 基因数<300 或 线粒体>40% 排除 | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| scRNA-seq | Single-cell RNA sequencing，单细胞转录组测序 |
| 10× Genomics Chromium | 油包水液滴系统，单细胞文库构建平台 |
| CellRanger | 10×官方单细胞分析套件 |
| Seurat | R语言单细胞分析主流工具包 |
| Harmony | 单细胞批次校正算法 |
| UMI | Unique Molecular Identifier，唯一分子标签 |
| FindAllMarkers | Seurat中差异表达基因识别函数 |

## 复现
- 工具/URL：
  - CellRanger: https://support.10xgenomics.com/single-cell-gene-expression/software
  - Seurat: https://satijalab.org/seurat/
  - Harmony: https://portals.broadinstitute.org/hartmann/Harmony/
- 代码片段：
```R
library(Seurat)
library(harmony)
data <- Read10X(data.dir = "filtered_feature_bc_matrix/")
seurat_obj <- CreateSeuratObject(counts = data, project = "dMMR_CRC")
seurat_obj <- NormalizeData(seurat_obj)
seurat_obj <- ScaleData(seurat_obj)
seurat_obj <- RunHarmony(seurat_obj, group.by.vars = "sample")
seurat_obj <- FindClusters(seurat_obj, resolution = 0.5)
markers <- FindAllMarkers(seurat_obj)
```

## 生物学意义
单细胞转录组揭示了肿瘤微环境中细胞组成的异质性，特别是CD8+ T细胞、NK细胞、巨噬细胞（M1/M2极化）等与免疫治疗响应密切相关的细胞亚群的分布差异。

## 涉及 Figures
- **Fig. 4** — 单细胞转录组解析，UMAP、细胞组成、细胞毒性评分、巨噬细胞极化分析
- **Supplementary Figure S5** — 单细胞聚类结果
