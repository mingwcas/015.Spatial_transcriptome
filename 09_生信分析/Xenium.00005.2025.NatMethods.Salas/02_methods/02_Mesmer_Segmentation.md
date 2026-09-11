# Method: Mesmer Segmentation

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 5 分割策略比较
> Segmentation strategies were selected to represent different segmentation outputs. Methods on the y-axis were colored depending on the expansion performed after segmentation.

## 解读

### 意义
Mesmer 是 Deepcell 公司开发的深度学习细胞分割方法，结合细胞核和细胞质标记进行高精度的细胞分割，适用于多种组织类型的空间转录组数据。

### 输入
- DAPI 染色图像（细胞核）
- 细胞质标记图像（可选）
- 组织类型参数

### 输出
- 细胞分割掩膜
- 分割后的细胞边界
- 转录本分配结果

### 核心步骤
1. 预处理图像（归一化）
2. 应用 Mesmer 分割模型
3. 可选的细胞膨胀（expansion）处理
4. 生成最终细胞掩膜
5. 转录本分配

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Mesmer | segmentation method | 深度学习分割方法 |
| Expansion | r20, r30, r40 等 | 细胞膨胀半径 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Mesmer | Deepcell 开发的深度学习分割工具 |
| Expansion | 细胞膨胀处理，增加细胞边界范围 |
| r20/r30/r40 | 膨胀半径参数 |

## 复现
- 工具/代码/URL：Mesmer (https://github.com/vanvalenlab/deepcell-applications)
- 代码片段：
```python
# Mesmer segmentation
from deepcell.applications import Mesmer
app = Mesmer()
masks = app.predict(image, compartment='nuclear')
```

## 生物学意义
Mesmer 通过深度学习提供高精度的细胞分割，在复杂组织背景下表现优异，对空间转录组数据的细胞边界识别具有重要价值。

## 涉及 Figures
- **ED Fig. 5** — Mesmer 分割性能评估，包含不同膨胀半径 (r20, r30, r40) 的比较
