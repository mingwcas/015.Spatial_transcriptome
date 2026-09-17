# Method: Tissue Slides and Fixation

## 原文（Methods）
> To thaw the tissue slides, they were taken out of the freezer, placed on a bench at room temperature for 10 minutes, and then cleaned with 1X phosphate buffer saline (PBS) supplemented with RNase inhibitor (0.05U/mL, Enzymatics). If the tissue slides were frozen sections, they were first fixed by immersing in 4% formaldehyde (Sigma) for 20 minutes. Afterward, the tissue slides were dried with forced nitrogen air and then ready to use for spatial barcoding.

## 解读

### 意义
该方法确保冷冻组织载玻片在实验前被正确解冻和固定，保护RNA完整性并为空间条码操作做准备。

### 输入
- 冷冻组织载玻片（-80°C储存）
- 1X PBS
- RNase抑制剂（0.05U/mL）
- 4%甲醛

### 输出
- 固定好的组织载玻片，干燥待用

### 核心步骤
1. 从-80°C取出冷冻载玻片
2. 室温放置10分钟解冻
3. 用含RNase抑制剂的1X PBS清洗
4. 如为冷冻切片，4%甲醛固定20分钟
5. 强制氮气吹干

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 解冻时间 | 10分钟 | 室温 |
| PBS | 1X | 标准渗透压缓冲液 |
| RNase抑制剂浓度 | 0.05U/mL | 保护RNA |
| 甲醛浓度 | 4% | 交联固定20分钟 |
| 固定时间 | 20分钟 | 充分固定 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RNase inhibitor | 核糖核酸酶抑制剂，防止RNA降解 |
| Formaldehyde fixation | 甲醛固定，交联蛋白质和RNA，保持空间定位 |

## 复现
- 工具/代码/URL：RNase抑制剂（Enzymatics, Y9240L）
- 关键调用：NA

## 生物学意义
甲醛固定是DBiT-seq兼容固定组织而非冷冻组织的主要原因。交联固定保持了mRNA在组织中的空间位置，RNase抑制剂确保在操作过程中RNA不被降解，为后续原位逆转录和条码连接提供完整的模板。

## 涉及 Figures
- **Fig. 1A** — Workflow中包含组织固定步骤
