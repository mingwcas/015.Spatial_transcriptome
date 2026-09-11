# Method: Data Preprocessing

## 原文（Methods）
> scRNA-seq data were processed with cellranger (v.7.0.0). Visium HD FFPE data were processed with spaceranger (v.3.0.0). Stereo-seq v1.3 data were processed with SAW (v.8.0). GRCh38 was used as the reference genome. For Xenium 5K, we retained the calls with Phred-scaled quality scores higher than 20. The calls from CosMx 6K underwent filtration based on the methodologies described in the previous study24. The morphology staining images of all field of views from CosMx 6K were stitched using napari-cosmx (https://github.com/Nanostring-Biostats/CosMx-Analysis-Scratch-Space). We performed tissue masking to remove the calls located outside the tissue using the Python package OpenCV (v.4.10.0) for both Xenium 5K and CosMx 6K. To enable a fair comparison, we binned the data from Stereo-seq v1.3, CosMx 6K, and Xenium 5K at a resolution of 8 μm, and used the 8 μm resolution output of Visium HD FFPE for basic metric evaluations.

## 解读

### 意义
数据预处理将各平台原始数据统一化为可比较的分析格式，包括质控过滤、组织掩膜去除背景信号、统一空间分辨率（8 μm bin），为后续跨平台比较奠定基础。

### 输入
- 各平台原始测序/图像数据
- 细胞ranger/spaceranger/SAW输出

### 输出
- 质控后的表达矩阵
- 组织掩膜过滤后的空间转录组数据
- 8 μm分辨率的bin-level数据

### 核心步骤
1. 各平台数据分别处理：
   - scRNA-seq: cellranger v.7.0.0
   - Visium HD FFPE: spaceranger v.3.0.0
   - Stereo-seq v1.3: SAW v.8.0
   - Xenium 5K: 保留Phred质量评分 > 20的calls
   - CosMx 6K: 按He et al., 2022方法过滤calls
2. CosMx 6K所有视野的形态学染色图像拼接（napari-cosmx）
3. Xenium 5K和CosMx 6K进行组织掩膜过滤（OpenCV v.4.10.0），去除组织外信号
4. 为公平比较，将Stereo-seq v1.3、CosMx 6K、Xenium 5K数据统一为8 μm分辨率
5. 使用GRCh38作为参考基因组

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 参考基因组 | GRCh38 | 人类参考 |
| Xenium 5K质量阈值 | Phred-scaled quality score > 20 |  |
| 比较分辨率 | 8 μm | 所有平台统一 |
| cellranger版本 | v.7.0.0 | scRNA-seq |
| spaceranger版本 | v.3.0.0 | Visium HD FFPE |
| SAW版本 | v.8.0 | Stereo-seq v1.3 |
| OpenCV版本 | v.4.10.0 | 组织掩膜 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 组织掩膜 (Tissue Masking) | 识别并去除组织外背景信号的步骤 |
| bin | 空间上的规则网格单元，用于平台间比较 |
| Phred质量评分 | Q = -10×log10(P_error)，常用于过滤低质量reads |

## 复现
- cellranger: v.7.0.0 (10x Genomics)
- spaceranger: v.3.0.0 (10x Genomics)
- SAW: v.8.0 (STOmics/BGI)
- OpenCV: v.4.10.0 (Python)
- napari-cosmx: GitHub (Nanostring-Biostats)
- GRCh38参考基因组

## 生物学意义
统一预处理流程确保了四种平台数据的可比性。8 μm分辨率是生物学上有意义的单位，接近小免疫细胞的典型直径，使得跨平台敏感性、特异性和扩散控制的公平比较成为可能。

## 涉及 Figures
- **Fig. 1** — 8 μm bin水平的敏感性比较
- **Fig. 2** — 8 × 8 μm水平的假阳性评估
