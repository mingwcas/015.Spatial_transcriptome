# Method: Amplicon Purification, Sequencing Library Preparation and Quality Assessment

## 原文（Methods）
> The PCR product was then purified by Ampure XP beads (Beckman Coulter) at 0.6X ratio. The mRNA-derived cDNAs (> 300 bp) were then collected from the beads. If the cDNAs were less than 300 bp, they remained in the supernatant fraction. If the protein detection was conducted like CITE-seq, this fraction was used instead. For sequencing antibody-DNA conjugate-derived cDNAs, we further purified the supernatant using 2X Ampure XP beads. The purified cDNA was then amplified using a PCR reaction mix containing 45 μL purified cDNA fraction, 50 μL 2x KAPA HiFi PCR Master Mix(Kapa Biosystems), 2.5 μL P7 primer of 10 mM and 2.5 μL P5 cite primer at 10 mM. PCR was performed in the following conditions: first incubated at 95°C for 3 minutes, then cycled at 95°C for 20 s, 60°C for 30 s and 72°C for 20 s, for 10 cycles, lastly 72°C for 5 minutes. The PCR product was further purified by 1.6X Ampure XP beads. For sequencing mRNA-derived cDNAs, the quality of amplicon was analyzed first using Qubit (Life Technologies) and then using an Agilent Bioanalyzer High Sensitivity Chip. The sequencing library was then built with a Nextera XT kit (Illumina) and sequenced using a HiSeq 4000 sequencer using a pair-end 100x100 mode. To conduct joint profiling of proteins and mRNAs, the DNA-antibody conjugate-derived sequencing library was combined with mRNA-derived cDNA library at a 1:9 ratio, which is sufficient to detect the finite set of proteins and minimally affects the sequencing depth required for mRNAs.

## 解读

### 意义
该方法完成文库构建和质控，将扩增的cDNA转化为可测序的文库，并评估文库质量以确保测序效果。

### 输入
- PCR扩增产物
- Ampure XP beads
- KAPA HiFi PCR Master Mix
- P5/P7引物
- Nextera XT DNA Preparation Kit (Illumina)

### 输出
- 测序文库（Illumina HiSeq 4000, paired-end 100x100）
- 文库质控数据（Qubit, Bioanalyzer）

### 核心步骤
1. Ampure XP beads (0.6X)纯化PCR产物
2. 收集>300bp的mRNA-derived cDNA
3. 如有蛋白检测，收集<300bp的supernatant，用2X Ampure XP beads进一步纯化（抗体-cDNA）
4. cDNA文库PCR：45μL cDNA + 50μL 2x KAPA HiFi + 2.5μL P7 primer(10mM) + 2.5μL P5 cite primer(10mM)
5. PCR：95°C 3分钟；95°C 20秒，60°C 30秒，72°C 20秒，10个循环；72°C 5分钟
6. 1.6X Ampure XP beads纯化
7. Qubit和Bioanalyzer High Sensitivity Chip质控
8. Nextera XT kit构建测序文库
9. HiSeq 4000测序，paired-end 100x100
10. 蛋白与mRNA文库混合比1:9

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Ampure XP比例 | 0.6X（第一轮），1.6X（第二轮） | 片段选择 |
| 片段截断 | >300bp（mRNA），<300bp（蛋白） | 分别收集 |
| PCR循环数 | 10个循环 | 充分扩增不过度 |
| 测序模式 | Paired-end 100x100 | 高通量测序 |
| 文库混合比 | 1:9（蛋白:mRNA） | 蛋白检测充分且不干扰mRNA |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Ampure XP beads | 磁珠，基于SPRI(selective binding of PCR primers)原理纯化DNA |
| Nextera XT | Illumina文库构建试剂盒，使用tagmentation技术 |
| Qubit | 荧光定量仪，测定DNA浓度 |
| Bioanalyzer | 安捷伦生物分析仪，电泳检测片段大小分布 |

## 复现
- 工具/代码/URL：Nextera XT DNA Preparation Kit (Illumina, FC-131-1024)
- 关键调用：NA

## 生物学意义
文库构建是DBiT-seq实验的最后一步。通过片段大小选择将mRNA来源的长cDNA（>300bp）和抗体-cDNA衍生的短片段（<300bp）分开，分别构建文库保证了两种分子的正确表征。Nextera XT的tagmentation技术高效地将DNA片段化并添加接头，1:9的混合比例确保蛋白数据有足够覆盖深度，同时不显著降低mRNA的测序深度。

## 涉及 Figures
- **Fig. S2A** — cDNA大小分布峰值900-1100bp
