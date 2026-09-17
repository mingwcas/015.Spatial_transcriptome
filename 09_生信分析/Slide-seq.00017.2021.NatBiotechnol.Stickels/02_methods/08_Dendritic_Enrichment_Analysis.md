# Method: Dendritic Enrichment Analysis

## 原文（Methods）
> To test for dendritic enrichment, for each gene the gene expression in the soma layer (defined as ±32.5 µm from the peak of the profile counts for all genes) was compared against the gene expression in the proximal dendrites (greater than 32.5 μm away from the peak of the CA1 layer)... A two-sample t-test was performed to identify differentially expressed genes, and pFDR was calculated as described previously45.

## 解读

### 意义
Dendritic enrichment analysis利用CA1 pyramidal neuron的极化结构（soma层与dendritic neuropil分离），在全基因组范围内筛选dendritically localized mRNAs。

### 输入
- Slide-seqV2 DGE matrix from mouse hippocampus
- CA1 marker gene expression profile
- Existing scRNA-seq data for cell type marker exclusion
- 4 tissue sections (n=4)

### 输出
- 213 dendritically enriched genes (fold change >2, q<0.05)
- Spatial expression profiles along CA1 neuropil axis
- 4 clusters of dendritic genes (k-means)

### 核心步骤
1. **Define spatial regions**: 
   - Soma layer: ±32.5 μm from CA1 pyramidal layer peak
   - Proximal dendrites: >32.5 μm from peak
2. **Filter non-neuronal genes**: Exclude genes with >0.5 TPM in non-CA1 cell types (from scRNA-seq data)
3. **Calculate enrichment**: 
   - Normalize to total UMI counts per compartment
   - Compute fold change (dendrite/soma)
4. **Statistical test**: Two-sample t-test, n=4 sections
5. **Multiple testing correction**: FDR (Storey 2002)
6. **Threshold**: FC>2, q<0.05

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Soma definition | ±32.5 μm from peak | CA1 pyramidal layer |
| Dendrite definition | >32.5 μm from peak | Stratum radiatum |
| Fold change cutoff | >2 | 显著dendritic enrichment |
| P-value cutoff | q < 0.05 | FDR校正后 |
| Sections | n=4 | 生物学重复 |
| Min expression | >0.5 TPM in CA1 | 过滤低表达 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Dendritic enrichment | 基因在dendrite相对于soma的表达比率 |
| CA1 neuropil | CA1区域的Dendritic region (stratum radiatum) |
| Stratum pyramidale | CA1 pyramidal neuron soma层 |
| FDR | False Discovery Rate，多重检验校正 |
| TPM | Transcripts Per Million |

## 复现
- **工具**: Custom R/Python scripts
- **scRNA-seq reference**: Saunders et al. Cell 2018
- **统计方法**: Storey FDR (2002)
- **聚类**: k-means, gap-statistic for k selection
- **代码**: https://github.com/rstickels/Slide_seqv2

## 生物学意义
Dendritic mRNA localization对突触可塑性、蛋白质合成依赖的LTP至关重要。该分析在全基因组层面鉴定dendritically localized mRNAs，发现了213个显著enriched基因，验证了Slide-seqV2检测低丰度转录本的能力。

## 涉及 Figures
- **Fig. 2c** — 213 dendritically enriched genes
- **Fig. 2d,e** — 4 spatial clusters
- **Fig. 2f** — Example genes from each cluster
- **Supplementary Table 3** — Full gene list
