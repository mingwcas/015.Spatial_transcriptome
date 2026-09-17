# Method: RNA In Situ Hybridization (RNA ISH)

## 原文（Methods）
> We further validated the spatial distribution of Stereo-seq signals for selected marker genes by RNA in situ hybridization (RNA ISH).

## 解读

### 意义
RNA原位杂交是一种在组织切片上验证基因表达空间分布的经典方法，用于验证Stereo-seq数据的准确性和可靠性。

### 输入
- Stereo-seq空间表达数据
- 选择的验证基因（如Sst、Gad2等）
- 相邻连续切片

### 输出
- 基因表达的空间分布图像
- Stereo-seq与RNA ISH的对比验证
- 细胞类型注释验证

### 核心步骤
1. 设计探针：针对目标基因设计特异性探针
2. 组织切片准备：使用与Stereo-seq相邻的连续切片
3. 杂交：探针与目标mRNA杂交
4. 信号检测：酶促显色或荧光检测
5. 对比分析：比较RNA ISH与Stereo-seq的空间分布一致性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 验证基因 | Sst, Gad2, Neurod6, Gad1, Gfap等 | 神经元和EGC标记基因 |
| 对比结果 | 分布模式相似，细胞比例估计一致 | 验证Stereo-seq数据可靠性 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RNA ISH | RNA原位杂交 |
| Stereo-seq | 空间增强分辨率组学测序 |
| Marker genes | 标记基因 |
| Validation | 验证 |

## 复现
- **工具/代码/URL**: 无特定工具（实验方法）
- **代码片段**: 无

## 生物学意义
RNA ISH验证了Stereo-seq数据的可靠性，证明该技术可以像传统RNA ISH一样准确地在单细胞水平解析基因表达的空间分布。这为Stereo-seq在空间转录组学研究中的应用提供了方法学基础。

## 涉及Figures
- **Fig. 1D** — Stereo-seq与RNA ISH对比验证
- **Fig. 1E** — sstIN分布验证
