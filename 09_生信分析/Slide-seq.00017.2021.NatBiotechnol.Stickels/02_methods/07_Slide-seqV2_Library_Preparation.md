# Method: Slide-seqV2 Library Preparation

## 原文（Methods）
> RNA hybridization: Pucks in 1.5-ml tubes were immersed in 200 μl of hybridization buffer (6× SSC with 2 U μl–1 Lucigen NxGen RNase inhibitor) for 30 min at room temperature. First-strand synthesis was performed by incubating the pucks in RT solution... Tissue digestion: 200 μl of 2× tissue digestion buffer was then added... Second-strand synthesis was performed on the beads... Library amplification: ...Terra Direct PCR mix... PCR cleanup and Nextera tagmentation: ...Nextera XT kit...

## 解读

### 意义
Slide-seqV2 library preparation是将组织切片中的mRNA转化为可测序的cDNA文库的关键分子生物学流程，相比原始Slide-seq增加了~9倍灵敏度。

### 输入
- Pucks with tissue sections
- Hybridization buffer (6× SSC, RNase inhibitor)
- RT solution (Maxima H Minus RT, dNTPs, template switch oligo)
- 2× tissue digestion buffer (Tris-Cl, NaCl, SDS, EDTA, proteinase K)
- Second-strand synthesis mix

### 输出
- Illumina-sequencing-ready cDNA library
- ~200 million reads per puck

### 核心步骤
1. **RNA hybridization** (30 min, RT): 6× SSC buffer中让poly(T) beads结合mRNA
2. **First-strand synthesis** (1.5 h, 52°C): Maxima H Minus RT生成cDNA，template switching添加3' priming site
3. **Tissue digestion** (30 min, 37°C): Proteinase K消化组织，释放cDNA
4. **ExoI treatment** (50 min, 37°C): 去除残余寡核苷酸
5. **NaOH处理** (5 min, RT): 变性，去除RNA
6. **Second-strand synthesis** (1 h, 37°C): 新增步骤，显著提高灵敏度
7. **Library PCR** (13 cycles): Terra Direct PCR mix
8. **Nextera tagmentation**: 600 pg DNA用于建库
9. **Sequencing**: NovaSeq S2, 44+8+50 bp reads

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Hybridization | 6× SSC, 30 min, RT | 标准条件 |
| RT酶 | Maxima H Minus (Thermo) | 高效逆转录 |
| Template switch oligo | 50 μM (Qiagen) | 添加PCR priming site |
| Proteinase K | 32 U/ml | 组织消化 |
| Second-strand | Klenow enzyme, 1h, 37°C | 新增关键步骤 |
| PCR cycles | 13 (4+9) | 线性扩增 |
| Input for Nextera | 600 pg | 微量建库 |
| Read structure | 44+8+50 bp | Read1+Index+Read2 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Template switching | RT酶在cDNA 3'端添加非模板C碱基，与 oligo配对添加已知序列 |
| Second-strand synthesis | 原本法一步，现在增加的第二链合成提高cDNA产量 |
| Nextera tagmentation | Illumina的转座子建库技术 |
| UMI | Unique Molecular Identifier，计数原始mRNA分子 |

## 复现
- **试剂**: 
  - NxGen RNase inhibitor (Lucigen)
  - Maxima H Minus RT (Thermo EP0751)
  - Template switch oligo (Qiagen 339414YCO0076714)
  - Nextera XT kit (Illumina FC-131-1096)
  - Terra Direct PCR mix (Takara 639270)
  - AMPure XP beads (Beckman A63880)
- **设备**: Bioanalyzer High Sensitivity DNA chip (Agilent 5067-4626)
- **测序**: Illumina NovaSeq S2, 24 samples/run

## 生物学意义
Library preparation的优化，特别是second-strand synthesis步骤，是Slide-seqV2灵敏度提升(~9倍)的关键。这使得检测低丰值mRNA（如dendritic mRNAs）成为可能。

## 涉及 Figures
- **Fig. 1b** — Effect of second-strand synthesis on UMI counts
- **Fig. 1** — All figures use data from this library prep
