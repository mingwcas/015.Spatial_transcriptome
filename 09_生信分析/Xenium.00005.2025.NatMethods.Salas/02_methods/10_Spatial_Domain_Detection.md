# Method: Spatial Domain Detection

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 7 空间域识别
> Spatial map of the manually annotated domains identified in the mouse brain section (ROI2) and the domains identified by different algorithms.

## 解读

### 意义
空间域检测旨在识别组织中具有空间连续性和功能相关性的区域，是理解组织结构和微环境的关键步骤。

### 输入
- 空间转录组数据
- 细胞空间坐标
- 基因表达矩阵

### 输出
- 空间域划分结果
- 每个域的标记基因
- 域间空间关系

### 核心步骤
1. 预处理数据（归一化、HVG 选择）
2. 构建空间邻域图
3. 应用空间域检测算法
4. 评估不同 domain 数量
5. 与手动注释比较

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| N° pred. domains | 5, 6, 10, 14, 16 | 预测的 domain 数量 |
| ROI2 | Mouse brain region 2 | 脑区感兴趣区域 |
| hierarchical annotation | 层次注释 | 多层次组织结构注释 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Spatial domain | 空间域，具有相似表达和空间连续性的区域 |
| ROI | Region of Interest，感兴趣区域 |
| hierarchical annotation | 层次注释，多层次组织结构 |
| domain detection | 域检测，识别空间连续区域 |

## 复现
- 工具/代码/URL：https://github.com/Moldia/Xenium_benchmarking v1.2.0
- 代码片段：
```python
# Spatial domain detection using SPACEL
from spacel import SPACEL
spacel = SPACEL()
spacel.fit(adata, n_domains=10)

# Visualize domains
import squidpy as sq
sq.pl.spatial_scatter(adata, color='spatial_domain')
```

## 生物学意义
空间域检测能够揭示组织的功能分区，帮助理解细胞在不同空间位置的相互作用和功能状态，对于研究组织微环境和疾病机制具有重要意义。

## 涉及 Figures
- **ED Fig. 7** — 空间域检测算法比较，包含手动注释和算法预测的比较
