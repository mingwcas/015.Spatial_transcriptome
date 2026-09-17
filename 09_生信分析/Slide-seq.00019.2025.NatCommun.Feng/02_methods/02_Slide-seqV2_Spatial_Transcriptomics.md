# Method: Slide-seqV2 Spatial Transcriptomics

## 原文（Methods）
> Cryosectioning was performed with consideration of anatomical landmarks, specifically targeting regions where the ventricular zone or cortical layers were discernible. OCT-embedded brain tissue was sectioned at a thickness of 10 μm at −21 °C using the CM1950 Leica cryostat and immediately mounted onto a 10×10 mm Slide-seq chip. In cases where the tissue covered less than 50% of the tile, an additional serial section was placed adjacently on the same tile to increase coverage. Libraries were sequenced on a Novaseq X flowcell 10B (100 cycles). Genome alignment, filtration, and normalization were performed using the Curio Seeker bioinformatic pipeline as per the manufacturer's recommendations.

## 解读

### 意义
Slide-seqV2是一种近单细胞分辨率的空间转录组学技术，可将组织切片中的RNA直接转移到带有DNA条形码的珠子表面，通过测序推断RNA的空间位置，解析DS产前人脑的空间转录组架构。

### 输入
- OCT包埋的冰冻脑组织（14-18 PCW；n=3 DS，n=3整倍体）
- 10×10 mm Slide-seq芯片（Curio Bioscience）
- Leica CM1950冰冻切片机

### 输出
- 空间转录组数据（每个珠子的基因表达）
- 细胞类型空间分布图
- RCTD去卷积结果

### 核心步骤
1. 以心室区和皮质层为标志定位脑组织
2. -21°C条件下10 μm厚度切片
3. 立即放置于Slide-seq芯片
4. Novaseq X flowcell 10B测序（100 cycles）
5. Curio Seeker流程进行基因组比对、过滤、标准化
6. RCTD将空间像素去卷积为细胞类型

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 10 μm | 标准空间转录组厚度 |
| 切片温度 | -21 °C | 冰冻切片条件 |
| 芯片规格 | 10×10 mm | Curio Slide-seq芯片 |
| 线粒体基因过滤 | ≥5% 排除 | 排除低质量像素 |
| 最小unique features | ≤200 排除 | 排除低复杂度像素 |
| 去卷积方法 | RCTD | 参照snRNA-seq数据集 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Slide-seqV2 | 新型空间转录组技术，RNA从组织转移到DNA条形码珠子 |
| RCTD | Robust Cell Type Decomposition，空间转录组去卷积方法 |
| Curio Seeker | Curio Bioscience的生物信息分析流程 |
| PCW | Post-Conception Weeks，孕后周数 |

## 复现
- 平台：Curio Bioscience Slide-seq
- 软件：Curio Seeker (GRCh37 genome reference)
- RCTD参考：https://github.com/dmcable/spacexr

## 生物学意义
Slide-seqV2揭示了DS产前脑的空间转录组变化，特别是在心室区oRG细胞邻近IP细胞减少，表明DS中oRG细胞可能发生功能和位置改变，对理解DS皮层发育异常具有重要意义。

## 涉及 Figures
- **Fig. 1** — Spatial representation of DS brain and ventricular zone
- **Fig. 2** — Spatial plots of ROBO1 and SLIT1 expression
