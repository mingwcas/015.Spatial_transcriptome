# Method: Spatially Non-random Gene Analysis

## 原文（Methods）
> The test for spatial non-randomness was performed as previously described1 with the following modifications. Genes were identified as spatially non-random using a custom MATLAB application. The set of pairwise Euclidean distances between all beads was calculated. Candidate genes for the statistical significance analysis were required to have at least one transcript on at least ten beads...

## 解读

### 意义
Spatially non-random gene analysis在全基因组范围内筛选具有显著空间表达模式的基因，是发现新spatial biomarkers的基础。

### 输入
- Slide-seqV2 DGE matrix
- Bead spatial coordinates (x, y)
- All detected genes

### 输出
- 1,349 spatially non-random genes (P < 0.005)
- Spatial expression patterns for each gene

### 核心步骤
1. **Calculate pairwise distances**: Euclidean distance between all beads
2. **Filter genes**: ≥1 transcript on ≥10 beads
3. **Compare distributions**: True gene vs random sampling (1,000 permutations)
4. **L1 norm test**: Compare distribution of pairwise distances
5. **P-value**: Fraction of random samples closer to mean than true sample
6. **Threshold**: P ≤ 0.005

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Min transcripts | ≥1 | 检测阈值 |
| Min beads | ≥10 | 统计要求 |
| Permutations | 1,000 | 随机采样次数 |
| P-value cutoff | P ≤ 0.005 | 显著空间非随机 |
| 方法 | L1 norm | 分布距离度量 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Spatially non-random | 基因表达的空间分布显著偏离随机 |
| Pairwise distance | 所有bead pairs之间的欧氏距离 |
| L1 norm | 曼哈顿距离，分布差异度量 |
| P-value | 随机采样中优于真实值的比例 |

## 复现
- **工具**: Custom MATLAB application
- **代码**: https://github.com/rstickels/Slide_seqv2
- **参考**: Rodriques et al. Science 2019 (原始方法)

## 生物学意义
识别空间非随机基因是发现spatial biomarkers和理解组织结构背后分子机制的关键步骤。在发育皮层中，这些基因往往与已知的功能域和细胞类型Marker重叠。

## 涉及 Figures
- **Supplementary Dataset 2** — Spatial expression plots for all genes
- **Fig. 3** — Uses spatially non-random genes for analysis
- **Supplementary Table 4** — Gene list
