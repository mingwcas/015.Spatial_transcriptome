# Method: Stereo-seq FFPE Library Preparation and Sequencing

## 原文（Methods）
> FFPE Tissue processing: FFPE tissues were sectioned using a microtome (Leica, HistoCore BIOCUT) at a thickness of 5μm, two sections were consecutively cut. The sections were floated in a water bath at around 45°C, one section was adhered to the Stereo-seq Chip N, then followed by baking at 42°C for 3 hours and overnight drying. Deparaffinating and Decrosslinking: The Stereo-seq Chip N attached with FFPE sections were baked at 60°C for 1 hour, followed by a deparaffinating process in a staining dish or a 50 ml centrifuge tube: Histo-clear (Haide, H6025) for 20 minutes twice; 100% ethanol for 5 minutes twice; 96% ethanol for 5 minutes twice; 90% ethanol→80% ethanol→70% ethanol and ddH2O for 2 minutes each. The chips were allowed to air dry, submerged in the FFPE Decrosslinking Reagent (STOmics, 211KN114-EA, 10000KG001) and incubated at 95°C for 30 minutes. Then the chips were cooled to room temperature and immersed in -20°C methanol for 20 minutes for fixation.

> FFPE dimer solution preparation: A total of 10 μL mixture prepared in a PCR tube, consisting of 1 μL of 100 μM random primer and 1μl of 100 μM splint oligo, 2.5 μL of 20×SSC buffer (Thermo Fisher Scientific, AM9770) and 5.5 μL Nuclease-Free Water (Thermo Fisher Scientific, AM9937). The mixture was mixed thoroughly and incubated at 55°C for 10 minutes for hybridization, then was transferred to ice immediately. 1 μL of the mixture was added to 99 μL of 5×SSC buffer with 0.05 U/μL RNase inhibitor (GCATBio, LS-EZ-E-00006Q) and thoroughly mixed, to obtain a final concentration of 0.01 μM FFPE Dimer solution.

> In situ reverse transcription and ligation: Tissue sections placed on the chips were incubated with 0.1% pepsin (Sigma, P7000) for 30 minutes for permeabilization, followed by washing once with 5×SSC buffer supplemented with 0.05 U/μL RNase inhibitor. 0.01μM FFPE Dimer solution containing random probes was added onto the tissue sections and hybridized for 1 hour at around 25°C. Then the chips were washed once with 0.1×SSC buffer supplemented with 0.05 U/μL RNase inhibitor. RNA was captured by random probes and reverse transcribed while being simultaneously ligated to the Stereo-seq Chip N, using Golden Reverse Transcriptase and T4 DNA ligase (GCATBio, LS-EZ-E-00024O, 10 U/μL Golden Reverse Transcriptase; GCATBio, LS-EZ-E-00008O, 1 U/μL T4 DNA ligase; 1 mM dNTPs, 0.25mM ATP, 1 M betaine solution PCR reagent, 7.5 mM MgCl2, 5 mM DTT, 2 U/μL RNase inhibitor, 2.5 mM FFPE Stereo-seq-TSO and 1×First-Strand buffer). After the reaction, tissue sections were washed twice with ddH2O. cDNA-containing chips were then subjected to cDNA Release mix (STOmics, 211KN114-EA, 1000028511, cDNA Release Enzyme within 1000028512, cDNA Release buffer) treatment for 5 hours at 55°C and were finally washed once with Nuclease-Free Water.

> Amplification, library construction and sequencing: The resulting cDNAs were amplified with Platinum High-Fidelity Ready Mix (2×) (GCATBio, LS-EZ-K-00008O) with 0.8 mM FFPE cDNA-PCR primers. PCR reactions were conducted as follows: incubation at 95°C for 5 minutes, 15 cycles at 98°C for 20 seconds, 58°C for 20 seconds, 72°C for 3 minutes and a final incubation at 72°C for 5 minutes. PCR products were purified using the VAHTS DNA Clean Beads (1.0×) (Vazyme, N411-03), the concentrations of the resulting PCR products were quantified by Qubit dsDNA Assay Kit (Thermo Fisher Scientific, Q32854), a total of 60 ng of DNA was used for DNB generation and finally sequenced on MGISEQ-2000RS, DNBSEQ-T1 or DNBSEQ-T7 sequencer.

## 解读

### 意义
这是Stereo-seq V2的核心实验流程，实现了对FFPE样本的总RNA空间转录组捕获。随机引物策略克服了FFPE样本RNA降解和3'偏倚的问题。

### 输入
- FFPE组织切片（5μm厚度）
- Stereo-seq Chip N
- 随机引物和splint oligo
- 各种试剂和酶

### 输出
- 测序文库
- 原始测序数据

### 核心步骤
1. FFPE组织切片制备：5μm厚度，附着于Chip N
2. 脱蜡复水：Histo-clear、乙醇系列
3. 去交联：95°C 30分钟
4. 甲醇固定：-20°C 20分钟
5. 随机引物二聚体溶液制备
6. 胃蛋白酶透化：0.1% pepsin 30分钟
7. 原位逆转录和连接：随机引物捕获+逆转录+连接
8. cDNA释放：55°C 5小时
9. PCR扩增：15个循环
10. 文库构建和测序

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 5μm | FFPE样本 |
| 脱蜡温度 | 60°C 1小时 | |
| 去交联温度 | 95°C | FFPE Decrosslinking Reagent |
| 去交联时间 | 30分钟 | |
| 甲醇固定 | -20°C 20分钟 | |
| 随机引物浓度 | 0.01 μM | FFPE Dimer solution |
| 透化 | 0.1% pepsin 30分钟 | |
| 逆转录/连接温度 | 25°C 1小时 | |
| cDNA释放 | 55°C 5小时 | |
| PCR循环数 | 15 cycles | |
| 上机测序 | MGISEQ-2000RS/DNBSEQ-T1/T7 | MGI平台 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| FFPE | 福尔马林固定石蜡包埋 |
| DV200 | RNA质量指标，降解片段>200nt的比例 |
| CID | 坐标身份条码 |
| DNB | DNA Nanoball |
| Random priming | 随机引物捕获策略 |

## 复现
- 商业试剂盒：Stereo-seq Transcriptomics Set for FFPE - Early Access (STOmics, 211SN114-EA)
- 测序平台：MGI DNBSEQ系列

## 生物学意义
该方法首次实现FFPE样本的高质量空间转录组分析，random priming策略提供了全基因体覆盖和无偏倚5'捕获，显著提升了FFPE样本的RNA捕获效率。

## 涉及 Figures
- Fig. 1A (workflow)
- Fig. 4 (FFPE样本分析)
