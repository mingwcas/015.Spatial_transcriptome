# Method: DSP Assay Workflow

## 原文（Methods）
> The nanoString GeoMx DSP is a tissue-based assay for high-plex profiling of protein and RNA within specific areas of interest. The main steps included in the workflow of this platform include tissue preparation with immunofluorescence biomarkers and DSP probes, regions of interest selection, oligo collection, hybridization, and counting and data analysis (Figure 1).

## 解读

### 意义
该方法提供了 GeoMx Digital Spatial Profiler (DSP) 的完整技术流程概述，涵盖从样本制备到数据分析的全流程，是理解该平台如何实现空间高plex蛋白/RNA分析的核心框架。

### 输入
- FFPE 或冷冻组织切片（5 μm 厚）
- 免疫荧光 biomarkers（可视化标记，VMs）
- DSP probes（连接光可切割 DNA 标签的抗体或 RNA 探针）

### 输出
- 各 ROI/AOI 的蛋白或 RNA 计数数据
- 原始计数矩阵（需经 QC 和 normalization）

### 核心步骤
1. **Tissue Preparation**：组织切片制备，孵育免疫荧光 biomarkers 和 DSP probes
2. **ROI Selection**：在 DSP 仪器上扫描图像，选择感兴趣区域（ROI）
3. **Oligo Collection**：紫外光照射，UV光可切割DNA标签，释放indexing oligos
4. **Hybridization & Counting**：indexing oligos 与荧光条码杂交，使用 nCounter 系统计数
5. **Data Analysis**：QC、归一化、可视化和统计分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织厚度 | 5 μm | 切片标准厚度 |
| 可视化标记数 | 最多4个 | 包括SYTO13（DNA）+ 3个荧光抗体/探针 |
| ROI 最大尺寸 | 660 × 785 μm | 单个ROI最大面积 |
| ROI 形状 | 矩形、方形、自由多边形 | 几何形状或轮廓剖面 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DSP | Digital Spatial Profiler，数字空间分析 profiler |
| ROI | Region of Interest，感兴趣区域 |
| AOI | Area of Illumination，照射区域（ROI或分割后的compartment） |
| VM | Visualization Marker，可视化标记 |
| DMD | Digital Micromirror Device，数字微镜装置（用于UV光照图案化） |
| FFPE | Formalin-Fixed Paraffin-Embedded，甲醛固定石蜡包埋 |
| nCounter | NanoString 单分子计数系统 |

## 复现
- 工具/代码/URL：[GeoMx DSP 官方产品页](https://nanostring.com/products/geomx-digital-spatial-profiler/)
- GeoMx Data Center 分析套件：[https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-data-center/](https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-data-center/)

## 生物学意义
DSP assay workflow 实现了在组织原位对蛋白和 RNA 的高通量空间分析，弥补了传统免疫组化只能检测少量标志物的不足。该流程可在同一张切片上同时分析数十至数百个靶点，并保留空间位置信息，对肿瘤微环境研究、免疫治疗biomarker发现和肿瘤异质性解析具有重要价值。但该平台不提供单细胞分辨率，限制了细胞间相互作用的精细研究。

## 涉及 Figures
- **Fig. 1** — DSP assay workflow 示意图，展示了从组织制备到数据输出的完整流程
