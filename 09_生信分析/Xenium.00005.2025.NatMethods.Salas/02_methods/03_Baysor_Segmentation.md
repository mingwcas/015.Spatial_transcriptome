# Method: Baysor Segmentation

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 5 分割策略比较
> Baysor with prior segmentation (Baysor Px.x). Xenium segmentation were also included in the comparison (XENIUM cel, XENIUM nuc).

## 解读

### 意义
Baysor 是一种结合转录本空间分布和细胞分割先验的贝叶斯分割方法，可以利用分割先验（segmentation prior）提高分割准确性，特别适合处理高质量的 Xenium 数据。

### 输入
- 转录本空间坐标
- DAPI 图像（可选）
- 分割先验图像（可选）
- seg.prior 参数（0-1 之间）

### 输出
- 细胞分割掩膜
- 每个细胞的转录本分配
- 分割置信度

### 核心步骤
1. 加载转录本坐标和图像数据
2. 设置分割先验参数（seg.prior）
3. 运行 Baysor 分割算法
4. 生成细胞掩膜
5. 评估分割质量

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| seg.prior | 0.8 | 分割先验强度 |
| seg.prior | 0 | 无先验 |
| Baysor P0.2-P0.99 | 不同先验值 | 先验强度变化 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Baysor | 基于贝叶斯推断的细胞分割工具 |
| seg.prior | segmentation prior，分割先验参数 |
| prior=0.8 | 高分割先验强度 |

## 复现
- 工具/代码/URL：Baysor (https://github.com/MouseLand/Baysor)
- 代码片段：
```python
# Baysor segmentation with prior
baysor segment --transcripts input.csv --image dapi.tiff --prior segmentation.tiff --seg-prior 0.8
```

## 生物学意义
Baysor 通过贝叶斯框架整合转录本空间分布和图像特征，能够在保持分割准确性的同时处理复杂的组织结构，对于空间转录组数据的细胞分割具有重要意义。

## 涉及 Figures
- **ED Fig. 5** — Baysor 分割策略评估，包含不同 seg.prior 参数的比较
