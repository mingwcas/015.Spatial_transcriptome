# 亚细胞定位分析 (Subcellular Localization Analysis)

## 原文 (Methods)

We examined 12,427 (83.1%) and 2533 (16.9%) amplicons in the cytoplasm and nuclei, respectively, and found that nuclear RNA was 2.1 [95% confidence interval (CI) 1.9 to 2.3] times more likely to be noncoding (P < 10−16), and antisense mRNA was 1.8 [95% CI 1.7 to 2.0] times more likely to be nuclear (P < 10−16). We confirmed nuclear enrichment of MALAT1 and NEAT1 by comparing their relative distribution against all RNAs or mitochondrial 16S ribosomal RNA (rRNA), whereas mRNA, such as COL1A1, COL1A2, and THBS1, localized to the cytoplasm.

## 解读

### 意义
亚细胞定位分析是 FISSEQ 技术的独特优势之一。通过将扩增子定位到细胞核或细胞质，可以研究 RNA 的亚细胞分布，揭示基因调控的空间维度。

### 输入
- FISSEQ 测序数据
- 细胞分割结果

### 输出
- 亚细胞定位统计
- 核/质 RNA 比例
- 非编码 RNA 和反义 mRNA 的定位偏好
- 特定基因的亚细胞定位

### 核心步骤
1. **细胞分割**：将细胞分割为细胞核和细胞质区域
2. **扩增子定位**：将扩增子定位到细胞核或细胞质
3. **统计分析**：计算核/质 RNA 比例
4. **差异分析**：比较不同类型 RNA 的定位偏好
5. **基因特异性分析**：分析特定基因的亚细胞定位

### 关键参数
- 细胞质扩增子：12,427 个（83.1%）
- 细胞核扩增子：2,533 个（16.9%）
- 核 RNA 非编码偏好：2.1 倍（95% CI 1.9-2.3）
- 反义 mRNA 核定位偏好：1.8 倍（95% CI 1.7-2.0）

## 名词/参数/指标

| 术语 | 定义 |
|------|------|
| 亚细胞定位 | RNA 在细胞内的空间分布 |
| 非编码 RNA | 不编码蛋白质的 RNA |
| 反义 mRNA | 与 mRNA 互补的 RNA |
| 置信区间 (CI) | 统计估计的可信范围 |

## 复现

### 所需软件
- 图像分割软件
- 统计分析软件
- 空间分析工具

### 所需设备
- 共聚焦显微镜
- 高性能计算设备

## 生物学意义

亚细胞定位分析揭示了：
- 非编码 RNA 优先定位于细胞核
- 反义 mRNA 优先定位于细胞核
- mRNA 主要定位于细胞质
- MALAT1 和 NEAT1 在细胞核中富集
- COL1A1、COL1A2、THBS1 定位于细胞质

这对于理解基因调控、RNA 功能和细胞生物学具有重要意义。

## 涉及 Figures

- **Fig. 3F**: 亚细胞定位富集分析
- **table S2**: MALAT1 和 NEAT1 定位数据
- **table S3**: mRNA 亚细胞定位数据
