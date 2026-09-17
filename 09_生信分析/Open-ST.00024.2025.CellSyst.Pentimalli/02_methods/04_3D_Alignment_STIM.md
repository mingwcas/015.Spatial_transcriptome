# Method: 3D Alignment of Spatial Transcriptomic Data with STIM

## 原文（Methods）
> To align high-plex, single-cell resolved spatial transcriptomic data from 6 sequential, non-consecutive sections, we leveraged the Spatial Transcriptomics ImgLib2/Imaging Project (STIM). With STIM, we ﬁrst converted our spatial transcriptomics data to the n5 image format for efﬁcient storage and processing using the 'st-resave' function. In doing so, we assigned a channel to each gene and modeled gene expression values as pixel intensities at the center of the segmentation mask. Then, we applied the 'st-align-pairs' function to align each section to the one above and below (r=1) using the Scale Invariant Feature Transform (SIFT) according to the expression of the 15 genes with highest standard deviation (n=15). Finally, we applied the 'st-align-global' function to identify a global optimum that minimizes the distances between all corresponding points across all pairs of slices.

## 解读

### 意义
利用计算机视觉技术将6张不连续切片的空间转录组数据进行3D配准，重建三维分子图谱，使细胞能够在3D空间中被分析。

### 输入
- 6张CosMx切片（sections 4, 10, 16, 22, 28, 34）的单细胞空间转录组数据
- 切片间距30μm

### 输出
- 3D配准后的单细胞分子图谱
- 中位细胞位移42μm的配准精度

### 核心步骤
1. 使用'st-resave'将空间转录组数据转换为n5图像格式（每个基因一个通道，表达值作为像素强度）
2. 使用'st-align-pairs'基于SIFT特征对齐相邻切片（使用标准差最高的15个基因）
3. 使用'st-align-global'找到全局最优对齐，最小化所有切片对应点间的距离
4. 验证呼吸道上皮细胞在3D中的连续性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 工具 | STIM v0.2.0 | 空间转录组3D对齐工具 |
| 数据格式 | n5 | 高效存储和处理的图像格式 |
| 对齐基因数 | 15 | 用于SIFT特征提取的高变异基因数 |
| 配对半径r | 1 | 每张切片与上下各1张切片配对 |
| 全局对齐参数 | --absoluteThreshold 100 --sf 0.5 --lambda 0.5 --skipICP | 全局优化参数 |
| 中位配准精度 | 42 μm | 配准后中位细胞位移 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| STIM | Spatial Transcriptomics ImgLib2/Imaging Project，空间转录组3D对齐工具 |
| SIFT | Scale Invariant Feature Transform，尺度不变特征变换，计算机视觉特征提取算法 |
| n5 | 高性能多维数组存储格式 |
| 3D配准 | 将多个2D切片在三维空间中对齐的过程 |

## 复现
- STIM v0.2.0: Preibisch et al., 2025 (Cell Systems)
- GitHub: https://github.com/PreibischLab/STIM
- 代码: https://github.com/rajewsky-lab/3D_lung
- SIFT特征: Lowe, 1999 (ICCV)

## 生物学意义
3D配准使得跨越多个切片的细胞邻域分析成为可能，揭示了2D切片无法捕捉的空间关系（如树突状细胞niche、T细胞niche的空间连续性）。仅需相对较小的变换（中位位移42μm），说明ROI定位精度高。30μm的切片间距是成本效益的折中策略——最大化3D信息的同时避免重复采样相同细胞。

## 涉及 Figures
- **Fig. 2A** — 3D配准后呼吸道上皮细胞的连续性验证
- **Fig. S2A** — 配准变换的量化
