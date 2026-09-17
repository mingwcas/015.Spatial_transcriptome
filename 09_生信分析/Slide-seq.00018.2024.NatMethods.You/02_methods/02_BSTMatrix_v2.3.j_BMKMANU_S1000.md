# Method: BSTMatrix v2.3.j (BMKMANU S1000)

## 原文（Methods）
> BMKMANU S1000 is a technology developed by BMKGENE (https://www.bmkgene.com/). Similar to HDST, it uses barcoded beads deposited on patterned array. Data were processed with BSTMatrix (v2.3.j), and aligned with STAR 2.7.10b.

## 解读

### 意义
BSTMatrix是BMKMANU S1000平台的专用分析管道，用于处理基于图案化阵列和条码珠的空间转录组数据。

### 输入
- 原始FASTQ文件
- BMKMANU S1000芯片上的空间条码信息
- 参照基因组（Mouse GRCm39）

### 输出
- 带有空间坐标的基因表达矩阵
- 质量控制报告

### 核心步骤
1. 解析FASTQ中的空间条码和UMI
2. 使用STAR比对到参考基因组
3. 质量过滤
4. 生成spot-by-gene矩阵

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| BSTMatrix version | v2.3.j | 专用分析管道 |
| aligner | STAR 2.7.10b | 基因组比对工具 |
| reference | Mouse GRCM39 | 小鼠参考基因组 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Barcoded beads | 图案化阵列上的条码磁珠 |
| Patterned array | 具有确定图案的捕获阵列 |

## 复现
- 工具/代码/URL：BMKGENE (https://www.bmkgene.com/)
- 代码：随论文提供的BSTMatrix管道

## 生物学意义
BMKMANU S1000在细胞状态检测方面存在挑战，特别是在识别黑色素细胞时，这可能与观察到的高水平分子横向扩散有关。

## 涉及 Figures
- **Fig. 3** — 分子扩散比较
- **Fig. 4** — 下游性能和聚类结果
