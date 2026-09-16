# Method: 跨注释分析（Cross-annotation analysis）

## 原文（Methods）
> To compare OPT's results with different reference annotations, we used the most recent releases of GENCODE basic (v47), GENCODE comprehensive (v47), RefSeq (v110), and CHESS (v3.1.3) annotation of the GRCh38 genome. Note that GENCODE 'basic' is the more reliable version of the annotation and is much closer to RefSeq and CHESS. GENCODE 'comprehensive' includes hundreds of thousands of low-quality annotations, which we included in some of our analyses for completeness. Note also that GRCh38 has many non-reference sequences called 'alternative scaffolds'; we removed these for our analysis. We then used gffread to extract transcripts as defined in these annotations by running:
> `$ gffread -w transcripts.fa -g grch38.p12/14.fa annotation.gff`
> The GRCh38.p14 assembly was used during transcript sequence extraction for all reference annotations, except for CHESS which specifies that the annotation maps genes and transcripts onto the GRCh38.p12 assembly. For RefSeq, we renamed the VD(J) segment features as transcript features to ensure consistency, and we also removed transcript sequences with the gene_biotype 'pseudogene'.

## 解读

### 意义
回答"脱靶预测结果有多依赖参考注释"这一方法学稳健性问题：OPT 的比对目标是由注释定义的转录本集合，不同注释（基因/转录本数量、质量、假基因收录策略不同）会改变转录本集合，从而改变哪些探针被判为脱靶。本文用四套注释平行运行，量化预测结果的注释依赖性，并给出实际操作建议。

### 输入
- 四套 GRCh38 注释（均为最新版本）：
  - GENCODE basic v47
  - GENCODE comprehensive v47
  - RefSeq v110
  - CHESS v3.1.3
- 参考基因组装配：GRCh38.p14（CHESS 除外，使用 GRCh38.p12）
- Xenium 乳腺面板探针靶序列（2582 条 / 313 基因）
- 预处理：移除 GRCh38 的 alternative scaffolds（非参考序列）

### 输出
- 每套注释对应的转录本 FASTA（`transcripts.fa`）
- 各注释下 OPT 预测的脱靶探针与受影响基因集合
- 跨注释比较结果：乳腺面板受影响基因数 GENCODE basic v47 为 14/313，CHESS v3.1.3 为 23/313
- 结论性判断：哪些脱靶预测是稳健的（跨注释一致），哪些是注释特异的

### 核心步骤
1. 下载四套最新注释：GENCODE basic v47、GENCODE comprehensive v47、RefSeq v110、CHESS v3.1.3
2. 移除 GRCh38 中的 alternative scaffolds（非参考序列），避免假比对
3. 用 gffread 从注释 + 参考基因组提取转录本序列：`gffread -w transcripts.fa -g grch38.p12/14.fa annotation.gff`
4. 装配选择：除 CHESS 用 GRCh38.p12（该注释自身指定）外，其余全部使用 GRCh38.p14
5. RefSeq 特殊处理：把 VD(J) segment 特征重命名为 transcript 特征以保持一致性
6. RefSeq 额外过滤：移除 gene_biotype 为 `pseudogene` 的转录本序列；`transcribed_pseudogene` 类型本就不注释转录本，仅注释假基因的转录本子集被视为注释错误
7. 将各注释提取的转录本 FASTA 作为 OPT 的 target 输入，对同一探针集重复脱靶预测
8. 跨注释比较受影响基因集合，评估预测对注释的敏感性（如 Appendix 1—figure 1、2）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| GENCODE basic | v47 | 更可靠、与 RefSeq/CHESS 更接近的注释版本 |
| GENCODE comprehensive | v47 | 含数十万低质量注释，为完整性纳入部分分析 |
| RefSeq | v110 | 需重命名 VD(J) segment 并去假基因 |
| CHESS | v3.1.3 | 唯一指定映射到 GRCh38.p12 的注释 |
| 参考基因组装配 | GRCh38.p14（CHESS 用 p12） | 提取转录本序列所用装配 |
| 非参考序列 | 移除 alternative scaffolds | 避免假比对 |
| 提取工具 | gffread | `-w transcripts.fa -g genome.fa annotation.gff` |
| RefSeq 过滤 | 移除 `gene_biotype == pseudogene` | 去除假基因转录本 |
| 探针集 | 2582 条 / 313 基因 | 乳腺面板 |
| 受影响基因数 | GENCODE basic v47：14/313；CHESS v3.1.3：23/313 | 注释间差异明显 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Reference annotation | 参考注释，定义基因/转录本结构（GFF/GTF） |
| GENCODE basic | GENCODE 的高置信子集，每个基因选一个代表性转录本 |
| GENCODE comprehensive | GENCODE 全量注释，含大量低质量/预测转录本 |
| RefSeq | NCBI 参考序列数据库注释 |
| CHESS | 哈佛 CHESS 项目的人类转录本注释，含大量新转录本 |
| Alternative scaffold | GRCh38 的非参考序列（未定位到主染色体的 contig） |
| gffread | 从 GFF/GTF + 基因组提取转录本序列的工具（Cufflinks 套件） |
| VD(J) segment | 免疫球蛋白/T 细胞受体基因的可变多样性连接片段特征 |
| gene_biotype | 基因生物类型（protein_coding、pseudogene、lncRNA 等） |
| Annotation dependency | 脱靶预测结果对所用注释版本的敏感程度 |

## 复现
- GENCODE v47：https://www.gencodegenes.org/human/release_47.html
- RefSeq（NCBI）：https://www.ncbi.nlm.nih.gov/refseq/
- CHESS v3.1.3：https://chess.personal-genome.org/
- GRCh38 装配（含 p12/p14）：https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.40/
- gffread：https://github.com/gpertea/gffread
- OPT：https://github.com/JEFworks-Lab/off-target-probe-tracker
- 代码片段（关键调用）：
```bash
# 从注释提取转录本序列（CHESS 用 grch38.p12，其余用 grch38.p14）
gffread -w transcripts.fa -g grch38.p14.fa annotation.gff
# RefSeq：重命名 VD(J) segment 为 transcript 并去除 pseudogene 后，再跑 OPT
python3 opt.py all -q probes.fa -t transcripts.fa -a annotation.gff -pl 10
```

## 生物学意义
"某个探针是否脱靶"并非纯粹的序列事实，而是相对于某个转录本集合的判断：注释越宽松（comprehensive、CHESS 收录大量新转录本与假基因），被判定为脱靶的机会越多，但也越可能引入低质量/假阳性注释；越严格（GENCODE basic、RefSeq）越保守，可能漏掉真实脱靶。本文因此建议以 GENCODE basic 为主、跨注释交叉验证。生物学上这与基因家族演化直接相关——旁系同源基因、假基因、lncRNA 是脱靶的主要来源，而这些序列在不同注释数据库中的收录口径差异最大。局限：无法判定未被任何注释记录的转录本造成的脱靶；不同注释的版本更新会随时间改变结论，方法学结论具有"时效性"。

## 涉及 Figures
- **Fig. 5 / Fig. 6** — 不同参考注释下预测脱靶基因的差异
- **Appendix 1—figure 1** — 跨注释脱靶预测比较
- **Appendix 1—figure 2** — 注释版本更新对预测结果的影响
- **Supplementary files 2–8** — 各注释下乳腺面板预测脱靶基因列表
