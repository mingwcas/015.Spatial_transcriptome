# Method: Immunoﬂuorescence (IF) Imaging and Image Registration

## 原文（Methods）
> The IF workﬂow for FFPE tissues was performed as previously described. FFPE tissue was deparafﬁnized, rehydrated and a two-step antigen retrieval was performed at pH 6 and pH 9 sequentially. Slides were blocked in Odyssey blocking buffer for 30 minutes. Prior to antibody incubation, a pre-bleaching step was performed in 4.5% H2O2 and 24 mM NaOH diluted in PBS for 30 minutes. Images were acquired on a Zeiss Axioscan7 Slide scanner using an EC Plan-Neoﬂuor 20x/0.5 M27 objective with 1x1 binning.

## 解读

### 意义
利用多重免疫荧光成像验证空间转录组鉴定的细胞类型和分子表型（如EMT），并将IF数据与CosMx ST数据配准进行多模态整合。

### 输入
- FFPE组织切片（section 12用于IF，section 10用于CosMx ST）
- 抗体：anti-E-Cadherin (AF488), anti-panCK (eFluor 570), anti-CD68 (PE), anti-IDO (AF647)

### 输出
- 多通道IF图像
- 与CosMx数据配准后的整合分析

### 核心步骤
1. FFPE脱蜡、复水、两步抗原修复（pH 6和pH 9）
2. Odyssey封闭缓冲液封闭30分钟
3. 4.5% H2O2 + 24mM NaOH预漂白30分钟
4. 一抗4°C过夜孵育
5. Hoechst 33342复染、ProLong Diamond封片
6. Zeiss Axioscan7扫描（20x物镜，1x1 binning）
7. ASHLAR算法拼接.czi图像
8. 背景校正（Background_subtraction v0.3.3）
9. wsireg 0.3.7将IF图像配准到CosMx图像

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 扫描仪 | Zeiss Axioscan7 | 全玻片荧光扫描仪 |
| 物镜 | EC Plan-Neofluor 20x/0.5 | 20倍物镜 |
| Binning | 1x1 | 像素合并模式 |
| 拼接工具 | ASHLAR v1.17.0 | 多通道全切片图像拼接 |
| 配准工具 | wsireg 0.3.7 | 全切片图像配准 |
| 封闭液 | Odyssey blocking buffer | LI-COR荧光封闭液 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| IF | 免疫荧光（Immunofluorescence） |
| panCK | 泛细胞角蛋白（pan-Cytokeratin），上皮细胞标记 |
| CDH1 | E-钙粘蛋白，上皮标志物，EMT下调 |
| IDO | 吲哚胺2,3-双加氧酶，免疫抑制酶 |
| ASHLAR | 全切片多通道图像拼接和配准算法 |

## 复现
- ASHLAR v1.17.0: Muhlich et al., 2022 (Bioinformatics)
- wsireg 0.3.7
- Background_subtraction v0.3.3: github.com/SchapiroLabor/Background_subtraction
- Bio-Formats v6.11.1
- Fiji v1.53t
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
IF成像提供了蛋白质水平的验证，弥补了RNA ISH的局限。关键验证包括：panCK+CDH1low细胞在EMT niche中的存在、CD68+巨噬细胞的空间分布。IF与CosMx数据的精确配准使得多模态整合分析成为可能，增强了发现的可信度。

## 涉及 Figures
- **Fig. S1B** — panCK IF与KRT19 ISH共定位验证
- **Fig. S1G** — panCK IF用于上皮细胞注释
- **Fig. S3D** — IF验证树突状细胞niche
- **Fig. S6E** — panCK+CDH1low细胞验证EMT niche
