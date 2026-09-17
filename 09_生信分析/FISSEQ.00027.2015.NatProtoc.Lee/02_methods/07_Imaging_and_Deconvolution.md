# Method: 成像与3D反卷积

## 原文（Methods）
> Epifluorescence microscopy can generate a reasonable number of alignable reads from relatively thin specimens (<5 µm), but thicker samples require confocal microscopy to obtain high-density reads. We use 3D deconvolution to reduce the out-of-focus background and to improve the quality of base calls. High-quality 3D deconvolution requires sampling near the Nyquist rate. The x-y pixel and z-step sizes should not be >1.7 times the Nyquist value for image deconvolution.

## 解读

### 意义
使用共聚焦显微镜获取高分辨率3D图像堆栈，通过3D反卷积减少背景噪声、提高碱基判读质量

### 输入
- 细胞内交联固定的荧光标记扩增子
- 共聚焦显微镜（4通道：Cy5, Texas Red, Cy3, FAM）

### 输出
- 反卷积后的3D图像堆栈（.ics/.ids格式）

### 核心步骤
1. 显微镜设置：4通道配置（FITC-488, Cy3-561, Texas Red-594, Cy5-633）
2. 确定Nyquist采样率（使用SVI NyquistCalculator）
3. 采集图像堆栈（从最长到最短波长：Cy5→Texas Red→Cy3→FAM）
4. 使用直方图调整激光功率防止饱和
5. 3D反卷积（CMLE模式，5-10次迭代，SNR 2-5）
6. 文件命名标准化：<Position>_<Primer #>_<Ligation #>_<Date_Time>.extension

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Nyquist采样率 | ≤1.7倍Nyquist值 | 图像采样要求 |
| 反卷积算法 | CMLE | 约束最大似然估计 |
| 反卷积迭代次数 | 5-10 | 迭代次数 |
| SNR设置 | 2-5 | 信噪比 |
| 物镜 | 20× NA 0.75, 40× NA 0.8, 63× NA 1.2 | 不同分辨率需求 |
| 成像时间/堆栈 | >30 min (激光扫描共聚焦) | 单次采集时间 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Nyquist rate | 满足Nyquist采样定理的最小采样频率 |
| CMLE | Constrained Maximum Likelihood Estimation，反卷积算法 |
| NA (Numerical Aperture) | 数值孔径，决定物镜分辨率和集光能力 |
| Chromatic aberration | 色差，不同波长光的焦点偏移 |

## 复现
- 商业软件：SVI Huygens (3D反卷积), Bitplane Imaris (3D可视化)
- 免费替代：Fiji/ImageJ, Bio-Formats插件
- 校准：使用FocalCheck荧光显微镜测试玻片测量色差

## 生物学意义
3D反卷积是提高FISSEQ碱基判读质量的关键步骤。高质量反卷积要求接近Nyquist采样率，但会增加采集和反卷积时间。作者建议使用高质量共聚焦成像配合最小反卷积，而非低质量成像配合大量反卷积。色差校准对多色成像至关重要。

## 涉及 Figures
- **Fig. 5a** — 原始与反卷积3D渲染对比
- **Fig. 6** — 成像步骤
- **Table 2** — 显微镜平台比较
