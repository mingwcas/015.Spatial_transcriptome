# Method: Adapter ligation, second cDNA synthesis, qPCR-guided indexing and library QC

## 原文（Methods）
> “To enable paired-end sequencing, a second sequencing handle must be introduced ... using single-stranded ligation ... another RT is performed.” Before indexing, “a quality-control real-time qPCR ... determine the optimal number of cycles.” (PDF pp.7, 25–27; Steps 89–145).

## 解读
### 意义
引入第二测序接头、控制PCR循环并获得可上机文库。
### 输入
aRNA、aRNA adapter、Superscript III、PCR InPE/index primers、qPCR mix、RNAClean XP beads。
### 输出
带样本index的paired-end文库及Qubit/Bioanalyzer QC。
### 核心步骤
1. aRNA adapter连接并RT。 2. RNAClean XP纯化。 3. qPCR观察扩增峰，峰值循环数减3–4确定index PCR循环。 4. PCR，每样本使用不同index。 5. bead纯化，Qubit和Bioanalyzer测量。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| qPCR程序 | 98°C 3 min；2–25 cycles: 98°C 20 s/60°C 30 s/72°C 30 s | 估算循环 |
| index循环 | qPCR峰值−3或−4；示例11、12、14、17 | 避免过扩增 |
| 成品长度 | 约400–500 bp | 上机文库标准 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| index PCR | 加样本index并扩增文库 |
| qPCR峰值−3/4 | 推荐循环决策规则 |
| Qubit/Bioanalyzer | 浓度/长度双重QC |

## 复现
- 工具/代码/URL：Qubit dsDNA HS、Agilent Bioanalyzer；无代码。
- 代码片段：不适用。

## 生物学意义
合适循环维持复杂度；过短文库可能降低基因组可比对率，低产可增加1–2个循环。

## 涉及 Figures
- **Fig. 3、Fig. 4** — qPCR曲线、文库长度和流程。
