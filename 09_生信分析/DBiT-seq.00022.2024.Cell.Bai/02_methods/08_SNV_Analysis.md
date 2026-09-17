# Method: Genome-wide Spatial Variant Profiling

## 原文（Methods）
> Genome-wide detection of spatial SNV distribution distinguishes malignant subclones. We hypothesized that Patho-DBiT could effectively capture sequence variations printed in pre-mRNA transcripts.

## 解读

### 意义
检测RNA中的单核苷酸变异，区分恶性亚克隆

### 输入
- 空间转录组数据
- 参考基因组
- 变异检测参数

### 输出
- SNV空间分布图
- 亚克隆识别结果
- 克隆演化关系

### 核心步骤
1. RNA序列变异检测
2. 空间SNV分布映射
3. 亚克隆识别
4. 克隆关系推断
5. 染色体变异分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 变异类型 | SNV | 单核苷酸变异 |
| 覆盖范围 | 全基因组 | 广泛检测 |
| 分析方法 | 空间分辨 | 保留位置信息 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SNV | 单核苷酸变异 |
| 亚克隆 | 肿瘤内的不同细胞群体 |
| 克隆演化 | 肿瘤细胞的进化关系 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
该方法揭示了肿瘤内部的异质性和演化过程，为理解肿瘤进展提供了新视角。

## 涉及 Figures
- **Fig. 5** — Genome-wide spatial variant profiling for differentiating malignant subclones
