# Method: Evaluation of Segmentation Results

## 原文（Methods）
> Manual segmentation was conducted using the software Labelme (v.5.5.0), where nuclear outlines were drawn manually based on DAPI and H&E staining. Solidity was calculated as the ratio of the contour area to its convex hull area, with higher values indicating convexity and lower values suggesting concavity. Circularity measures how closely a shape approximates an ideal circle, with a value of 1 corresponding to a perfect circle and 0 indicating a more irregular shape. The aspect ratio is the ratio of the width to the height of the bounding box that encloses the contour, which describes the elongation of the shape, with values greater than 1 indicating horizontal elongation and values less than 1 indicating vertical elongation. All metrics were calculated using the Python library OpenCV.

## 解读

### 意义
通过手动分割（Labelme）和形态学指标计算，评估各ST平台自动细胞分割的准确性。手动核分割作为ground truth，用于与CosMx 6K、Xenium 5K和Stereo-seq v1.3的自动分割结果进行比较。

### 输入
- DAPI和H&E染色图像
- CosMx 6K、Xenium 5K、Stereo-seq v1.3的自动分割结果

### 输出
- 手动分割的细胞核边界注释
- 形态学指标：solidity, circularity, aspect ratio, cell size
- 自动分割与手动分割的细胞数比较

### 核心步骤
1. 使用Labelme (v.5.5.0)手动标注核边界（基于DAPI和H&E染色）
2. 计算形态学指标（OpenCV）：
   - Solidity = 轮廓面积/凸包面积（值越高越凸，越低越凹）
   - Circularity = 4π×面积/周长²（1为完美圆形，0为不规则形状）
   - Aspect ratio = 边界框宽度/高度（>1水平延伸，<1垂直延伸）
3. 比较自动分割与手动分割的细胞数
4. 评估各平台的分割准确性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 手动分割工具 | Labelme v.5.5.0 |  |
| 形态学指标计算 | OpenCV v.4.10.0 | Python |
| 手动分割范围 | 5个区域（500×500 μm each），共72,405个细胞 |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Solidity | 实体性，轮廓面积与凸包面积之比 |
| Circularity | 圆度，接近完美圆的程度 |
| Aspect Ratio | 长宽比，描述细胞延伸程度 |
| Labelme | 开源图像注释工具 |
| StarDist | 深度学习细胞核分割算法 |

## 复现
- Labelme: v.5.5.0
- OpenCV: v.4.10.0
- StarDist: v.0.5.0 (用于全切片核分割)

## 生物学意义
准确的细胞分割对ST数据质量至关重要。研究发现CosMx 6K和Xenium 5K的自动分割结果与手动核分割高度一致，而Stereo-seq v1.3因染色伪影导致分割准确性较低。多通道染色支持的全细胞分割显著优于仅核分割方法。

## 涉及 Figures
- **Fig. 4a, b** — 自动分割与手动分割的比较
- **Supplementary Fig. 9a-d** — 形态学指标比较
- **Supplementary Fig. 13** — 多核细胞和肝细胞的特殊分割案例
