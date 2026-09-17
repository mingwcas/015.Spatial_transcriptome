# Fig. 4 — SOLiD颜色编码与解码方案

## Caption（原文）
> Schematic overview of the SOLiD color-coding and decoding scheme. (a) The base position within the template sequence is enclosed by white circles and should be used for naming the image files, and the actual sequencing cycle numbers are noted on both sides. Each ligation extension is shown in different colors, and cycles 15, 22 and 29 are shown in gray, as no images are acquired for these cycles. The red box at cycle 8 denotes a known base identity. (b) SOLiD dinucleotide coding scheme. (c) SOLiD color space decoding scheme. As long as any one of the base identities are known (here in red), the color space sequence can be converted to the nucleotide sequence. Image reproduced from Life Technologies (ref. 47). © 2014 Thermo Fisher Scientific, Inc. Used under permission.

## Panel-by-Panel 解读

### Panel a — 测序循环与引物偏移
**结论**：展示5个测序引物的循环编号和碱基位置对应关系

**关键数据**：
- Primer N: 循环1,2,3,4,5,6,7 → 位置2,7,12,17,22,27,32
- Primer N-1: 位置1,6,11,16,21,26,31
- Primer N-2: 位置0,5,10,15,20,25,30
- Primer N-3: 位置4,9,14,19,24,29
- Primer N-4: 位置3,8,13,18,23,28
- 循环15,22,29不采集图像（灰色）

### Panel b — 双碱基编码方案
**结论**：SOLiD使用双碱基编码，每个颜色代表4种可能的双碱基组合

**关键数据**：
- Probe set 1 (2-base encoding)
- 4种颜色：Blue(B), Orange(O), Red(R), Green(G)
- 每种颜色对应4种双碱基组合
- 例如：AAGCAGTCA = BORGOGOG

### Panel c — 颜色空间解码
**结论**：只要知道任何一个碱基的身份，就可以将颜色序列转换为核苷酸序列

**关键数据**：
- 输入颜色序列 + 一个已知碱基（红色标记）
- 通过转换表逐碱基推断
- 任何缺失或错误的碱基调用会影响整个读取

## 总体结论
Fig. 4详细解释了SOLiD测序的颜色编码系统，这是理解FISSEQ数据处理的关键。SOLiD的双碱基编码方案使每个碱基被检测两次，理论上可降低错误率，但也意味着颜色空间到碱基空间的转换容易传播错误。因此，FISSEQ的数据分析必须在颜色空间中进行，这是使用Bowtie 1.0（支持颜色空间）的关键原因。

## 关联 Figures / Extended Data
- **Box 1** — SOLiD测序化学详细说明
- **Fig. 1b** — 测序原理
- **Fig. 5c** — 碱基判读
