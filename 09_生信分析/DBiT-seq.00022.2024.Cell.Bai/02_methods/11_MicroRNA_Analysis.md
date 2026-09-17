# Method: MicroRNA Profiling and Analysis

## 原文（Methods）
> In total, Patho-DBiT detected 1,063 microRNAs, peaking at 22 nt in the count of mapped reads. Additionally, miR-122 showed high expression in the liver.

## 解读

### 意义
检测和分析microRNA的空间表达，揭示miRNA调控网络

### 输入
- 空间转录组数据
- miRNA参考数据库
- 靶基因预测数据

### 输出
- miRNA表达矩阵
- 空间miRNA分布图
- miRNA调控网络

### 核心步骤
1. miRNA序列识别
2. miRNA表达定量
3. 空间表达模式分析
4. miRNA靶基因预测
5. 调控网络构建

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 检测数量 | 1,063个miRNA | 检测范围 |
| 读段长度 | 峰值22 nt | miRNA特征长度 |
| 验证方法 | miR-142 KO细胞 | 功能验证 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| microRNA | 小非编码RNA，调控基因表达 |
| miR-142 | 淋巴细胞特异性miRNA |
| 靶基因 | miRNA调控的基因 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
miRNA是重要的基因表达调控因子，空间分辨的miRNA分析揭示了组织特异性的调控网络。

## 涉及 Figures
- **Fig. 1** — Patho-DBiT workflow and spatial whole transcriptome mapping of mouse embryo
- **Fig. 6** — Spatial microRNA regulations in the MALT section
