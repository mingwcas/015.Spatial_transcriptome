# Method: Spatial Latent Time Analysis

## 原文（Methods）
> Spatially identified genes were binned along 20 spatial contours of the same LT as fitted by the surface described above. Expression was normalized for each bin by the total number of counts observed. For each gene, the Pearson correlation coefficient and the P value of the correlation between the binned expression in the spatial LT axis was correlated with a linear function of slope 1.

## 解读

### 意义
Spatial LT analysis将scVelo的latent time投影到物理空间，创建"spatial trajectory"来识别沿发育轨迹差异表达的基因。

### 输入
- scVelo latent time values per bead
- Spatial coordinates (x, y) per bead
- 1,349 spatially non-random genes

### 输出
- 1,043 genes significantly correlated with spatial LT (pFDR < 0.005)
- Spatial LT surface (3D fitted surface)
- Rate of differentiation across cortex

### 核心步骤
1. **Fit 3D surface**: (x, y, LT) → surface using MATLAB differentiate function
2. **Bin genes by LT**: 20 spatial contours
3. **Normalize expression**: By total counts per bin
4. **Correlate with LT**: Pearson correlation against linear function (slope=1)
5. **Multiple testing correction**: FDR q < 0.005

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| LT bins | 20 contours | 分 bin 数量 |
| Grid size | 80 μm × 80 μm | 表面拟合网格 |
| Correlation | Pearson r | 与 linear LT 相关 |
| Significance | pFDR < 0.005 | 筛选阈值 |
| Spatial LT genes | 1,043 / 1,349 | 显著 genes |

## 名词/参数/参数/指标
| 名词 | 定义 |
|------|------|
| Spatial LT surface | 将LT值拟合到物理空间的3D曲面 |
| Spatial derivative | 曲面在各点的斜率，反映发育速率 |
| 3D surface fitting | MATLAB differentiate function |
| pFDR | Proportion of false discoveries |

## 复现
- **工具**: MATLAB 2017a (surface fitting), Python (correlation analysis)
- **代码**: Custom Python scripts
- **scVelo**: https://github.com/theislab/scvelo (v0.1.25)

## 生物学意义
Spatial LT分析发现发育早期（VZ-SVZ/IZ）变化速率最快，随着细胞进入CP逐渐减缓。这揭示了发育时间与空间位置的对应关系，对理解cortical development有重要意义。

## 涉及 Figures
- **Fig. 3b** — Arrow magnitude = spatial derivative of LT
- **Fig. 3c** — Sample genes correlated with spatial LT
- **Fig. 3d** — 2D density plot of correlation vs significance
- **Supplementary Table 4** — 1,349 spatially varying genes
