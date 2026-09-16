# Method: cFos 行为激活映射（parenting、mating、aggression）

## 原文（Methods）
> To investigate the role of specific neuronal populations in discrete social behaviors, we included cFos in MERFISH measurements and characterized animals after parenting, aggression, or mating. We performed clustering analysis of these behavioral samples together with naïve samples not subjected to behavioral stimuli and did not observe any cluster that was present only in behavioral samples.
> For each behavior, only a few neuronal clusters, each characterized by key markers, exhibited a statistically significant enrichment in cFos-positive cells (Fig. 8, A and B, and fig. S20).
> Red bars marked with asterisks are clusters with statistically significant enrichment in cFos-positive cells... (binomial test; false-discovery rate < 5%). Error bars represent standard error of the mean (n = 3 to 5 replicates).

**来源**：正文 Results（PDF p.10–11）与 Fig. 8 caption（PDF p.10）。

## 解读

### 意义
把"分子定义的细胞类型"与"行为发生时被激活"连接起来，识别 parenting、mating 和 aggression 各自偏好的神经元集群，并比较性别/生理状态差异。

### 输入
- MERFISH 细胞 × 155 基因矩阵，额外包含 immediate-early gene **cFos**
- naïve 动物与行为刺激动物的细胞分割、集群标签
- 行为组：virgin female + pups、mothers、fathers、virgin male + pups（pup-directed aggression）、inter-male aggression、female mating、male mating
- 每个行为组 3–5 个生物学重复；行为组每只动物 4 片（naïve 为 12 片）

### 输出
- 各神经元集群 cFos+ 细胞富集比例与显著性
- 行为特异性激活集群列表与 Venn diagram
- 16 μm 切片的 ISH 验证图
- 关键细胞类型：I-14、I-10、I-15、I-16、I-2、I-24、E-1、E-8、E-15 等

### 核心步骤
1. 将 cFos 纳入 MERFISH gene panel，并对行为后动物做组织取样
2. 用与 naïve 样本相同的方法聚类，确认行为刺激没有产生只存在于行为组的新集群
3. 对每个集群计算 cFos+ 细胞比例，与全部细胞的 cFos+ 背景比例比较
4. 采用二项检验，跨集群多重比较控制 FDR < 5%
5. 仅展示每种行为中至少 2 个重复各有 ≥10 个细胞的集群；误差条为 SEM
6. 用 2–3 色 ISH 验证能由两个 marker + 空间位置明确界定的集群
7. 以 Venn diagram 汇总不同性别、生理状态与行为的共同/特异激活集群

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 活动标志物 | cFos | immediate-early gene，行为活动读出 |
| 显著性检验 | binomial test，FDR < 5% | 集群 cFos+ 富集 |
| 生物学重复 | n = 3–5 | 每种行为组的独立动物重复 |
| 切片数 | 行为组 4 / naïve 12 per animal | 行为动物因实验设计减少采样 |
| 最低显示条件 | ≥10 cells in ≥2 behavior replicates | 排除极低丰度不稳定集群 |
| 验证切片 | 16 μm-thick | cFos 与 cluster marker 的 ISH 共定位 |
| MERFISH 切片 | 10 μm-thick | 主实验成像切片 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| cFos enrichment | 某集群 cFos+ 比例相对全细胞背景的富集 |
| IEG | immediate-early gene，即时早期基因 |
| Parenting | 母亲/父亲/未孕雌性对幼崽的育幼行为 |
| Pup-directed aggression | 未交配雄性对幼崽的攻击行为 |
| Binomial test | 二项分布检验，用于比较 cFos+ 比例 |
| SEM | standard error of the mean，均值标准误 |

## 复现
- 数据：Dryad **10.5061/dryad.8t8s248**
- 代码：https://github.com/ZhuangLab/MERFISH_analysis
- 行为协议参考：Wu et al. (2014)、Kimchi et al. (2007)、Stowers et al. (2002)

```python
# 概念性统计流程
for cluster in clusters:
    p = binom_test(cfos_positive[cluster], n_cells[cluster],
                   p=background_cfos_rate)
q = fdr_correction(p, method="BH")
sig = clusters[q < 0.05]
```

## 生物学意义
cFos-MERFISH 证明三类社会行为各自主要激活少数分子定义的集群，同时许多集群有较弱的广泛激活，提示专门回路与跨回路串扰并存。I-14（Gal/Avpr1a）在所有 parenting 动物激活；I-10（Oxtr）在 mother/father 激活；I-15（Esr1）在 mating female 最突出；I-16（Gal/Th、Vmat2/Ddc、Oprd1/Oprk1）在雄性攻击和父亲育幼中激活。局限：cFos 低诱导时可能低于背景而漏检弱激活集群；行为组每只动物仅 4 片，空间采样少于 naïve；统计富集不等于该集群对行为的因果必要性。

## 涉及 Figures
- **Fig. 8A** — 各行为/性别组的 cFos+ 集群富集（binomial test，FDR < 5%）
- **Fig. 8B** — 激活集群的 marker 与受体表达谱
- **Fig. 8C** — 16 μm ISH 验证（I-14、E-1、I-2、I-16 等）
- **Fig. 8D** — 行为激活集群的 Venn diagram
- **fig. S20 / S21** — 行为样本完整激活统计与 ISH 验证
