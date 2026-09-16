# Fig. 1 — Xenium 脱靶结合原理示意图

## Caption（原文）
> Figure 1. Schematic of potential off-target binding in 10x Genomics Xenium. In this illustration, the arms of the padlock probes were designed to bind an RNA sequence intended to correspond to a target gene (green). However, these probes exhibit off-target binding and bind to an RNA sequence in a different off-target gene (red). The probe is circularized and subsequently amplified via rolling circle amplification (RCA). Hybridization of fluorescent probes to the RCA product enables the generation of a fluorescent signal that is used to quantify RNA expression within cells.

## Panel-by-Panel 解读

### Panel 单一示意 — Padlock 探针脱靶结合
**结论**：锁式（padlock）探针的两条臂本应结合目标基因（绿色）的 RNA 序列，但当脱靶基因（红色）存在高度相似的序列时，探针臂会退火到脱靶转录本上；连接酶随后仍将其环化，经滚环扩增（RCA）产生荧光信号，该信号被错误地计入目标基因的表达量。

**关键数据**：
- 探针结构：两条 20 bp 臂 → 拼接形成 40 bp 探针靶序列
- 信号放大：连接酶环化 → RCA → 荧光探针杂交
- 绿色 = intended target gene；红色 = off-target gene

### 示意中的信号流
**结论**：脱靶结合与真实结合在下游读出上**不可区分**——两者都经过同样的环化、RCA 与荧光标记步骤，因此脱靶信号会被直接加和进目标基因的表达计数。

**关键数据**：
- 无任何序列层面的"纠错"环节可区分二者
- 需依赖计算预测（OPT）或正交平台（Visium / scRNA-seq）才能发现

## 总体结论
该图确立了全文的核心问题：探针序列同源性导致的脱靶结合，会通过 RCA 放大成可被误读为真实表达的荧光信号，从而扭曲 Xenium 的空间基因表达谱。它解释了为何"探针特异性"是基于探针的原位空间转录组数据可靠性的先决条件。

## 关联 Figures / Extended Data
- Appendix 1—figure 6 — 探针自杂交与探针-探针互作等其它非特异信号来源
- Fig. 2, Fig. 3 — 脱靶结合在真实数据中的表现与验证
