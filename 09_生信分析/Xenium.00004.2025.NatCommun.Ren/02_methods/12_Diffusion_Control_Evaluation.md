# Method: Evaluation of Diffusion Control for Stereo-seq v1.3 and Visium HD FFPE

## 原文（Methods）
> To account for variability in sequencing depth, the total transcript count for each bin was normalized by the mean transcript count across all bins. Diffusion distance was defined as the Euclidean distance from each bin located outside the tissue boundary to its nearest neighboring bin within the tissue, computed using the NearestNeighbors function from the Python package scikit-learn (v.1.5.2). Given the larger chip size of Stereo-seq v1.3 and its potential for long-range transcript diffusion, we restricted our analysis to bins with diffusion distances shorter than the maximum observed in Visium HD FFPE, thereby ensuring comparability across platforms.

## 解读

### 意义
评估测序型空间转录组平台（sST）中转录本扩散（diffusion）程度，即转录本在组织边界外出现的现象，是影响空间定量准确性的关键指标。通过测量组织外bins的转录本丰度与距离关系，量化扩散水平。

### 输入
- Stereo-seq v1.3和Visium HD FFPE的8 μm bin水平表达矩阵
- H&E染色图像（用于定义组织边界）

### 输出
- 组织外bins的标准化转录本计数
- 扩散距离（到最近组织内bin的欧氏距离）
- 扩散水平比值（组织外/组织内平均计数）

### 核心步骤
1. 每个bin的总转录本计数按所有bins的平均值标准化（消除测序深度差异）
2. 使用scikit-learn的NearestNeighbors计算每个组织外bin到最近组织内bin的欧氏距离
3. 限制最大扩散距离分析范围（取两平台中较小的最大距离）确保可比性
4. 绘制扩散距离-标准化转录本计数的关系图
5. 计算组织外bins与组织内bins的平均转录本比值

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 分析分辨率 | 8 μm | bin大小 |
| 标准化 | 按所有bins平均值标准化 | 消除测序深度差异 |
| 距离计算 | NearestNeighbors (scikit-learn v.1.5.2) | 欧氏距离 |
| 最大距离限制 | 两平台中Visium HD的最大扩散距离 | 确保可比性 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 转录本扩散 (Transcript Diffusion) | 转录本出现在其实际细胞外的现象 |
| 扩散距离 | 组织外bin到最近组织内bin的欧氏距离 |
| 组织掩膜 | 基于图像分割组织区域与背景 |

## 复现
- Python包：scikit-learn v.1.5.2
- 图像分割：OpenCV v.4.10.0

## 生物学意义
研究发现Stereo-seq v1.3表现出显著的转录本扩散，约为Visium HD FFPE的3.4倍。这可能与FFPE样本的通透化处理条件及组织固定方式有关，对于准确的空间定量分析构成挑战。

## 涉及 Figures
- **Fig. 2d-f** — 转录本扩散评估
- **Supplementary Fig. 5f-h** — 扩散距离详细分析
