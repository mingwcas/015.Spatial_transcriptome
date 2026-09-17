# Method: Microenvironment Analysis (Spatial Cell Proximity)

## 原文（Methods）
> This custom analysis aimed to quantify changes in local cell type compositions between DS and euploid in the Slide-seq and MERFISH datasets. For each cell type A (center cell), we identified its closest Ntotal neighboring cells based on spatial coordinates obtained from the spatial transcriptomics data. We calculated the B ratio, which represents the proportion of a specific cell type B (query cell) within these top Ntotal neighboring cells of cell type A, where NB is the number of neighboring cells of type B within the Ntotal nearest neighbors of cell i of type A. In our analysis, we set Ntotal = 100 to capture the immediate cellular microenvironment around each cell. This B ratio allows us to detect whether the local environment of a specific cell type B is enriched or depleted around another cell type A in the DS brain compared to euploid. An increased B ratio in DS indicates a higher local density of cell type B around cell type A. We used the Wilcoxon rank-sum test to assess differences in B ratio distributions between DS and euploid for each cell pair (A-B). A Linear Mixed-Effects Model was applied to account for inter-sample variability, with the B ratio log-transformed for normality.

## 解读

### 意义
微环境分析量化细胞在空间上与其他细胞类型的邻近关系，揭示DS脑中细胞-细胞空间关系的改变，为理解DS皮层发育异常提供空间层面的证据。

### 输入
- Slide-seq或MERFISH的空间坐标数据
- 细胞类型注释
- Ntotal = 100（最近邻细胞数）

### 输出
- B ratio（目标细胞类型在中心细胞邻近的占比）
- DS与整倍体之间的差异
- LOSO（留一受试者-out）验证结果

### 核心步骤
1. 对每个中心细胞类型A，识别其Ntotal=100个最近邻细胞
2. 计算细胞类型B（查询细胞）在Ntotal邻域中的占比（B ratio）
3. Wilcoxon rank-sum检验比较DS与整倍体的B ratio分布
4. 线性混合效应模型控制样本间变异（B ratio对数转换）
5. Benjamini-Hochberg方法多重检验校正
6. LOSO方法迭代验证结果的稳健性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Ntotal | 100 | 最近邻细胞数 |
| 统计检验 | Wilcoxon rank-sum + 线性混合效应模型 | 比较B ratio分布 |
| 多重检验校正 | Benjamini-Hochberg | FDR控制 |
| 显著性阈值 | FDR ≤0.05 | 微环境改变阈值 |
| 验证方法 | LOSO | 留一受试者-out交叉验证 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| B ratio | 目标细胞类型在中心细胞邻域中的占比 |
| LOSO | Leave-One-Subject-Out，留一受试者-out |
| 线性混合效应模型 | 考虑固定效应和随机效应的统计模型 |
| 微环境 | 细胞周围100个最近邻细胞构成的空间生态位 |

## 复现
- 自定义代码：https://github.com/annaminyifeng/Molecular-Cartography-of-DS-Brain
- Code Ocean：https://doi.org/10.24433/CO.4591687.v2

## 生物学意义
微环境分析揭示了DS产前脑中心室区oRG细胞邻近IP细胞减少，以及Ts65Dn小鼠脑中不同发育时间点和脑区微环境的改变。这些发现表明DS中存在细胞空间组织异常，可能与神经发育和迁移受损相关。

## 涉及 Figures
- **Fig. 3** — Cellular compositional changes in VZ and cortex
- **Fig. 6** — Microarchitectural changes in Ts65Dn brain
- **Supplementary Fig. 7** — LOSO validation
