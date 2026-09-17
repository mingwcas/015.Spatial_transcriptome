# 转录起始位点测序 (Transcription Start Site Sequencing)

## 原文 (Methods)

We applied these concepts to sequence the transcription start site of inducible mCherry mRNA in situ, analogous to 5′ rapid amplification of cDNA ends–polymerase chain reaction (RACE-PCR). After RT and molecular amplification of the 5′ end followed by fluorescent probe hybridization, we quantified the concentration- and time-dependent mCherry gene expression in situ. Using sequencing-by-ligation, we then determined the identity of 15 contiguous bases from each amplicon in situ, corresponding to the transcription start site. When the sequencing reads were mapped to the vector sequence, 7472 (98.7%) amplicons aligned to the positive strand of mCherry, and 3967 (52.4%) amplicons mapped within two bases of the predicted transcription start site.

## 解读

### 意义
转录起始位点测序验证了 FISSEQ 技术在单碱基分辨率下定位 RNA 序列的能力。类似于 5′ RACE-PCR，但可以在原位进行，保留了空间信息。

### 输入
- 表达 mCherry 的细胞
- 荧光探针

### 输出
- 15 个连续碱基的序列
- 转录起始位点定位
- 基因表达定量数据

### 核心步骤
1. **逆转录**：在固定细胞内进行逆转录
2. **5′ 端扩增**：对 5′ 端进行分子扩增
3. **探针杂交**：荧光探针杂交
4. **连接测序**：使用连接法测序确定 15 个连续碱基
5. **序列比对**：将测序读数比对到载体序列

### 关键参数
- 测序读长：15 个碱基
- 对齐率：98.7% 的扩增子对齐到正链
- 起始位点定位：52.4% 的扩增子在预测位点的 2 个碱基内

## 名词/参数/指标

| 术语 | 定义 |
|------|------|
| 5′ RACE-PCR | 5′ 末端快速扩增 cDNA 末端-聚合酶链反应 |
| 转录起始位点 | RNA 转录开始的位置 |
| 连接法测序 | 通过连接荧光寡核苷酸进行测序 |
| 正链 | DNA 的有义链 |

## 复现

### 所需试剂
- mCherry 表达载体
- 荧光探针
- 连接酶
- 荧光标记的连接子

### 所需设备
- 荧光显微镜
- 共聚焦显微镜

## 生物学意义

转录起始位点测序验证了 FISSEQ 技术的：
- 单碱基分辨率
- 高准确率（98.7% 对齐率）
- 原位定位能力
- 定量基因表达分析能力

这对于研究基因调控、启动子活性和转录起始具有重要意义。

## 涉及 Figures

- **fig. S7**: mCherry 转录起始位点测序
