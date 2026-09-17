# Method: CellPhoneDB v4 (Cell Communication Analysis)

## 原文（Methods）
> CellPhoneDB was applied by transforming mouse genes into their human homologs using the biomaRt package. Using the CellPhoneDB database for cellphone analysis, we conducted using 1,000 random permutations in the analysis following the tutorial. The minimum cell percentage threshold required to consider a gene as expressed in the analysis was set to 0.1, and significance was determined with a p-value threshold of less than 0.05.

## 解读

### 意义
CellPhoneDB是另一种广泛使用的细胞间通讯分析方法，基于配体-受体对的表达推断细胞通讯。

### 输入
- 细胞类型注释结果
- 表达矩阵
- CellPhoneDB数据库

### 输出
- 显著富集的配体-受体相互作用
- 细胞类型对之间的通讯强度

### 核心步骤
1. 将小鼠基因转换为人源同源基因
2. 使用CellPhoneDB数据库分析
3. 1000次随机置换检验
4. 筛选显著相互作用（p < 0.05）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| CellPhoneDB version | v4 | 细胞通讯分析方法版本 |
| Permutations | 1,000 | 随机置换次数 |
| Min cell percentage | 0.1 | 基因表达的最小细胞比例阈值 |
| P-value threshold | < 0.05 | 显著性阈值 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Homolog conversion | 同源基因转换 |
| Permutation test | 置换检验 |

## 复现
- 工具/代码/URL：https://github.com/ventolab/CellphoneDB

## 生物学意义
与CellChat类似，未发现跨平台一致性的细胞通讯结果。

## 涉及 Figures
- **Supplementary Figure 20** — 细胞通讯分析结果
