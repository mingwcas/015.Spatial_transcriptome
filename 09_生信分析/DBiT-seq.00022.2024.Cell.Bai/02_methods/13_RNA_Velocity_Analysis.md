# Method: RNA Velocity Analysis

## 原文（Methods）
> Employing scVelo, we delineated transient cellular states of all the identified clusters. We focused our analysis exclusively on the tumor B-cell clusters.

## 解读

### 意义
分析RNA剪接动态，推断细胞状态转换和分化轨迹

### 输入
- 空间转录组数据
- 内含子/外显子读段
- scVelo算法

### 输出
- RNA速度向量
- 细胞状态转换轨迹
- 分化动态

### 核心步骤
1. 内含子/外显子读段区分
2. RNA速度计算
3. 细胞状态推断
4. 分化轨迹分析
5. 驱动基因识别

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 算法 | scVelo | RNA速度分析 |
| 分析对象 | 肿瘤B细胞簇 | 特定细胞类型 |
| 读段类型 | 内含子/外显子 | 未剪接/已剪接 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RNA速度 | 基于剪接状态的细胞动态 |
| scVelo | RNA速度分析工具 |
| 内含子读段 | 来自未剪接RNA的读段 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
RNA速度分析揭示了细胞状态的动态变化，为理解肿瘤分化和进展提供了时间维度信息。

## 涉及 Figures
- **Fig. 5** — Genome-wide spatial variant profiling for differentiating malignant subclones
