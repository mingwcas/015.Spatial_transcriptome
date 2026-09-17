# Method: 3D Reconstruction Using STIM

## 原文（Methods）
> The Spatial Transcriptomics ImgLib2/Imaging Project (STIM, v0.2.0) was leveraged for the alignment of the 19 Open-ST sections of the metastatic lymph node dataset. For alignment purposes, we treated sections as sequential. First, the coordinates of each pairwise-aligned and segmented h5ad file were rescaled by a factor 1:2.

## 解读

### 意义
将多个2D切片整合为3D虚拟组织块，揭示在2D中不可见的空间结构和分子模式。

### 输入
- 19个连续切片的空间转录组数据
- 配对后的H&E图像

### 输出
- 3D虚拟组织块
- 3D渲染的基因表达和细胞类型分布

### 核心步骤
1. 将每个切片的坐标缩放1:2
2. 将数据转换为n5格式
3. 使用预定义基因进行成对切片对齐
4. 使用st-align-global进行全局对齐
5. 将变换矩阵应用于H&E图像
6. 使用ParaView进行3D渲染

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 坐标缩放 | 1:2 | 坐标重缩放因子 |
| 对齐半径 | r=3 | 上下各3个切片用于成对对齐 |
| 最小内点数 | 15 | 仿射模型的最小内点数 |
| 平滑因子 | 4.0 | 高斯渲染的平滑参数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| STIM | 空间转录组成像框架，用于3D重建 |
| n5 | 高效图像处理的数据格式 |
| 仿射变换 | 包含平移、旋转、缩放的线性变换 |
| 等值面 | 3D空间中相同值的曲面 |

## 复现
- 工具/代码/URL: https://github.com/PreibischLab/STIM
- 代码片段: 使用openst包的from_3d_registration程序

## 生物学意义
3D重建能够揭示肿瘤边界、淋巴结结构等在2D切片中不可见的空间组织，为理解肿瘤微环境和转移机制提供新视角。

## 涉及 Figures
- **Fig. 1F** — 3D虚拟组织块构建流程
- **Fig. 7** — 3D虚拟组织块分析
