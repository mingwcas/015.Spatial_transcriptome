# Method: Correlation Between ST and CODEX Data

## 原文（Methods）
> We evaluated the concordance between CODEX-based cell annotations and ST-derived features including: (1) individual marker gene expression, (2) cell-type-specific gene signatures, and (3) cell type abundance. To construct gene signatures, we selected the top 15 differentially expressed genes for each cell type from matched scRNA-seq data, and retained those present in at least two tissue types. To mitigate platform-specific gene panel differences, we intersected these genes with common genes shared by all four ST platforms. The shared regions of ST and CODEX data were binned at multiple spatial resolutions (100, 200, 300, 400, and 500 μm). For each spatial bin, we quantified ST-derived features at all three levels, alongside corresponding cell counts inferred from CODEX. Pearson correlation coefficients were then computed across all spatial bins to assess the spatial concordance between the ST-derived features and CODEX annotations. Smooth muscle cells (SMCs) and fibroblasts identified by the ST platforms were both categorized as fibroblasts in alignment with CODEX data, as they all express ACTA2, which encodes α-SMA—the marker used to annotate fibroblasts in the CODEX data.

## 解读

### 意义
在空间网格水平评估ST平台与CODEX蛋白数据之间的一致性，从三个层面（单个标记基因、细胞类型特征基因、细胞类型丰度）全面评估各ST平台的空间定量准确性。

### 输入
- ST平台空间表达数据
- CODEX细胞类型注释和蛋白表达数据
- scRNA-seq差异表达基因

### 输出
- 跨空间分辨率（100-500 μm）的Pearson相关系数
- 各细胞类型的空间一致性评分

### 核心步骤
1. 从scRNA-seq数据选择每种细胞类型的top 15差异表达基因
2. 保留在≥2种组织类型中存在的基因
3. 与四平台共享基因交集以消除平台特异性基因面板差异
4. 在共享区域将ST和CODEX数据按多空间分辨率（100, 200, 300, 400, 500 μm）分bins
5. 量化每个空间bin的三级ST特征：
   - 单个标记基因表达
   - 细胞类型特征基因 scores
   - 细胞类型丰度
6. 计算ST特征与CODEX注释的Pearson相关系数
7. SMC和fibroblast统一为fibroblast（均表达ACTA2/α-SMA）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 特征基因数 | 每种细胞类型top 15 DEGs | 来自scRNA-seq |
| 基因过滤 | ≥2种组织类型存在 |  |
| 空间分辨率 | 100, 200, 300, 400, 500 μm | 多尺度分析 |
| 一致性指标 | Pearson相关系数 |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 细胞类型特征基因 | Cell-type signature genes，定义某细胞类型的基因集 |
| 空间一致性 | ST转录组与CODEX蛋白的空间分布相关性 |
| SMC | Smooth Muscle Cell，平滑肌细胞 |

## 复现
- 分析工具：Python (numpy, scipy, pandas, scanpy)
- 无需特殊软件，标准统计计算

## 生物学意义
研究发现Visium HD FFPE和Xenium 5K与CODEX表现出更高的空间一致性，证明了其在空间定量方面的准确性。该分析还揭示了不同细胞类型间的一致性差异：上皮细胞因分布广泛且丰度高，平台间差异较小；而免疫细胞因体积小，各平台检测能力差异更显著。

## 涉及 Figures
- **Fig. 3b, c** — 转录本-蛋白相关性
- **Fig. 5e, f** — 细胞类型丰度与CODEX的相关性
- **Supplementary Fig. 7e, f** — 各类细胞与CODEX的相关性
