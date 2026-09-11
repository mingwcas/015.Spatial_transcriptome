# Method: CosMx 6K Data Generation

## 原文（Methods）
> CosMx 6K assay is compatible with FFPE-embedded tissues and H&E staining. RNA quality of the tissue block was assessed by calculating the percentage of RNA fragments >200 nucleotides (DV200) extracted from tissue sections. DAPI and H&E staining were also used to assess tissue morphology before performing the CosMx 6K assay. Tissue sections were cut at a thickness of 5 μm following the CosMx SMI Manual Slide Preparation for RNA Assays (MAN-10184-02, NanoString Technologies), spread out in RNase-free water at 42 °C, and attached to the slides (CIITOTEST #188105) within the scan area (with a maximum size of 2.0 × 1.5 cm). The slides were dried at room temperature for 30 min and baked at 65 °C for 30 min. The follow-up experiment was carried out after drying overnight at room temperature.
> Deparafﬁnization, target retrieval, protease digestion, blocking, hybridization, stringent washing, blocking, nuclear and segmentation markers staining, and imaging followed the CosMx SMI Manual Slide Preparation for RNA Assays (MAN-10184-02, NanoString Technologies). Human 6K Discovery Panel, 6K-plex, RNA (#121500041, NanoString Technologies) was used. The tissue sections were deparafﬁnized, subjected to target retrieval at 100 °C for 15 min, treated with protease for digestion at 40 °C for 30 min, incubated with applied fiducials for 5 min, post-fixed, blocked, and incubated with the human 6K Discovery Panel overnight. The slides were washed and blocked, followed by nuclear staining. Then the sections were incubated with Marker Stain Mix (PanCK, CD45) and Cell Segmentation Mix (CD298, B2M) using CosMxTM Human Universal Cell Segmentation Kit (RNA) (121500020, NanoString Technologies). The slides were washed again and loaded onto the CosMx SMI system (cat #101000, S/N: SMI_2307H0124) for UV bleaching, imaging acquisition, cycling processing, and scanning according to the Instrument User Manual (MAN-10161-05, NanoString Technologies). The raw images were subsequently decoded using Atomx (v.1.3.2). Finally, the slides were washed to perform post-run H&E staining.

## 解读

### 意义
CosMx 6K是NanoString的成像型空间转录组平台（iST），使用荧光探针和迭代杂交成像技术，检测6,175个基因，提供单分子精度空间信息。本研究中使用该平台作为iST类别代表之一，与Xenium 5K进行直接比较。

### 输入
- FFPE组织块（5 μm切片，DV200评估RNA质量）
- 扫描面积最大2.0 × 1.5 cm的载玻片（CIITOTEST #188105）
- Human 6K Discovery Panel (#121500041, NanoString, 6,175个基因)
- 细胞分割试剂盒：CosMx™ Human Universal Cell Segmentation Kit (RNA) (#121500020)

### 输出
- 原始显微镜图像
- Atomx (v.1.3.2)解码后的转录本calls
- 细胞分割结果

### 核心步骤
1. 5 μm FFPE切片附于载玻片 → 室温30 min干燥 → 65°C烤30 min → 过夜干燥
2. 脱蜡 → 靶标Retrieval（100°C，15 min）→ 蛋白酶消化（40°C，30 min）
3. 应用fiducials（5 min）→ 后固定 → 封闭
4. 与人类6K Discovery Panel杂交过夜
5. 洗涤 → 封闭 → 核染色
6. Marker Stain Mix (PanCK, CD45)和Cell Segmentation Mix (CD298, B2M)染色
7. CosMx SMI系统（#101000）上机：UV漂白 → 成像采集 → 循环处理 → 扫描
8. Atomx (v.1.3.2)解码原始图像
9. 洗脱后H&E复染

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织类型 | FFPE |  |
| 切片厚度 | 5 μm |  |
| 扫描面积 | 最大2.0 × 1.5 cm |  |
| 目标基因数 | 6,175 genes | Human 6K Discovery Panel |
| 蛋白酶消化 | 40°C，30 min |  |
| 靶标Retrieval | 100°C，15 min |  |
| 杂交 | 过夜 |  |
| 分割试剂 | CosMx™ Human Universal Cell Segmentation Kit (#121500020) |  |
| 分割标记 | CD298, B2M（核/细胞质） |  |
| 形态学染色 | PanCK, CD45（膜） |  |
| 解码软件 | Atomx v.1.3.2 |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CosMx SMI | Spatial Molecular Imager，NanoString的成像型空间转录组平台 |
| Atomx | CosMx图像解码软件 |
| PanCK | Pan-Cytokeratin，上皮细胞/肿瘤细胞膜标记 |
| CD45 | 白细胞共同抗原，免疫细胞标记 |
| CD298, B2M | 细胞分割用核/质标记 |

## 复现
- 试剂：Human 6K Discovery Panel, 6K-plex, RNA (#121500041)
- 分割试剂盒：CosMx™ Human Universal Cell Segmentation Kit (RNA) (#121500020)
- 仪器：CosMx SMI system (#101000, S/N: SMI_2307H0124)
- 载玻片：CIITOTEST #188105
- 操作手册：MAN-10184-02, MAN-10161-05 (NanoString Technologies)
- 解码软件：Atomx v.1.3.2

## 生物学意义
CosMx 6K虽然检测到较高总转录本数，但表现出较高的背景噪声和负对照信号，且与scRNA-seq的基因水平相关性低于Xenium 5K。研究表明其对低丰度基因的假阳性检测风险较高，可能降低注释保真度。

## 涉及 Figures
- **Fig. 1** — 多平台基因检测敏感性比较
- **Fig. 2** — 假阳性评估（背景噪声）
- **Fig. 4** — 细胞分割比较
- **Fig. 5** — 细胞聚类与注释准确性比较
