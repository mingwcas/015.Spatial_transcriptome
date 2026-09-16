# Method: 获取 Xenium v1 人类乳腺基因表达面板的探针靶序列

## 原文（Methods）
> To identify potential off-target binding impacting the 10x Genomics Xenium v1 Human Breast Gene Expression Panel, we obtained the FASTA file of probe target sequences from the Janesick et al. publication courtesy of 10x Genomics and available as Supplementary file 1 for preservation. Notably, this panel slightly deviates from the commercially available Xenium v1 Human Breast Gene Expression Panel (Appendix Note). The target gene names and IDs were extracted from the probe IDs of the following format: > gene_id|gene_name|accession
> We expected the provided FASTA file to contain probe target sequences to be the reverse-complemented sequence of their intended target genes and hence align to the reverse strand of their target isoforms. However, when we aligned the breast panel probe target sequences to the GENCODE basic (v47) reference transcripts using nucmer, we found that 2563/2582 of probe target sequences aligned on the reverse strand of their target transcripts (i.e., isoforms of their target genes). For consistency, we enforced that all probe target sequences be oriented in the same direction and align to the forward strand of their target genes and transcripts. As such, we reverse-complemented these 2563 probe target sequences.

## 解读

### 意义
解决"探针靶序列从哪来、以何种链方向存在"的问题：把 10x Genomics 提供的 Xenium v1 乳腺面板探针序列整理为与参考转录本同向（forward strand）的 FASTA，作为 OPT 脱靶预测的合规输入，避免因链方向不一致造成的假阴性。

### 输入
- Janesick et al. 发表的 Xenium v1 Human Breast Gene Expression Panel 探针靶序列 FASTA（由 10x Genomics 提供，本文作为 Supplementary file 1 存档）
- 参考注释：GENCODE basic (v47) 参考转录本
- 探针 ID 命名格式：`>gene_id|gene_name|accession`

### 输出
- 2582 条探针靶序列（40 bp）
- 覆盖 **313 个唯一基因**，平均 8 条探针/基因，范围 2–21 条
- 链方向统一后的（forward-oriented）探针 FASTA，供 OPT `track` 使用
- 其中 2563 条被反向互补（reverse-complemented）

### 核心步骤
1. 从 Janesick et al. 发表材料中取得探针靶序列 FASTA（本文存档为 Supplementary file 1）
2. 按 `gene_id|gene_name|accession` 格式解析探针 ID，提取靶基因名与基因 ID
3. 用 nucmer 将全部探针靶序列比对到 GENCODE basic (v47) 参考转录本
4. 检查比对链方向：发现 2563/2582 条比对到靶转录本的**反义链**
5. 对这 2563 条探针靶序列做反向互补，使全部探针与靶基因/转录本同为 forward 方向
6. 该功能被固化为 OPT 的 `flip` 模块，保证下游结合预测以同向比对为前提

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 探针靶序列数 | 2582 | 面板内全部探针靶序列条数 |
| 靶基因数 | 313 | 面板覆盖的唯一基因数 |
| 探针长度 | 40 bp | 两条 20 bp 臂拼接后的靶区长度 |
| 每基因探针数 | 平均 8（范围 2–21） | 单基因的探针冗余度 |
| 需反向互补的探针 | 2563 / 2582 | 原始 FASTA 中比对到反义链的比例（≈99.3%） |
| 参考注释 | GENCODE basic v47 | 用于判断链方向 |
| 比对器 | nucmer | MUMmer 套件 |
| 探针 ID 格式 | `gene_id\|gene_name\|accession` | 解析靶基因的依据 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Probe target sequence | 探针靶序列，Xenium 中为两条 20 bp 臂拼接成的 40 bp 序列 |
| Flip | OPT 模块，将比对到靶基因反义链的探针靶序列反向互补 |
| Forward strand | 与参考转录本同向的链方向；本文统一后的方向 |
| Reverse complement | 反向互补，DNA 双链另一条链的等价序列 |
| Janesick panel | Janesick et al. 使用的 Xenium v1 乳腺面板，与商品化面板略有差异 |
| Supplementary file 1 | 本文存档的探针靶序列 FASTA |

## 复现
- 探针序列来源：Janesick A et al., Nat. Commun. 14, 8353 (2023)；本文 Supplementary file 1 存档
- 面板与数据下载：https://www.10xgenomics.com/products/xenium-in-situ/preview-dataset-human-breast
- OPT 工具：https://github.com/JEFworks-Lab/off-target-probe-tracker
- 代码片段（关键调用）：
```bash
# 用 nucmer 检查探针比对链方向（GENCODE basic v47 转录本）
nucmer --sam-short ref_transcripts.fa probe_targets.fa
# 对反义链探针做反向互补（OPT flip 模块）
python3 opt.py flip -q probe_targets.fa -t transcripts.fa -a gencode.v47.basic.gff
```

## 生物学意义
Xenium 探针为锁式探针（padlock probe），其两条 20 bp 臂需与 mRNA 上相邻序列互补结合后才能被连接酶环化并滚环扩增——因此**链方向与序列互补性缺一不可**。10x 提供的 FASTA 中绝大多数探针为反义链取向，说明该文件面向的是"与 mRNA 互补"的物理探针序列，而非 mRNA 同向序列；不统一方向直接比对，会系统性低估完美匹配并导致脱靶预测假阴性。局限：探针靶序列的公开交付格式不统一（且该面板与商品化面板并不完全一致），流程的可复现性依赖于上游是否公布了原始 FASTA。

## 涉及 Figures
- **Appendix Note** — 本文使用面板与商品化 Xenium v1 Human Breast 面板的差异说明
- **Supplementary file 1** — 探针靶序列 FASTA 的存档
- **Fig. 1** — 探针靶序列与靶基因关系的示意
