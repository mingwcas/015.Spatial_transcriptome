# Method: Chromatin Loop Analysis

## 原文（Methods）
> Cell type-specific chromatin loops were identified using the following strategy: (1) chromatin loops were called from pseudobulk data for each sample using Peakachu at 10-kb resolution. (2) Chromatin interaction strengths at each loop were then quantified for individual spatial pixel. (3) A one-way ANOVA was performed across cell types for each loop, with loops showing P < 0.05 defined as cell type-specific chromatin loops. Cell type- or cluster-based chromatin loops were identified using Peakachu at 25-kb resolution using the corresponding sequencing depth model.

## 解读

### 意义
鉴定细胞类型特异性的染色质环（chromatin loops），揭示不同细胞类型中基因启动子与远端调控元件之间的特异性相互作用。

### 输入
- 伪批量Hi-C接触矩阵（每个样本）
- 单像素Hi-C数据（带细胞类型注释）
- Peakachu深度学习模型

### 输出
- 细胞类型特异性染色质环列表
- 每个环的统计显著性（ANOVA P值）
- 聚合峰分析（APA）图

### 核心步骤
1. 使用Peakachu在10-kb分辨率下从伪批量数据中调用染色质环
2. 量化每个空间像素中每个环的染色质相互作用强度
3. 对每个环执行跨细胞类型的单因素方差分析（ANOVA）
4. P < 0.05的环定义为细胞类型特异性染色质环
5. 使用25-kb分辨率和相应测序深度模型调用基于聚类的环

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 分辨率 | 10 kb / 25 kb | 接触矩阵的bin大小 |
| 统计阈值 | P < 0.05 | ANOVA显著性阈值 |
| 工具 | Peakachu | 染色质环检测的监督学习框架 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Chromatin loop | 基因组上两个远端区域之间的物理接触 |
| APA | Aggregate Peak Analysis，聚合峰分析，用于验证环的可靠性 |
| Peakachu | 基于监督学习的染色质环检测框架 |
| ANOVA | Analysis of Variance，方差分析 |

## 复现
- 工具/代码/URL
  - Peakachu: https://github.com/tjs233/Peakachu
  - 代码: https://github.com/wangjuan001/Spatial-ATAC-Hi-C (MIT License)
- 代码片段（关键调用，≤10 行）
```python
# Peakachu环调用示例
from peakachu import call_loops
# 伪批量环调用
call_loops(input_cool='pseudobulk.mcool', resolution=10000, model='depth_model.pkl')
# 单像素环强度量化
loop_strength = quantify_pixel_loops(pixel_contacts, loop_list)
```

## 生物学意义
染色质环是基因调控的关键机制，将增强子等远端调控元件与目标基因启动子物理连接。通过在空间背景下鉴定细胞类型特异性染色质环，可以揭示不同细胞类型中基因调控的三维组织基础。例如，本研究发现兴奋性神经元特异性环连接Satb2基因启动子到约1Mb外的远端染色质可及区域，而抑制性神经元特异性环连接Gpr88基因区域。这些发现将3D基因组结构与细胞类型特异性基因表达直接联系起来。

## 涉及 Figures
- **Fig. 3c-h** — 兴奋性和抑制性神经元特异性染色质环示例
- **Fig. 3i** — 细胞类型特异性环的APA图和GO富集分析
- **Fig. 5j** — GBM样本中聚类特异性染色质环
- **Extended Data Fig. 6b** — R6样本细胞类型特异性环的APA图
- **Extended Data Fig. 6c-h** — R8样本细胞类型特异性环分析
