# Method: In Situ Polyadenylation

## 原文（Methods）
> After tissue permeabilization, enzymatic in situ polyadenylation enables detection of uncategorized RNAs. Patho-DBiT detected 47% of reads mapped to uncategorized RNAs. Among these, tRNA, snRNA, and other non-coding RNAs were identified.

## 解读

### 意义
为FFPE组织中降解的RNA分子添加poly(A)尾，使其能够被逆转录和测序检测

### 输入
- 透化后的组织切片
- poly(A)聚合酶
- ATP

### 输出
- 带有poly(A)尾的RNA分子
- 扩大检测的RNA种类范围

### 核心步骤
1. 组织透化处理
2. poly(A)聚合酶反应
3. 为各种RNA类型添加poly(A)尾
4. 逆转录合成cDNA

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 酶 | poly(A)聚合酶 | 添加poly(A)尾 |
| 反应条件 | 优化条件 | 确保高效加尾 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 原位多聚腺苷酸化 | 在组织中原位为RNA添加poly(A)尾 |
| poly(A)尾 | RNA分子3'端的腺苷酸序列 |
| 非编码RNA | 不翻译为蛋白质的RNA分子 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
该方法显著扩展了可检测的RNA种类，包括传统方法难以检测的非编码RNA，为全面研究FFPE组织中的RNA生物学提供了可能。

## 涉及 Figures
- **Fig. 1** — Patho-DBiT workflow and spatial whole transcriptome mapping of mouse embryo
