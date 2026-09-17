# Method: Differential Expression and Functional Analysis

## 原文（Methods）
> Differentially expressed genes (DEGs) were identified using FindAllMarkers with a stringent threshold (log2FC > 1, adjusted p value <0.001, only.pos = TRUE). p-values were adjusted using the Benjamini-Hochberg (BH) method. Pathway and biological process enrichment analyses for Gene Ontology (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) were conducted on DEG using the 'clusterProfiler' R package (v4.8.3). Terms with a false discovery rate (FDR) of less than 0.05 were considered to be significantly enriched.

## 解读

### 意义
差异表达分析识别不同细胞亚群或不同组织类型之间转录水平的显著变化，结合通路富集分析揭示相关的生物学功能和信号通路。

### 输入
- 聚类后的Seurat对象
- 细胞分组信息（亚群或组织类型）
- clusterProfiler包和GO/KEGG数据库

### 输出
- 显著差异表达基因列表（log2FC > 1, adj.p < 0.001）
- GO和KEGG富集通路
- FDR < 0.05的显著富集terms

### 核心步骤
1. FindAllMarkers鉴定DEGs（log2FC>1, adj.p<0.001, only.pos=TRUE）
2. Benjamini-Hochberg校正p值
3. clusterProfiler进行GO/KEGG富集分析
4. FDR < 0.05筛选显著通路

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| log2FC阈值 | > 1 | 差异表达基因筛选 |
| adj.p值阈值 | < 0.001 | BH校正后的显著性 |
| only.pos | TRUE | 仅返回上调基因 |
| FDR阈值 | < 0.05 | 通路显著性 |
| clusterProfiler版本 | v4.8.3 | 富集分析工具 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DEG | Differentially expressed gene，差异表达基因 |
| GO | Gene Ontology，基因本体论 |
| KEGG | Kyoto Encyclopedia of Genes and Genomes，京都基因与基因组百科全书 |
| BH method | Benjamini-Hochberg方法，FDR校正 |
| log2FC | log2 fold change，对数倍数变化 |

## 复现
- 工具/代码/URL：
  - clusterProfiler: https://doi.org/10.1089/omi.2011.0118
  - Bioconductor: http://bioconductor.org/packages/release/bioc/html/clusterProfiler.html
- 代码片段：
```r
# Differential expression analysis
markers <- FindAllMarkers(pbmc, log2fc.threshold = 1,
                          only.pos = TRUE, return.thresh = 0.001)
# Functional enrichment
library(clusterProfiler)
ego <- enrichGO(gene = markers$gene,
                OrgDb = org.Hs.eg.db,
                ont = "BP",
                pAdjustMethod = "BH",
                pvalueCutoff = 0.05)
```

## 生物学意义
差异表达分析揭示了C5、C6、C9亚群的特征基因（如FYN、NR2F2、HIF1A、SERPINA1等），这些基因与转移、细胞周期调控、代谢重编程和血管生成相关。KEGG通路分析显示这些亚群富集于细胞迁移、增殖和侵袭相关的生物学过程。

## 涉及 Figures
- **Fig. 2C** — C5、C6、C9亚群的差异基因热图和富集通路
- **Fig. 3E, 3F, 3G** — 免疫细胞DEGs和保守转录趋势
