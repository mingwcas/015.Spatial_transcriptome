# Method: 误差稳健编码方案（MHD4 16-bit / MHD2 14-bit code words）

## 原文（Methods）

> For the simple binary encoding scheme in which all possible N-bit binary words are assigned to unique RNA species, the number of possible code words is 2N. The number of words that could be used to encode RNA is actually 2N − 1 because the code word '00…0' does not contain detectable fluorescence in any hybridization round, but for simplicity the word corresponding to all '0's was not removed from subsequent calculations.
>
> In a codebook where the minimum Hamming distance is 4 (HD4 code), at least four bits must be read incorrectly to change one code word into another (fig. S2A). As a result, every single-bit error produces a word that is uniquely close to a single code word, allowing such errors to be detected and corrected (fig. S2B).
>
> To generate our MHD4 code where the number of '1' bits for each code word is set to 4, we first generated the HD4 codes as described above, and then removed all code words that did not contain four '1's. … because a single error can produce a word equally close to two different code words, error correction is no longer possible for this modified Hamming-distance-2 (MHD2) code.
>
> Each RNA species in our target set was randomly assigned a binary code word either from all 140 possible code words of the 16-bit MHD4 code or from all 1001 possible code words of the 14-bit MHD2 code, as we describe in the main text. The encoding schemes are provided in Tables S1 and S3.

## 解读

### 意义
用"组合标记 + 误差稳健编码"把 smFISH 的通量从 10–30 个 RNA species 提升到 140 / 1001 个，同时把单比特读出错误"检测出来并可纠正"，避免朴素二进制编码在高位数下 misidentification rate 爆炸。

### 输入
- 目标基因列表（130 个编码 RNA + 10 个对照；或 985 个编码 RNA + 16 个对照）
- 位数 N（140 基因实验 N = 16；1001 基因实验 N = 14）
- 每 bit 的经验错误率：1→0 错误 10%，0→1 错误 4%

### 输出
- codebook（每个 RNA species 对应一个固定 4 个"1"位的二进制词；Tables S1 / S3）
- 预测的 addressable species 数、calling rate、misidentification rate 曲线（Fig. 1, B–D）
- 用于解码的汉明距离判据

### 核心步骤
1. 先生成标准扩展 Hamming distance 4（HD4）码的生成矩阵，确定可用码字数随位数 N 的变化。
2. 去除所有不包含 4 个"1"位的码字，得到 MHD4 码（每词恰好 4 个"1"），降低 1→0 错误带来的偏倚。
3. 若不需要纠错、只求快速扩展：把最小汉明距离从 4 降到 2（MHD2），取所有 14-bit 中含 4 个"1"位的词 → 1001 个词。
4. 把码字随机分配给目标 RNA species，保留一部分码字不分配给任何 RNA，作为 misidentification controls（blank words / no-target words）。
5. 用解析式（Eq. 1–6）在给定 p1 = 10%、p0 = 4% 下预测 calling rate 与 misidentification rate。
6. 解码时：MHD4 允许"精确匹配或差 1 bit"即归属该 RNA；MHD2 只允许精确匹配。

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 140 基因实验编码 | 16-bit MHD4 | 16 轮杂交，每词 4 个"1"位 |
| 1001 基因实验编码 | 14-bit MHD2 | 14 轮杂交，每词 4 个"1"位 |
| MHD4 可用码字 | 140 | 130 编码 RNA + 10 对照（5 blank + 5 no-target） |
| MHD2 可用码字 | 1001 | 985 编码 RNA + 16 对照（11 blank + 5 no-target） |
| 最小汉明距离 | MHD4 = 4 / MHD2 = 2 | 决定能否纠错 |
| 1→0 错误率 | ~10% | 平均每轮每 bit |
| 0→1 错误率 | ~4% | 平均每轮每 bit |
| 32-bit MHD4（4 个"1"位） | 1,240 species | 预测可扩展规模 |
| 32-bit MHD4（6 个"1"位） | 27,776 species | 约等于人类转录组规模 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Code word（码字） | 分配给某一 RNA species 的 N-bit 二进制词，每一位对应一轮杂交的"有/无信号" |
| Hamming distance（汉明距离） | 两个等长二进制词之间不同位的个数 |
| HD4 / MHD4 | 最小汉明距离 4 的码；MHD4 额外要求每词恰好 4 个"1"位 |
| MHD2 | 最小汉明距离 2 的码，只能检测错误不能纠正 |
| Calling rate | 被正确识别为该 RNA species 的分子占该 species 真实分子的比例 |
| Misidentification rate | 被错误识别为另一个 RNA species 的分子比例 |
| Blank word | 未分配 encoding probe 的对照码字 |
| No-target word | 有 encoding probe 但靶向序列不靶向任何细胞内 RNA 的对照码字 |
| 1→0 / 0→1 error | 该读"1"却读成 0 / 该读 0 却读出信号 |

## 复现
- 论文未提供公开代码；码字表见 Tables S1（140-gene MHD4）与 S3（1001-gene MHD2）。
- HD4 码由标准 BCH/Hamming 生成矩阵构造，可用任意线性码库实现：

```python
from itertools import combinations
# 1) 构造 HD4（扩展汉明码）码字，2) 只保留恰好 4 个 "1" 的词
hd4 = build_extended_hamming_distance4_code(n_bits=16)
mhd4 = [w for w in hd4 if bin(w).count("1") == 4]        # -> 140 words
# 3) MHD2：14 位中任取 4 个 "1" 的全部组合
mhd2 = [sum(1 << i for i in c) for c in combinations(range(14), 4)]  # C(14,4)=1001
```

## 生物学意义
编码方案本身不是生物学发现，而是 MERFISH 的"物理层"：它把不可靠的单分子荧光读出（约 10% 漏检、4% 假阳性）转换成可统计、可纠错的数字信号，从而保证拷贝数定量在 3 个数量级的丰度范围内保持无偏。局限在于：MHD2 牺牲纠错换取通量，calling rate 降至约 1/3；MHD4 增加通量必须增加杂交轮次，实验时间与样本降解风险随之上升。

## 涉及 Figures
- **Fig. 1B–D** — 直接来自本方法的解析预测：addressable species 数、calling rate、misidentification rate 随 N 的变化（黑 = 简单二进制，蓝 = HD4，紫 = MHD4）。
- **Fig. 1E** — MHD4 编码的物理实现（encoding probe + 4 个 readout sequences）。
- **Fig. 2** — 16-bit MHD4 实测（140 基因）；**Fig. 5** — 14-bit MHD2 实测（1001 基因）。
