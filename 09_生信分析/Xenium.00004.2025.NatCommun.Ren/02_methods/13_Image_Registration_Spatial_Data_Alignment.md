# Method: Registration of Images and Alignment of Spatial Data

## 原文（Methods）
> We manually annotated key landmarks on paired images and employed the SimpleITK library (v.2.4.0) to achieve accurate registration. Specifically, the Similarity2DTransform, SetMetricAsMattesMutualInformation, and sitkLinear functions were utilized to perform automated adjustment after the initial transformation derived from paired landmarks. For the alignment of Visium HD FFPE, CosMx 6K, and Xenium 5K data, we set the grayscale H&E image of Visium HD FFPE as the fixed reference and registered the DAPI images of CosMx 6K and Xenium 5K to it. The derived transformations were subsequently applied to map the CosMx 6K and Xenium 5K data onto the coordinate system of the Visium HD FFPE data. For the alignment of ST data with adjacent CODEX data, the grayscale H&E images of Stereo-seq v1.3 and Visium HD FFPE were used as the fixed references. For CosMx 6K and Xenium 5K, the DAPI images were used as the fixed references. The fixed references were rescaled to match the resolution of CODEX, and the DAPI channel of CODEX was registered to these references. The derived transformations were subsequently applied to the remaining CODEX channels. To enable direct comparisons across FFPE samples, we used the Python package OpenCV to extract tissue masks of each ST data based on the paired staining images and intersected them to define the shared regions. A similar approach was used to extract overlapping regions between ST data and adjacent CODEX data.

## 解读

### 意义
图像配准和数据对齐是实现跨平台、跨模态（转录组-蛋白组）比较的关键技术。通过将不同平台的数据转换到统一坐标系统，使相邻切片间的空间比较成为可能。

### 输入
- 各ST平台的染色图像（H&E, DAPI, IF）
- 相邻CODEX染色图像
- 手动标注的关键地标

### 输出
- 统一坐标空间的空间数据
- 跨平台共享区域
- ST与CODEX的重叠区域

### 核心步骤
1. 手动在配对图像上标注关键地标
2. 使用SimpleITK (v.2.4.0)进行精确配准：
   - Similarity2DTransform: 初始变换
   - SetMetricAsMattesMutualInformation: 自动化调整
   - sitkLinear: 插值
3. FFPE样本对齐：以Visium HD FFPE的灰度H&E图像为固定参考，将CosMx 6K和Xenium 5K的DAPI图像配准到参考系
4. ST与CODEX对齐：
   - Stereo-seq v1.3和Visium HD FFPE: 使用H&E作为固定参考
   - CosMx 6K和Xenium 5K: 使用DAPI作为固定参考
   - 将CODEX的DAPI通道配准到固定参考，再将变换应用到其他CODEX通道
5. 使用OpenCV提取各ST数据的组织掩膜，交叉定义共享区域

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 配准工具 | SimpleITK v.2.4.0 | 医学图像配准 |
| 变换类型 | Similarity2DTransform | 相似性变换（缩放+旋转+平移） |
| 相似度度量 | Mattes互信息 |  |
| 插值方法 | sitkLinear (线性插值) |  |
| 掩膜工具 | OpenCV v.4.10.0 | 组织区域分割 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 图像配准 (Image Registration) | 将不同图像对齐到同一坐标空间 |
| 地标 (Landmarks) | 手动标注的解剖学参考点 |
| 共享区域 (Shared Regions) | 多个平台数据重叠的空间区域 |
| SimpleITK | ITK的简化封装，用于医学图像处理 |

## 复现
- SimpleITK: v.2.4.0
- OpenCV: v.4.10.0
- 地标注释：手动

## 生物学意义
精确的图像配准是将ST数据与CODEX蛋白数据进行空间比较的前提，使转录本-蛋白一致性分析成为可能。研究中所有跨模态相关性分析均依赖于此对齐流程。

## 涉及 Figures
- **Supplementary Fig. 6** — 图像配准流程示意
- **Fig. 3, 5, 6** — ST与CODEX的空间相关性分析（依赖配准结果）
