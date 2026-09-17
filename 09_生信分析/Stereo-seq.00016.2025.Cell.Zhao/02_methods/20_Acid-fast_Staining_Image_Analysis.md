# Method: Automated Identification of Positive Regions in Acid-fast Staining Images

## 原文（Methods）
> (from method details) The analysis used U-Net model for automated identification of positive regions in acid-fast staining images.

## 解读

### 意义
使用深度学习自动识别抗酸染色图像中的阳性区域，定位Mtb感染部位。

### 输入
- 抗酸染色图像

### 输出
- Mtb阳性区域分割结果

### 核心步骤
1. 使用U-Net模型进行图像分割
2. 识别抗酸染色阳性区域
3. 用于后续空间转录组分析

### 关键参数
| 参数 | 值 | 含义 |
|------|-----|------|
| 模型 | U-Net | 深度学习分割 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| U-Net | 图像分割深度学习模型 |
| 抗酸染色 | Acid-fast staining，检测Mtb |

## 复现
- U-Net模型用于图像分割

## 生物学意义
自动化图像分析提供客观、一致的Mtb感染区域识别。

## 涉及 Figures
- Fig. 6C, 7H (acid-fast staining)
