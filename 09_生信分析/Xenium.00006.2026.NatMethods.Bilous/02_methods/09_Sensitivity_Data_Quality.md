# Method: Sensitivity and Data Quality Assessment

## 原文（Methods）
> After applying QC filters to raw or corrected count matrices, standard QC metrics were computed per cell, including the total number of UMIs or reads detected, and the number of genes expressed (defined as genes with >0 counts). Mean and median values for the number of genes expressed per cell, as well as the mean UMI count per cell, were calculated across all cells.
> To assess the biological fidelity of the expression profiles, we compared them with reference Chromium data. Pseudo-bulk expression profiles were generated for each identified cell type in our dataset by summing gene expression across all cells assigned to that type. We then calculated the cosine similarity between log-normalized pseudo-bulk profiles and corresponding cell type profiles derived from Chromium scRNA-seq. The similarity calculation was performed using all shared genes.

## 解读

### 意义
评估数据敏感性和生物学保真度，确保校正方法不会过度删除有效信号，并验证与金标准snRNA-seq的一致性。

### 输入
- 原始或校正后的计数矩阵
- 细胞类型注释
- Chromium snRNA-seq参考图谱

### 输出
- 每个细胞的UMI数和表达基因数
- Pseudo-bulk表达谱与Chromium参考的余弦相似度
- 数据质量指标（均值、中位数）

### 核心步骤
1. 应用QC过滤
2. 计算每个细胞的UMI总数和表达基因数
3. 对每种细胞类型生成pseudo-bulk表达谱（所有细胞表达求和）
4. Log标准化
5. 计算与Chromium参考的余弦相似度
6. 使用共有基因进行分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| min.genes | 5-10 | 最小表达基因数（QC阈值） |
| min.counts | 10 | 最小UMI数（QC阈值） |
| gene expressed | >0 counts | 表达基因定义 |
| cosine similarity | - | 与Chromium相似度计算 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| UMI counts | 原始分子标签计数 |
| Pseudo-bulk | 同类型细胞的表达谱汇总 |
| Cosine similarity | 衡量表达谱相似度 |
| Biological fidelity | 生物学保真度 |

## 复现
- 工具：Python/NumPy, scikit-learn
- 代码：https://github.com/bdsc-tds/xenium_analysis_pipeline

## 生物学意义
敏感性分析确保校正方法不会过度删除有效信号。余弦相似度与Chromium参考比较验证了数据的生物学真实性。SPLIT校正后相似度提高，表明污染减少、生物学保真度提升。

## 涉及 Figures
- **Fig. 4c,d** — 细胞数和基因数比较
- **Fig. 4f** — Xenium与Chromium T细胞pseudo-bulk的余弦相似度
