# Method: Surface capture, reverse transcription and tissue removal

## 原文（Methods）
> “The tissue is permeabilized ... mRNA molecules hybridize to the capture probes ... Reverse transcription is then performed overnight ... followed by enzymatic degradation and removal of the tissue.” (PDF p.5; Steps 30–40). RT uses Superscript III; overnight or at least 6 h at 42°C.

## 解读
### 意义
将组织中poly(A) RNA按空间spot捕获并原位转成cDNA。
### 输入
已固定/染色/成像组织、条码oligo-dT probes、pepsin、RT mix、proteinase K（纤维组织可加β-mercaptoethanol）。
### 输出
array表面的空间条码cDNA；去除组织后的洁净array。
### 核心步骤
1. pepsin渗透。 2. 70 μl RT mix覆盖subarray，42°C至少6 h/过夜。 3. 非纤维组织proteinase K 56°C 1 h；纤维组织β-ME后proteinase K各56°C 1 h。 4. 50°C/室温洗涤。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| RT | 42°C，6–15 h | 生成表面cDNA |
| RT酶 | Superscript III 20 U/μl | 高敏感度 |
| 去组织 | 56°C，300 rpm，1 h | 暴露cDNA |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| poly(A) capture | oligo-dT与mRNA poly(A)尾杂交 |
| spatial barcode | 每spot唯一序列，提供坐标 |
| UMI | 分子标签，用于去扩增重复 |

## 复现
- 工具/代码/URL：实验流程；参见 Fig.1。
- 代码片段：不适用。

## 生物学意义
在不解离组织的情况下保留空间信息；100 μm spot通常覆盖5–100个细胞，非单细胞分辨率。

## 涉及 Figures
- **Fig. 1、Fig. 2、Fig. 5** — 捕获、优化和计算输入。
