# Method: Chromium Single Cell Gene Expression Flex (scFFPE-seq)

## 原文（Methods）
> Our goal in producing scFFPE-seq data was to precisely define the cell types present in serial tissue sections to enable downstream integration of data types. 50 μm FFPE curls were dissociated with the Miltenyi Biotech FFPE Tissue Dissociation Kit. Approximately 600,000 cells were washed, counted, and resuspended, loading 16,000 cells per each of four GEM wells (targeting 10,000 recovered cells) on a single Chromium X chip. Sequencing libraries were generated following the User Guide (CG000477). Libraries were sequenced on an Illumina NovaSeq with paired-end dual-indexing (28 cycles Read 1, 10 cycles i7, 10 cycles i5, 90 cycles Read 2). Sequencing libraries were demultiplexed with bcl2fastq (Illumina). FASTQ files were processed with Cell Ranger v7.0.1 (10x Genomics) using the multi pipeline and the GRCh38-2020-A reference.

## 解读

### 意义
从FFPE组织中获得全转录组单细胞分辨率数据，定义细胞类型组成，为Visium和Xenium数据的注释和整合提供参考

### 输入
- 50 μm FFPE curls（2×25 μm合并）
- Miltenyi Biotech FFPE Tissue Dissociation Kit

### 输出
- 基因-细胞矩阵（feature-cell matrix）
- 17个无监督聚类，中位1480个基因/细胞
- 细胞类型注释标签

### 核心步骤
1. 使用Miltenyi FFPE Tissue Dissociation Kit解离50 μm FFPE curls
2. 洗涤、计数约600,000个细胞
3. 在单张Chromium X芯片上加载4个GEM well，每个加载16,000个细胞（目标回收10,000个）
4. 按照User Guide (CG000477)生成测序文库
5. Illumina NovaSeq测序（28+10+10+90 cycles双端双索引）
6. bcl2fastq解复用，Cell Ranger v7.0.1 multi pipeline处理

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| FFPE curls输入 | 50 μm（2×25 μm） | 组织起始量 |
| 解离试剂盒 | Miltenyi Biotech FFPE Tissue Dissociation Kit | FFPE组织专用解离方案 |
| 每GEM well加载细胞数 | 16,000 | 目标回收约10,000细胞 |
| GEM wells数量 | 4 | 单张Chromium X芯片 |
| 测序深度 | ~10,000 reads/cell（推荐） | 后续分析时的标准化深度 |
| 探针集 | 18,536 genes / 54,018 probes | 与Visium使用相同探针集 |
| 参考基因组 | GRCh38-2020-A | 10x Genomics人类参考 |
| Cell Ranger版本 | v7.0.1 multi pipeline | 支持Flex/RTL技术的分析流程 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| scFFPE-seq | Single Cell FFPE Sequencing，基于RNA模板连接（RTL）技术的FFPE单细胞分析 |
| RTL | RNA Templated Ligation，通过互补探针与靶标RNA杂交后连接，克服甲醛交联和片段化问题 |
| Flex（Gene Expression Flex） | 10x Genomics的新型单细胞基因表达方案，兼容FFPE样本 |
| GEM well | 凝胶珠乳液反应单元，每个对应一次独立的液滴封装 |
| 探针集（probe set） | 用于靶向捕获mRNA的DNA探针集合，scFFPE-seq与Visium共享同一套18,536基因探针 |

## 复现
- 工具/代码/URL：Cell Ranger v7.0.1（10x Genomics），Miltenyi FFPE Tissue Dissociation Kit（商业产品）
- 代码片段：
```bash
# Cell Ranger multi pipeline for scFFPE-seq
cellranger multi --id=scFFPE_sample \
  --csv=config.csv \
  --transcriptome=/ref/GRCh38-2020-A
```

## 生物学意义
scFFPE-seq是本研究的核心发现工具之一，提供了全转录组单细胞分辨率数据。相比传统Chromium 3′/5′ GEX，scFFPE-seq对FFPE样本的灵敏度更高（中位基因灵敏度高于3′和5′ GEX）。该技术与Visium共享相同探针集（18,536基因），极大简化了数据整合。scFFPE-seq识别出17个细胞聚类，为后续Visium空间注释和Xenium监督标记提供了基础。局限性：无法捕获脂肪细胞（adipocytes），且因材料需求仅能产生1个重复。

## 涉及 Figures
- **Fig. 1** — 实验设计示意图，展示scFFPE-seq在三种技术中的位置
- **Fig. 2a** — scFFPE-seq数据t-SNE投影及17个聚类注释
- **Fig. 3i** — scFFPE-seq全转录组vs. 313基因子集的比较
- **Supp. Fig. 6a** — scFFPE-seq无法捕获脂肪细胞
- **Supp. Fig. 7** — scFFPE-seq与3′/5′ GEX灵敏度基准比较
