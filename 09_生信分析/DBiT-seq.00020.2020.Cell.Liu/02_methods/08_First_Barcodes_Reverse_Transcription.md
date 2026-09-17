# Method: Adding the First Set of Barcodes and Reverse Transcription

## 原文（Methods）
> To perform spatial barcoding of mRNAs for transcriptomic mapping, the slides were blocked by 1% BSA plus RNase inhibitor (0.05U/mL, Enzymatics) for 30 minutes at room temperature. After cleaning with 1x PBS and quickly with DI water, the first PDMS microfluidic chip was roughly aligned and placed on the tissue glass slide such that the center of the flow barcoding region covered the tissue of interest. This tissue section was then permeabilized by loading 0.5% Triton X-100 in PBS into each of the 50 channels followed by incubation for 20 minutes and finally were cleaned thoroughly by flowing through 20 mL of 1X PBS. A vial of RT mix was made from 50 μL of RT buffer (5X, Maxima H Minus kit), 32.8 μL of RNase free water, 1.6 μL of RNase Inhibitor (Enzymatics), 3.1 μL of SuperaseIn RNase Inhibitor (Ambion), 12.5 μL of dNTPs (10 mM, Thermo Fisher), 25 μL of Reverse Transcriptase (Thermo Fisher), 100 μL of 0.5X PBS with Inhibitor (0.05U/mL, Enzymatics). To perform the 1st microfluidic flow barcoding, we added to each inset a 5 μL of solution containing 4.5 μL of the RT mix described and 0.5 μL of one of the 50 DNA barcodes (A1-A50) solution (25 μM), and then pulled in using a house vacuum for < 3 minutes depending on channel width. Afterward, the binding of DNA oligomers to mRNAs fixed in tissue was allowed to occur at room temperature for 30 minutes and then incubated at 42°C for 1.5 hours for in situ reverse transcription. To prevent the evaporation of solution inside the channels, the whole device was kept inside a sealed wet chamber (Gervais and Delamarche, 2009). Finally, the channels were rinsed by flowing NEB buffer 3.1(1X, New England Biolabs) supplemented with 1% RNase inhibitor (Enzymatics) continuously for 10 minutes. During the flow barcoding step, optical images could be taken to record the exact positions of these microfluidic channels in relation to the tissue section subjected to spatial barcoding. It was done using an EVOS microscope (Thermo Fisher EVOS fl) in a light or dark field mode. Then the clamp was removed and the PDMS chip was detached from the tissue slide, which was subsequently dipped into a 50 mL Eppendorf tube containing RNase free water to rinse off remaining salts.

## 解读

### 意义
这是DBiT-seq的核心步骤之一，通过第一次微流控流动将Barcode A递送到组织表面，实现mRNA的原位逆转录和第一维空间条码标记。

### 输入
- 固定并封闭的组织载玻片
- PDMS微流控芯片（第一套，50条平行通道）
- RT mix（包含逆转录酶、dNTPs、RNase抑制剂）
- 50种DNA Barcode A溶液（A1-A50，25μM）
- 0.5% Triton X-100（透化剂）

### 输出
- 带Barcode A标记的原位合成cDNA
- 组织像素的第一维空间编码

### 核心步骤
1. 1% BSA + RNase抑制剂封闭30分钟（室温）
2. 1X PBS和DI水清洗
3. 对齐放置第一个PDMS芯片到组织上
4. 0.5% Triton X-100透化20分钟
5. 20mL 1X PBS彻底清洗
6. 制备RT mix：50μL 5X RT buffer + 32.8μL RNase-free水 + 1.6μL RNase抑制剂 + 3.1μL SuperaseIn + 12.5μL dNTPs(10mM) + 25μL逆转录酶 + 100μL 0.5X PBS with抑制剂
7. 每个入口加入5μL溶液（4.5μL RT mix + 0.5μL对应Barcode A，25μM）
8. 真空抽吸（<3分钟）
9. 室温结合30分钟
10. 42°C原位逆转录1.5小时
11. 湿盒中操作防止蒸发
12. NEB buffer 3.1 + 1% RNase抑制剂清洗10分钟
13. 成像记录通道位置
14. 移除夹具，剥离PDMS芯片
15. RNase-free水清洗载玻片

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Barcode A浓度 | 25 μM | 高效结合 |
| 每入口体积 | 5 μL | 充满通道 |
| 真空抽吸时间 | <3分钟 | 依通道宽度而定 |
| 结合时间 | 30分钟（室温） | 寡核苷酸与mRNA杂交 |
| 逆转录时间 | 1.5小时（42°C） | 充分逆转录 |
| 清洗缓冲液 | NEB buffer 3.1 + 1% RNase抑制剂 | 去除未结合物 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| In situ reverse transcription | 原位逆转录，在组织内合成cDNA |
| Flow barcoding | 流动条码，通过微流控递送DNA条码 |
| Wet chamber | 湿盒，维持湿度防止蒸发 |

## 复现
- 工具/代码/URL：Maxima H Minus逆转录酶（Thermo Fisher, EP0751）
- 关键调用：NA

## 生物学意义
这是DBiT-seq技术的核心创新点之一。通过微流控限域递送条码，实现了mRNA在原位的逆转录和空间条码标记。第一维条码（A1-A50）定义了组织像素的一个维度（条纹状），为后续第二维条码的交叉形成二维像素阵列奠定基础。

## 涉及 Figures
- **Fig. 1A** — Schematic workflow
- **Fig. 1C** — 验证空间条码（红色Cy3标记的Barcode A条纹）
