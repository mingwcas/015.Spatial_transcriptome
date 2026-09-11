# Method: Watershed Segmentation

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 5 分割策略比较
> Watershed (WA), Mesmer, Baysor (BA) and Baysor with prior segmentation (Baysor Px.x).

## 解读

### 意义
Watershed 是一种基于形态学的传统图像分割算法，通过对图像进行分水岭变换来分离重叠的细胞，适用于初步细胞边界划分。

### 输入
- DAPI 染色图像
- 细胞核标记图像
- 标记图像（种子点）

### 输出
- 细胞分割掩膜
- 分离的细胞区域

### 核心步骤
1. 预处理图像（高斯滤波）
2. 计算前景和背景标记
3. 应用 Watershed 算法
4. 生成细胞掩膜
5. 后处理（去除小区域）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Watershed | segmentation method | 基于分水岭变换的分割 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Watershed | 分水岭分割算法 |
| marker-based segmentation | 基于标记的分割 |
| morphological segmentation | 形态学分割 |

## 复现
- 工具/代码/URL：scikit-image (https://scikit-image.org/)
- 代码片段：
```python
# Watershed segmentation using scikit-image
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
distance = ndimage.distance_transform_edt(mask)
local_max = peak_local_max(distance, labels=mask)
markers = label(local_max)
labels = watershed(-distance, markers, mask=mask)
```

## 生物学意义
Watershed 作为传统方法，提供了一个基准分割策略，可以与深度学习方法进行比较，验证新方法的有效性。

## 涉及 Figures
- **ED Fig. 5** — Watershed 分割策略在多种分割方法中的比较
