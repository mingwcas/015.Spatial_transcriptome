# Method: Chromium 3′ and 5′ Single-Cell Gene Expression (GEX)

## 原文（Methods）
> We collected Chromium 3′ and 5′ GEX data from dissociated tumor cells to benchmark performance against the scFFPE-seq data. Dissociated tumor cells were recovered following Demonstrated Protocol CG000233. For the 3′ and 5′ workflows, cells were loaded on to the Chromium X instrument following the library preparation protocols in the Chromium Next GEM Single Cell 3′ Reagent Kits v3.1 User Guide (CG000204) and Chromium Next GEM Single Cell 5′ Reagent Kits v2 (Dual Index) User Guide (CG000331), respectively. Libraries were sequenced on an Illumina NovaSeq with paired-end dual-indexing (28 cycles Read 1, 10 cycles i7, 10 cycles i5, 90 cycles Read 2). All of the 3′ and 5′ flowcells were demultiplexed with bcl2fastq (Illumina). FASTQ files were processed with Cell Ranger v7.0.1 (10x Genomics), using the cellranger count pipeline on each GEM well with the GRCh38-2020-A reference to produce gene-barcode matrices and other output files, followed by aggregation of GEM wells with the cellranger aggr pipeline.

## 解读

### 意义
生成配对的Chromium 3′和5′单细胞数据，作为scFFPE-seq和Xenium灵敏度基准比较的参考标准

### 输入
- Sample #1配对的解离肿瘤细胞（冻存于液氮）
- Demonstrated Protocol CG000233（解冻复苏协议）

### 输出
- 基因-细胞矩阵（gene-barcode matrices）
- Cell Ranger处理后的聚合数据

### 核心步骤
1. 从液氮中解冻复苏配对解离肿瘤细胞（Protocol CG000233）
2. 将细胞加载至Chromium X仪器，分别进行3′和5′文库制备
3. 在Illumina NovaSeq上进行双端双索引测序（28+10+10+90 cycles）
4. 使用bcl2fastq进行FASTQ文件解复用
5. 使用Cell Ranger v7.0.1的cellranger count处理各GEM well
6. 使用cellranger aggr聚合多个GEM well的数据

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 测序平台 | Illumina NovaSeq | 高通量测序仪 |
| 测序模式 | PE双端双索引 (28+10+10+90) | Read1 28bp, i7 10bp, i5 10bp, Read2 90bp |
| 参考基因组 | GRCh38-2020-A | 10x Genomics人类参考基因组 |
| Cell Ranger版本 | v7.0.1 | 单细胞数据处理软件 |
| 基准测序深度 | 10,000 reads/cell（推荐深度） | 用于跨平台比较时的下采样标准 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Chromium X | 10x Genomics单细胞捕获仪器 |
| GEM well | 凝胶珠乳液（Gel Bead-in-Emulsion）反应单元，每个对应一个独立的单细胞捕获实验 |
| 3′ GEX | 3′端基因表达捕获，检测mRNA 3′端 |
| 5′ GEX | 5′端基因表达捕获，检测mRNA 5′端 |
| cellranger count | Cell Ranger的核心分析流程，完成比对、定量和细胞过滤 |
| cellranger aggr | Cell Ranger的聚合流程，归一化并合并多个样本的数据 |

## 复现
- 工具/代码/URL：Cell Ranger v7.0.1（10x Genomics，需商业许可）
- 代码片段：
```bash
# Cell Ranger count
cellranger count --id=sample_3prime \
  --transcriptome=/ref/GRCh38-2020-A \
  --fastqs=/data/fastqs/ \
  --sample=sample_3prime

# Cell Ranger aggregation
cellranger aggr --id=aggregated \
  --csv=aggregation.csv
```

## 生物学意义
Chromium 3′和5′ GEX数据在本文中主要用于基准比较（benchmarking），而非直接用于生物学发现。通过将这些传统单细胞技术的灵敏度与scFFPE-seq进行对比，作者发现scFFPE-seq在相同测序深度（~10,000 reads/cell）下的中位基因灵敏度高于3′和5′ GEX，证明了FFPE兼容的RTL技术在灵敏度方面的优势。该比较对验证新技术的可靠性至关重要。

## 涉及 Figures
- **Supp. Fig. 7a, b** — scFFPE-seq与Chromium 3′/5′ GEX灵敏度比较
- **Supp. Fig. 7c** — 各Chromium技术零计数基因的Venn图
