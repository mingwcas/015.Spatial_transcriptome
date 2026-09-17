# Method: Cross-Platform SRT Comparison

## 原文（Methods）
> Xenium was compared with other spatially resolved transcriptomics (SRT) platforms using matched tissue sections. Gene detection efficiency was quantified as SRT/scRNA-seq ratios across hippocampal and thalamic regions. Pairwise comparisons of detection efficiency between platforms were performed using common genes, with median of ratios as the summary statistic.

## 解读

### 意义
在相同组织样本上系统比较不同空间转录组平台的性能，为平台选择提供客观依据。

### 输入
- 匹配组织切片的多平台SRT数据（Xenium, MERFISH, Slide-seq, 10x Visium等）
- 匹配的单细胞RNA-seq参考数据

### 输出
- 各平台基因检测效率比
- 转录本空间定位精度比较
- 平台间优劣排名

### 核心步骤
1. 在相同脑区（海马、丘脑、皮层）采集多平台SRT数据
2. 计算各平台相对于scRNA-seq的基因检测效率比
3. 对各平台进行配对比较，仅使用共有基因
4. 计算转录本到细胞质心的距离分布（空间定位精度）
5. 对各平台数据进行统一resegmentation后比较
6. 使用负共表达纯度(NCP)评估平台特异性噪声

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 脑区 | hippocampus, thalamus, cortex | 比较的解剖区域 |
| 参考数据 | scRNA-seq | 单细胞RNA-seq作为检测效率基准 |
| 效率比 | SRT/scRNA-seq | 空间方法相对于单细胞方法的检测效率 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Gene detection efficiency ratio | SRT方法检测到的转录本数与scRNA-seq检测数的比值 |
| NCP (Negative Coexpression Purity) | 负共表达纯度，衡量平台特异性噪声 |
| Transcript-to-centroid distance | 转录本到细胞质心的距离，评估空间定位精度 |
| Resegmentation | 对原始数据重新进行细胞分割 |

## 复现
- 工具/代码：自定义Python/R分析脚本
- 代码片段：
```python
# 计算效率比
efficiency_ratio = srt_counts.reindex(common_genes) / scrna_counts.reindex(common_genes)
median_ratio = efficiency_ratio.median()
```

## 生物学意义
不同空间转录组平台在灵敏度、分辨率和噪声水平上存在显著差异。了解各平台的优劣有助于根据具体生物学问题选择最合适的技术方案。

## 涉及 Figures
- **Extended Data Fig. 4** — Xenium与其他SRT平台比较
