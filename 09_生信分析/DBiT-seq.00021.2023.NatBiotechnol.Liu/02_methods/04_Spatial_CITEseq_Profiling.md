# Method: Spatial-CITE-seq Profiling of Tissue

## 原文（Methods）
> OCT embedded tissue sections stored in a −80 °C freezer were left on the working bench for 10 minutes. Sections were then fixed with 4% formaldehyde for 20 minutes and washed three times with 1× PBS with 0.05 U μl−1 RNAse Inhibitor (Enzymatics, 40 U μl−1). The tissue was then permeabilized with 0.5% Triton X-100 in 1× PBS for another 20 minutes before washing three times with 1× PBS. The sections were quickly dipped in RNase-free water and dried with air. We then covered the tissue using 1× blocking buffer with 0.05 U μl−1 RNAse Inhibitor (Enzymatics, 40 U μl−1) and incubated at 4 °C for 10 minutes. After washing three times with 1× PBS buffer, ADT cocktails (diluted 20 times from original stock) from BioLegend were added onto the tissue and incubated for 30 minutes at 4 °C. The ADT cocktail was removed by washing three times with 1× PBS, and the slide was dipped in water briefly to remove any remaining salts. A whole tissue image scan was performed with an EVOS microscope using a ×10 objective. In-tissue reverse transcription was conducted by flowing reverse transcription reagents into each of the 50 channels. [...] After peeling off the first PDMS chip, the tissue was dipped in RNase-free water and kept dry at 4 °C until the next step. In-tissue ligation was performed in the second PDMS chip, which has 50 channels with orthogonal direction. [...] The whole tissue section was digested by proteinase K to release the cDNAs.

## 解读

### 意义
在组织内完成ADT标记、原位逆转录、条码连接和cDNA释放，实现蛋白质和转录组的空间共索引。

### 输入
- -80°C保存的OCT包埋组织切片
- ADT鸡尾酒（稀释20倍）
- Barcode A和Barcode B寡核苷酸
- 逆转录和连接试剂

### 输出
- 带有空间条码的cDNA（mRNA来源和ADT来源）
- 组织明场图像

### 核心步骤
1. 组织固定：4%甲醛固定20分钟，PBS+RNase inhibitor洗涤3次
2. 通透化：0.5% Triton X-100/PBS处理20分钟，PBS洗涤3次
3. 封闭：1× blocking buffer + RNase inhibitor，4°C孵育10分钟
4. ADT染色：BioLegend ADT鸡尾酒（20倍稀释），4°C孵育30分钟
5. 组织成像：EVOS显微镜×10物镜全组织扫描
6. 原位逆转录：第一块PDMS芯片放置于组织上，50个通道分别灌注Barcode A + RT混合物，室温30分钟后42°C 90分钟
7. 原位连接：第二块PDMS芯片（垂直方向）放置于组织上，灌注Barcode B + 连接子混合物，37°C孵育30分钟
8. 组织裂解：蛋白酶K在55°C裂解2小时释放cDNA
9. cDNA提取：DNA纯化试剂盒 → 链霉亲和素磁珠捕获生物素化cDNA → 模板转换 → PCR扩增
10. 文库构建：mRNA cDNA用Nextera XT试剂盒，ADT cDNA用PCR扩增，分别建库

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 甲醛浓度 | 4% | 组织固定浓度 |
| 固定时间 | 20 min | 甲醛固定时间 |
| 通透化剂 | 0.5% Triton X-100 | 细胞膜通透化 |
| ADT稀释倍数 | 20× | 从原液稀释 |
| ADT孵育 | 4°C, 30 min | 抗体孵育条件 |
| RT孵育 | 室温30min + 42°C 90min | 逆转录反应条件 |
| 连接孵育 | 37°C, 30 min | T4 DNA连接酶反应 |
| 裂解温度/时间 | 55°C, 2h | 蛋白酶K裂解条件 |
| PCR循环数 | 20 cycles | cDNA扩增循环数 |
| 测序平台 | NovaSeq 6000 | Illumina测序系统 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| In-tissue reverse transcription | 组织内原位逆转录，在组织切片内合成cDNA |
| In-tissue ligation | 组织内原位连接，将Barcode B连接到Barcode A上 |
| Template switch | 模板转换，为cDNA添加第二端PCR handle |
| SPRI beads | 固相可逆固定化磁珠，用于DNA纯化和大小选择 |
| Streptavidin beads | 链霉亲和素磁珠，捕获5'生物素修饰的Barcode B-cDNA |
| Proteinase K | 蛋白酶K，用于裂解组织释放cDNA |
| Nextera XT | Illumina文库构建试剂盒 |

## 复现
- 工具/代码/URL
  - BioLegend ADT cocktails（cat. 99502, 99833）
  - Enzymatics RNase Inhibitor（40 U/µl）
  - Maxima H Minus Reverse Transcriptase（Thermo Fisher）
  - T4 DNA Ligase（NEB, 400 U/µl）
  - KAPA HiFi HotStart Master Mix
  - Nextera XT Library Prep Kit（Illumina, FC-131-1024）
  - Dynabeads MyOne Streptavidin C1（Invitrogen）
  - Zymo Research DNA purification kit（ZD4014）
- 代码片段：N/A（实验操作流程）

## 生物学意义
这是spatial-CITE-seq的核心实验步骤，通过微流控芯片在组织内实现空间确定性条码标记。两步法（逆转录+连接）将二维空间信息编码到每个cDNA分子上，使后续测序数据可追溯到组织中的精确位置。该流程同时捕获mRNA和ADT，实现转录组-蛋白质组的同步空间映射。

## 涉及 Figures
- **Fig. 1a** — Spatial-CITE-seq工作流程示意图
- **Extended Data Fig. 1** — 详细的实验步骤和Barcode结构
- **Extended Data Table 3** — 使用的化学品和试剂清单
