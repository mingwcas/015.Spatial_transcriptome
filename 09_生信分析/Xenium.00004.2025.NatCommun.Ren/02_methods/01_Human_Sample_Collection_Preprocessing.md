# Method: Human Sample Collection and Preprocessing

## 原文（Methods）
> This study was approved by the Research and Biomedical Ethical Committee of Peking University (IRB00001052-24061) and conducted following pertinent ethical regulations. All patients provided informed consent for collecting clinical information and tumor samples. All protocols adhered to the Interim Measures for the Administration of Human Genetic Resources, administered by the Ministry of Science and Technology of China. Participants received no compensation for their participation. Sex was self-reported by participants, and no sex- or gender-related factors were incorporated into the study design or data analysis. The tumor specimens were obtained from three patients at the Chinese PLA General Hospital and Peking University People's Hospital, with each individual presenting a distinct cancer diagnosis: COAD, HCC, and OV. Necrotic areas and regions adjacent to major blood vessels were excluded during collection. Each tissue was further evenly divided into three sections. The middle portion was submerged in the MACS® Tissue Storage Solution (Miltenyi #130-100-008) and further processed for scRNA-seq. One of the remaining sections was fixed in a 10% neutral formalin fixing solution (Solarbio #G2161) for 24 to 48 h before paraffin embedding. The other section was embedded in 4 °C OCT compound (Sakura #4583), quickly frozen on dry ice, and transferred to a –80 °C freezer for storage until further experimentation. The entire process was completed within 30 min to minimize RNA degradation. Serial sections of FFPE samples were prepared at Peking University and loaded onto platform-specific chips under the supervision of trained technicians for Visium HD FFPE, Xenium 5K, and CosMx 6K. Sections adjacent to all ST sections were reserved for subsequent CODEX profiling. The tissue samples were destroyed after the analysis.

## 解读

### 意义
建立标准化的样本收集与预处理流程，确保来自三名患者的三种不同癌症（COAD、HCC、OV）组织样本能够以统一方式处理，为后续四个空间转录组平台的平行比较提供可比性基础。

### 输入
- 治疗初期的肿瘤样本（来自中国解放军总医院和北京大学人民医院）
- 均为单一癌症类型：COAD、HCC、OV

### 输出
- FFPE组织块（用于Visium HD FFPE、Xenium 5K、 CosMx 6K）
- OCT包埋组织块（用于Stereo-seq v1.3）
- 单细胞悬液（用于scRNA-seq）
- 相邻组织切片（用于CODEX）

### 核心步骤
1. 收集三名患者的治疗初期肿瘤样本（排除坏死区域和大血管区域）
2. 将每份组织均分为三部分：
   - 中间部分：MACS®组织存储溶液保存 → scRNA-seq
   - 一部分：10%中性福尔马林固定24-48h → 石蜡包埋（FFPE）
   - 另一部分：4°C OCT包埋 → 速冻于干冰 → -80°C保存
3. 整个过程在30 min内完成，最大限度减少RNA降解
4. 连续切片分别用于各ST平台和CODEX

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 福尔马林固定时间 | 24–48 h | 10%中性福尔马林 |
| OCT包埋温度 | 4 °C |  |
| 速冻方式 | 干冰 |  |
| 保存温度 | -80 °C |  |
| 全程处理时间 | ≤30 min | 最大限度减少RNA降解 |
| 切片厚度（ST） | 5 μm（FFPE）/ 10 μm（FF） | 平台特定 |
| FFPE切片制备 | 北京大学 |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| FFPE | Formalin-Fixed Paraffin-Embedded，福尔马林固定石蜡包埋 |
| OCT | Optimal Cutting Temperature compound，用于快速冷冻组织块 |
| CODEX | Co-Detection by indEXing，多重蛋白荧光成像技术 |
| scRNA-seq | 单细胞RNA测序 |

## 复现
- 伦理批准：Peking University IRB (IRB00001052-24061)
- 存储溶液：MACS® Tissue Storage Solution (Miltenyi #130-100-008)
- 固定液：10%中性福尔马林 (Solarbio #G2161)
- OCT：Sakura #4583

## 生物学意义
标准化预处理确保来自三名患者的肿瘤组织在后续各平台的样本处理中具有可比性，同时最大限度保留RNA完整性。该流程考虑了不同平台对样本类型的特定需求（FFPE vs. FF vs. 单细胞悬液）。

## 涉及 Figures
- **Fig. 1a** — 实验流程示意图，展示样本采集、三分处理、各平台样本分配
