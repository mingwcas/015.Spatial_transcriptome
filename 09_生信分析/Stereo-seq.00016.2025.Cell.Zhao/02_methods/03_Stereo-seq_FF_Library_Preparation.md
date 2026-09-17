# Method: Stereo-seq Fresh Frozen Library Preparation and Sequencing

## 原文（Methods）
> Fresh Frozen (FF) Tissue processing: Mouse brain was dissected from an 8-week-old C57BL/6J male mouse. After collection, the brain was snap-frozen on dry ice in Tissue-Tek OCT (Sakura, 4583) and transferred to a Leica CM1950 cryostat for sectioning. The mouse brain was sectioned at a thickness of 10 μm, two sections were consecutively cut. One section was adhered to one Stereo-seq chip T and the other was adhered to one Stereo-seq chip N, then both chips were incubated on a 37°C-slide dryer for 5 minutes immediately. Then, the sections were fixed in methanol and incubated for 30 minutes at -20°C before Stereo-seq library preparation.

> Stereo-seq V1 of FF—In situ reverse transcription and Amplification: Stereo-seq V1 of in situ reverse transcription and amplification based on chip T were performed as described in 2022 (Chen et al., 2022).

> Stereo-seq V2 of FF—In situ reverse transcription and Amplification: The dimer solution preparation and in situ reverse transcription and ligation were carried out as detailed in the Stereo-seq FFPE section mentioned above.

> Stereo-seq V1 and V2 FF Library construction and sequencing: The concentrations of the resulting PCR products were quantified by Qubit dsDNA Assay Kit (Thermo, Q32854). A total of 20 ng of dsDNA were then fragmented with in-house Tn5 transposase at 55°C for 10 minutes, after which the reactions were stopped by the addition of 0.02% SDS and gently mixing at 37°C for 5 minutes after fragmentation. Fragmented products were amplified as described below: 25 μL of fragmentation product, 50 μL Platinum High-Fidelity Ready Mix (2×) (GCATBio, LS-EZ-K-00008O) and 0.3 mM Stereo-seq-Library-F primer, 0.3 mM Stereo-seq-Library-R primer in a total volume of 100 μL with the addition of NF-H2O. The reaction was then run as: 1 cycle of 95°C 5 minutes, 13 cycles of 98°C 20 seconds, 58°C 20 seconds and 72°C 30 seconds, and 1 cycle of 72°C 5 minutes. PCR products were purified using the VAHTS DNA Clean Beads (0.55 and 0.15) (Vazyme, N411-03), used for DNB generation and finally sequenced on MGI DNBSEQ-Tx sequencer.

## 解读

### 意义
新鲜冷冻样本的Stereo-seq V1和V2文库构建流程，用于与FFPE样本进行性能比较。

### 输入
- 新鲜冷冻小鼠脑组织（8周龄C57BL/6J雄鼠）
- Stereo-seq Chip T (V1) 和 Chip N (V2)
- OCT包埋

### 输出
- 测序文库（V1和V2）
- 原始测序数据

### 核心步骤
1. 新鲜组织获取和OCT包埋
2. 10μm冰冻切片
3. 切片分别附着于Chip T和Chip N
4. 甲醇固定：-20°C 30分钟
5. V1: 传统poly(T)捕获
6. V2: 随机引物捕获（与FFPE相同流程）
7. Tn5片段化
8. PCR扩增（13 cycles）
9. DNB生成和测序

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 10μm | 冰冻切片 |
| 固定 | 甲醇 -20°C 30分钟 | |
| Tn5片段化 | 55°C 10分钟 | |
| PCR循环数 | 13 cycles | |
| 上机量 | 20 ng dsDNA | |
| 测序平台 | MGI DNBSEQ-Tx | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Fresh Frozen (FF) | 新鲜冰冻样本 |
| OCT | Optimal Cutting Temperature compound |
| DNB | DNA Nanoball |

## 复现
- 原始方法参考：Chen et al., 2022, Cell
- 测序平台：MGI DNBSEQ-Tx

## 生物学意义
通过在相同组织上直接比较V1和V2，验证了随机引物策略在新鲜样本中同样有效，且提供更好的基因体覆盖。

## 涉及 Figures
- Fig. 1B, 1C (correlation between V1 and V2)
- Fig. 3 (gene body coverage comparison)
