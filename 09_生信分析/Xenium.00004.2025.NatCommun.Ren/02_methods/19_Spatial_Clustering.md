# Method: Spatial Clustering of ST and CODEX Data

## 原文（Methods）
> CellCharter was used to perform spatial clustering on both ST and CODEX data. CODEX enables accurate measurement of marker protein distribution across major cell types, providing a reliable reference for tissue architecture. Given this, we leveraged the optimal number of clusters derived from CODEX data to guide the clustering of ST data. For HCC, CD34, CD4, FOXP3, and HLA-A channels were excluded from CODEX clustering due to quality concerns. To investigate the clustering concordance between CODEX and ST data, we computed cell proportions within spatial grids (100, 200, 300, 400, and 500 μm) for each cluster and assessed their correlations across all grids. For each CODEX cluster, we identified the best-matching ST cluster based on the maximal correlation, and the final metric was defined as the average correlation across all matched cluster pairs.

## 解读

### 意义
使用CellCharter进行空间聚类，评估各ST平台在空间域识别方面的能力。通过将CODEX聚类数量作为参考，比较各ST平台在解析组织空间结构方面与蛋白组学的一致性。

### 输入
- ST平台细胞水平数据
- CODEX聚类结果（作为ground truth）
- 空间网格（100-500 μm）

### 输出
- 空间聚类结果
- 各ST聚类与CODEX聚类的最优匹配相关性
- 平均聚类一致性

### 核心步骤
1. 使用CellCharter对CODEX数据进行空间聚类，确定最优聚类数
2. 使用相同聚类数对各ST平台数据进行空间聚类
3. HCC分析中排除CD34, CD4, FOXP3, HLA-A通道（质量原因）
4. 计算每个空间网格（100-500 μm）中各聚类的细胞比例
5. 评估所有网格上的相关性
6. 每个CODEX聚类匹配相关性最高的ST聚类
7. 最终指标：所有匹配聚类对的平均相关性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 聚类工具 | CellCharter | 空间聚类专用 |
| 空间网格 | 100, 200, 300, 400, 500 μm | 多尺度分析 |
| HCC排除通道 | CD34, CD4, FOXP3, HLA-A | 质量原因 |
| 聚类数 | 采用CODEX最优聚类数 | 指导ST聚类 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CellCharter | 专门用于空间转录组数据聚类分析的工具 |
| 空间聚类 | 识别空间上连续的细胞群（niches） |
| 最优匹配 | 基于最大相关性的一对一聚类匹配 |

## 复现
- CellCharter (用于空间聚类分析)
- 无需特殊参数设置

## 生物学意义
研究发现所有ST平台与CODEX在空间聚类方面表现出相当的一致性，但Stereo-seq v1.3在HCC中一致性较低，提示平台特定局限性可能影响特定组织的表现。空间聚类还揭示了肿瘤核心与边界的空间分布差异，以及肿瘤浸润性CD8+ T细胞的特殊空间模式。

## 涉及 Figures
- **Fig. 6a, b** — 空间聚类一致性与恶性细胞分布
- **Supplementary Fig. 15** — 空间聚类详细结果
