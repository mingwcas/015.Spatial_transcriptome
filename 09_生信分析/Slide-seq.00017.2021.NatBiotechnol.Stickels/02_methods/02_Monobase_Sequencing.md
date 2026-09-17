# Method: Monobase Sequencing Strategy

## 原文（Methods）
> The monobase-sequencing strategy interrogated 14 split-pool bases using three modes of sequencing by ligation. This strategy is motivated by the need to eliminate the use of proprietary cleavage reagents from SOLiD and to allow for sequencing using commercially available oligonucleotides. The overall sequencing strategy consisted of hybridization of a sequencing primer to interrogate the +2 base from the ligation junction followed by a ligation to interrogate a split-pool base followed by dehybridiation of the sequencing primer and subsequently ligated sequencing oligonucleotide using formamide before moving onto the next ligation.

## 解读

### 意义
Monobase sequencing是Slide-seqV2开发的开源测序方案，替代了SOLiD的proprietary dibase encoding，使任何实验室都能使用通用试剂进行bead array indexing。

### 输入
- Bead arrays (pucks)
- 荧光标记的寡核苷酸探针 (IDT合成)
- T4 DNA ligase及buffer
- Flow cell设备

### 输出
- 每个bead的14位split-pool barcode序列
- 荧光图像用于base calling

### 核心步骤
1. **5' ligation模式**: 使用T-1, T, T+1, T+2, UP-1, UP, UP+1, UP+2引物
2. **3' ligation模式**: 使用3UP+1, 3UP, 3UP-1引物
3. **SEDAL模式**: 使用T+3, UP+3, UP+4引物与degenerative primers
4. 每轮ligate后成像，然后strip (80% formamide)

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Split-pool碱基数 | 14 | 组成barcode |
| 测序模式 | 3种 (5' ligation, 3' ligation, SEDAL) | 多模式组合测序 |
| 5' ligation轮数 | 8轮 | 读取J1-J8 |
| 3' ligation轮数 | 3轮 | 读取J9-J11 |
| SEDAL轮数 | 3轮 | 读取J12-J14 |
| Primer浓度 | 5 μM | 注入flow cell浓度 |
| Ligation时间 | 40 min (5'/3'), 2 h (SEDAL) | 反应时间 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SOLiD dibase encoding | Applied Biosystems的专利双碱基编码测序技术 |
| Monobase sequencing | 本文开发的单碱基逐一测序策略，使用商用试剂 |
| Sequencing by ligation | 通过DNA连接酶将荧光标记探针与引物连接进行测序 |
| SEDAL | Sequencing primer hybridization and ligation with a Degenerate primer in solution |
| Offset primers | 带有随机N碱基的引物，用于区分 ligation junction |
| Hamming distance | 两个barcode之间不同碱基的数目，用于匹配reads和beads |

## 复现
- **工具/代码**: 
  - PuckCaller: https://github.com/MacoskoLab/PuckCaller/
  - 荧光oligos: IDT (Supplementary Table 6)
- **代码片段**:
```python
# Barcode matching using Hamming distance
cmatcher.cpp calculates Hamming distance between Illumina barcodes 
and bead barcodes with tolerance ≤1
```

## 生物学意义
Monobase sequencing策略完全开源，使Slide-seqV2技术可被广泛采用。相比SOLiD系统，该策略避免了颜色空间到碱基空间的转换，且具有相同的测序准确性。

## 涉及 Figures
- **Supplementary Fig. 1a-c** — Monobase sequencing strategy schematic
- **Supplementary Fig. 1d,e** — Comparison of SOLiD vs monobase performance
- **Fig. 1a** — Overview showing array generation and indexing
