# Method: DNA barcode sequencing, annealing and DNA oligonucleotides

## 原文（Methods）
> The DNA oligonucleotides were synthesized by Integrated DNA Technologies with HPLC purification. Barcode A1–50 or B1–50 was first annealed with ligation linker 1 or 2, 10 µl of 100 µM ligation linker1 or 2, 10 µl of 100 µM each barcode A or B, and 20 µl of 2× annealing buffer (20 mM Tris, pH 7.5–8.0, 100 mM NaCl and 2 mM EDTA) and mixed well. DNA oligonucleotides used for PCR and library construction are shown in Supplementary Table 1. All DNA barcode sequences are provided in Supplementary Table 2.

## 解读

### 意义
制备空间条形码寡核苷酸，用于在微流控通道中标记DNA片段，实现空间位置编码

### 输入
- DNA寡核苷酸（Integrated DNA Technologies合成，HPLC纯化）
  - Barcode A1-50（50种不同的A条形码）
  - Barcode B1-50（50种不同的B条形码）
  - Ligation linker 1和2
  - 2×退火缓冲液（20 mM Tris pH 7.5-8.0, 100 mM NaCl, 2 mM EDTA）

### 输出
- 退火完成的条形码-连接子复合物
- 用于微流控原位连接的条形码试剂

### 核心步骤
1. 合成DNA寡核苷酸（IDT，HPLC纯化）
2. 准备Barcode A1-50和Barcode B1-50（各50种不同序列）
3. 准备Ligation linker 1和2
4. 退火反应：10 µl 100 µM连接子 + 10 µl 100 µM条形码 + 20 µl 2×退火缓冲液
5. 混合均匀，形成条形码-连接子双链复合物
6. 准备PCR和文库构建所需的其他寡核苷酸（Supplementary Table 1）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 条形码数量 | 50种A + 50种B | 组合产生2500个空间像素（50×50） |
| 寡核苷酸浓度 | 100 µM | 退火反应的起始浓度 |
| 退火缓冲液 | 2×退火缓冲液 | 20 mM Tris pH 7.5-8.0, 100 mM NaCl, 2 mM EDTA |
| 纯化方式 | HPLC纯化 | 确保寡核苷酸纯度和质量 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Barcode A/B | 两种不同系列的空间条形码，分别对应微流控芯片的两个方向 |
| Ligation linker | 连接子序列，用于将条形码连接到DNA片段上 |
| 退火 | 两条互补寡核苷酸形成双链的过程 |
| HPLC纯化 | 高效液相色谱纯化，确保寡核苷酸纯度 |

## 复现
- 工具/代码/URL
  - 寡核苷酸合成：Integrated DNA Technologies (IDT)
  - 条形码序列：Supplementary Table 2
  - PCR引物：Supplementary Table 1
- 代码片段
  ```bash
  # 条形码退火流程
  # 1. 准备100 µM寡核苷酸溶液
  # 2. 混合：10 µl linker + 10 µl barcode + 20 µl 2×退火缓冲液
  # 3. 95°C加热5分钟，缓慢冷却至室温
  # 4. 保存退火产物用于后续连接反应
  ```

## 生物学意义
DNA条形码系统是Spatial-ATAC-Hi-C空间编码的核心：
- **空间编码原理**：通过两种条形码（A和B）的组合，实现2D空间位置编码
- **微流控标记**：条形码通过微流控通道在X和Y方向分别引入
- **组合编码**：50种A条形码 × 50种B条形码 = 2500个空间像素
- **位置信息保留**：每个DNA片段携带其空间位置信息

该技术的创新点：
- 将微流控技术与DNA条形码结合，实现高通量空间编码
- 条形码设计允许同时分析多个样本（通过不同的条形码组合）
- 退火反应简单高效，便于大规模制备

局限性：
- 条形码数量限制了空间分辨率（本文为50×50像素）
- 条形码合成成本较高
- 需要严格的退火条件控制以避免错配

## 涉及 Figures
- **Fig. 1a** — Spatial-ATAC-Hi-C实验流程，展示条形码标记步骤
- **Supplementary Table 1** — PCR和文库构建寡核苷酸序列
- **Supplementary Table 2** — 所有DNA条形码序列
