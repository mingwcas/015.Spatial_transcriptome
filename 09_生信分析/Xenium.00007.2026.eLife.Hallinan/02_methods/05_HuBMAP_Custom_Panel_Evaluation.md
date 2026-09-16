# Method: HuBMAP 定制探针面板的提取与评估

## 原文（Methods）
> To evaluate potential off-target binding in the HuBMAP placenta and multi-tissue (heart, kidney, and lung) custom probe panels, we first downloaded the corresponding BED files from the HuBMAP portal. Using pyfaidx and pandas in Python, we extracted each probe's target gene name, gene identifier, and genomic coordinates from the BED files, and then generated FASTA files by retrieving the corresponding sequences from the reference genome (GRCh38). These FASTA files were then used as input to OPT to predict potential off-target binding.
> To assess whether predicted off-target genes were likely to confound Xenium results in the HuBMAP custom probe panels, we evaluated the expression of the predicted off-target genes in matched HuBMAP RNA-seq datasets corresponding to the tissues for which each panel was designed. Four RNA-seq datasets were downloaded from the HuBMAP portal: a bulk RNA-seq dataset for the placenta and scRNA-seq datasets for the heart, kidney, and lung.
> For each tissue, raw count matrices were normalized to CPM and averaged across all cells to obtain a bulk-like mean expression profile. Log1p-transformed mean CPM values were used for all downstream comparisons. OPT was run on the two HuBMAP custom probe panels with all RNA species included and a pad length of 10. Since OPT reports transcript-level identifiers, we removed transcript-specific suffixes from Ensembl IDs to align them with gene symbols present in the RNA-seq datasets.

## 解读

### 意义
把本文的方法从商品化面板推广到**用户自建（custom）探针面板**这一高风险场景：自建面板缺乏厂商的探针特异性验证，需先预测脱靶，再结合配对组织的 RNA-seq 判断"预测到的脱靶基因在该组织里是否真的表达"——只有表达的脱靶基因才会造成实际污染。

### 输入
- HuBMAP 定制面板 BED 文件（BED 含探针的基因组坐标、靶基因名与基因 ID）
  - 胎盘（placenta）定制面板
  - 多组织（heart, kidney, lung）定制面板
- 参考基因组 GRCh38（用于按坐标取序列）
- 四个配对 HuBMAP RNA-seq 数据集：胎盘 bulk RNA-seq；心脏、肾脏、肺 scRNA-seq
- OPT 参数：包含所有 RNA species，pad length = 10

### 输出
- 由 BED 坐标提取的各面板探针靶序列 FASTA（作为 OPT 输入）
- 每个靶基因的预测脱靶基因列表（OPT 结果）
- 各组织 log1p(mean CPM) 表达谱
- 热图：行 = 预期靶基因，列 = 其预测脱靶基因（按表达从高到低排序），用于比较脱靶表达的幅度与组织特异性
- 关键数字：胎盘面板 49 个基因存在预测脱靶；多组织面板 24 个基因存在预测脱靶

