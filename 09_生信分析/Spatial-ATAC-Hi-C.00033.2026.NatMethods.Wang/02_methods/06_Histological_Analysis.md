# Method: Histological image and analysis of cell number per pixel

## 原文（Methods）
> All tissue samples were performed H&E staining following the manufacture’s procedure (Abcam, cat. no. ab245880). High-resolution histological images were obtained with Aperio GT-450 DX Scanner (Leica), and human patient samples were confirmed by a board-certified neuropathologist. These histological images were analyzed using QuPath open-source image-analysis software v.0.6.0. Cells were counted with the cell-detection feature using nuclear segmentation on matched histology images. Thresholds were set by comparison of segmentation of each nucleus at different parameters and then applied to all images of the experiment.

## 解读

### 意义
获取组织切片的高分辨率组织学图像，并定量分析每个空间像素内的细胞数量，用于后续数据标准化和生物学解释

### 输入
- 完成Spatial-ATAC-Hi-C实验的组织切片
- H&E染色试剂（Abcam, cat. no. ab245880）
- 高分辨率扫描仪（Aperio GT-450 DX Scanner）

### 输出
- 高分辨率H&E染色组织学图像
- 每个空间像素的细胞数量定量数据
- 用于后续数据标准化的细胞密度信息

### 核心步骤
1. **H&E染色**：
   - 按照制造商程序进行苏木精-伊红染色
   - 使用Abcam H&E染色试剂盒（cat. no. ab245880）

2. **图像采集**：
   - 使用Aperio GT-450 DX Scanner（Leica）获取高分辨率图像
   - 人类样本由认证神经病理学家确认

3. **图像分析**：
   - 使用QuPath开源图像分析软件（v.0.6.0）
   - 细胞检测功能：基于核分割的细胞计数
   - 参数优化：通过比较不同参数下的分割结果设置阈值
   - 应用统一阈值到实验中的所有图像

4. **细胞计数定量**：
   - 对每个空间像素区域进行细胞计数
   - 生成细胞密度矩阵，用于后续数据标准化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 染色方法 | H&E染色 | 苏木精-伊红染色，显示细胞核和细胞质 |
| 扫描仪 | Aperio GT-450 DX Scanner (Leica) | 高分辨率组织学图像扫描仪 |
| 分析软件 | QuPath v.0.6.0 | 开源图像分析软件 |
| 分割方法 | 核分割 | 基于细胞核的细胞检测 |
| 阈值设置 | 比较不同参数后的统一阈值 | 确保所有图像分析的一致性 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| H&E染色 | 苏木精-伊红染色，组织学常规染色方法，细胞核呈蓝色，细胞质呈红色 |
| 核分割 | Nuclear segmentation，基于细胞核形态的图像分割方法 |
| QuPath | 开源生物图像分析软件，支持组织学图像分析 |
| 细胞密度 | 单位面积内的细胞数量，用于数据标准化 |

## 复现
- 工具/代码/URL
  - H&E染色试剂：Abcam (cat. no. ab245880)
  - 扫描仪：Leica Aperio GT-450 DX Scanner
  - 分析软件：QuPath v.0.6.0 (https://qupath.github.io/)
  - 开源代码：QuPath GitHub (https://github.com/qupath/qupath)
- 代码片段
  ```bash
  # QuPath细胞计数流程（概念性）
  # 1. 导入H&E染色图像到QuPath
  # 2. 设置图像参数和比例尺
  # 3. 使用细胞检测功能（核分割）
  # 4. 优化分割参数（阈值设置）
  # 5. 应用统一阈值到所有图像
  # 6. 导出细胞计数数据
  # 7. 与空间像素数据匹配
  ```

## 生物学意义
组织学分析和细胞计数在Spatial-ATAC-Hi-C中具有重要作用：

**质量控制**：
- H&E染色验证组织结构和完整性
- 确认组织切片质量适合后续分析
- 人类样本由病理学家确认，确保样本质量

**数据标准化**：
- 细胞计数用于标准化ATAC-seq和Hi-C信号
- 消除细胞密度差异对信号强度的影响
- 提供生物学背景信息（细胞类型分布）

**空间信息整合**：
- 组织学图像与空间组学数据对齐
- 识别组织区域和结构
- 辅助生物学解释

该方法的优势：
- H&E染色是标准组织学方法，操作简单
- QuPath开源软件，可重复性好
- 高分辨率扫描提供详细的组织形态信息

局限性：
- H&E染色分辨率有限，可能无法识别所有细胞类型
- 核分割可能低估细胞数量（特别是对于细胞核不明显的细胞）
- 图像分析需要手动优化参数，可能存在主观性
- 扫描和分析时间较长

## 涉及 Figures
- **Fig. 1c** — H&E染色组织学图像与空间数据对比
- **Extended Data Fig. 1** — 组织学图像质量控制和细胞计数验证
- **Fig. 2** — 空间数据与组织学图像的整合分析
