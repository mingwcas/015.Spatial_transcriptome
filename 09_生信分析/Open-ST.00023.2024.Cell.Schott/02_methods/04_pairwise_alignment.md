# Method: Pairwise Alignment of Data Modalities

## 原文（Methods）
> A two-step protocol was designed to align spatial transcriptomics data to tile scans of tissue staining from the same section. First, rescaled H&E images were coarsely aligned to low-resolution pseudoimages of ST data via the pre-trained Detector-Free Local Feature Matching with Transformers (LoFTR) outdoor model. For a more precise alignment, fine registration was performed, leveraging feature matching on H&E images and pseudoimages with higher resolution.

## 解读

### 意义
实现H&E成像数据与空间转录组数据的精确配对，是将转录本分配到分割细胞的前提。

### 输入
- H&E染色图像
- 空间转录组伪图像
- 条形码坐标信息

### 输出
- 配对后的空间坐标
- 细胞×基因表达矩阵

### 核心步骤
1. 生成空间转录组伪图像（扫描py空间函数或KDE方法）
2. 使用LoFTR模型进行粗对齐
3. 使用RANSAC估计鲁棒变换模型
4. 在更高分辨率下进行精细配准
5. 自动检测基准标记（YOLO模型）
6. 使用openst包的GUI进行视觉评估和手动精修
7. 将转录本聚合到分割的细胞中

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 粗对齐分辨率 | ~7 μm/pixel | 低分辨率配准 |
| 精细对齐分辨率 | ~1.5 μm/pixel | 高分辨率配准 |
| 对齐精度 | ~1 μm | 最终配准误差 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| LoFTR | 基于Transformer的无检测器局部特征匹配模型 |
| RANSAC | 随机抽样一致性算法，用于鲁棒变换估计 |
| 伪图像 | 从空间转录组数据生成的图像表示 |
| 基准标记 | 流式细胞上可见的圆形标记，用于配准 |

## 复现
- 工具/代码/URL: https://github.com/rajewsky-lab/openst
- 代码片段: 使用openst包的pairwise_aligner功能

## 生物学意义
精确的多模态配准是Open-ST的核心优势之一，使得同一组织切片的形态学和分子信息能够整合分析，为细胞类型注释和空间分析提供基础。

## 涉及 Figures
- **Fig. 1E** — 多模态数据整合流程
- **Fig. S1I** — 配准精度评估
