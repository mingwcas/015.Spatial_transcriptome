# Method: Spacemake Pipeline for Read Processing

## 原文（Methods）
> Spacemake automatically performs quality control, read preprocessing, alignment, mapping to spatial locations, and gene quantification. The output of spacemake is organized into two main categories: non-meshed files (original 0.6 μm resolution) and meshed files (aggregated into ~7 μm-side hexagons, by default).

## 解读

### 意义
使用 spacemake 流程进行原始测序数据的预处理、比对、空间映射和基因定量，生成空间表达矩阵。

### 输入
- 原始测序 FASTQ/BCL 文件
- 条形码坐标映射文件（来自方法 1）
- 参考基因组和注释文件
- 样本配置信息

### 输出
- 每个样本每个 tile 的 h5ad 文件
- 合并的统一 h5ad 文件（包含所有 tiles）
- QC 报告（HTML 格式）
- 数字基因表达（DGE）文件

### 核心步骤
1. 安装 micromamba 环境管理器
2. 下载 spacemake 环境文件并创建环境
3. 安装 openst 和 spacemake 包
4. 初始化 spacemake 并配置参考基因组
5. 添加样本到 spacemake 项目
6. 运行 spacemake 流程（自动执行 QC、预处理、比对、空间映射、定量）
7. 检查 QC 报告和自动分析结果

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| barcode_flavor | openst | 条形码处理模式 |
| run_mode | openst | 运行模式 |
| map_strategy | STAR:genome:final | 比对策略 |
| cores | 16 | 并行处理核心数 |
| 网格大小 | 7 μm hexagons | 默认网格化分辨率 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| spacemake | 空间转录组数据处理流程 |
| h5ad | AnnData 格式，用于存储单细胞/空间数据 |
| DGE | Digital Gene Expression，数字基因表达矩阵 |
| Meshed data | 网格化数据，聚合为伪细胞 |
| QC report | 质量控制报告 |

## 复现
- 工具/代码/URL：https://github.com/rajewsky-lab/spacemake
- 代码片段：
```bash
# 安装环境
mamba env create -n openst -f environment.yaml
mamba activate openst
pip install openst spacemake

# 初始化
spacemake init --dropseq_tools dropseq-3.0.0
spacemake config add_species \
  --name species_name \
  --reference genome \
  --sequence /path/to/genome.fa \
  --annotation /path/to/annotation.gtf

# 添加样本
spacemake projects add_sample \
  --project_id project_id \
  --sample_id sample_id \
  --R1 /path/to/R1.fastq.gz \
  --R2 /path/to/R2.fastq.gz \
  --species species_name \
  --puck openst \
  --run_mode openst \
  --barcode_flavor openst \
  --puck_barcode_file /path/to/fc_tiles/*.txt.gz \
  --map_strategy STAR:genome:final

# 运行
spacemake run --cores 16 --keep-going
```

## 生物学意义
spacemake 是 Open-ST 的核心数据处理流程，将原始测序数据转化为空间基因表达矩阵。它自动处理质量控制、条形码解析、序列比对和基因定量。网格化（meshing）将相邻的捕获位点聚合为类似细胞大小的伪细胞（7 μm 六边形），便于后续分析。QC 报告提供了样本质量的全面评估，包括比对率、rRNA 含量、UMI 和基因检测数量等指标。

## 涉及 Figures
- **Fig. 3** — Physical organization of the spatially barcoded flow cell, and data processing workflow
- **Fig. 4** — File structure after running spacemake and first assessment of quality of datasets
