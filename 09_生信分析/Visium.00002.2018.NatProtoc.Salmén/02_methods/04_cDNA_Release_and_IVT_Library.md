# Method: cDNA release, second-strand synthesis and IVT library construction

## 原文（Methods）
> “The cDNA is enzymatically cleaved from the surface and collected in tubes ... a modified version of the CEL-Seq method ... based on in vitro transcription (IVT).” (PDF p.7; Steps 42–88). “The fragment length ... ~300–500 nt” and aRNA is assessed with Bioanalyzer.

## 解读
### 意义
释放空间标记cDNA并以线性IVT扩增保持文库复杂度。
### 输入
表面cDNA、USER/second-strand体系、T7启动子、beads、T7 IVT体系。
### 输出
扩增RNA（aRNA）、其长度/产量QC。
### 核心步骤
1. USER释放（37°C 2 h），收集65 μl。 2. Cy3杂交后成像spot。 3. 二链合成、bead纯化/浓缩。 4. T7 IVT过夜；bead纯化并Bioanalyzer定量。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| release | 37°C，2 h，300 rpm | 从表面释放cDNA |
| aRNA期望 | 主体约300–500 nt；>200 nt且高产为佳 | 文库质量 |
| IVT | 过夜 | 线性扩增 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| IVT | T7 RNA polymerase体外转录扩增 |
| aRNA | amplified RNA |
| Bioanalyzer | 检测RNA长度与产量分布 |

## 复现
- 工具/代码/URL：Agilent Bioanalyzer；CEL-Seq概念（Ref.43–44）。
- 代码片段：不适用。

## 生物学意义
固定造成的约300–500 nt cDNA长度限制有助于减少长度偏倚；低产或短aRNA提示RNA质量、固定/渗透需优化。

## 涉及 Figures
- **Fig. 1、Fig. 3、Fig. 4** — 释放、QC和流程。
