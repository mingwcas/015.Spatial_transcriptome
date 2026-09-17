# Method: Slide-seq V2 Preprocessing

## 原文（Methods）
> Slide-seqV2 generated bam files of pucks of mouse eyes (Puck 190926 03) and hippocampus (Puck 191204 01 and Puck 200115 08) were downloaded.

## 解读

### 意义
Slide-seq V2是一种基于珠子的空间转录组技术，具有较高的捕获灵敏度。本研究使用已发表的Slide-seq V2数据进行分析。

### 输入
- 预处理的BAM文件（包含空间条码、UMI和比对信息）
- 来自公开数据库的Slide-seq V2 puck数据

### 输出
- 带有空间坐标的基因表达矩阵
- 空间表达模式可视化

### 核心步骤
1. 下载已处理的BAM文件
2. 解析空间条码和UMI
3. 提取比对到基因的reads
4. 生成表达矩阵

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Puck ID (eye) | Puck 190926 03 | 鼠标眼球样本 |
| Puck ID (hippocampus) | Puck 191204 01, Puck 200115 08 | 鼠标海马体样本 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Puck | Slide-seq使用的流通池设备 |
| Barcoded bead | 表面带有空间条码的磁珠 |

## 复现
- 数据来源：已发表的Slide-seq V2数据（公共数据集）
- 处理管道：scPipe (v2.0.0)用于统一处理

## 生物学意义
Slide-seq V2在归一化测序深度后表现出最高灵敏度，在downsampled数据中始终优于其他平台。然而，它在血细胞污染方面最低，有利于更纯净的组织表达谱分析。

## 涉及 Figures
- **Fig. 2** — 灵敏度比较：Slide-seq V2表现最佳
- **Fig. 3** — 扩散比较：Slide-seq V2和V1.5扩散控制较好
