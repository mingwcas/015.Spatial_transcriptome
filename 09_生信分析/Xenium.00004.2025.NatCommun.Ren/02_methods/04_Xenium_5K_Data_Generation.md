# Method: Xenium 5K Data Generation

## 原文（Methods）
> Xenium 5K assay is compatible with FFPE-embedded tissues and H&E staining. RNA quality of the tissue block was assessed by calculating the percentage of RNA fragments >200 nucleotides (DV200) extracted from tissue sections. DAPI and H&E staining were also used to assess tissue morphology before performing the Xenium 5K assay.
> Tissue sections were cut at a thickness of 5 μm following the Xenium In Situ for FFPE-Tissue Preparation Guide (CG000578, 10x Genomics), spread out in RNA enzyme-free water at 42 °C, and attached to the Xenium slides (PN-3000941, 10x Genomics) within the sample area (with a maximum size of 10.45 × 22.45 mm) without overlapping with the surrounding fiducials. The slides were dried at room temperature for 30 min and baked at 42 °C for 3 h. The follow-up experiment was carried out after drying overnight at room temperature.
> After drying overnight, the Xenium slides were subjected to deparaffinization and decrosslinking following the Xenium In Situ Protocol for FFPE-Deparafﬁnization and Decrosslinking (CG000580, 10x Genomics). Priming hybridization, RNase treatment & polishing, probe hybridization, probe ligation, amplification, cell segmentation staining, autoﬂuorescence quenching, and nuclear staining followed the Xenium Prime In Situ Gene Expression with optional Cell Segmentation Staining (CG000760, 10x Genomics). The Xenium Cell Segmentation Staining Reagents (PN-1000661, 10x Genomics) were used for membrane, cytoplasm and nuclear staining. The assay was performed using the Xenium Prime 5K Human Pan Tissue & Pathways Panel (PN-1000724, 10x Genomics), which targets 5,001 individual human genes. After priming hybridization and RNase treatment & polishing steps, the Xenium slides were incubated with probes at 50 °C for 16-24 h for probe hybridization and then washed with PBS-T. Then the slides were subjected to probe ligation at 42 °C for 30 min, amplification enhancement at 4 °C for 2 h, and amplification at 30 °C for 1.5 h. Following additional washing procedures, the slides underwent cell segmentation staining, then treatment with an auto-ﬂuorescence suppressor and nuclear staining. The slides were loaded onto Xenium Analyzer (PN-1000529, 10x Genomics) according to the Xenium Analyzer User Guide (CG000584, 10x Genomics) and run for about 90 h. The Xenium Onboard Analysis pipeline v.3.1.0 (10x Genomics) was run directly on the instrument for imaging processing, cell segmentation, image registration, decoding, deduplication, and secondary analysis. After that, the slides were washed to perform post-run H&E staining.

## 解读

### 意义
Xenium 5K是10x Genomics的成像型空间转录组平台（iST），使用荧光标记探针和迭代杂交成像技术，单分子精度检测5,001个基因，分辨率达亚细胞水平。该平台提供多通道染色（核、膜、细胞质）支持的细胞分割，在四种平台中表现出最高的细胞类型注释准确性和最强的背景噪声控制能力。

### 输入
- FFPE组织块（5 μm切片，DV200评估RNA质量）
- Xenium载玻片（PN-3000941，最大样本面积10.45 × 22.45 mm）
- Xenium Prime 5K人类泛组织与通路面板（PN-1000724，5,001个基因）

### 输出
- 原始图像数据
- Xenium Onboard Analysis v.3.1.0处理的转录本calls（含Phred质量评分）
- 细胞分割结果、空间坐标文件

### 核心步骤
1. 5 μm FFPE切片附于Xenium载玻片 → 室温30 min干燥 → 42°C烤3 h → 过夜干燥
2. 脱蜡和去交联（CG000580）
3. 引发杂交（50°C，16-24 h）
4. RNase处理和抛光
5. 探针杂交（50°C，16-24 h）→ PBS-T洗涤
6. 探针连接（42°C，30 min）
7. 扩增增强（4°C，2 h）→ 扩增（30°C，1.5 h）
8. 细胞分割染色（膜、细胞质、核）→ 自发荧光淬灭 → 核染色
9. Xenium Analyzer（PN-1000529）上机运行约90 h
10. Xenium Onboard Analysis v.3.1.0机载分析：成像处理→细胞分割→图像配准→解码→去重→二次分析
11. 洗脱后进行H&E复染

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织类型 | FFPE |  |
| 切片厚度 | 5 μm |  |
| 样本面积 | 最大10.45 × 22.45 mm |  |
| 目标基因数 | 5,001 genes | Xenium Prime 5K面板 |
| 探针杂交时间 | 50°C，16-24 h |  |
| 探针连接时间 | 42°C，30 min |  |
| 扩增增强 | 4°C，2 h |  |
| 扩增 | 30°C，1.5 h |  |
| 运行时间 | 约90 h | Xenium Analyzer |
| 质量过滤 | Phred-scaled quality score > 20 |  |
| 分析软件 | Xenium Onboard Analysis pipeline v.3.1.0 |  |
| 分割染色试剂 | PN-1000661 |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Xenium Prime 5K | 10x Genomics高plex成像空间转录组平台 |
| 多通道染色 | 膜、细胞质、核标记，支持全细胞分割 |
| Phred质量评分 | 转录本call质量指标，Q = -10*log10(P_error) |
| 机载分析 | 在Xenium Analyzer仪器上自动完成的完整分析流程 |

## 复现
- 平台：Xenium Analyzer (PN-1000529)
- 载玻片：Xenium Slides (PN-3000941)
- 试剂盒：Xenium Prime 5K Human Pan Tissue & Pathways Panel (PN-1000724)
- 分割染色试剂：Xenium Cell Segmentation Staining Reagents (PN-1000661)
- 操作指南：CG000578, CG000580, CG000584, CG000760
- 分析软件：Xenium Onboard Analysis pipeline v.3.1.0

## 生物学意义
Xenium 5K凭借多通道染色实现的全细胞分割显著提升了细胞边界划定准确性，减少了转录本跨细胞泄漏。本研究中该平台在细胞类型注释一致性、标记基因表达清晰度及与CODEX蛋白数据空间一致性方面均表现最优。

## 涉及 Figures
- **Fig. 1** — 多平台基因检测敏感性比较
- **Fig. 2** — 假阳性评估（背景噪声控制）
- **Fig. 4** — 细胞分割比较
- **Fig. 5** — 细胞聚类与注释准确性比较
