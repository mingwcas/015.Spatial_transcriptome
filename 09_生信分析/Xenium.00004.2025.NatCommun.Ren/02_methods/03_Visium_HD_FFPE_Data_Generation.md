# Method: Visium HD for FFPE Data Generation

## 原文（Methods）
> Visium HD assay is compatible with FFPE-embedded tissues and H&E staining. RNA quality of FFPE samples was assessed by calculating the percentage of RNA fragments >200 nucleotides (DV200) extracted from tissue sections. DAPI and H&E staining were also used to assess tissue morphology before performing the Visium HD assay. Tissue sections were cut at a thickness of 5 μm following the Visium HD FFPE Tissue Preparation Handbook (CG000684, 10x Genomics), spread out in RNA enzyme-free water at 42 °C, and loaded onto the slides prepared in advance (Fisher Scientific #1255015). Subsequently, these slides were air-dried at room temperature for 30 min and baked at 42 °C for 3 h. The subsequent experiments were carried out after drying overnight at room temperature.
> Tissue sections were subjected to deparaffinization, H&E staining, and imaging following the Visium HD FFPE Tissue Preparation Handbook (CG000684, 10x Genomics). Probe hybridization, probe ligation, Visium HD slide preparation, probe release, extension, library construction, and sequencing followed the Visium HD Spatial Gene Expression Reagent Kits User Guide (CG000685, 10x Genomics). The tissue sections were destained and decrosslinked after H&E staining. The human whole transcriptome probe panel, consisting of about three specific probes per target gene, was added to the tissue sections. After hybridization, the Probe Ligation Enzyme (PN-2000425, 10x Genomics) was added to establish connections between the probe pairs hybridized to RNA, resulting in the formation of ligation products. The subsequent release and capture of these probes within the 6.5 × 6.5 mm capture areas were facilitated by the Visium CytAssist instrument following the User Guide. Treatment with RNase Enzyme and Perm Enzyme detached the single-stranded ligation products from the tissue and directed them onto the Visium HD Slide for capture. These ligation products were then elongated by adding the Spatial Barcode, UMI, and partial Read1 primer. Subsequent elution and amplification of the ligation products prepared them for indexing through the sample index PCR. The final libraries were cleaned up by SPRIselect. Sequencing was performed on an Illumina NovaSeq 6000 to obtain paired-end reads.

## 解读

### 意义
Visium HD FFPE是10x Genomics的靶向捕获型测序空间转录组平台，使用poly(dT)寡核苷酸探针靶向18,085个基因，分辨率2 μm，适用于FFPE组织，支持全转录组分析。本研究使用该平台作为sST类别代表之一。

### 输入
- FFPE组织块（5 μm切片）
- DV200指标评估RNA质量
- Visium HD载玻片（Fisher Scientific #1255015，6.5 × 6.5 mm捕获区域）

### 输出
- 配对末端测序数据（Illumina NovaSeq 6000）
- Space Ranger处理后的空间转录组数据

### 核心步骤
1. FFPE切片（5 μm）附于载玻片
2. 空气干燥30 min → 42°C烤3 h → 室温过夜干燥
3. 二甲苯脱蜡 → H&E染色 → 成像
4. 探针杂交（人类全转录组探针面板，每基因约3个探针）
5. 探针连接酶连接成连接产物
6. Visium CytAssist仪器处理 → 6.5×6.5 mm捕获区释放并捕获探针
7. RNase酶和Perm酶处理 → 单链连接产物洗脱
8. 添加Spatial Barcode、UMI、Read1引物 → 延伸
9. 文库构建 → SPRIselect纯化 → NovaSeq 6000测序

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织类型 | FFPE |  |
| 切片厚度 | 5 μm |  |
| 捕获区域大小 | 6.5 × 6.5 mm |  |
| 探针设计 | 每基因约3个特异性探针 | 人类全转录组面板 |
| 目标基因数 | 18,085 genes |  |
| 空间分辨率 | 2 μm |  |
| 测序平台 | Illumina NovaSeq 6000 |  |
| 处理软件 | spaceranger v3.0.0 |  |
| 参考文档 | CG000684, CG000685 (10x Genomics) |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DV200 | >200核苷酸的RNA片段百分比，FFPE样本RNA质量指标 |
| CytAssist | 10x Genomics的空间基因表达试剂盒配套仪器 |
| SPRIselect | 磁珠纯化文库 |
| spaceranger | 10x Genomics的Visium数据处理流程 |

## 复现
- 试剂盒：Visium HD Spatial Gene Expression Reagent Kits (10x Genomics)
- 探针：人类全转录组探针面板
- 仪器：Visium CytAssist
- 耗材：Fisher Scientific #1255015
- 探针连接酶：PN-2000425 (10x Genomics)
- 分析软件：spaceranger v3.0.0
- 操作手册：CG000684, CG000685

## 生物学意义
Visium HD FFPE利用靶向捕获策略，具有较高的转录检测特异性。本研究发现其在灵敏度和特异性方面优于Stereo-seq v1.3，且扩散控制更有效。但因缺乏可靠的细胞分割算法，细胞类型注释能力受限。

## 涉及 Figures
- **Fig. 1** — 多平台基因检测敏感性比较
- **Fig. 2** — 假阳性评估（扩散控制）
