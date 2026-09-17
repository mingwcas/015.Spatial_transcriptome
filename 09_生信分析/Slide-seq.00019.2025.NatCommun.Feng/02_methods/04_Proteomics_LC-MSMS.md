# Method: Proteomics (DIA LC-MS/MS)

## 原文（Methods）
> Prenatal human brain tissue was lysed in 500 µL of 5% SDS, 50 mM TEAB. Samples were sonicated at 30% amplitude for 15 sec (5 sec on, 3 sec off for three cycles) with 1/8" microtip, then resuspended with a pipette. Because of DNA, 1 µL (250U) of Turbonuclease was added to each sample, and they were sonicated again. To ensure proper lysis, samples were resuspended with a pipette and centrifuged at 16,000xg for 5 min. Supernatant was moved to a new tube, and the BCA protein concentration assay was performed. 10 µg of protein material (in 5% SDS, 50 mM TEAB) was reduced at 20 mM DTT for 10 min at 95 °C and alkylated with 40 mM iodoacetamide for 30 min in the dark. Samples were brought up to final concentration of 5% SDS and phosphoric acid was added to a final concentration of 1.2%. 165 µL of S-Trap protein binding buffer (90% methanol, 100 mM TEAB) was added to 27.5 µL of acidified lysate. Resulting mixture was passed through the micro column at 4000xg. The micro-column was washed 4 times with the S-Trap protein binding buffer. Each sample was digested with 1 µL of trypsin (in 20 µL of 50 mM TEAB) for 1 hr at 47 °C.

## 解读

### 意义
基于数据非依赖采集（DIA）的液相色谱-质谱联用技术，可在蛋白质组水平揭示DS产前脑的蛋白质表达变化，验证转录组发现并发现新的生物学通路。

### 输入
- 7个产前人脑组织样本（13-17 PCW；n=4 DS，n=3整倍体）
- S-Trap蛋白富集消化
- Orbitrap™ Astral™质谱仪

### 输出
- 差异丰度蛋白质列表
- GO通路富集分析
- 与转录组数据的整合分析

### 核心步骤
1. 5% SDS, 50 mM TEAB裂解组织
2. 超声破碎（30%振幅，15秒）
3. Turbonuclease处理DNA
4. BCA法定量蛋白浓度
5. DTT还原，IAA烷基化
6. S-Trap微柱蛋白富集和胰蛋白酶消化
7. nano-HPLC分离（Aurora Elite TS色谱柱）
8. DIA LC-MS/MS分析（Orbitrap Astral）
9. Spectronaut v18.7搜库鉴定

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 蛋白上样量 | 10 µg | 消化前蛋白量 |
| 还原条件 | 20 mM DTT, 95°C, 10 min | 二硫键还原 |
| 烷基化条件 | 40 mM IAA, 暗处30 min | 半胱氨酸烷基化 |
| 消化酶 | Trypsin | 胰蛋白酶 |
| 消化时间 | 47°C, 1 hr | 酶解条件 |
| 液相流速 | 600 nl/min | nano-HPLC条件 |
| 质谱分辨率 | 240,000 (MS1) | Orbitrap分辨率 |
| FAIMS CV | -50V | 气相离子迁移分离 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DIA | Data-Independent Acquisition，数据非依赖采集 |
| S-Trap | 蛋白质组学样品制备技术 |
| TEAB | Triethylammonium bicarbonate，三乙基碳酸氢铵缓冲液 |
| FAIMS | Field Asymmetric Ion Mobility Spectrometry，场不对称离子迁移谱 |
| DTT | Dithiothreitol，二硫苏糖醇 |
| IAA | Iodoacetamide，碘乙酰胺 |

## 复现
- 仪器：Vanquish Neo UHPLC + Orbitrap Astral (Thermo Fisher)
- 软件：Spectronaut v18.7 directDIA+
- 数据库：UniProt UP000005640 reviewed human database
- 数据存储：MassIVE repository (MSV000096108)

## 生物学意义
蛋白质组学揭示了DS产前脑中免疫相关通路（补体系统）的显著激活、蛋白质翻译和剪接通路的下调，以及与突触信号和染色质组织相关蛋白的减少。这些发现与转录组数据相互验证，为理解DS神经发育异常提供了蛋白质层面的证据。

## 涉及 Figures
- **Fig. 4** — Proteomics analysis showing immune activation
