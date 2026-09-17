# Method: Cell Segmentation and Single-Cell Quantification

## 原文（Methods）
> This step involves segmenting individual cells from the aligned imaging data and assigning transcripts to these segmented cells. It creates a cell-by-gene expression matrix that integrates spatial information with transcriptomic data, enabling single-cell level analysis within the tissue context.

## 解读

### 意义
从对齐的成像数据中分割单个细胞，并将转录本分配到分割的细胞中，生成单细胞分辨率的空间表达矩阵。

### 输入
- 对齐后的 h5ad 文件（包含图像和转录组数据）
- Cellpose 细胞分割模型

### 输出
- 细胞分割掩码
- 单细胞基因表达矩阵（h5ad 格式）

### 核心步骤
1. 使用 openst segment 进行细胞分割
2. 选择合适的 Cellpose 模型（如 HE_cellpose_rajewsky）
3. 可视化分割结果（使用 Napari）
4. 如需要，调整参数重新分割
5. 创建单细胞基因表达矩阵（transcript_assign）
6. 导出包含分割细胞的 h5ad 文件

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| flow-threshold | 0.5 | Cellpose 流阈值，越高检测到的细胞越少 |
| cellprob-threshold | 0 | Cellpose 细胞概率阈值，越高检测越严格 |
| diameter | 20 | Cellpose 细胞直径参数（像素） |
| dilate-px | 10 | 分割掩码扩展像素数 |
| tissue-masking-gaussian-sigma | 5 | 组织隔离高斯模糊 sigma |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Cell segmentation | 细胞分割，从图像中识别单个细胞边界 |
| Cellpose | 基于深度学习的细胞分割工具 |
| Segmentation mask | 分割掩码，标记每个细胞的像素区域 |
| Transcript assignment | 转录本分配，将转录本映射到对应的细胞 |
| Napari | Python 多维图像查看器 |

## 复现
- 工具/代码/URL：
  - Cellpose: https://github.com/MouseLand/cellpose
  - openst: https://github.com/rajewsky-lab/openst
  - Napari: https://napari.org
- 代码片段：
```bash
# 细胞分割
openst from_spacemake \
  --project-id project_id \
  --sample-id sample_id \
  segment \
  --model HE_cellpose_rajewsky

# 转录本分配
openst from_spacemake \
  --project-id project_id \
  --sample-id sample_id \
  transcript_assign \
  --spatial-key obsm/spatial_manual_fine \
  --mask-in uns/spatial/staining_image_mask

# 预览结果
openst from_spacemake \
  --project-id project_id \
  --sample-id sample_id \
  preview \
  --image-keys uns/spatial/staining_image uns/spatial/staining_image_mask
```

## 生物学意义
细胞分割是将空间转录组数据从"点"级别提升到"细胞"级别的关键步骤。Open-ST 使用 Cellpose 进行基于核的分割并径向扩展，可以处理大多数细胞类型。对于细胞密集的组织（如淋巴结），可能需要调整参数或使用两步分割策略。分割后的单细胞表达矩阵可以用于下游分析，如聚类、差异表达和细胞类型注释。用户也可以导入其他分割工具（如 QuPath、ImageJ）的结果。

## 涉及 Figures
- **Fig. 6** — Interactive visualization and quality assessment of cell segmentation with Napari
