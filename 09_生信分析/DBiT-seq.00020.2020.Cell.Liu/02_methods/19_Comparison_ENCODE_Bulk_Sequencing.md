# Method: Comparison with ENCODE Bulk Sequencing Data

## 原文（Methods）
> Public bulk RNA-Seq datasets were downloaded from ENCODE (liver, heart and neural tube from mouse embryo E11.5) and the raw expression counts were normalized with FPKM. For DBiT-seq data, ''pseudo-bulk'' gene expression profiles were obtained by summing counts for each gene in each tissue region and divided by the sum of total UMI counts in this specific region, and further multiplied by 1 million. The scatterplots were plotted using log10(FPKM+1) value for bulk data and log10(pseudo gene expression+1)) for DBiT-seq data. Pairwise Pearson correlation coefficients were calculated. Good correlations (r > 0.784) were observed between the two different sets of data.

## 解读

### 意义
该方法通过与ENCODE公共bulk RNA-seq数据对比，验证DBiT-seq数据的准确性和可靠性。

### 输入
- ENCODE bulk RNA-seq数据（E11.5小鼠胚胎的liver, heart, neural tube）
- DBiT-seq的pseudo-bulk数据（按组织区域汇总）

### 输出
- DBiT-seq与ENCODE bulk数据的散点图
- Pearson相关系数（r > 0.784）

### 核心步骤
1. 从ENCODE下载公共bulk RNA-seq数据
2. Bulk数据用FPKM标准化
3. DBiT-seq数据：汇总每个组织区域的每个基因counts
4. 除以该区域总UMI counts，再乘以1,000,000（转换为类似CPM）
5. Bulk数据取log10(FPKM+1)
6. DBiT-seq数据取log10(pseudo expression+1)
7. 绘制散点图，计算Pearson相关系数

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Bulk标准化 | FPKM | 每千碱基每百万映射reads |
| DBiT-seq标准化 | Pseudo-bulk CPM | 区域汇总后标准化 |
| 相关性阈值 | r > 0.784 | 良好相关性 |
| 组织 | liver, heart, neural tube | E11.5小鼠胚胎 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| FPKM | Fragments Per Kilobase Million，基因长度标准化的表达量 |
| CPM | Counts Per Million，总counts标准化 |
| Pseudo-bulk | 将像素汇总模拟bulk样本 |
| Pearson correlation | 线性相关度量 |

## 复现
- 工具/代码/URL：ENCODE (https://www.encodeproject.org/)
- 关键调用：NA

## 生物学意义
与公共金标准数据的高度相关性（r > 0.784）证明了DBiT-seq数据的可靠性。这对于新技术的验证至关重要，表明尽管DBiT-seq是空间分辨的技术，其定量准确性与传统bulk RNA-seq相当。

## 涉及 Figures
- **Fig. S6** — ENCODE bulk RNA-seq与DBiT-seq pseudo-bulk对比
