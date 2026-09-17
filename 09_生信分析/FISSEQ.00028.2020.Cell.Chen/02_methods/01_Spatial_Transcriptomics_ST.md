# Method: Spatial Transcriptomics (ST)

## 原文（Methods）
> We layered tissue sections onto a spatially barcoded array to collect in situ 2D-RNaseq of Spatial Transcriptomics (Lot#10001, Spatial Transcriptomics, Stockholm, Sweden). Each spatially barcoded array has 1007 TDs, with a diameter of 100 μm and a center-to-center distance of 200 μm, over an area of 6.2 mm by 6.6 mm. One coronal section normally covers the area of 500 to 600 spots on the array, each spot defining one TD. Each spot contains approximately 200 million barcoded reverse-transcription oligo(dT) primers allowing to get a global transcriptomic profile of a TD with a volume of 0.00008 mm³. Cryosectioned tissues were fixed on a spatially barcoded array by 3.7% formaldehyde solution at room temperature for 10 min, and stained by hematoxylin for 7 min, bluing buffer for 2 min, and eosin for 20 s. After imaging, tissues were immediately permeabilized by collagenase in HBSS-BSA buffer for 20 min and 0.1% pepsin in 0.1M HCl for 6 min at 37°C, and followed by in situ reverse transcription by adding cDNA synthesis master mix at 42°C for 18-20 hours. Tissue on the array was then removed by incubation with 2.5 mg/ml proteinase K in PDK buffer at 56°C for 1h. We collected the cDNA probes by probe cleavage using 100U/ml USER enzyme. Library preparation was performed including second strand synthesis, in vitro transcription, adaptor ligation, second cDNA synthesis, qPCR quantification, and PCR amplification (8-11 cycles). Paired end sequencing was performed on an Illumina NextSeq500 sequencer.

## 解读

### 意义
Spatial Transcriptomics (ST) 是本研究的核心技术，能够在组织切片的空间位置上进行全基因组转录组分析，保留了基因表达的空间信息，使得研究者可以将基因表达变化与组织病理学（如淀粉样斑块沉积）直接关联。

### 输入
- 冷冻包埋的小鼠或人脑组织切片（10 μm厚度）
- 空间条形码阵列芯片（1007个TD点，直径100 μm，间距200 μm）
- bregma -2.0 至 -2.2 的冠状切片

### 输出
- 每个TD的全基因组转录组计数矩阵
- 空间坐标信息
- 每个TD的平均检测到31,283 ± 7,441个UMI和6,578 ± 987个基因
- 每个冠状切片500-600个有效TD

### 核心步骤
1. 冷冻切片（10 μm厚度）放置于空间条形码阵列上
2. 3.7%甲醛固定10分钟，H&E染色
3. Zeiss Axio Scan.Z1载玻片扫描仪采集H&E图像
4. 胶原酶和胃蛋白酶组织通透化处理
5. 原位逆转录（42°C，18-20小时）
6. 蛋白酶K消化去除组织
7. USER酶切割释放cDNA探针
8. 文库制备（二链合成、体外转录、接头连接、qPCR定量、PCR扩增8-11循环）
9. Illumina NextSeq500双端测序
10. Cy3荧光探针杂交确定TD精确位置

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| TD直径 | 100 μm | 每个组织域的空间分辨率 |
| TD间距 | 200 μm | 中心到中心距离 |
| TD数量 | 1007/芯片 | 每个阵列的总捕获点数 |
| 切片厚度 | 10 μm | 冷冻切片厚度 |
| 甲醛浓度 | 3.7% | 组织固定浓度 |
| 通透化 | 胶原酶20min + 0.1%胃蛋白酶6min | 组织通透化处理 |
| RT时间 | 18-20小时 | 原位逆转录时间 |
| RT温度 | 42°C | 逆转录温度 |
| PCR循环数 | 8-11 | 文库扩增循环数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| TD (Tissue Domain) | 组织域，ST阵列上直径100μm的捕获区域 |
| UMI (Unique Molecular Identifier) | 唯一分子标识符，用于定量去除PCR重复 |
| Spatial Transcriptomics (ST) | 空间转录组学技术，基于空间条形码阵列的原位转录组分析 |
| 2D-RNaseq | 二维RNA测序，ST技术的别称 |
| RIN (RNA Integrity Number) | RNA完整性数值，评估RNA质量（本文8.6-9.45） |

## 复现
- 工具/代码/URL
  - ST Library Preparation Manual (Spatial Transcriptomics, Stockholm, Sweden)
  - ST pipeline: https://github.com/SpatialTranscriptomicsResearch/st_pipeline
  - 数据: GEO: GSE152506
- 代码片段（关键调用）
```bash
# ST pipeline 处理原始测序数据
st_pipeline_run --input-filenames sample_R1.fastq.gz sample_R2.fastq.gz \
  --output-folder output/ \
  --genome mouse_genome \
  --ids-file spatial_array_IDs.txt
```

## 生物学意义
ST技术使研究者首次能够在全基因组水平上分析淀粉样斑块周围100μm直径范围内的转录组变化，无需组织解离，保留了空间信息。该技术虽然不能达到单细胞分辨率，但为后续ISS和RNAscope验证提供了无偏的全基因组筛选基础，发现了PIG和OLIG两个关键基因共表达网络。

## 涉及 Figures
- **Fig. 1** — ST实验设计、TD分布、t-SNE聚类
- **Fig. 2** — ST数据与Aβ沉积的关联分析
- **Fig. 3** — PIG模块的ST鉴定
- **Fig. 6** — OLIG模块的ST分析
- **Figure S1** — ST实验设置和数据质量
