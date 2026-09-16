# Fig. 1 — MERFISH: combinatorial labeling and error-robust encoding

## Caption（原文）
> Fig. 1. MERFISH: a highly multiplexed smFISH approach enabled by combinatorial labeling and error-robust encoding. (A) Schematic depiction of the identification of multiple RNA species in N rounds of imaging. Each RNA species is encoded with a N-bit binary word and during each round of imaging, only the subset of RNAs that should read ‘1’ in the corresponding bit emit signal. (B to D) The number of addressable RNA species (B), the rate at which these RNAs are properly identified – calling rate (C), and the rate at which RNAs are incorrectly identified as a different RNA species – misidentification rate (D) plotted as a function of the number of bits (N) in the binary words encoding RNA. Black, a simple binary code that includes all 2N-1 possible binary words. Blue, the HD4 code where the Hamming distance separating words is 4. Magenta, the modified HD4 (MHD4) code where the number of ‘1’ bits are kept at four. The calling and misidentification rates are calculated with per bit error rates of 10% for the 1→0 error and 4% for the 0→1 error. (E) Schematic diagram of the implementation of a MHD4 code for RNA identification. Each RNA species is first labeled with ~192 encoding probes that convert the RNA into a unique combination of readout sequences (Encoding hyb). These encoding probes each contain a central RNA targeting region flanked by two readout sequences, drawn from a pool of N different sequences, each associated with a specific hybridization round. Encoding probes for a specific RNA species contain a unique combination of four of the N readout sequences, which correspond to the four hybridization rounds where this RNA should read ‘1’. N subsequent rounds of hybridization with the fluorescent readout probes are used to probe the readout sequences (hyb 1, hyb 2, …, hyb N). The bound probes are inactivated by photobleaching between successive rounds of hybridization. For clarity only one possible pairing of the readout sequences is depicted for the encoding probes; however, all possible pairs of the four readout sequences are used at the same frequency and distributed randomly along each cellular RNA in the actual experiments.

## Panel-by-Panel 解读

### Panel A — N-bit binary identification
**结论**：每个 RNA species 用 N-bit code word 编码，每轮只读出应为“1”的 RNA 子集，顺序读出即可识别多种 RNA。

**关键数据**：N 轮成像理论上可寻址 2^N−1 个可检测词；实际 140/1001 基因分别采用 16/14 轮。

### Panel B — 可寻址 RNA species
**结论**：随着 bit 数 N 增加，组合编码带来的可寻址 RNA 数指数增长。

**关键数据**：简单二进制为 2^N−1；32-bit MHD4 固定 4 个“1”位可达 1,240，固定 6 个“1”位可达 27,776 species。

### Panel C — Calling rate
**结论**：简单二进制随轮数增加快速丢失正确调用；HD4/MHD4 通过距离约束缓解误差。

**关键数据**：计算采用 1→0 error = 10%、0→1 error = 4%；实测 MHD4 calling rate ~80%。

### Panel D — Misidentification rate
**结论**：HD4/MHD4 将单 bit 错误变成可检测错误，显著降低错误归属；MHD4 以固定低“1”位进一步降低假阳性。

**关键数据**：HD4 最小汉明距离为 4，MHD4 每词 4 个“1”位；MHD2 距离 2，只能检错。

### Panel E — MHD4 probe implementation
**结论**：约 192 条 encoding probes 先把每个 RNA 转为四个 readout sequence 的组合，再经 N 轮荧光 readout 与漂白读取。

**关键数据**：每个 encoding probe 含 central RNA targeting region + 两条 readout sequences；每个 RNA 的四条 readout 分布在四轮。

## 总体结论
Fig. 1 建立 MERFISH 的工程逻辑：组合条码提供指数级通量，汉明距离提供 error detection / correction，而两步 encoding/readout 设计把昂贵的直接 RNA 杂交转换为快速的 readout 杂交。以 10% 与 4% 的实测 bit 错误率为基准，MHD4 在通量和准确性之间取得平衡，并为 1,000 至近全转录组规模扩展提供理论路径。

## 关联 Figures / Extended Data
- Fig. 2（16-bit MHD4 的 140 RNA species 实测）
- Fig. 5（14-bit MHD2 的 1001 RNA species 实测）
- Fig. S1–S3（组合编码、汉明码与探针合成示意）
