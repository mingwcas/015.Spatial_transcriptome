# Method: SOLiD连接法测序（Sequencing-by-Ligation）

## 原文（Methods）
> We use sequencing-by-ligation (SOLiD) because it works well at room temperature, and so a heated stage is not required. SOLiD uses a dinucleotide detection scheme in which a base position is interrogated twice per sequencing run, and this can reduce the base calling error rate. A sequencing primer hybridizes to the adapter sequences in individual amplicons, and fluorescent eight-base probes interrogate the adjacent dinucleotide pair. After imaging, the three bases attached to a fluorophore are cleaved, generating a phosphorylated 5′ end at the ligation complex suitable for additional ligation cycles interrogating every fifth dinucleotide pairs.

## 解读

### 揄义
在室温下使用SOLiD连接化学在扩增子上进行原位测序，通过荧光探针逐碱基读取cDNA序列

### 输入
- 细胞内交联固定的RCA扩增子
- 5个测序引物（N, N-1, N-2, N-3, N-4）、SOLiD荧光探针、T4 DNA连接酶

### 输出
- 最多35轮原始3D图像堆栈（5个引物 × 7轮连接）

### 核心步骤
1. 固定样品在显微镜载物台上
2. 测序引物N杂交（2.5 µM, 5× SASC, 80°C预热, 10 min）
3. T4 DNA连接酶连接荧光八碱基探针（室温45 min）
4. 洗涤 → 成像（4色共聚焦）
5. 荧光基团切割（cleave solution 1 + 2.1）
6. 重复步骤3-5共7轮
7. 热甲酰胺剥离引物/探针
8. 使用引物N-1, N-2, N-3, N-4重复步骤2-7

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 测序引物数 | 5个 (N, N-1~N-4) | 每个偏移1个碱基 |
| 每个引物连接轮数 | 7轮 | 每轮探测2个碱基 |
| T4 DNA连接酶 | 6 U µl⁻¹ | 连接荧光探针 |
| 探针长度 | 8 bases | 荧光八碱基探针 |
| 连接时间 | 45 min (RT) | 连接反应时间 |
| 成像通道 | 4色 (FAM, Cy3, Texas Red, Cy5) | 荧光检测 |
| 总测序时间 | 10 d (30 cycles) | 包括所有引物和轮次 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SOLiD | Sequencing by Oligonucleotide Ligation and Detection |
| Color space | SOLiD特异的双碱基颜色编码空间 |
| Dinucleotide interrogation | 每次连接探测一个双碱基对 |
| Terminator cleavage | 切割荧光基团和3个碱基，产生磷酸化5'端用于下一轮连接 |
| Strip buffer | 80%甲酰胺，用于剥离引物/探针 |

## 复现
- 试剂：SOLiD ToP sequencing kit (Applied Biosystems 4449388), T4 DNA ligase (Enzymatics L6030-LC-L)
- 关键：连接法测序在室温工作，无需加热台；颜色空间序列必须保持在颜色空间中比对

## 生物学意义
SOLiD连接法测序的优势：1）室温工作，可在标准显微镜上进行；2）双碱基探测方案每个碱基被检测两次，降低错误率；3）使用标准荧光团（FAM, Cy3, Texas Red, Cy5）。劣势：1）颜色空间序列转换易传播错误；2）读长受限（~30 bp）。每轮连接后图像质量下降，25轮后显著退化。

## 涉及 Figures
- **Fig. 1b** — SOLiD测序原理示意
- **Fig. 4** — SOLiD颜色编码与解码方案
- **Box 1** — SOLiD测序化学详细说明
- **Fig. 6** — 测序步骤23-33
