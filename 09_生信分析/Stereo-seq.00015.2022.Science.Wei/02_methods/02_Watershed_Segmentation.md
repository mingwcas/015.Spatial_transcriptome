# Method: Watershed Segmentation for Single-Cell Segmentation

## 原文（Methods）
> To mark the position of individual cells on the section, we performed DNA staining to highlight the nucleus, where newly transcribed pre-mRNAs undergo splicing. Indeed, intron-containing transcripts were observed in nuclear regions and were separated from spliced transcripts. We then used the watershed algorithm to extract transcripts in each nucleus and its surrounding region, in which both nuclear and cytoplasmic transcript-containing areas were included for cell boundary demarcation. In this way, we were able to assign transcripts to individually defined cell areas, achieving single-cell resolution.

## 解读

### 意义
Watershed分割算法结合DNA染色和未剪接/剪接转录本的空间分离，实现了单细胞边界的精确划定，从而将转录本准确分配给每个单细胞。

### 输入
- DNA染色图像（细胞核定位）
- Stereo-seq转录本空间位置数据
- 未剪接和剪接转录本的空间分布

### 输出
- 单细胞分割结果
- 每个细胞的转录本分配
- 单细胞分辨率的表达矩阵

### 核心步骤
1. DNA染色：用DAPI或类似染料对细胞核进行染色
2. 图像配准：将DNB图像与核酸染色图像手动配准
3. 背景去除：去除背景信号
4. 欧氏距离计算：计算染色图像的欧氏距离
5. Watershed分割：使用scikit-image包进行分水岭算法分割
6. 转录本分配：将每个DNB位点的转录本分配到对应的细胞区域

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 每细胞DNB位点数 | ~850 | 分割后每细胞平均包含的DNB数量 |
| 平均UMI/细胞 | 6291 | 单细胞平均检测到的UMI数 |
| 平均基因数/细胞 | 1680 | 单细胞平均检测到的基因数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Watershed algorithm | 分水岭算法，用于图像分割 |
| DNA staining | DNA染色，用于标记细胞核 |
| Un spliced transcripts | 未剪接转录本（含有内含子） |
| Spliced transcripts | 剪接转录本（已去除内含子） |
| DNB | DNA nanoball，DNA纳米球 |

## 复现
- **工具/代码/URL**: 
  - scikit-image: https://scikit-image.org/
  - 参考文献: (53) Pedregosa et al., JMLR 2011
- **代码片段**:
```python
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
# 欧氏距离变换后应用分水岭算法
labels = watershed(-distance_transform, markers)
```

## 生物学意义
单细胞分割是将空间转录组数据精确分配到单个细胞的关键步骤。Watershed算法利用细胞核染色和转录本的空间分布信息，实现了高精度的细胞边界划定。这对于后续的细胞类型注释、空间分布分析和细胞状态转换研究至关重要。

## 涉及Figures
- **Fig. 1B** — 单细胞分割结果展示
