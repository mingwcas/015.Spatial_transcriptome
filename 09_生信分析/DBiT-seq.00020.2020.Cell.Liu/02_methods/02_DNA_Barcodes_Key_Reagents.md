# Method: DNA Barcodes and Key Reagents

## 原文（Methods）
> Oligos used were listed in Table S1. Antibody-Oligo sequences and Table S2. DNA oligos and DNA barcodes. All other key reagents used were listed as Table S3.

## 解读

### 意义
该方法定义了DBiT-seq技术中使用的DNA条码序列和关键试剂，为空间条码的精确递送和分子识别提供化学基础。

### 输入
- 抗体-DNA结合物（Table S1）
- DNA寡核苷酸和条码（Table S2）
- 其他关键试剂（Table S3）

### 输出
- Barcode A (A1-A50)：含oligo-dT（结合mRNA）、空间条码(8-mer)、连接接头(15-mer)
- Barcode B (B1-B50)：含连接接头(15-mer)、空间条码(8-mer)、UMI、PCR handle（带生物素）

### 核心步骤
1. Barcode A组成：oligo-dT序列 + 空间条码Ai(8-mer) +  ligation linker(15-mer)
2. Barcode B组成：ligation linker(15-mer) + 空间条码Bj(8-mer) + UMI + PCR handle(22-mer，带生物素)
3. 抗体衍生DNA标签(ADT)含独特条码(15-mer)和poly-A尾

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Barcode A数量 | 50 (A1-A50) | 第一次流动递送 |
| Barcode B数量 | 50 (B1-B50) | 第二次流动递送 |
| Barcode序列长度 | 8-mer (空间条码) | 理论2500个组合 |
| UMI | 包含在Barcode B中 | 唯一分子标识 |
| PCR handle | 22-mer，带生物素 | 用于cDNA纯化 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Barcode A | 第一次微流控流动递送的DNA条码，含oligo-dT |
| Barcode B | 第二次微流控流动递送的DNA条码，含UMI和PCR handle |
| ADT | Antibody-Derived DNA Tag，抗体衍生DNA标签 |
| Ligation linker | 连接接头，用于A和B条码的连接 |
| UMI | Unique Molecular Identifier，唯一分子标识符 |

## 复现
- 工具/代码/URL：IDT提供寡核苷酸合成（见Table S2）
- 关键调用：NA

## 生物学意义
DNA条码设计是DBiT-seq实现空间分辨多组学的核心。Barcode A的oligo-dT用于原位捕获mRNA，Barcode B的生物素化PCR handle便于后续cDNA纯化。A1-A50和B1-B50的交叉连接形成2500个独特的二维空间条码(i×j)，实现了组织像素的高密度空间编码。

## 涉及 Figures
- **Fig. 1A** — Schematic workflow showing barcode design
