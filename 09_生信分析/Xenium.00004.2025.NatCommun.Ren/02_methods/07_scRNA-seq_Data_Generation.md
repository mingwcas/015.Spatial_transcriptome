# Method: scRNA-seq Data Generation

## 原文（Methods）
> Single-cell suspensions from primary human tumor tissue were generated using the Tumor Dissociation Kit (Miltenyi Biotec, #130-095-929). The proportion of viable cells exceeded 85% in all samples. The single-cell suspension was processed with the Chromium Single Cell 3' GEM, Library & Gel Bead Kit v3.1 (10x Genomics, PN-1000268) and loaded onto a Chromium Single Cell Chip (Chromium Single Cell G Chip Kit, 10x Genomics, PN-1000120) according to the manufacturer's instructions for co-encapsulation with barcoded Gel Beads. The captured cells were lysed, and the released RNA was barcoded through reverse transcription in individual single-cell gel beads in the emulsion (GEMS). In each droplet, cDNA was generated and amplified through reverse transcription on a T100 PCR Thermal Cycler (Bio-Rad) at 53 °C for 45 min, followed by 85 °C for 5 min and a hold at 4 °C. Then, cDNA concentration and quality were assessed using a Qubit Fluorometer (Thermo Scientific) and bioanalyzer 2100 (Agilent), respectively. scRNA-seq libraries were then constructed and sequenced on the Illumina platform according to the manufacturer's introduction.

## 解读

### 意义
scRNA-seq作为本研究的重要ground truth参考，使用10x Genomics Chromium平台生成三名患者肿瘤组织的单细胞转录组数据，提供无空间信息的细胞类型注释参考，用于评估各ST平台的基因表达检测准确性和细胞类型注释能力。

### 输入
- 原发性人肿瘤组织样本（COAD、HCC、OV）
- Tumor Dissociation Kit (Miltenyi Biotec, #130-095-929)
- Chromium Single Cell 3' GEM, Library & Gel Bead Kit v3.1 (10x Genomics, PN-1000268)

### 输出
- 单细胞GEM乳液中的barcoded cDNA
- Illumina测序的scRNA-seq文库
- Cellranger v.7.0.0处理后的表达矩阵

### 核心步骤
1. 使用Tumor Dissociation Kit将肿瘤组织解离为单细胞悬液
2. 活细胞比例验证 > 85%
3. 细胞悬液与Barcoded Gel Beads通过Chromium Chip G共封装于GEM中
4. 细胞裂解 → RNA释放 → 乳化液中单细胞逆转录（RT barcoding）
5. 逆转录：T100 PCR仪 53°C 45 min → 85°C 5 min → 4°C保持
6. cDNA浓度和质量检测（Qubit + Bioanalyzer 2100）
7. 文库构建 → Illumina测序

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 活细胞比例 | >85% | 所有样本均满足 |
| 逆转录温度/时间 | 53°C 45 min → 85°C 5 min → 4°C | T100 PCR仪 |
| 试剂盒 | Chromium Single Cell 3' GEM, Library & Gel Bead Kit v3.1 (#1000268) | 10x Genomics |
| 芯片 | Chromium Single Cell G Chip Kit (#1000120) | 10x Genomics |
| 解离试剂 | Tumor Dissociation Kit (#130-095-929) | Miltenyi Biotec |
| 分析软件 | cellranger v.7.0.0 |  |
| 质控仪器 | Qubit Fluorometer, Bioanalyzer 2100 |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| GEM | Gel Beads-in-Emulsion，单细胞凝胶珠乳液 |
| Gel Bead | 带barcode的凝胶珠，用于单细胞标记 |
| 3' GEM | 捕获3'端poly(A) RNA的GEM |
| Cellranger | 10x Genomics的scRNA-seq数据分析流程 |
| UMI | Unique Molecular Identifier，唯一分子标签 |

## 复现
- 解离试剂：Tumor Dissociation Kit (Miltenyi Biotec, #130-095-929)
- 10x平台：Chromium Single Cell 3' GEM, Library & Gel Bead Kit v3.1 (#1000268)
- 芯片：Chromium Single Cell G Chip Kit (#1000120)
- 分析软件：cellranger v.7.0.0
- 测序：Illumina平台
- 仪器：T100 PCR Thermal Cycler (Bio-Rad), Qubit Fluorometer, Bioanalyzer 2100

## 生物学意义
scRNA-seq提供了无空间信息的细胞转录组参考谱，作为细胞类型注释的金标准。研究发现scRNA-seq在各平台中始终检测到最多的每细胞转录本和基因数，但当限制于iST平台共享基因时，iST平台表现出与scRNA-seq相当的单细胞检测能力。

## 涉及 Figures
- **Fig. 1** — 与scRNA-seq的基因表达相关性比较
- **Fig. 4c** — 各平台每细胞转录本/基因数与scRNA-seq比较
- **Fig. 4e** — 互斥标记基因对的表达相关性
