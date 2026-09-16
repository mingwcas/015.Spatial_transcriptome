# Method: OPT (Off-target Probe Tracker)

## 原文（Methods）
> OPT (Off-target Probe Tracker) is a Python program that runs nucmer (Marçais and Kingsford, 2011) for alignment and then processes the results to predict probe binding based on sequence homology. OPT is available as an open-source Python toolkit at https://github.com/JEFworks-Lab/off-target-probe-tracker. When a user provides a query probe target sequence file, a target transcript sequence file, and the annotation used to extract these transcripts, OPT outputs which gene each probe is likely to bind to. By default, OPT saves nucmer results in SAM format and finds perfect sequence matches between a query probe and a target transcript, requiring that alignments consist of only matches and cover the entirety of the query. OPT consists of four modules: (1) flip for reverse complementing probe target sequences aligned to the opposite strand of their target genes; (2) track for aligning probe target sequences and processing alignment results; (3) stat for compiling summary statistics on the number of off-target binding probes and affected genes; and (4) all for running the flip, track, and stat modules at once.

## 解读

### 意义
本文提出的核心计算工具，通过将探针靶序列比对到参考转录组，预测探针的脱靶结合（off-target binding），从而在数据分析前评估 Xenium 基因面板的探针特异性。

### 输入
- Query：探针靶序列 FASTA 文件（Xenium 为 40 bp）
- Target：参考转录组序列文件（由注释 GFF + 参考基因组提取）
- Annotation：用于提取转录本的基因组注释（GENCODE / RefSeq / CHESS）
- 参数：`-pl`（pad length，允许末端错配的长度）

### 输出
- 每个探针最可能结合的基因（SAM 格式中间结果）
- 脱靶结合探针数与被影响基因数的汇总统计
- 靶基因 → 预测脱靶基因 的映射表（Supplementary files 2–10）

### 核心步骤
1. 用 `gffread` 从注释 + GRCh38 提取转录本序列
2. `flip` 模块：将比对到靶基因反义链的探针靶序列反向互补（本文 2563/2582 条需翻转）
3. `track` 模块：调用 nucmer，以 maximal exact matches 为锚点连接更长比对；默认要求**完全匹配且覆盖整条 query**
4. `stat` 模块：统计脱靶探针数与受影响基因数
5. `all` 模块：一键运行 flip + track + stat
6. 同义词处理：若比对到靶基因的同义名（如 NARS → NARS1），仍视为 on-target（同义词来自 GeneCards/HGNC）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 探针靶序列长度 | 40 bp | Xenium v1 padlock 探针两条 20 bp 臂拼接而成 |
| 默认匹配模式 | 完美匹配（perfect homology） | 100% identity 且覆盖整条 query |
| `-pl`（pad length） | 0（默认）/ 10（本文宽松模式） | 允许 query 两端各 N bp 内出现错配/插入/缺失/clipping |
| `-pl = 10` 实际含义 | 中间 20 bp 必须匹配 | 保留含连接位点的核心区 |
| 参考注释 | GENCODE basic v47 / GENCODE comprehensive v47 / RefSeq v110 / CHESS v3.1.3 | GRCh38 基因组 |
| nucmer 输出格式 | SAM | 默认 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| OPT | Off-target Probe Tracker，本文开发的脱靶探针预测工具 |
| Off-target binding | 探针结合到非预期靶基因的转录本上 |
| Padlock probe | 锁式探针，两条 20 bp 臂结合 mRNA 后由连接酶环化，形成 40 bp 靶区 |
| Ligation site | 连接位点，位于探针靶序列中央，连接酶偏好特定 2 bp 连接 |
| Perfect sequence homology | 完全序列同源（100% identity、40 bp 全覆盖） |
| Synonym | 基因同义名，比对到同义名不算脱靶 |
| nucmer | 基于 maximal exact matches 的快速核苷酸比对器（MUMmer 套件） |

## 复现
- OPT 开源工具：https://github.com/JEFworks-Lab/off-target-probe-tracker
- 归档快照（Software Heritage）：swh:1:rev:8ca930d2e8e53a72c053c3a1a12077ae4a711333
- 依赖：nucmer（MUMmer）、pyfaidx、pandas、gffread（提取转录本）
- 代码片段（关键调用）：
```bash
# 1) 从注释提取转录本序列
gffread -w transcripts.fa -g grch38.p14.fa annotation.gff
# 2) 反向互补靶向反义链的探针
python3 opt.py flip -q probes.fa -t transcripts.fa -a annotation.gff
# 3) 比对 + 统计（-pl 10 允许末端 10 bp 错配）
python3 opt.py all -q probes.fa -t transcripts.fa -a annotation.gff -pl 10
```

## 生物学意义
探针特异性是基于探针的原位空间转录组（Xenium）数据可靠性的前提。OPT 将"探针是否脱靶"从实验后的偶然发现，变为实验前的可计算预测。本文证明脱靶主要发生在**旁系同源基因（paralogs）**——基因复制后序列高度相似的大家族成员（如 actin、tubulin、keratin、APOBEC3、ADH 家族），以及假基因（pseudogenes）和 lncRNA。局限：序列比对只能提示"可能脱靶"，不能判断脱靶基因是否在该组织中表达；因此需结合组织特异性的 RNA-seq 图谱共同判断（如本文的 HuBMAP 分析）。此外 OPT 无法捕捉探针自杂交、探针-探针互作等非序列同源来源的非特异信号。

## 涉及 Figures
- **Fig. 1** — 脱靶结合的示意图（探针臂结合非靶基因）
- **Appendix 1—figure 1, 2** — 跨注释脱靶预测差异
- **Appendix 1—figure 6** — 末端错配脱靶与探针互作示意