### 核心步骤
1. 从 HuBMAP portal 下载胎盘面板与多组织面板的 BED 文件
2. 用 **pyfaidx + pandas** 从 BED 中解析每条探针的靶基因名、基因 ID、基因组坐标
3. 按坐标从 GRCh38 参考基因组取出对应序列，生成 FASTA
4. 将 FASTA 输入 OPT，预测潜在脱靶结合（含所有 RNA species，`-pl 10`）
5. 从 HuBMAP portal 下载 4 个配对 RNA-seq 数据集（胎盘 bulk；心/肾/肺 scRNA-seq）
6. 各组织 raw count 矩阵 CPM 归一化，并在所有细胞上取平均，得到类 bulk 的平均表达谱
7. 下游比较统一使用 **log1p 变换后的 mean CPM**
8. 因 OPT 输出转录本级 Ensembl ID，去除 ID 的转录本后缀（版本/`.N`），与 RNA-seq 中的 gene symbol 对齐
9. 对面板中每个靶基因，汇总其全部预测脱靶基因，检查这些脱靶在该组织 RNA-seq 中是否表达
10. 绘制热图（行 = 靶基因，列 = 预测脱靶基因，按表达降序），直观展示脱靶表达的幅度与组织特异性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 面板来源 | HuBMAP 定制面板（胎盘；心/肾/肺多组织） | BED 文件 |
| BED 解析工具 | pyfaidx + pandas（Python） | 提取基因名/ID/坐标 |
| 参考基因组 | GRCh38 | 按坐标取探针靶序列 |
| OPT `-pl`（pad length） | 10 | 允许两端各 10 bp 错配，中间 20 bp 须匹配 |
| OPT RNA species | 全部包含 | 不限定 biotype，纳入各类 RNA |
| ID 处理 | 去除 Ensembl 转录本后缀 | 使 OPT 转录本 ID 与 gene symbol 对齐 |
| 归一化 | CPM → log1p | 各组织表达谱 |
| 组织平均 | 所有细胞求均值 | 生成类 bulk 平均表达谱 |
| 预测脱靶基因数 | 胎盘 49 / 多组织 24 | 有预测脱靶的靶基因数 |
| 配对 RNA-seq | 胎盘 bulk；心/肾/肺 scRNA-seq | 共 4 个 HuBMAP 数据集 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Custom probe panel | 用户自建探针面板，未经厂商特异性验证 |
| BED file | 记录基因组区间（此处为探针坐标）的制表符分隔文件 |
| pyfaidx | Python 库，可按坐标从 FASTA 随机访问序列 |
| GRCh38 | 人类参考基因组装配 |
| Bulk-like mean profile | 将单细胞/单 spot 计数平均后得到的类 bulk 表达谱 |
| mean CPM | 每百万计数均值，跨样本可比的表达量 |
| log1p-transformed | log(1+x) 变换 |
| Ensembl transcript ID suffix | Ensembl ID 的转录本/版本后缀（如 `.1`、`.2`），需去除以匹配 gene symbol |
| RNA species | 转录本类型（mRNA、lncRNA、假基因等） |
| Tissue specificity | 脱靶基因在目标组织中是否表达 |

## 复现
- 面板 BED 文件：
  - 胎盘面板：https://portal.hubmapconsortium.org/browse/dataset/28fe8e4ac8a4193f82fdd9f4d4eb0bb2
  - 多组织面板：https://portal.hubmapconsortium.org/browse/dataset/6f597ca43db80f2499443f5c5bfac97c
- 配对 RNA-seq 数据：
  - 胎盘 bulk：https://doi.org/10.35079/HBM549.BBBQ.445
  - 心脏 scRNA-seq：https://doi.org/10.35079/HBM378.WGXD.394
  - 肾脏 scRNA-seq：https://doi.org/10.35079/HBM793.TLPP.486
  - 肺 scRNA-seq：https://doi.org/10.35079/HBM826.BQLS.392
- OPT：https://github.com/JEFworks-Lab/off-target-probe-tracker
- 代码片段（关键调用，Python + CLI）：
```python
from pyfaidx import Fasta
import pandas as pd
genome = Fasta("grch38.fa")
bed = pd.read_csv("panel.bed", sep="\t", header=None)
seqs = {f"{r[3]}": str(genome[r[0]][int(r[1]):int(r[2])]) for _, r in bed.iterrows()}
```
```bash
# OPT：纳入所有 RNA species，pad length = 10
python3 opt.py all -q hubmap_probes.fa -t transcripts.fa -a annotation.gff -pl 10
```

## 生物学意义
自建面板通常针对特定组织/细胞类型挑选基因，探针设计往往只考虑靶序列本身的唯一性，未系统评估跨基因同源性——因此脱靶风险可能高于商品化面板。本文用"预测脱靶 × 组织表达"双重过滤来判断实际风险：只有在目标组织中被表达的脱靶基因才真正污染信号。局限：该方法上限取决于配对 RNA-seq 能否覆盖全部脱靶基因（gene symbol 匹配可能漏掉部分转录本）；bulk/scRNA-seq 的平均化掩盖细胞类型特异性；OPT 依赖参考注释完整性，且仍无法判断探针自杂交、探针互作等非序列同源来源的非特异信号。

## 涉及 Figures
- **Fig. 5** — HuBMAP 定制面板预测脱靶基因及其在配对组织 RNA-seq 中的表达热图
- **Supplementary file 9 / 10** — 两个 HuBMAP 面板的预测脱靶基因列表
- **Fig. 1** — 探针脱靶结合示意
