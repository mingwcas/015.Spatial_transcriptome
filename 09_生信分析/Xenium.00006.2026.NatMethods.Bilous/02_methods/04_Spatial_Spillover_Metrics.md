# Method: Spatial Spillover and Contamination Metrics

## 原文（Methods）
> A cell's neighborhood composition is defined as the relative proportion of cell types within a cell's spatial neighborhood. The spatial neighborhood consists of up to 20 nearest cells within a 15-µm radius. Each neighbor is represented by two cell types (primary and secondary) with associated weights defined above (namely w1 and w2), obtained from the RCTD decomposition. Within a neighborhood, weights are aggregated by cell type and normalized to sum to 1, yielding a vector of relative cell-type proportions, referred to as the neighborhood composition.
> The pairwise spillover index is defined as the cosine similarity between a cell's secondary cell-type weight (w2) and the proportion of that same cell type within the cell's spatial neighborhood, computed across all cells sharing a specific primary and secondary cell-type pair.
> The cell-type spillover index is derived by averaging the pairwise spillover indices across all primary cell types for each given secondary (contaminating) cell type.

## 解读

### 意义
量化转录本溢出程度，建立细胞类型污染与空间邻域组成的数学关联，为SPLIT校正提供定量依据。

### 输入
- RCTD输出的每个细胞的w1/w2权重
- 每个细胞的空间邻域信息（20个最近邻，15µm半径）

### 输出
- 细胞对的pairwise spillover index（余弦相似度）
- 每种细胞类型的cell-type spillover index
- 污染信号与空间邻域组成的定量关系

### 核心步骤
1. 定义空间邻域：15µm半径内最近的20个细胞
2. 计算邻域组成：聚合邻域内各细胞类型的w1/w2权重
3. 计算pairwise spillover index：w2与邻域同类型比例的余弦相似度
4. 汇总得到cell-type spillover index
5. 统计显著性检验（置换检验，FDR<0.01）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| neighborhood_radius | 15µm | 空间邻域半径 |
| max_neighbors | 20 | 邻域最大细胞数 |
| permutation_n | 1000 | 置换检验次数 |
| FDR threshold | 0.01 | 显著性阈值 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Spillover index | 转录本溢出指数，衡量污染程度 |
| Cosine similarity | 余弦相似度，衡量向量方向一致性 |
| Neighborhood composition | 空间邻域中各细胞类型的相对比例 |
| w2 | 次细胞类型权重，代表污染信号 |

## 复现
- 工具/代码：https://github.com/bdsc-tds/xenium_analysis_pipeline
- 分析语言：Python/R

## 生物学意义
恶性细胞具有最高的溢出指数，表明其高RNA含量是造成周围细胞污染的主要原因。T细胞等低RNA含量细胞更易被污染。该指标揭示了转录本溢出的空间依赖性特征。

## 涉及 Figures
- **Fig. 3c-e** — Spillover index分析结果
- **ED Fig. 5, 6** — 各panel的spillover index分布
