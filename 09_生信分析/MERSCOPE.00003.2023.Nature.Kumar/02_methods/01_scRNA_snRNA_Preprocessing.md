# Method: scRNA-seq/snRNA-seq 预处理与质控

## 原文（Methods）
> Sequencing reads from single cells and single nuclei from the 10x Genomics Chromium were demultiplexed, aligned to the GRCh38.p12 human genome reference using the default parameters of the Cell-Ranger pipeline (v.3.1.0, 10x Genomics). Count matrices were generated for both datasets that were further analysed using Seurat (v.3.2.3). Cells from each sample were further filtered for low quality by removing cells with fewer than 500 UMIs or 200 genes detected. Potential doublets and multiplets were classified as cells expressing more than 20,000 UMIs or 5,000 genes and were removed. Cells with higher than 10% mitochondrial or 50% ribosomal transcripts were also filtered.

## 解读
### 意义
将10x原始读段转换为可分析的单细胞/单核表达矩阵并去除低质量细胞、双ts。
### 输入
10x Chromium scRNA/snRNA FASTQ；GRCh38.p12参考基因组。
### 输出
Cell Ranger UMI/count矩阵；Seurat可分析对象。
### 核心步骤
1. Cell Ranger v3.1.0解复用并比对GRCh38.p12。
2. 生成基因×细胞/细胞核矩阵并载入Seurat v3.2.3。
3. 去除低于UMI/基因阈值、双ts及高线粒体/核糖体比例细胞。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| 最低UMI | 500 | scRNA/snRNA共同阈值 |
| 最低基因数 | 200（scRNA）；150（snRNA） | 检出基因下限 |
| 双ts上限 | 20,000 UMI或5,000基因 | 超过即剔除 |
| 线粒体/核糖体 | >10%/>50%剔除 | 低质量指标 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| UMI | 唯一分子标识计数 |
| Cell Ranger | 10x读段比对与定量流水线 |
| GRCh38.p12 | 人基因组参考版本 |

## 复现
- Cell Ranger v3.1.0；Seurat v3.2.3。
- 关键调用：`cellranger count --transcriptome=GRCh38.p12 ...`；`subset(obj, nCount_RNA>=500 & nFeature_RNA>=200)`。

## 生物学意义
严格质控提高细胞类型和状态识别可靠性，但阈值可能排除低RNA含量细胞核或稀有细胞。

## 涉及 Figures
- **Fig. 1** — 714,331细胞与117,346细胞核整合聚类。
- **Fig. 3–6** — 各细胞群重聚类结果。
