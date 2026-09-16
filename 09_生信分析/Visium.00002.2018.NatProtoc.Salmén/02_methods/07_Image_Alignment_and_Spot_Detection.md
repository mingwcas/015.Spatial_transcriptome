# Method: Bright-field/Cy3 image alignment and spot/tissue detection

## 原文（Methods）
> “Launch the ST Spot Detector and load the two images ... Align the two images ... Perform automatic spatial spot and tissue detection ... Export the adjusted coordinates ... and the alignment matrix.” (PDF pp.11, 27–28; Steps 147–152).

## 解读
### 意义
将组织形态与空间spot坐标配准，限定组织覆盖spot。
### 输入
bright-field H&E图、Cy3空间spot荧光图。
### 输出
组织下spot调整坐标、3×3 affine alignment matrix。
### 核心步骤
1. 保持两图方向/区域一致。 2. 以可见spot或组织边界选择参考点并叠加对齐。 3. 自动检测spot和组织。 4. 导出坐标及矩阵。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| 输入图像 | 相同倍率和定义区域，JPG | 保证像素对应 |
| 结果矩阵 | 3×3 affine matrix | 视觉叠加转换 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| ST Spot Detector | spot/tissue检测和配准工具 |
| affine matrix | 图像坐标变换矩阵 |

## 复现
- 工具/代码/URL：https://github.com/SpatialTranscriptomicsResearch/st_spot_detector；容器 https://github.com/SpatialTranscriptomicsResearch/st_spot_detector_singularity
- 代码片段：浏览器加载两张图→overlay alignment→automatic detection→export。

## 生物学意义
只分析组织覆盖spot可减少背景数据冗余；错配会把表达信号投射到错误形态区域。

## 涉及 Figures
- **Fig. 1、Fig. 5、Fig. 6** — spot图、配准流程及组织质量。
