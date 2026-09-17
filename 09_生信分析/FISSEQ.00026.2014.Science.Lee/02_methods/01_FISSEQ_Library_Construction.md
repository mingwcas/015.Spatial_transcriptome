# FISSEQ 文库构建 (FISSEQ Library Construction)

## 原文 (Methods)

RNA was reverse-transcribed in fixed cells with tagged random hexamers. We incorporated aminoallyl deoxyuridine 5′-triphosphate (dUTP) during reverse transcription (RT) and refixed the cells using BS(PEG)9, an amine-reactive linker with a 4-nm spacer. The cDNA fragments were then circularized before rolling circle amplification (RCA), and BS(PEG)9 was used to cross-link the RCA amplicons containing aminoallyl dUTP. We found that random hexamer-primed RT was inefficient, but cDNA circularization was complete within hours. The result was single-stranded DNA nanoballs 200 to 400 nm in diameter, consisting of numerous tandem repeats of the cDNA sequence.

## 解读

### 意义
FISSEQ 文库构建是实现原位 RNA 测序的核心步骤。通过在固定细胞内进行逆转录和扩增，保留了 RNA 的空间位置信息，使得后续可以在原位进行测序和成像。

### 输入
- 固定的细胞或组织样本
- 带标签的随机六聚体引物
- aminoallyl dUTP
- BS(PEG)9 交联剂

### 输出
- 单链 DNA 纳米球（200-400 nm 直径）
- 包含 cDNA 序列的串联重复序列

### 核心步骤
1. **逆转录 (RT)**：使用带标签的随机六聚体引物在固定细胞内进行逆转录
2. **dUTP 掺入**：在逆转录过程中掺入 aminoallyl dUTP
3. **重新固定**：使用 BS(PEG)9（4 nm 间隔臂）重新固定细胞
4. **cDNA 环化**：将 cDNA 片段环化
5. **滚环扩增 (RCA)**：进行滚环扩增
6. **交联**：使用 BS(PEG)9 交联含有 aminoallyl dUTP 的 RCA 扩增产物

### 关键参数
- 随机六聚体引物带标签
- BS(PEG)9 间隔臂长度：4 nm
- DNA 纳米球直径：200-400 nm
- cDNA 环化时间：数小时内完成

## 名词/参数/指标

| 术语 | 定义 |
|------|------|
| FISSEQ | 荧光原位 RNA 测序 (Fluorescent In Situ RNA Sequencing) |
| RCA | 滚环扩增 (Rolling Circle Amplification) |
| BS(PEG)9 | 胺反应性连接子，带有 4 nm 间隔臂 |
| aminoallyl dUTP | 氨基烯丙基脱氧尿苷三磷酸 |
| 随机六聚体 | 随机序列的 6 个碱基的 DNA 引物 |

## 复现

### 所需试剂
- 固定液（如多聚甲醛）
- 逆转录酶
- 带标签的随机六聚体引物
- aminoallyl dUTP
- BS(PEG)9 交联剂
- 环化连接酶
- RCA 扩增试剂

### 所需设备
- 细胞培养设备
- 荧光显微镜
- 共聚焦显微镜

## 生物学意义

FISSEQ 文库构建方法使得在细胞内原位进行 RNA 测序成为可能，保留了 RNA 的空间位置信息。这对于研究：
- RNA 的亚细胞定位
- 细胞异质性
- 组织空间结构
- 发育过程中的基因表达模式

具有重要意义。

## 涉及 Figures

- **Fig. 1**: 3D RNA-seq 文库构建示意图
- **fig. S1**: FISSEQ 工作流程
- **fig. S2**: 逆转录和文库构建细节
- **fig. S3**: 逆转录效率和环化动力学
- **fig. S4**: DNA 纳米球和扩增产物特性
