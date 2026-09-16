# Method: 155 基因 MERFISH Panel 设计（135 组合 smFISH + 20 顺序 FISH）

## 原文（Methods）
> Next, we performed MERFISH measurements of the preoptic region (1.8 by 1.8 by 0.6 mm, Bregma +0.26 to –0.34), within the area characterized with scRNA-seq, targeting a set of 155 genes (Fig. 3A and table S6) (29). These genes were composed of two groups: (i) 85 preselected genes that were either known markers for major cell classes or relevant to neuronal functions of the hypothalamus, such as neuropeptides and neuromodulator receptors, and (ii) 70 additional genes that were identified with scRNA-seq as neuronal cluster markers but not already included in the 85 preselected genes. Among these 155 genes, 135 genes were imaged by using combinatorial smFISH with an error-robust barcoding scheme, as demonstrated previously for MERFISH (20, 26, 40).
> The remaining 20 genes were relatively short and/or expressed at high levels, which is challenging for combinatorial smFISH detection, and hence were measured in sequential rounds of multicolor FISH after the combinatorial run.
> We imaged 155 genes in MERFISH measurements, with 135 genes imaged by using combinatorial smFISH measurements and 20 additional genes imaged by using sequential rounds of noncombinatorial FISH.

**来源**：正文 Results "MERFISH measurements of the preoptic region"（PDF p.4–5）与 Methods summary（PDF p.12）。

## 解读

### 意义
在成像通道数与成像轮次受限的前提下，把"要测哪些基因"变成可执行的编码方案——用纠错条形码把 135 个基因压进有限轮次，用顺序 FISH 单独处理不适合组合编码的基因。

### 输入
- scRNA-seq 得到的神经元集群差异表达基因清单（70 个新增）
- 文献已知的主要细胞类 marker 与下丘脑功能基因（85 个预选）
- 目标成像区域：1.8 × 1.8 × 0.6 mm（Bregma +0.26 至 –0.34）

### 输出
- 155 基因 panel（table S6）
  - 135 基因：组合 smFISH + 纠错条形码（error-robust barcoding）
  - 20 基因：组合成像后再做顺序多色 FISH（non-combinatorial）
- 全部探针序列（tables S10、S11）
- "最富信息 ~75 基因可恢复 ~90% 集群"的降维结论

### 核心步骤
1. 汇集 85 个预选基因：主要细胞类 marker + 下丘脑相关神经肽 / 神经调质受体
2. 从 scRNA-seq 差异表达结果补充 70 个集群 marker 基因（不与预选 85 个重复）
3. 对 135 个基因分配误差鲁棒条形码，做组合 smFISH 多轮成像
4. 把 20 个"转录本短和/或高表达"（组合检测困难）的基因挑出，改用顺序多色 FISH
5. 评估基因数对聚类的影响：~75 个最富信息基因即可恢复 ~90% 神经元集群

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因总数 | 155 genes | MERFISH 靶基因数 |
| 组合 smFISH | 135 genes | 用纠错条形码并行编码 |
| 顺序 FISH | 20 genes | 组合轮次后单独测（短/高表达基因） |
| 预选基因 | 85 genes | 细胞类 marker + 下丘脑功能基因 |
| scRNA-seq 新增 | 70 genes | 由单细胞数据发现的集群 marker |
| 信息饱和点 | ~75 genes → ~90% clusters | 最富信息基因的边际收益拐点 |
| 成像区域 | 1.8 × 1.8 × 0.6 mm | Bregma +0.26 to –0.34 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| MERFISH | multiplexed error-robust FISH，多重纠错荧光原位杂交 |
| combinatorial smFISH | 多轮组合编码的单分子 FISH，一轮测多位 |
| error-robust barcoding | 允许单比特纠错的条形码方案（如 MHD4 码） |
| sequential FISH | 非组合的顺序多色 FISH，逐轮单独测量 |
| table S6 | 155 基因列表及其分组归属 |

## 复现
- 探针序列：tables S10、S11（Supplementary Materials）
- 方法学基础：Chen et al., Science 348, aaa6090 (2015)；Moffitt et al., PNAS 113, 11046 (2016)
- 代码：https://github.com/ZhuangLab/MERFISH_analysis

```python
# 概念性流程：编码分配 → 探针设计
genes_pre = preselected_markers()          # 85 genes
genes_new = de_markers_from_scRNAseq()     # 70 genes
panel = genes_pre + genes_new              # 155 genes
comb  = [g for g in panel if not short_or_high(g)]   # 135
seqf  = [g for g in panel if short_or_high(g)]       # 20
assign_error_robust_barcodes(comb, min_hamming=4)
```

## 生物学意义
Panel 设计体现了"发现（scRNA-seq）→ 验证与定位（MERFISH）"的闭环：85 个先验基因保证主要细胞类与已知功能细胞可被捕获，70 个数据驱动基因保证新集群可分。局限：155 基因远非全转录组，未入 panel 的基因信息完全缺失；部分 scRNA-seq 集群因此无法在 MERFISH 中找到对应。~75 基因即达 90% 恢复率说明大量基因是冗余的——但剩余 10% 集群恰恰可能需要那 80 个"低信息"基因。

## 涉及 Figures
- **Fig. 3A** — MERFISH 测量流程示意（135 组合 + 20 顺序 + 分割共染）
- **fig. S13** — 基因数对神经元集群恢复率的影响（~75 基因 → ~90%）
- **table S6 / S10 / S11** — 基因列表与探针序列
