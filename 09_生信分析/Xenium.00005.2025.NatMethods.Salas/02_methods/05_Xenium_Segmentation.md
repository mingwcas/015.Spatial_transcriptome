# Method: Xenium Segmentation

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 5 分割策略比较
> Xenium segmentation were also included in the comparison (XENIUM cel, XENIUM nuc).

## 解读

### 意义
Xenium segmentation 是 10X Genomics 官方提供的细胞分割方法，提供细胞（cell）和细胞核（nucleus）两种分割模式，是 Xenium 平台的原生分割方案。

### 输入
- Xenium 原始图像数据
- 转录本位置文件
- 分割模式选择

### 输出
- Xenium 原生细胞分割掩膜
- 细胞边界定义
- 转录本分配

### 核心步骤
1. 加载 Xenium 图像数据
2. 选择分割模式（cell 或 nucleus）
3. 应用 Xenium 分割算法
4. 生成细胞掩膜
5. 转录本分配

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| XENIUM cel | cell segmentation | Xenium 细胞分割模式 |
| XENIUM nuc | nucleus segmentation | Xenium 细胞核分割模式 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Xenium cel | 10X Xenium 细胞分割模式 |
| Xenium nuc | 10X Xenium 细胞核分割模式 |
| Native segmentation | 平台原生分割方案 |

## 复现
- 工具/代码/URL：10X Xenium analysis pipeline
- 代码片段：
```python
# Xenium segmentation via 10X pipeline
# Used Xenium output directly from 10X Genomics official pipeline
```

## 生物学意义
Xenium 原生分割提供了与平台紧密集成的分割方案，是 Xenium 数据分析的重要基线，其分割质量直接影响后续空间转录组分析的准确性。

## 涉及 Figures
- **ED Fig. 5** — Xenium cell 和 nucleus 分割模式的性能评估
