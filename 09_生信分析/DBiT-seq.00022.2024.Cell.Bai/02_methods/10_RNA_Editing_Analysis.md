# Method: A-to-I RNA Editing Analysis

## 原文（Methods）
> Patho-DBiT also identified spatial isoform distribution, unveiling a distinctive editing ratio landscape across different regions. In line with prior findings, thalamus exhibited a high editing ratio.

## 解读

### 意义
分析RNA中的A-to-I编辑事件，揭示RNA修饰的空间分布

### 输入
- 空间转录组数据
- 参考基因组
- ADAR基因表达数据

### 输出
- A-to-I编辑位点列表
- 空间编辑比率图
- ADAR基因表达图

### 核心步骤
1. RNA编辑位点检测
2. 编辑比率计算
3. 空间编辑模式分析
4. ADAR基因表达关联分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 编辑类型 | A-to-I | 腺苷到肌苷编辑 |
| 检测方法 | 序列比对 | 识别编辑位点 |
| 关联分析 | Spearman相关 | ADAR表达关联 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| A-to-I编辑 | 腺苷脱氨为肌苷的RNA修饰 |
| ADAR | 腺苷脱氨酶，催化A-to-I编辑 |
| 编辑比率 | 编辑位点的编辑程度 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
RNA编辑是重要的转录后修饰，空间分辨的编辑分析揭示了脑区特异性的RNA修饰模式。

## 涉及 Figures
- **Fig. 2** — Spatial co-mapping of gene expression and RNA processing in the mouse brain
