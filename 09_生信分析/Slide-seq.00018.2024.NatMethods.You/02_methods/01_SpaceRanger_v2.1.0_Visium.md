# Method: SpaceRanger v2.1.0 (Visium)

## 原文（Methods）
> Visium data were processed with spaceranger (v2.1.0), and aligned with STAR 2.7.10b.

## 解读

### 意义
SpaceRanger是10X Genomics官方分析管道，用于处理Visium空间转录组数据，将原始FASTQ文件转换为带有空间坐标的基因表达矩阵。

### 输入
- 原始FASTQ文件（包含细胞条码和UMI信息）
- 参照基因组（Mouse GRCm39）

### 输出
- 带有空间坐标的基因表达矩阵（barcode x gene）
- H&E图像与表达数据的对齐结果
- 聚类和差异表达分析结果

### 核心步骤
1. 读取FASTQ文件，解析空间条码和UMI
2. 使用STAR将reads比对到参考基因组
3. 过滤低质量reads和条码
4. 生成spot-by-gene表达矩阵
5. 与H&E图像对齐
6. 执行基本的聚类分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| spaceranger version | v2.1.0 | 官方分析管道版本 |
| aligner | STAR 2.7.10b | 基因组比对工具 |
| reference | Mouse GRCm39 | 小鼠参考基因组 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Spot | Visium芯片上的捕获区域，每个spot包含多个细胞 |
| Spatial barcode | 空间位置条码，用于关联表达数据与空间位置 |
| UMI | Unique Molecular Identifier，唯一分子标签，用于定量 |

## 复现
- 工具/代码/URL：10X Genomics SpaceRanger (https://www.10xgenomics.com/products/space-ranger)
- 代码片段：
```bash
spaceranger count --id=sample1 \
  --transcriptome=/path/to/refdata-gex-GRCm39 \
  --fastqs=/path/to/fastq \
  --image=/path/to/image.tif \
  --slide=V19T25-014 \
  --area=A1
```

## 生物学意义
Visium是目前最广泛使用的商业化空间转录组平台，但本研究发现其存在基因捕获偏好性（gene-capturing bias），例如Crybb3和Cryaa等镜头特异性基因在Visium数据中未被检测到，可能影响对特定组织的解读。

## 涉及 Figures
- **Fig. 2** — 灵敏度比较：Visium与其他平台的UMI counts比较
- **Fig. 4** — 下游性能比较：聚类和细胞注释结果
