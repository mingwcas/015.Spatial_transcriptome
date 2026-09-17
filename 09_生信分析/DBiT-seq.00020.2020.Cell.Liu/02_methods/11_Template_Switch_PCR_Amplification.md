# Method: Template Switch and PCR Amplification

## 原文（Methods）
> The cDNAs bound to beads were cleaned and resuspended into the template switch solution. The template switch reaction mix contains 44 μL of 5X Maxima RT buffer (Thermo Fisher), 44 μL of 20% Ficoll PM-400 solution (Sigma), 22 μL of 10 mM dNTPs each (Thermo Fisher), 5.5 μL of RNase Inhibitor (Enzymatics), 11 μL of Maxima H Minus Reverse Transcriptase (Thermo Fisher), and 5.5 μL of a template switch primer (100 μM). The reaction was conducted at room temperature for 30 minutes followed by an additional incubation at 42°C for 90 minutes. The beads were rinsed once with a buffer containing 10 mM Tris and 0.1% Tween-20 and then rinsed again with RNase free water using a magnetic separation process. PCR was conducted following these two steps. In the first step, a mixture of 110 μL Kapa HiFi HotStart Master Mix (Kapa Biosystems), 8.8 μL of 10 mM stocks of primers 1 and 2, and 92.4 μL of water was added to the cleaned beads. If the protein detection was conducted in conjunction using a process similar to CITE-seq, a primer 3 solution (1.1 μL, 10 mM) was also added at this step. PCR reaction was then done using the following conditions: first incubate at 95°C for 3 mins, then cycle five times at 98°C for 20 s, 65°C for 45 s, 72°C for 3 minutes and then the beads were removed from the solution by magnet. Evagreen (20X, Biotium) was added to the supernatant with 1:20 ratio, and a vial of the resultant solution was loaded into a qPCR machine (BioRad) to perform a second PCR step with an initial incubation at 95°C for 3 minutes, then cycled at 98°C for 20 s, 65°C for 20 s, and finally 72°C for 3 minutes. The reaction was stopped when the fluorescence signal just reached the plateau.

## 解读

### 意义
该方法通过模板切换技术给cDNA添加额外的PCR handle，然后进行两步PCR扩增以获得足够的文库模板。

### 输入
- 结合在链霉亲和素磁珠上的cDNA
- 模板切换反应混合液（Maxima RT buffer、Ficoll、dNTPs、RNase抑制剂、逆转录酶、模板切换引物）
- Kapa HiFi HotStart Master Mix
- PCR引物1、2、3（如检测蛋白）

### 输出
- 扩增的cDNA文库（用于后续文库构建）

### 核心步骤
1. 模板切换反应混合液：44μL 5X Maxima RT buffer + 44μL 20% Ficoll PM-400 + 22μL 10mM dNTPs + 5.5μL RNase抑制剂 + 11μL Maxima H Minus逆转录酶 + 5.5μL模板切换引物(100μM)
2. 室温反应30分钟，然后42°C 90分钟
3. 磁珠用10mM Tris + 0.1% Tween-20洗1次，RNase-free水洗1次
4. 第一步PCR：110μL Kapa HiFi + 8.8μL引物1和2 (10mM) + 92.4μL水，加入磁珠
5. PCR条件：95°C 3分钟；98°C 20秒，65°C 45秒，72°C 3分钟，5个循环
6. 磁力架分离磁珠，收集上清
7. 加入Evagreen(20X, 1:20稀释)到上清
8. 第二步qPCR：95°C 3分钟；98°C 20秒，65°C 20秒，72°C 3分钟
9. 信号达平台期时停止反应

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Ficoll浓度 | 20% | 增加溶液粘度，促进模板切换 |
| 模板切换时间 | 30分钟(室温) + 90分钟(42°C) | 充分模板切换 |
| 第一步PCR循环数 | 5个循环 | 预扩增 |
| qPCR监测 | Evagreen荧光 | 实时监测扩增 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Template switch | 模板切换，逆转录酶在cDNA末端添加非模板胞嘧啶，与模板切换引物结合 |
| Ficoll PM-400 | 右旋糖酐衍生物，增加粘度，促进酶反应 |
| Evagreen | 荧光染料，结合双链DNA用于qPCR监测 |

## 复现
- 工具/代码/URL：Maxima H Minus Reverse Transcriptase (Thermo Fisher, EP0751)
- 关键调用：NA

## 生物学意义
模板切换技术通过逆转录酶的非模板活性在cDNA 3'端添加寡核苷酸序列，作为后续PCR扩增的handle。这使得cDNA可以从磁珠上洗脱并充分扩增。两步PCR（预扩增+qPCR监控）确保了文库在最佳循环数下停止，避免过度扩增导致偏倚。

## 涉及 Figures
- **Fig. S2A** — PCR产物cDNA大小分布，峰值在900-1100 bp
