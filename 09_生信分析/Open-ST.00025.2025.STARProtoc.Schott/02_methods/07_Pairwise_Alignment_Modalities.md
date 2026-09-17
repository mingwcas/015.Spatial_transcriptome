# Method: Pairwise Alignment of Imaging and Transcriptomics

## 原文（Methods）
> This step integrates the stitched microscopy images with the spatial transcriptomics data, creating a unified dataset for analysis. It includes spatial stitching of individual microscopy imaging tiles, merging imaging and transcriptomics modalities, and performing pairwise alignment between the imaging and transcriptomic data to enable accurate spatial mapping of gene expression.

## 解读

### 意义
将显微镜成像数据与空间转录组数据进行配对对齐，实现两种模态的精确空间映射。

### 输入
- 缝合后的显微镜图像（TIFF 格式）
- spacemake 生成的 h5ad 文件
- 坐标系统文件

### 输出
- 包含对齐后空间坐标的 h5ad 文件
- 对齐后的图像叠加可视化

### 核心步骤
1. 准备缝合后的成像数据（TIFF 格式）
2. 使用 openst 将单个 tile 数据合并为单一文件（spatial_stitch）
3. 将图像数据集成到 h5ad 对象（merge_modalities）
4. 执行自动配对对齐（pairwise_aligner）
5. 可视化对齐结果（GUI 界面）
6. 如需要，手动调整对齐（manual_pairwise_aligner）
7. 应用最终变换（apply_transform）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| rescale-factor-coarse | 20 | 粗对齐图像缩放因子 |
| pseudoimage-size-coarse | 500 | 粗对齐伪图像大小（像素） |
| ransac-coarse-residual-threshold | 2 | RANSAC 残差阈值 |
| rescale-factor-fine | 10 | 细对齐图像缩放因子 |
| pseudoimage-size-fine | 2000 | 细对齐伪图像大小（像素） |
| fine-min-matches | 50 | 细对齐最小匹配关键点数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Pairwise alignment | 配对对齐，将两个模态的空间数据对齐 |
| RANSAC | Random Sample Consensus，随机采样一致性算法 |
| Pseudoimage | 伪图像，用于对齐的中间表示 |
| Keypoints | 关键点，用于对齐的对应点 |
| Fiducial circles | 基准圆，flow cell 上的对齐标记 |

## 复现
- 工具/代码/URL：https://github.com/rajewsky-lab/openst
- 代码片段：
```bash
# 合并 tile 数据
openst from_spacemake \
  --project-id project_id \
  --sample-id sample_id \
  spatial_stitch

# 集成图像数据
openst from_spacemake \
  --project-id project_id \
  --sample-id sample_id \
  merge_modalities

# 自动配对对齐
openst from_spacemake \
  --project-id project_id \
  --sample-id sample_id \
  pairwise_aligner

# 手动对齐（如需要）
openst from_spacemake \
  --project-id project_id \
  --sample-id sample_id \
  manual_pairwise_aligner

# 应用变换
openst apply_transform --keypoints-in keypoints.json
```

## 生物学意义
成像与转录组数据的精确对齐是 Open-ST 分析的关键步骤。通过对齐，可以将基因表达数据映射到组织形态学上，实现"虚拟组织学"——在组织形态背景下观察基因表达模式。自动对齐使用 RANSAC 算法处理大规模特征匹配，而手动对齐 GUI 允许用户基于基准圆等视觉标记进行精确调整。对齐后的坐标单位为像素，需要乘以 mm/pixel 因子转换为物理单位。

## 涉及 Figures
- **Fig. 5** — Manual Pairwise Alignment Graphical User Interface (GUI) for Open-ST data
