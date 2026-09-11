# Method: SPLIT Correction

## 原文（Methods）
> RCTD provides, for each cell, the primary and secondary cell-type labels, along with their weights w1 and w2 = 1 − w1, which reflect the relative contributions of the primary and secondary reference profiles to the observed expression. Using these weights and the reference profiles, we computed a purified expression profile designed to separate the contribution of the primary cell type from the secondary cell type.
> Specifically, for each cell: xdoublet−SPLIT = (w1×ref1)/(w1×ref1 + w2×ref2) ⊙ xobserved
> We call this approach doublet-SPLIT and by default apply it to cells classified as 'doublets_certain' and 'singlets' that showed signs of contamination.
> For cells labeled as 'doublets_uncertain', only the primary cell type is confidently assigned, and we performed a full-SPLIT: xfull−SPLIT = (w1×ref1)/(Σi wi×refi) ⊙ xobserved
> We also implemented a label-correction step termed SPLIT-shift. If a cell has primary label ct1 and secondary label ct2, but its transcriptomic neighborhood is primarily composed of ct2 cells, we assume a potential label swap and perform purification using ct2 as the primary identity.

## 解读

### 意义
SPLIT是本文提出的核心方法，通过RCTD权重和参考图谱分解混合信号，分离污染转录本，提升细胞类型解析的准确性。

### 输入
- RCTD输出的细胞类型标签（primary/secondary）
- RCTD权重w1和w2
- 参考细胞类型的平均表达谱ref1和ref2
- （可选）细胞的转录组学邻域信息（k=10 kNN图）

### 输出
- 校正后的纯化表达谱（xdoublet-SPLIT或xfull-SPLIT）
- SPLIT-shift后的校正表达谱
- 决定哪些细胞需要校正的模式（default或balance_score_based）

### 核心步骤
1. 对每个细胞计算doublet-SPLIT：基于w1/w2比例重新分配转录本
2. 对doublet_uncertain细胞计算full-SPLIT：考虑所有参考类型
3. SPLIT-shift：检查是否存在primary/secondary标签交换
4. 决定哪些细胞需要纯化（default模式或balance_score_based模式）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| SPLIT模式 | doublet/full | doublet用于确定双细胞，full用于不确定情况 |
| balance_score_based | 可选 | 仅对有邻域污染证据的细胞进行纯化 |
| kNN (k) | 10 | 转录组学邻域k值 |
| neighborhood_radius | 15µm | 空间邻域半径（用于SPLIT-shift） |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SPLIT | Spatial Purification of Layered Intracellular Transcripts |
| doublet-SPLIT | 用于确定双细胞混合的SPLIT |
| full-SPLIT | 用于不确定双细胞类型的SPLIT |
| SPLIT-shift | 基于邻域同质性校正标签交换 |

## 复现
- SPLIT R包：https://github.com/bdsc-tds/SPLIT
- 分析pipeline：https://github.com/bdsc-tds/xenium_analysis_pipeline
- 复现分析代码：https://github.com/bdsc-tds/Bilous2026

## 生物学意义
SPLIT解决了空间转录组中的转录本污染问题，使低RNA含量细胞（如T细胞）的真实转录特征得以显现。SPLIT-shift处理了RCTD偶尔将primary/secondary标签交换的情况。该方法使邻近恶性细胞的T细胞耗竭特征得以准确检测。

## 涉及 Figures
- **Fig. 3h** — SPLIT原理示意图
- **Fig. 4** — SPLIT与其他校正方法的比较
- **ED Fig. 7, 8** — SPLIT校正效果的UMAP可视化
