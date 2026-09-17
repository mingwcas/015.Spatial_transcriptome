# Method: Spatial Variable Feature (SVF) Identification

## 原文（Methods）
> Multiple algorithms for identifying spatial variable features (SVFs) were benchmarked, including SpatialDE, SPARK, Moran's I, and other methods. Running times were profiled across different cell numbers. Algorithm performance was evaluated using manually annotated tissue domains as ground truth, with ARI, VI, NMI, and Fowlkes-Mallows Index as metrics.

## 解读

### 意义
鉴定在空间上具有显著变异模式的基因，揭示组织空间结构和细胞间通讯的关键分子特征。

### 输入
- Xenium细胞×基因表达矩阵
- 细胞空间坐标
- 手动注释的组织域标签（ground truth）

### 输出
- 空间可变基因列表及显著性
- 各算法运行时间和性能比较
- 组织域识别的算法排名

### 核心步骤
1. 运行多种SVF鉴定算法（SpatialDE, SPARK, Moran's I等）
2. 在不同细胞数量下测试各算法的运行时间
3. 评估各算法识别组织域的准确性（与手动注释比较）
4. 使用ARI、VI、NMI、FMI四个指标综合评估
5. 预测各算法处理全数据集（~150,000细胞）的运行时间
6. 在小鼠脑组织ROI上验证算法性能

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 细胞数测试范围 | 5,000 - 150,000 | 运行时间评估的细胞数量范围 |
| 评估指标 | ARI, VI, NMI, FMI | 四种聚类/分类一致性指标 |
| 组织域数 | 基于手动分层注释 | 算法预测的域数量参考 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SVF (Spatial Variable Feature) | 空间可变特征，空间表达模式显著的基因 |
| SpatialDE | 基于高斯过程的空间差异表达分析工具 |
| SPARK | 基于统计检验的空间可变基因鉴定工具 |
| Moran's I | 空间自相关统计量 |
| NMI (Normalized Mutual Information) | 标准化互信息 |
| Tissue domain | 组织域，具有相似细胞组成的空间区域 |

## 复现
- 工具/代码：SpatialDE (https://github.com/theislab/spatialde), SPARK
- 代码片段：
```python
import SpatialDE
results = SpatialDE.run(spatial_coords, expression_matrix)
svf_genes = results.query('qval < 0.05')
```

## 生物学意义
空间可变基因是理解组织空间组织的关键。这些基因往往标记不同的功能区域、细胞微环境或发育梯度，对于理解组织功能和疾病机制具有重要意义。

## 涉及 Figures
- **Extended Data Fig. 7** — SVF鉴定算法扩展分析
