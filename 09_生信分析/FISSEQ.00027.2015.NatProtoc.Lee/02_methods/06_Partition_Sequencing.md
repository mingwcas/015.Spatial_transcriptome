# Method: 分区测序（Partition Sequencing）

## 原文（Methods）
> T4 DNA ligase has a single-base specificity at the ligation junction, and sequencing primers differing by one base can recognize different sets of amplicons. By dividing imaging over multiple separate runs, spatially overlapping amplicons can be enumerated using multiple sequencing primers even on a low-resolution microscope. The cDNA or padlock probe template can include three random nucleotides in equal proportions. By controlling the length of the complementary portion of the sequencing primer to the random bases, one can ligate fluorescent probes to different amplicon pools of varying sizes.

## 解读

### 意义
通过利用cDNA模板中3个随机核苷酸的组合多样性，将空间重叠的扩增子分区到不同子集进行成像，克服光学分辨率限制

### 输入
- 含3个随机核苷酸（P1, P2, P3）的cDNA扩增子
- 具有不同长度互补区的测序引物

### 输出
- 不同大小的扩增子池的独立成像结果，可外推估计实际扩增子数量

### 核心步骤
1. cDNA模板中包含3个随机核苷酸（4³ = 64种组合）
2. 使用不同互补长度的测序引物（0-3个碱基互补）进行连接测序
3. 每种引物识别不同大小的扩增子子集（1/64, 4/64, 16/64, 64/64）
4. 从每个引物类别的平均计数外推估计实际扩增子数量

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 随机核苷酸数 | 3个 | 4³ = 64种组合 |
| 测序引物互补长度 | 0, 1, 2, 3 bases | 控制扩增子池大小 |
| 最大分区数 | 64 bins | 理论上可区分64个子集 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Partition sequencing | 利用随机条形码将扩增子分区的策略 |
| Random barcode | cDNA模板中的3个随机核苷酸 |
| Serial dilution analogy | 类似于连续稀释实验的计数方法 |

## 复现
- 需要修改RT引物设计以包含3个随机核苷酸
- 需要合成具有不同互补长度的测序引物
- 需要自动化以处理多次成像运行

## 生物学意义
分区测序解决了FISSEQ中一个关键问题：在低分辨率显微镜下无法区分空间重叠的扩增子。通过将扩增子随机分配到64个bin中，即使在低分辨率下也能准确计数。此策略特别适用于量化短条形码序列而非全长RNA序列。

## 涉及 Figures
- **Fig. 3** — 分区测序原理与扩增子计数
