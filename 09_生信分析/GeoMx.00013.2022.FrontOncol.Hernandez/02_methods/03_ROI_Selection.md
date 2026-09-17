# Method: ROI Selection

## 原文（Methods）
> Once the incubation is complete, slides are loaded onto the DSP instrument, and scanned to produce a digital image that displays the tissue with histological features highlighted by the fluorescent VM. Then, ROIs of different sizes (up to 660 × 785 μm) and shapes (rectangles, squares, and free hand shaped polygons) can be selected. These ROIs can be placed in different areas defined by biomarker expression, spatial location, and/or morphological features... After ROI selection, at the discretion of the investigator, these regions can be segmented in more than one compartment using the VM and assisted by an image analysis software embedded in the DSP device; the compartments can be defined as malignant epithelial cells vs. stroma (based on pancytokeratin expression), or in individual sets of cell populations such as CD45+, CD3+, or CD68+ cells (10, 11).

## 解读

### 意义
ROI（感兴趣区域）选择是 DSP 实验的核心步骤，决定了哪些组织区域将被用于后续的分子分析。研究者可依据组织学特征、biomarker 表达或空间位置灵活选择 ROI，并通过 compartment segmentation 实现不同细胞群体的分层分析。

### 输入
- DSP 仪器扫描的荧光图像（包含 VMs 标记的组织结构）
- ROI 选择策略（基于 biomarker 表达、空间位置或形态学特征）

### 输出
- 选定的 ROI 位置和形状坐标
- 分割后的 compartment 区域定义

### 核心步骤
1. 将染色后的切片加载到 DSP 仪器，扫描获取数字图像
2. 根据 VM 标记的组织学特征选择 ROI：
   - 形状：矩形、方形、自由多边形
   - 尺寸：最大 660 × 785 μm
   - 位置依据：biomarker 表达（CD45高/低区域）、空间位置（肿瘤中心vs侵袭边缘）、形态特征
3. 可选：使用 image analysis software 对 ROI 进行 compartment segmentation
   - 肿瘤/间质分割（基于 panCK 表达）
   - 细胞群体分割（CD45+, CD3+, CD68+ 等）
4. 设定 collection order（建议从低丰度到高丰度）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| ROI 最大尺寸 | 660 × 785 μm | 单个 ROI 上限 |
| 最小 ROI 尺寸 | 5 mm × 5 mm | 可放置的最小几何 ROI |
| ROI 形状类型 | 矩形、方形、多边形、轮廓剖面 | 多种几何选项 |
| 分割定义 | segment definition | 确定每个 AOI 的细胞组成（肿瘤/间质/免疫） |
| 侵蚀参数 | erosion | 增加 segment 边界间距 |
| N-扩张 | N-dilation | 扩大 UV 光罩 |
| 孔洞大小 | hole size | 填充小于设定值的 AOI 空洞 |
| 粒径 | particle size | 排除小于设定值的 AOI 颗粒（默认2 μm） |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ROI | Region of Interest，感兴趣区域 |
| AOI | Area of Illumination，照射区域（ROI 或分割后的 compartment） |
| panCK | Pancytokeratin，广谱细胞角蛋白（肿瘤细胞标记） |
| Compartment Segmentation | 将 ROI 进一步分割为不同细胞群体区域 |
| Morphology Marker | 形态学标记物（CD45, CD3, CD68 等） |
| TLS | Tertiary Lymphoid Structure，三级淋巴结构 |

## 复现
- 工具/代码/URL：GeoMx DSP 仪器配套软件（内置于 DSP 设备）
- [GeoMx Data Center](https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-data-center/)

## 生物学意义
ROI 选择策略直接决定了研究的生物学发现。该方法允许研究者在肿瘤内不同区域（免疫富集区vs免疫缺乏区、肿瘤中心vs侵袭边缘）进行比较分析，也可通过 segmentation 区分肿瘤细胞与间质/免疫细胞，实现空间异质性的精细刻画。这种灵活性对于理解肿瘤微环境的空间组织结构具有重要价值。

## 涉及 Figures
- **Fig. 3** — 多边形 ROI 选择策略（invasive basaloid rectal carcinoma）
- **Fig. 5** — 不同 segmentation 策略（肿瘤/间质/T细胞/B细胞分割）
