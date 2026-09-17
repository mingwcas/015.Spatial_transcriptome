# Method: Image Processing and Basecalling

## 原文（Methods）
> Image processing was performed as previously described, and we have made an easy-to-use image processing and basecalling MATLAB package that has been deposited at https://github.com/MacoskoLab/PuckCaller/. Input images are four-channel sequencing images for each puck for each time point of sequencing. For each bead, the sequence string for the bead barcode is output.

## 解读

### 意义
Image processing将荧光显微镜图像转换为每个bead的barcode序列，是连接光学成像与测序数据的关键步骤。

### 输入
- 4通道荧光测序图像（每轮ligaton一张）
- 每个puck的多个时间点图像

### 输出
- 每个bead的barcode序列字符串
- Bead位置坐标 (x, y)
- 用于下游匹配的bead annotations

### 核心步骤
1. **图像拼接**: 多个视野拼接成完整puck图像 (6,030 × 6,030 pixels)
2. **Bead detection**: 识别每个荧光点作为潜在bead
3. **荧光信号提取**: 提取每个bead在4个通道的荧光强度
4. **Base calling**: 将荧光颜色转换为碱基 (A/C/T/G)
5. **Monobase处理**: 直接从颜色space转换到basespace（无需colorspace转换）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 图像格式 | 4通道tiff | 每轮ligation |
| 输出 | barcode string | 每个bead的序列 |
| 颜色转换 | 直接basespace | monobase策略优势 |
| 工具 | MATLAB PuckCaller | GitHub开源 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| PuckCaller | MacoskoLab开发的MATLAB包，用于图像处理和basecalling |
| Basecalling | 将荧光信号转换为碱基序列 |
| Bead annotation | 每个bead的位置和barcode对应关系 |
| Colorspace | SOLiD原始数据格式，需转换到basespace |
| Basespace | 标准碱基序列格式 |

## 复现
- **工具**: MATLAB PuckCaller
- **URL**: https://github.com/MacoskoLab/PuckCaller/
- **输入**: 4通道测序图像 (tiff格式)
- **输出**: bead barcode sequences

## 生物学意义
准确的basecalling确保每个空间位置被正确标注。Monobase策略避免了SOLiD colorspace到basespace的转换，简化了流程并减少了错误。

## 涉及 Figures
- **Supplementary Fig. 9** — Slide-seq tools workflow
- **Fig. 1a** — Pipeline overview
