# Method: Encoding probe 设计与 oligopool 构建

## 原文（Methods）

> We used array-synthesized oligopools as templates to make the encoding probes (22, 23). The template molecule for each encoding probe contains three components: i) a central targeting sequence for in situ hybridization to the target RNA, ii) two flanking readout sequences designed to hybridize each of two distinct readout probes, and iii) two flanking primer sequences to allow enzymatic amplification of the probes (Fig. S3).
>
> The readout sequences were assigned to the encoding probes such that for any RNA species each of the 4 readout sequences were distributed uniformly along the length of the target RNA and appeared at the same frequency.
>
> To design the central targeting sequences of the encoding probes, we first compiled the abundance of different transcripts in IMR90 cells using Cufflinks v2.1 (45), total RNA data from the ENCODE project (46), and human genome annotations from Gencode v18 (20). Probes were designed from gene models corresponding to the most abundant isoform using OligoArray2.1 (47) with the following constraints: the target sequence region is 30-nt long; the melting temperatures of the hybridized region of the probe and cellular RNA target is greater than 70°C; there is no cross hybridization targets with melting temperatures greater than 72°C; there is no predicted internal secondary structures with melting temperatures greater than 76°C; and there is no contiguous repeats of 6 or more identical nucleotides.
>
> The final probes were eluted in 100 μL of RNase-free deionized water, evaporated in a vacuum concentrator, and then resuspended in 10 μL of encoding hybridization buffer (recipe below). Probes were stored at -20°C.

## 解读

### 意义
用"两步标记"（先 encoding probe 把 RNA 转换成 readout sequence 组合，再用荧光 readout probe 读出）替代"each gene 一套荧光探针"，把探针成本与杂交时间从不可承受降到可行：readout 杂交仅需 15 min，而直接杂交到细胞 RNA 需 >10 小时。

### 输入
- IMR90 转录组丰度（Cufflinks v2.1 + ENCODE total RNA）+ Gencode v18 注释
- 每个 RNA species 的 code word（决定 4 个 readout sequences）
- 阵列合成 oligopool（CustomArray），140 基因库与 1001 基因库可嵌在同一个 pool 中用 indexed PCR 选择性扩增

### 输出
- encoding probe 模板库与最终探针（resuspend 于 10 μL encoding hybridization buffer）
- 每基因约 192 条（140 基因实验）/ 约 94 条（1001 基因实验）探针
- Table S5 中的全部模板序列

### 核心步骤
1. 以最丰富 isoform 的 gene model 为起点，把 isoform 切成 1-kb 区块以降低计算量。
2. 用 OligoArray2.1 设计 30-nt 靶向序列，满足 Tm 与二级结构约束（见下表）。
3. BLAST+ 剔除映射到 >1 个 RNA species 的探针；保留在同一 RNA 上有多个靶点的探针。
4. 拼接 index primer + readout sequences + targeting region，生成 198 条（140 基因）或 96 条（1001 基因）候选序列。
5. BLAST+ 二次筛选拼接产生的新同源区：与 rRNA/tRNA 同源 >14 nt、与高表达基因（FPKM > 10,000）同源 >17 nt 的探针剔除 → 得 ~192（SD 2）/ ~94（SD 6）条/基因。
6. 四步合成：limited-cycle PCR（含 T7 反向引物）→ 高产量 IVT → 反转录成 DNA → EDTA/NaOH 95°C 水解 RNA 后柱纯化。
7. 变性 PAGE 与吸收光谱质检：90–100% 反转录引物转为全长探针，纯化回收 70–80%。

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 靶向序列长度 | 30 nt | 中心 RNA 靶向区 |
| 每条 encoding probe readout sequences | 2 条 | 4 个 readout 中的 2 个 |
| 140 基因实验 readout 池 | 16 条（bit 1–16） | 对应 16 轮杂交 |
| 1001 基因实验 readout 池 | 14 条（bit 1–14） | 对应 14 轮杂交 |
| readout sequence 长度 | 30 nt | 由正交引物片段拼接而成 |
| 探针/基因（140 基因） | ~192（SD 2） | 起始 198 条候选 |
| 探针/基因（1001 基因） | ~94（SD 6） | 起始 96 条候选，需从单一 100,000-member pool 合成 |
| 靶向区 Tm | >70°C | 探针–RNA 杂交区 |
| 交叉杂交 Tm 上限 | ≤72°C | 特异性约束 |
| 内部二级结构 Tm 上限 | ≤76°C | 避免自折叠 |
| 连续重复 | 无 ≥6 nt 同核苷酸重复 | 合成与杂交质量 |
| 同源剔除阈值 | >14 nt（rRNA/tRNA）；>17 nt（FPKM>10,000） | 脱靶过滤 |
| PCR 引物长度 | 20 nt（源自 25-nt 正交集） | Tm 70–80°C、含 GC clamp |
| 每轮每 RNA 最多结合的 readout probe | ~96 | 192 条探针 × 一半 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Encoding probe | 中心靶向序列 + 两侧 readout sequences + 两侧 PCR 引物序列的探针 |
| Readout sequence | 被荧光 readout probe 识别的序列，一轮杂交对应一条 |
| Readout probe | 与 readout sequence 互补、3′ 端 Cy5 标记的荧光探针 |
| Oligopaint 式扩增 | 从阵列 oligopool 出发，经 PCR→IVT→反转录大量扩增探针的流程 |
| Indexed PCR | 用实验特异的正交引物从一个混合 oligopool 中选择性扩增目标探针 |
| No-target word | 有 encoding probe 但靶向序列为随机序列、不靶向任何细胞 RNA 的对照 |

## 复现
- 工具：OligoArray2.1（靶向序列设计）、BLAST+（脱靶筛选）、Cufflinks v2.1（丰度）、Gencode v18（注释）
- 试剂：CustomArray oligopool；NEB E2040S IVT；Maxima H- 反转录酶（Thermo EP0751）；Zymo D4003 / D4030
- 关键调用：

```bash
# 靶向序列设计约束（OligoArray2.1 思路的等价约束）
# Tm(probe-RNA) > 70 C; cross-hyb Tm <= 72 C; internal structure Tm <= 76 C
# no >=6 nt homopolymer; target length = 30 nt
blastn -query candidate_probes.fa -db human_rRNA_tRNA -outfmt 6   # 剔除 >14 nt 同源
blastn -query candidate_probes.fa -db highly_expressed_genes -outfmt 6  # 剔除 >17 nt 同源
```

## 生物学意义
探针设计决定了 MERFISH 的灵敏度下限（信号背景比）与特异性上限（脱靶导致的假阳性）。每 RNA 约 192 条探针是本文用于保证单分子可辨识度的选择，作者明确指出探针数可大幅减少（文献 17, 48, 49），增加每条探针的 readout 数或使用光学切片降低背景也可进一步减少。局限：靶向最丰富 isoform 意味着 isoform 层面的信息被平均掉；1001 基因库受单一 oligopool 容量限制，每基因探针数被迫减半。

## 涉及 Figures
- **Fig. 1E** — encoding probe 结构（中心靶向区 + 两侧 readout sequences）与两步标记流程示意。
- **Fig. S3** — 探针四步合成流程图（PCR → IVT → 反转录 → 纯化）。
- **Fig. 2 / Fig. 5** — 两套探针库（~192/基因、~94/基因）的实际测量结果。
