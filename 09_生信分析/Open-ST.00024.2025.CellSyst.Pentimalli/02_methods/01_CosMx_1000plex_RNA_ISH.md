# Method: CosMx 1000-plex RNA In Situ Hybridization (ISH) for Spatial Transcriptomics

## 原文（Methods）
> CosMx sample processing, staining, imaging, and cell segmentation were performed as previously described. Brieﬂy, tissue sections were placed to VWR Superfrost Plus Micro Slide for optimal adherence. Slides were then dried at 37°C overnight, followed by deparafﬁnization, antigen retrieval and proteinase mediated permeabilization. 1 nM RNA-ISH probes were applied for hybridization at 37°C overnight. After stringent wash, a ﬂow cell was assembled on top of the slide and cyclic RNA readout on CosMx was performed (16-digit encoding strategy). After all cycles were completed, additional visualization markers for morphology and cell segmentation were added including pan-cytokeratin, CD45, CD3, CD298/B2M, and DAPI. Twenty-four 0.985mm × 0.657mm ﬁelds of view (FOVs) were selected for data collection in each slice.

## 解读

### 意义
利用CosMx空间分子成像仪对FFPE临床样本进行1000-plex RNA原位杂交，在单细胞分辨率下同时检测960个癌症相关基因的空间表达，实现肿瘤微环境的高通量分子组织学分析。

### 输入
- 34张连续5μm厚FFPE组织切片（来自NSCLC手术切除标本）
- 每6张切片取1张用于CosMx分析（sections 4, 10, 16, 22, 28, 34），切片间距30μm
- 1000-plex RNA ISH探针（检测960个癌症相关基因 + 20个阴性对照探针）

### 输出
- 单细胞分辨率的空间转录组数据
- 6个ROI区域共155,055,865个转录本
- 340,644个分割细胞（中位数101个基因/细胞，198个转录本/细胞）
- 74.1%的转录本被分配到细胞

### 核心步骤
1. FFPE切片脱蜡、抗原修复、蛋白酶介导的通透处理
2. 1 nM RNA-ISH探针37°C杂交过夜
3. 严格洗涤后组装流动池，进行16轮循环读出（16-digit编码策略）
4. 添加形态学标记物（panCK, CD45, CD3, CD298/B2M, DAPI）用于细胞分割
5. 每张切片采集24个FOV（0.985mm × 0.657mm）
6. 3D多通道图像栈采集（每FOV 9层，步长0.8μm）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 探针浓度 | 1 nM | RNA-ISH探针工作浓度 |
| 杂交温度/时间 | 37°C过夜 | 探针杂交条件 |
| 编码策略 | 16-digit | 循环读出编码位数 |
| FOV尺寸 | 0.985mm × 0.657mm | 每个视野的物理尺寸 |
| 每切片FOV数 | 24 | 每张切片采集的视野数 |
| Z-stack层数 | 9 | 每FOV的Z轴层数 |
| Z步长 | 0.8 μm | Z轴层间距 |
| 切片厚度 | 5 μm | 组织切片厚度 |
| 切片间距 | 30 μm | CosMx分析切片间的物理距离 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CosMx | NanoString空间分子成像仪，基于原位杂交的空间转录组平台 |
| FFPE | 福尔马林固定石蜡包埋（Formalin-Fixed Paraffin-Embedded），临床常规样本保存方式 |
| FOV | 视野（Field of View），成像仪单次采集的区域 |
| DV200 | RNA片段>200nt的百分比，用于评估RNA完整性 |
| panCK | 泛细胞角蛋白（pan-Cytokeratin），上皮细胞标记物 |
| 阴性探针 | 靶向人类组织中不存在序列的探针，用于评估非特异性信号 |

## 复现
- 工具/代码/URL
  - CosMx Spatial Molecular Imager: https://nanostring.com/products/cosmx-spatial-molecular-imager/
  - 原始数据: https://doi.org/10.5281/zenodo.7899173
  - 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
CosMx 1000-plex RNA ISH使得在FFPE临床样本上同时检测近千个基因的单细胞空间表达成为可能。阴性探针仅占检测分子的0.27%，表明检测高度特异。该方法与临床常规FFPE样本兼容（DV200=60%），为从存档临床样本中提取空间分子信息提供了可行路径。局限性在于探针panel为预设的癌症相关基因panel（960个靶基因），非全转录组无偏检测。

## 涉及 Figures
- **Fig. 1** — 展示CosMx分子组织学结果，包括18种细胞类型鉴定和空间分布
- **Fig. S1** — 数据质量评估，包括阴性探针统计、转录本计数相关性、聚类结果
