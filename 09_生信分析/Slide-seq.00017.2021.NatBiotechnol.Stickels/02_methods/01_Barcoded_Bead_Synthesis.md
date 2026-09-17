# Method: Barcoded Bead Synthesis

## 原文（Methods）
> Bead barcodes were synthesized either by the ChemGenes Corporation or in house on an Akta Oligopilot 10 on one of two polystyrene supports, Agilent PLRP-S-1000A 10-μm particles or 10-μm custom polystyrene from AMBiotech. Oligonucleotide synthesis was performed as described below. Beads were used with one of the two following sequences...

## 解读

### 意义
Barcoded bead是Slide-seqV2技术的核心，通过在10μm聚苯乙烯微珠上合成唯一DNA条形码，实现空间转录组的 bead-level indexing。

### 输入
- 聚苯乙烯微珠（Agilent PLRP-S-1000A 10-μm 或 AMBiotech 10-μm custom）
- DNA合成试剂（5'-CE phosphoramidites）
- Split-pool反应设备

### 输出
- ~10⁹ unique barcode sequences (415 distinct barcodes × multiple copies per bead)
- Barcoded bead arrays ("pucks")

### 核心步骤
1. **功能化微珠**: PLRP-S树脂用non-cleavable linker功能化
2. **反向DNA合成** (5'→3'): 使用标准固相DNA合成协议
3. **Split-pool合成**: 15轮循环（8+7 cycles）产生415种独特barcode
4. **去保护**: 30%氨水+10%二乙胺处理40小时
5. **清洗**: 丙酮、乙腈、水、Tris-EDTA缓冲液依次洗涤

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 微珠直径 | 10 μm | 空间分辨率 |
| Split-pool循环 | 15次 (8+7) | 产生415种barcode |
| 合成温度 | 室温 | 标准条件 |
| 去保护时间 | 40 h | 30%氨水室温 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Barcoded bead | 10μm聚苯乙烯微珠，每个微珠上所有寡核苷酸具有相同J碱基barcode |
| Split-pool synthesis | 分批-混合合成策略，通过多轮分批反应和混合产生组合多样性 |
| J bases | Split-pool过程中生成的barcode区域碱基 |
| N bases | 标准碱基混合生成的区域（每个珠上的寡核苷酸不同） |
| PLRP-S | 聚苯乙烯树脂，用于DNA固相合成 |

## 复现
- **工具**: Akta Oligopilot 10 (GE Healthcare)
- **试剂供应商**: ChemGenes Corporation, Glen Research (phosphoramidites), Agilent
- **代码/URL**: 无开源代码，工艺为专有

## 生物学意义
Barcoded bead是空间转录组芯片的核心元件。通过在珠表面固定带barcode的poly(T)寡核苷酸，可以捕获组织切片中的mRNA，实现高密度空间基因表达分析。每个珠的barcode是其在阵列中位置的唯一标识。

## 涉及 Figures
- **Fig. 1a** — Overview of the Slide-seq method showing array generation
