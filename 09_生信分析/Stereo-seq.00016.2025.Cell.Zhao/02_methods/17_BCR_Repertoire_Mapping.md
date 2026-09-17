# Method: BCR Repertoire Mapping and Assembling

## 原文（Methods）
> To identify the BCR repertoire, firstly, we performed immune repertoire analyses with MIXCR. For both Stereo-seq V2 data and public bulk data, we uniformly applied the "align" pipeline with the following parameters: "-species mmu" (for human data, "-species hsa"), "-p rna-seq", "-OallowPartialAlignments=true", and "-OallowNoCDR3PartAlignments=true", to align raw FASTQ files to the reference genome. Then the alignment files were performed in two rounds of "assemblePartial" for better yield. BCR clonotypes identification and quantification were performed with the "assemble" and "exportClones". V gene and J gene mutations were used to assess mutation levels for each BCR clonotype. When V gene and J gene mutation frequencies are greater than 0, it indicates that a BCR clonotype may experience hypermutation.

> For stereo-seq V2 data, ST_BarcodeMap was used to assign BCR-related gene reads and BCR clonotypes to each DNB spot. Only 1 mismatch is allowed for barcode matching. To make the BCR clonotypes more spatially representative, the alignment reads and BCR clonotypes were tracked into larger pseudo-spots with a 50 × 50 window size (bin50 for short). Subsequently, the data were converted into anndata format for input into Scanpy for BCR clone visualization.

## 解读

### 意义
从Stereo-seq V2数据中组装BCR (B Cell Receptor)克隆型，分析免疫 repertoire 的空间分布。

### 输入
- 原始Fastq文件（BCR reads）
- 参考基因组（mmu/hsa）

### 输出
- BCR克隆型列表
- V/J基因突变频率
- 空间BCR克隆分布

### 核心步骤
1. MIXCR align：比对reads到BCR参考（参数：-species, -p rna-seq, allowPartial）
2. 两轮assemblePartial提高产量
3. assemble和exportClones鉴定克隆型
4. ST_BarcodeMap将BCR reads分配到DNB spots
5. Bin50窗口追踪伪spot
6. 转换为AnnData用于Scanpy可视化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| MIXCR物种 | mmu (小鼠), hsa (人) | |
| 允许部分比对 | true | |
| barcode错配 | ≤1 | |
| 空间窗口 | bin50 (50×50) | 伪spot大小 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| BCR | B Cell Receptor，B细胞受体 |
| CDR3 | Complementarity Determining Region 3 |
| MIXCR | 免疫 repertoire 分析工具 |
| clonotype | 克隆型 |

## 复现
- MIXCR: https://github.com/milaboratory/mixcr
- 版本：4.5.0
- ST_BarcodeMap: https://github.com/STOmics/ST_BarcodeMap

## 生物学意义
BCR repertoire分析揭示了体液免疫应答的多样性和亲和力成熟过程。

## 涉及 Figures
- Fig. 7 (BCR clone dynamics in Mtb infection)
