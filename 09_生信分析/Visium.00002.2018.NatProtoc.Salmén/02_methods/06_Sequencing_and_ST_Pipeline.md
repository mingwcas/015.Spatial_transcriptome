# Method: Sequencing, demultiplexing, alignment, gene counting and UMI filtering

## 原文（Methods）
> “We recommend using the open-source ST Pipeline ... automates the data processing ...” It requires R1/R2 FASTQ, a STAR genome index, GFF/3 annotation and ids-file; output is TSV unique-gene matrix, BED molecules and log (PDF pp.11, 27–28; Steps 146, 153–156).

## 解读
### 意义
把测序reads转换为每个空间spot的去重复基因计数。
### 输入
NextSeq FASTQ（R1/R2）、STAR genome index、GFF/3注释、spatial barcode/position ids-file。
### 输出
TSV（行=spot坐标、列=gene、值=unique molecules）、BED分子空间位置、处理log。
### 核心步骤
1. 每个index合并FASTQ。 2. quality trimming。 3. STAR基因组比对/计数。 4. spatial barcode demultiplexing。 5. UMI filtering去除扩增重复。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| 测序 | NextSeq 500/550 HO v2，75 cycles；R1通常26 bases；4–6样本/run；1–1.2 pM，15% PhiX | 获得配对读段 |
| 推荐深度 | 每样本约80–100 M reads | 约1,500–5,000 genes/spot |
| 资源 | Linux服务器，≥32 GB RAM，多核 | ST Pipeline/STAR |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| UMI filtering | 合并/去除扩增产生的重复分子 |
| unique molecule | 去UMI重复后的分子计数 |
| ids-file | barcode与空间位置对应文件 |

## 复现
- 工具/代码/URL：ST Pipeline https://github.com/SpatialTranscriptomicsResearch/st_pipeline；STAR https://github.com/alexdobin/STAR
- 代码片段：`st_pipeline --help`（按手册配置R1/R2、genome index、GFF3、ids-file）。

## 生物学意义
输出将转录本丰度映射至空间区域；结果受测序深度、RNA质量、细胞数量和纤维组织影响。

## 涉及 Figures
- **Fig. 5、Fig. 7** — 计算流程和计数结果。
