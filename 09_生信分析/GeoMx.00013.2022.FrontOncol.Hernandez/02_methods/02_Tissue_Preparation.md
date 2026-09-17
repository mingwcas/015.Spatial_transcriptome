# Method: Tissue Preparation

## 原文（Methods）
> This technique is compatible with formalin-fixed paraffin-embedded (FFPE) and frozen tissue. For both types of samples, sections of 5-mm thickness should be obtained following the specifications of sample preparation guidelines from nanoString (14). Then, deparaffinization and antigen retrieval are performed similar to the standard immunohistochemistry assay using manual or an automated stainer platform. Then, a single step of reagents is applied to the tissue, which consists of a cocktail of immunofluorescence biomarkers and probes or antibodies linked to photo-cleavable DNA tags. The immunofluorescence biomarkers will be used as visualization markers (VMs), and they include a DNA marker (SYTO13) and up to three specific antibodies or RNA probes conjugated to fluorophores (13, 15).

## 解读

### 意义
组织制备是 DSP 实验成功的基础步骤，确保组织形态完整且抗原表位暴露充分，同时完成免疫荧光标记和 DSP probes 的孵育，为后续 ROI 选择和 oligo 收集创造条件。

### 输入
- FFPE 或冷冻组织切片（5 μm 厚）
- 自动化或手动染色平台
- nanoString 认证的染色试剂

### 输出
- 完成免疫荧光染色和 DSP probes 孵育的切片
- 可在 DSP 仪器上扫描成像

### 核心步骤
1. 切片厚度调整为 5 μm（按 nanoString 指南）
2. FFPE 样本进行脱蜡和抗原修复（手动或自动染色仪）
3. 孵育包含可视化标记（VMs）的混合试剂：
   - SYTO13（DNA核标记）
   - 最多3个特异性抗体或 RNA 探针（偶联荧光染料：AF532, AF594, AF647）
4. 抗体/探针同时连接光可切割 DNA 标签（photo-cleavable DNA tags）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 5 μm | 标准 DSP 样本厚度 |
| DNA 标记 | SYTO13 | 细胞核可视化标记 |
| 荧光染料 | AF532, AF594, AF647 | DSP 兼容的荧光染料 |
| 可用 VMs 数 | 最多4个 | SYTO13 + 3个抗体/探针 |
| 固定方式 | FFPE 或冷冻 | 两种组织类型均兼容 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SYTO13 | 绿色荧光 DNA 结合染料，用作核标记 |
| Visualization Marker (VM) | 可视化标记，用于在 DSP 扫描时识别组织结构 |
| Photo-cleavable DNA tag | 光可切割 DNA 标签，偶联在抗体/探针上，UV照射后释放 |
| AF532/AF594/AF647 | Alex Fluor 532/594/647，依次为绿、橙、红荧光染料 |
| 抗原修复 | 恢复甲醛固定过程中被遮蔽的抗原表位 |

## 复现
- 工具/代码/URL：[GeoMx DSP Manual Slide Preparation (MAN-10150-01)](https://nanostring.com/wp-content/uploads/2022/06/MAN-10150-01-GeoMx-DSP-Manual-Slide-Preparation-User-Manual.pdf)
- [GeoMx Morphology Markers](https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-morphology-markers/)

## 生物学意义
组织制备的质量直接影响后续所有步骤的可靠性。FFPE 样本需严格控制固定时间（10%中性福尔马林18–24小时，室温，组织厚度<0.5cm），老旧样本（>4年）或固定不当会导致信号强度显著下降。冷冻样本需注意冰晶形成可能破坏组织结构。该步骤确保了 DSP 可在有限的临床样本上实现高通量空间分析。

## 涉及 Figures
- **Fig. 2** — 多种肿瘤组织的免疫荧光 biomarker 可视化示例图
