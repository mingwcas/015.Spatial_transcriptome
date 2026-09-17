# Method: Platform Comparison (DSP vs. Other Spatial Profiling Platforms)

## 原文（Methods）
> Spatial Gene Expression (Visium)... Multiplex ImmunoFluorescence (mIF)... In Situ Hybridization Techniques... Spatial Phenotyping (PhenoCycler/CODEX)... Multiplexed Ion Beam Imaging (MIBI)... Imaging Mass Cytometry (IMC)... Multiplexed Error-Robust Fluorescent In Situ Hybridization (MERFISH)...

## 解读

### 意义
DSP 作为空间高plex 分析平台，与其他现有空间组学技术各有优劣。理解各平台间的技术差异有助于研究者为特定研究问题选择最合适的工具，或进行多平台整合分析。

### 输入
- 各空间分析平台的技术参数和性能指标（来自文献）
- 研究需求（分辨率、靶标数量、样本类型等）

### 输出
- 各平台的对比分析结果（分辨率、靶标数、优势、局限）
- 平台选择的参考依据

### 核心步骤（各平台比较）

#### DSP (GeoMx Digital Spatial Profiler)
- **原理**：光可切割 oligo 标记的抗体/探针 + nCounter 计数
- **分辨率**：ROI 级别（~665–785 μm），非单细胞
- **靶标数**：蛋白 panel 约 60–100 个；RNA panel 约 1,500–2,000+ 个基因
- **优势**：高通量、非破坏性（切片可用于后续分析）、样本兼容性好（FFPE/冷冻）
- **局限**：无单细胞分辨率；ROI 数量和面积受限；SNR 归一化对低丰度标记物有挑战

#### Visium (10x Genomics)
- **分辨率**：55 μm 直径 spot（平均 1–10 个细胞）
- **靶标数**：全转录组（FFPE/冷冻）
- **优势**：全转录组无偏分析；整个组织全覆盖
- **局限**：分辨率仍为 multicell 级别；组织需分割适配 capture area；RNA 质量需额外评估

#### mIF (Multiplex ImmunoFluorescence)
- **分辨率**：单细胞级别（x,y 坐标）
- **靶标数**：每轮最多 8 个抗体
- **优势**：单细胞空间信息；可研究细胞间相互作用
- **局限**： multiplex 有限；需要数字图像分析；ROI 选择受时间限制

#### CODEX / PhenoCycler
- **分辨率**：单细胞级别
- **靶标数**：多达 60 个蛋白标记
- **优势**：全片单细胞分辨率；无偏表型分析
- **局限**：FFPE 兼容性相对受限；组织制备挑战（22×22 mm 盖片限制）

#### MIBI (Multiplexed Ion Beam Imaging)
- **分辨率**：亚细胞级别
- **靶标数**：40+ 个标记
- **优势**：单细胞分辨率；金属标签减少光谱重叠
- **局限**：抗体验证复杂；组织破坏性（无法重复使用）

#### IMC (Imaging Mass Cytometry)
- **分辨率**：1,000 nm（可降至 260 nm）
- **靶标数**：40+ 个标记
- **优势**：单细胞分辨率；FFPE/冷冻兼容
- **局限**：组织破坏性；panel 设计验证复杂

#### MERFISH
- **分辨率**：单细胞 + 亚细胞级别
- **靶标数**：全转录组尺度
- **优势**：单细胞空间转录组；亚细胞定位
- **局限**：目前主要适用冷冻组织；FFPE 工作流程验证中

### 关键参数（本文设置）
| 平台 | 靶标数 | 分辨率 | 样本兼容性 | 组织破坏性 |
|------|--------|--------|------------|------------|
| DSP | ~60–2000+ | ROI (~665 μm) | FFPE/冷冻 | 否（非破坏性） |
| Visium | 全转录组 | ~55 μm spot | FFPE/冷冻 | 部分 |
| mIF | ~8/轮 | 单细胞 | 主要 FFPE | 部分 |
| CODEX/PhenoCyler | ~60 | 单细胞 | FFPE/冷冻 | 部分 |
| MIBI | ~40+ | 亚细胞 | FFPE/冷冻 | 是 |
| IMC | ~40+ | ~260–1000 nm | FFPE/冷冻 | 是 |
| MERFISH | 全转录组 | 单细胞+亚细胞 | 冷冻（FFPE 验证中） | 部分 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Visium | 10x Genomics 空间转录组平台，基于 spot 的全覆盖方法 |
| mIF | Multiplex ImmunoFluorescence，多重免疫荧光 |
| CODEX | Co-Detection by Indexing，基于寡核苷酸和顺序荧光报告的表型分析 |
| MIBI | Multiplexed Ion Beam Imaging，多重离子束成像 |
| IMC | Imaging Mass Cytometry，成像质谱流式 |
| MERFISH | Multiplexed Error-Robust Fluorescent In Situ Hybridization，多重纠错荧光原位杂交 |

## 复现
- 工具/代码/URL：
  - Visium: [https://www.10xgenomics.com/spatial-transcriptomics](https://www.10xgenomics.com/spatial-transcriptomics)
  - PhenoCycler: [https://www.akoyabio.com/phenocycler/](https://www.akoyabio.com/phenocycler/)
  - MERFISH: [https://vizgen.com/](https://vizgen.com/)

## 生物学意义
不同空间组学平台的选择取决于研究问题的空间尺度需求。若关注肿瘤内异质性和空间免疫微环境，DSP 的 ROI 策略可提供有针对性的分析；若需要单细胞级别的细胞间相互作用研究，则 mIF、CODEX、IMC 或 MERFISH 更适合。DSP 与 bulk mRNA 或单细胞 RNA-seq 的整合分析可弥补其非单细胞分辨率的不足，实现对空间组织的深度解读。

## 涉及 Figures
- 无直接涉及（平台比较为综述讨论内容）
