# Method: Cell–Cell Communication Analysis

## 原文（Methods）
> Cell–cell communication was inferred using the CellChat R package (v2.1.2). Normalized scRNA-seq data from each metastatic lesion were used to construct independent CellChat objects, and ligand–receptor interactions were analyzed using the built-in human secreted signaling, ECM, and cell–cell contact databases. For each dataset, overexpressed ligands, receptors, and interaction pairs were identified, and communication probabilities were estimated using CellChat's permutation-based statistical framework. Significant interactions (P < 0.05) were retained for downstream analysis, and pathway-level signaling was inferred by aggregating ligand–receptor pairs into curated signaling modules. Communication strength, information flow, and sender/receiver roles were computed using the default pipeline. For comparing pembrolizumab-resistant and -sensitive lesions, communication probabilities were averaged within each group, and differential pathway activity was summarized using log₂ fold-change and CellChat's built-in comparison functions.

## 解读

### 意义
CellChat基于单细胞转录组数据推断细胞间通讯网络，量化配体-受体相互作用强度，揭示免疫治疗响应相关的通讯模式差异。

### 输入
- 各转移灶的normalized scRNA-seq数据
- CellChat R包 v2.1.2
- 内置人类分泌信号、ECM、细胞-细胞接触数据库

### 输出
- 细胞间通讯网络图（Circle plots）
- 通讯强度热图（Sender-Receiver heatmap）
- 差异信号通路分析
- log2FC差异分析结果

### 核心步骤
1. 各转移灶scRNA-seq数据独立构建CellChat对象
2. 使用人类分泌信号、ECM、细胞-细胞接触数据库
3. 识别过表达配体、受体和互作对
4. CellChat置换检验框架估算通讯概率
5. 保留显著互作（P < 0.05）
6. 通路水平信号汇总（聚合为信号模块）
7. 计算通讯强度、信息流、发送者/接收者角色
8. 敏感组vs抵抗组通讯概率比较
9. log2FC差异分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 分析工具 | CellChat R v2.1.2 | |
| 数据库 | 人类分泌信号、ECM、细胞-细胞接触 | 内置 |
| 显著性阈值 | P < 0.05 | |
| 比较方法 | log2FC + CellChat内置比较函数 | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CellChat | 单细胞通讯网络推断工具 |
| 配体-受体互作 | Ligand-Receptor interaction，细胞间信号传导基础 |
| 信息流 | Information flow，网络中信号通路活跃度 |
| Sender/Receiver | 信号发送/接收细胞类型 |
| log2FC | log2 Fold Change，对数倍数变化 |

## 复现
- 工具/URL：https://github.com/sqjin/CellChat
- 代码片段：
```R
library(CellChat)
cellchat <- createCellChat(object = scRNA, group.by = "cell_type")
cellchat <- setDatabase(cellchat, database = "humanSEC")
cellchat <- identifyOverExpressedGenes(cellchat)
cellchat <- identifyOverExpressedInteractions(cellchat)
cellchat <- computeCommunProb(cellchat)
cellchat <- aggregateNet(cellchat)
cellchat <- compareCommunProb(cellchat, group.by = "response_group")
```

## 生物学意义
CellChat揭示了敏感和抵抗肿瘤微环境中细胞间通讯网络的本质差异，特别是SPP1+ TAMs驱动的免疫抑制网络和CD4+ T细胞-NK细胞-巨噬细胞免疫激活网络的对比。

## 涉及 Figures
- **Fig. 5** — 细胞间通讯网络分析，Circle plots、热图、通路分析
- **Supplementary Figure S5** — 单细胞通讯网络补充数据
