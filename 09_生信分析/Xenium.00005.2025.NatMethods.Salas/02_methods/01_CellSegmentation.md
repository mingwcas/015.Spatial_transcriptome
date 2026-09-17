# Method: Cell Segmentation Benchmarking

## 原文（Methods）
> Segmentation strategies were compared including Cellpose (nuclei and cyto models), binning, clustermap, watershed, Mesmer, Baysor, and Baysor with prior segmentation. Xenium's built-in segmentation outputs (cell and nucleus) were also evaluated. A grid search of 315 configurations was performed across hyperparameters and expansion distances.

## 解读

### 意义
确定最优的细胞分割策略，以准确将转录本分配到正确的细胞中，是空间转录组数据分析的基础步骤。

### 输入
- Xenium 原始转录本坐标数据
- DAPI 核染色图像
- 多种分割算法的输出 masks

### 输出
- 各分割策略的评估指标（ARI、NCP、转录本分配率）
- 最优分割策略推荐

### 核心步骤
1. 运行多种分割算法（Cellpose nuclei/cyto、binning、clustermap、watershed、Mesmer、Baysor）
2. 对每种算法进行网格搜索，测试不同超参数和扩展距离
3. 评估315种配置组合，筛选出各组top 52表现最优者
4. 使用 Adjusted Rand Index (ARI) 比较不同分割输出之间的一致性
5. 计算负标记物纯度 (Negative Marker Purity, NCP) 评估分割质量
6. 统计各策略分配到细胞的转录本比例

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Cellpose models | nuclei, cyto | 核分割 vs 细胞质分割模型 |
| Grid search configs | 315 | 总评估配置数 |
| Top performers | 52 per group | 每组保留的最优配置数 |
| ROI size | 160×160 μm | 评估区域大小 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ARI (Adjusted Rand Index) | 调整兰德指数，衡量两个分割结果的一致性 |
| NCP (Negative Coexpression Purity) | 负共表达纯度，评估细胞中不应表达的基因的表达水平 |
| Cellpose | 基于深度学习的细胞分割算法 |
| Baysor | 基于贝叶斯方法的转录本分割工具 |
| Mesmer | 基于深度学习的细胞核/细胞分割算法 |

## 复现
- 工具/代码：Cellpose (https://github.com/MouseLand/cellpose), Baysor, Mesmer (DeepCell)
- 代码片段：
```python
from cellpose import models
model = models.CellposeModel(gpu=True, model_type='cyto')
masks, flows, styles = model.eval(image, diameter=None)
```

## 生物学意义
细胞分割的准确性直接影响下游细胞类型注释和基因表达分析。错误的分割会导致转录本错误分配，产生假阳性或假阴性的细胞类型标记物，从而影响生物学结论的可靠性。

## 涉及 Figures
- **Fig. 3** — 主要分割策略比较
- **Extended Data Fig. 5** — 扩展分割基准测试
