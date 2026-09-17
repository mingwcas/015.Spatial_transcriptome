# Method: Experimental Design Considerations for DSP

## 原文（Methods）
> Similar to other tissue-based profiling techniques, the experimental design should be tailored to specific research questions and follow standardized protocols that consider the tissue selection, analytical validation of morphology biomarkers, harmonized strategy of ROI selection with full annotation of histological and biomarker features, several steps in quality control from tissue-related steps to data interpretation, and a standardized data management workflow.

## 解读

### 意义
DSP 实验设计需要系统性考虑从样本选择到数据分析的全流程各个细节，包括组织类型和样本质量、形态学标记物验证、ROI 选择策略、质控和标准化数据管理，是获得高质量、可重复结果的关键保障。

### 输入
- 研究问题和临床样本
- 可用组织类型（全组织切片、穿刺样本、TMA、细胞学标本、脱钙标本）
- 形态学标记物候选（VM）

### 输出
- 标准化的实验方案和 SOP
- ROI 放置策略文档
- Batch randomization 方案
- 外部对照设置方案

### 核心步骤
1. **Tissue Selection & Pre-Analytic QC**：
   - 10% 中性福尔马林固定 18–24 h（组织厚度<0.5 cm）
   - FFPE 块建议<4年（RNA分析）
   - ROI 内细胞数：蛋白质检测≥20 cells，RNA检测≥200 cells
   - 样本类型：手术切除样本、穿刺样本、TMA（0.6–6 mm）、细胞学标本、脱钙标本
2. **VM Validation**：
   - 最多4个形态学标记（SYTO13 + 3个荧光抗体/探针）
   - 自定义标记需先用标准 IHC 验证，再用 IF 优化
   - DAPI 不兼容于 DSP
3. **ROI Selection Strategy**：
   - 基于免疫浸润水平（CD45 表达）
   - 基于空间组织特征（肿瘤vs正常、中心vs边缘）
   - ROI 类型：几何 ROI、多边形 ROI、轮廓剖面、全组织网格
4. **Batch Randomization**：随机化不同队列样本，避免批次效应；设置外部对照评估批次间重现性
5. **Pathology QC**：病理学家确认染色质量和 ROI 选择合理性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 固定时间 | 10%福尔马林，18–24 h，室温 | nanoString 推荐 |
| 组织厚度 | <0.5 cm | 固定前组织厚度 |
| FFPE 保存时间 | <4年（RNA分析） | 建议样本保存期限 |
| 蛋白质 ROI 细胞数 | ≥20 cells | 最低细胞量要求 |
| RNA ROI 细胞数 | ≥200 cells | 最低细胞量要求 |
| TMA 核直径 | 0.6–6 mm | 兼容的 TMA 核尺寸 |
| DSP 扫描面积 | 36.6 × 14.6 mm | DSP 可扫描总面积 |
| AOI 最大尺寸 | 660 × 785 μm | 单个 AOI 上限 |
| 每周通量 | 最多8张切片/周/设备 | 实验室常规通量 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| TMA | Tissue Microarray，组织微阵列 |
| ROI 类型 - Geometric | 几何 ROI（矩形、方形、圆形），易操作和重复 |
| ROI 类型 - Polygon | 多边形 ROI，用于异质性评估和避免假阳性 |
| ROI 类型 - Contour Profile | 轮廓剖面，放射状 ROI，评估从中心结构向外的 oligo 表达变化 |
| ROI 类型 - Whole Tissue Gridding | 全组织网格化，覆盖整个样本 |
| Pre-analytic Variables | 分析前变量（固定时间、保存条件等） |

## 复现
- 工具/代码/URL：[GeoMx DSP Best Practices for Breast Cancer Research](https://doi.org/10.3390/cancers13174456)
- [GeoMx Manuals & Guides](https://nanostring.com/resources/geomx-manuals-guides/)

## 生物学意义
严格的实验设计对于 DSP 结果的可重复性和临床转化至关重要。组织样本的异质性和动态性（不同患者间、同一个肿瘤不同区域间）要求研究者充分记录并控制分析前变量。ROI 选择策略直接影响研究结果的生物学解释——选择肿瘤中心vs边缘、CD45高vs低区域等对应不同的生物学问题。该综述为 DSP 在肿瘤免疫学研究中的应用提供了详实的最佳实践指南。

## 涉及 Figures
- **Fig. 2** — 不同肿瘤类型的免疫荧光 biomarker 可视化示例
- **Fig. 3** — 多边形 ROI 在直肠癌活检中的应用
- **Fig. 4** — IF 染色中的假阳性示例（弹性纤维、红细胞）
- **Fig. 5** — NSCLC 中不同的 segmentation 策略
