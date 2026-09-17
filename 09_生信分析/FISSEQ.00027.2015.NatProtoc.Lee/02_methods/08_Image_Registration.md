# Method: 图像配准（Image Registration）

## 原文（Methods）
> As long as the input image files are correctly named, our software will generate the maximum intensity projection, register the images and correct for chromatic shifts. The resulting images are used for base calling and sequence alignment. Set the number of blocks per axis for local registration (default = 10); set the fraction overlap between neighboring blocks (default = 0.1); and adjust the alignment precision, where 10 will register images to 1/10 of a pixel.

## 解读

### 意义
将不同测序轮次和荧光通道的图像对齐，校正色差和时间漂移，为碱基判读做准备

### 输入
- 反卷积后的图像堆栈（decon_images文件夹）

### 输出
- 配准后的TIFF图像（registered_images文件夹）
- 最大强度投影图像
- 配准偏移量文件（Routput.mat, Rchadj.mat, Rtadj.mat）

### 核心步骤
1. MATLAB中设置输入/输出目录
2. 运行 register_FISSEQ_images(input_dir, output_dir, blocks, overlap, precision)
3. 算法执行：时间点配准 → 色差校正 → 最大强度投影
4. 用ImageJ检查配准质量（Bio-Formats打开TIFF文件）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| blocks per axis | 10 (默认) | 局部配准的分块数 |
| overlap fraction | 0.1 (默认) | 相邻块重叠比例 |
| alignment precision | 1 (默认，即1/10像素) | 配准精度 |
| 内存需求 | >100 GB | 高性能计算集群 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Maximum intensity projection (MIP) | 最大强度投影，沿Z轴取最大值 |
| Chromatic shift | 色差导致的图像偏移 |
| Block-wise registration | 分块局部配准算法 |
| Routput.mat | 块间配准偏移量 |
| Rchadj.mat | 色差校正矩阵 |
| Rtadj.mat | 时间序列配准偏移量 |

## 复现
- 工具：MATLAB + fisseq.zip中的register_FISSEQ_images函数
- 代码：`register_FISSEQ_images(input_dir, output_dir, 10, 0.1, 1)`
- 需要>100 GB RAM的高性能计算节点

## 生物学意义
图像配准确保不同测序轮次的同一位置正确对齐，是碱基判读准确性的基础。色差校正尤为重要，因为不同荧光通道可能存在亚像素级偏移。分块局部配准可处理图像不同区域的非刚性变形。

## 涉及 Figures
- **Fig. 5b** — 图像配准流程（未配准→时间点配准→色差校正）
- **Supplementary Fig. 5** — 配准参数设置
