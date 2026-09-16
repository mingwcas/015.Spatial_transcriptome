# Method: scRNA-seq测序、比对与质量控制

## 原文（Methods）
> Libraries were sequenced on the Illumina NovaSeq6000, and sequencing reads were aligned to the mouse reference transcriptome (M21, GRCm38.p6) using CellRanger v6.1.1 with default parameters. Doublets were identified using a modified DoubletFinder algorithm and removed when doublet score >0.3. For neurons (excluding granule cells) we used gene counts cutoff 2,000 and QC score cutoff 200.

## 解读
### 意义
去除低质量细胞、双细胞和降解细胞，获得可靠表达矩阵。
### 输入
10xv2/v3 FASTQ；M21/GRCm38.p6参考；10xMultiome为GRCm38(v98)/vM23。
### 输出
10xv3保留2,546,319细胞，10xv2保留1,769,304细胞；最终约4.0M高质量细胞。
### 核心步骤
1. CellRanger比对并生成基因-细胞矩阵。 2. 计算基因数、QC score及doublet score。 3. 按细胞类别设置阈值并过滤。
### 关键参数（本文设置）
|参数|值|含义|
|---|---|---|
|CellRanger|6.1.1|10x比对/定量|
|doublet阈值|>0.3|剔除双细胞|
|神经元gene-count cutoff|2,000|最低检测基因数|
|神经元QC score|200（snRNA 100）|完整性阈值|

## 名词/参数/指标
|名词|定义|
|---|---|
|QC score|62个 housekeeping 基因log表达之和，反映胞质mRNA完整性|
|Doublet score|DoubletFinder估计的双细胞分数|

## 复现
- CellRanger 6.1.1；scrattch.hicat v1.0.9 (https://github.com/AllenInstitute/scrattch.hicat)
- `cellranger count --transcriptome=GRCm38 --fastqs=FASTQ`

## 生物学意义
严格QC减少技术伪影，但高阈值可能丢失脆弱或低RNA细胞，尤其影响脑干稀有类型。

## 涉及 Figures
- **Fig. 1** — taxonomy细胞数；Extended Data Fig. 1
