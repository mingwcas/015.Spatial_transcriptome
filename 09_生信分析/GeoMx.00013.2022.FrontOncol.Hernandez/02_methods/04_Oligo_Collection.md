# Method: Oligo Collection (UV-Light Cleavage)

## 原文（Methods）
> After the ROIs are selected, and compartments have been segmented, these areas are exposed to ultraviolet (UV) light using a programmable digital micromirror device (DMD). This UV light process explains the term "Area of illumination" (AOI), which is used to refer to an entire ROI or compartment that will be illuminated in order to cleave DNA tags in a region-specific manner. The DMD will autoconfigure to match the exact spatial pattern defined previously in each ROI of each tissue section. The released indexing oligos are collected via microcapillary aspiration, and dispensed into a microplate (16).

## 解读

### 意义
Oligo collection 是 DSP 实现空间分辨的关键步骤——通过 UV 光在 ROI 特定区域照射，利用光可切割接头释放标记有独特index序列的oligos，实现不同空间位置的分隔收集，避免样本间交叉污染。

### 输入
- 已选择 ROI 并完成 segmentation 的染色切片
- DSP 仪器（包含 DMD 紫外光照射系统）

### 输出
- 各 AOI 对应的 indexing oligos（收集于 96 孔板）
- 原始 oligos 溶液（待后续杂交和计数）

### 核心步骤
1. ROI 选定后，通过可编程数字微镜设备（DMD）将 UV 光图案化
2. DMD 自动匹配每个 ROI / compartment 的精确空间形状
3. UV 光照射可切割 DNA 接头，释放该区域的 indexing oligos
4. 同一时间只照射一个 AOI（避免空间串扰）
5. 释放的 oligos 通过微毛细管吸取，分配至 96 孔板
6. 按设定顺序收集（建议从低丰度到高丰度，避免污染）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 光源 | UV 光（紫外） | 切割 photo-cleavable DNA tag |
| 照射方式 | DMD 图案化 | 精确匹配 ROI 形状 |
| 收集方式 | 微毛细管吸取 | 分离各 AOI 的 oligos |
| 接收容器 | 96 孔板 | 每孔对应一个 AOI |
| Collection order | 从低到高丰度 | 减少携带污染 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DMD | Digital Micromirror Device，数字微镜装置（可编程UV光照图案） |
| AOI | Area of Illumination，照射区域（ROI或分割后的compartment被UV照射的部分） |
| Indexing Oligo | 唯一索引序列，每个靶标对应唯一序列，用于后续定量 |
| Photo-cleavable linker | 光可切割接头，UV照射后断裂释放 oligos |
| Microcapillary aspiration | 微毛细管吸取，用于收集释放的 oligos |

## 复现
- 工具/代码/URL：GeoMx DSP 仪器（NanoString，商业平台）
- 参考：Merritt CR et al., bioRxiv 2019 (doi: 10.1101/559021)

## 生物学意义
DMD 引导的 UV 光切割技术是 DSP 实现空间分辨的核心创新。与流式或单细胞技术不同，DSP 不破坏组织完整性，且可在一张切片上同时分析数十个空间不同区域，每个区域独立收集并通过独特 index 序列加以区分。这一设计使其非常适合研究肿瘤内异质性和空间免疫微环境。

## 涉及 Figures
- **Fig. 1** — DSP assay workflow 中的 oligo collection 步骤示意
