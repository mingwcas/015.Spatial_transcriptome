# Method: 滚环扩增（RCA）

## 原文（Methods）
> Add 200 µl of RCA primer hybridization buffer containing 500 nM RCA primer to the glass-bottom dish and incubate at 60 °C for 1 h. Prepare an RCA reaction mixture and incubate it overnight at 30 °C. Additional dNTP (up to 10 µl) and φ29 DNA polymerase (up to 10 µl) can enhance the fluorescence signal from DNA amplicons.

## 解读

### 意义
将单个环状cDNA分子扩增为含有数百个串联重复拷贝的扩增子（amplicon），每个扩增子可结合多个荧光探针，信号增强20-50倍

### 输入
- 环状cDNA分子（已交联在细胞内）
- RCA引物（与adapter序列互补）、φ29 DNA聚合酶、dNTP + aminoallyl-dUTP

### 输出
- 细胞内线性串联重复的cDNA扩增子（含有多个adapter和cDNA拷贝）

### 核心步骤
1. RCA引物杂交（500 nM, 60°C, 1小时）
2. 严格洗涤去除多余引物
3. RCA反应混合物孵育（30°C过夜）
4. BS(PEG)9交联扩增子（室温1小时）— 保持扩增子空间位置
5. Tris淬灭

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| RCA引物浓度 | 500 nM | 引物杂交浓度 |
| 引物杂交温度/时间 | 60°C, 1 h | 杂交条件 |
| φ29 DNA聚合酶 | 1 U µl⁻¹ | 高持续性聚合酶 |
| dNTP终浓度 | 250 µM | 核苷酸 |
| Aminoallyl-dUTP | 40 µM | 用于扩增子交联 |
| RCA反应温度/时间 | 30°C过夜 | 扩增条件 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RCA (Rolling Circle Amplification) | 滚环扩增，φ29聚合酶沿环状模板连续合成 |
| φ29 DNA polymerase | 来自Bacillus phage φ29的高持续性DNA聚合酶 |
| Amplicon | RCA扩增产物，含数百个串联cDNA拷贝 |
| Adapter sequence | RT引物和RCA引物共有的接头序列 |

## 复现
- 试剂：φ29 DNA polymerase (Enzymatics P7020-HC-L), RCA primer (TCTTCAGCGTTCCCGA*G*A)
- 关键：aminoallyl-dUTP不能省略（用于后续交联）；扩增子交联对高质量测序至关重要

## 生物学意义
RCA将单个cDNA分子扩增为含有数百个拷贝的扩增子，使得每个位置的荧光信号增强20-50倍（相比smFISH）。扩增子直径约400-800 nm（20× NA 0.75物镜下），略大于衍射极限。交联后的扩增子形成高度多孔的3D核酸基质，可在标准显微镜上进行测序。

## 涉及 Figures
- **Fig. 1a** — RCA扩增与交联示意
- **Fig. 1b** — 扩增子结构（含串联重复的adapter和cDNA）
- **Fig. 6** — 实验步骤11-16
- **Anticipated Results** — 扩增子大小和亮度描述
