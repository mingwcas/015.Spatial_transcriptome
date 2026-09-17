# Method: snRNA-seq (10x Chromium)

## 原文（Methods）
> Nuclei were extracted from ten individual brain samples and processed using the 10x Genomics Chromium System. Libraries were sequenced using the Novaseq 6000 on S1 flow cell at the Centre for Applied Genomics (TCAG; The Hospital for Sick Children) in Toronto, ON, Canada. To ensure data quality, cells from individual replicates underwent stringent quality control filtering and were normalized using SCTransform. Cells with ≥5% mitochondrial genes, ≤200, and ≥2,500 unique feature counts were excluded from the datasets. Following, individual replicates were integrated, and Harmony was used to correct for potential batch effects. Seurat v5 (RRID:SCR_016341) was used to perform data normalization, dimensional reduction using PCA, and graph-based clustering with UMAP.

## 解读

### 意义
单细胞核RNA测序（snRNA-seq）可在单细胞水平解析唐氏综合征（DS）产前人脑的细胞组成和转录异质性，揭示DS神经发育异常的细胞类型特异性分子改变。

### 输入
- 10个冰冻人脑组织样本（13-19孕周；n=5 DS，n=5整倍体）
- 10x Genomics Chromium系统

### 输出
- 122,663个高质量细胞核的基因表达矩阵
- UMAP降维可视化
- 细胞类型注释（主要类型和细分类）

### 核心步骤
1. 从10个独立脑样本中提取细胞核
2. 使用10x Genomics Chromium系统处理
3. Novaseq 6000测序（S1 flow cell）
4. SCTransform标准化
5. 质控过滤：排除≥5%线粒体基因、≤200或≥2500 unique features的细胞
6. Harmony批次效应校正
7. Seurat v5进行PCA降维和UMAP聚类

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 线粒体基因过滤 | ≥5% 排除 | 排除低质量细胞 |
| 最小unique features | ≤200 排除 | 排除低复杂度细胞 |
| 最大unique features | ≥2,500 排除 | 排除 doublets |
| 标准化方法 | SCTransform | 单细胞标准化 |
| 批次校正 | Harmony | 整合多样本 |
| 降维工具 | Seurat v5 | PCA + UMAP |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| snRNA-seq | 单细胞核RNA测序，从细胞核中捕获mRNA |
| SCTransform | 单细胞RNA-seq的方差稳定化标准化方法 |
| Harmony | 批次效应校正工具 |
| UMAP | 一致流形逼近与投影，降维可视化 |
| PMI | Postmortem interval，死后间隔时间 |

## 复现
- 工具：10x Genomics Chromium, Seurat v5
- 参考：https://www.satijalab.org/seurat

## 生物学意义
snRNA-seq揭示了DS产前脑的细胞类型特异性转录改变，包括神经祖细胞（NPC）周期相关通路的下调、染色质重塑基因的改变，以及转座元件的去抑制。这些发现为理解DS神经发育异常的分子机制提供了细胞层面的见解。

## 涉及 Figures
- **Fig. 1** — Cellular characterization of the prenatal Down syndrome and euploid brain
