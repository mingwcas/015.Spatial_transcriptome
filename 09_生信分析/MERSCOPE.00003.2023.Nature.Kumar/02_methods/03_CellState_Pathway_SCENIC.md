# Method: 细胞状态重聚类、通路富集与SCENIC调控网络

## 原文（Methods）
> Each cell cluster was further extracted and underwent clustering and filtering as described above with different parameters. ... Differentially expressed genes were calculated ... using the FindMarkers function in Seurat with the Wilcoxon rank-sum test ... Expression states were further annotated by investigating the top 200 genes of each cluster and performing pathway enrichment.
> For gene set enrichment analysis, ranked genes ... were fed into the fgsea R package ... using 1,000 permutations ... Significantly enriched gene sets ... Benjamini–Hochberg adjusted P ≤ 0.05.
> For the RNA regulatory network analysis, we used SCENIC ... from the scRNA-seq and snRNA-seq data.

## 解读
### 意义
在主类型内部解析生物状态，解释其通路并推断转录因子调控网络。
### 输入
各主细胞类型子集、差异基因排序、MSigDB基因集、scRNA/snRNA表达矩阵。
### 输出
细胞状态簇、DEG、fgsea/GO/KEGG富集和SCENIC regulon分数。
### 核心步骤
1. 按主类型提取细胞并用特定dims、k.param、resolution重聚类。
2. FindMarkers（Wilcoxon）计算状态相对DEG，查看top 200基因。
3. fgsea以1,000 permutations做预排序富集；clusterProfiler做GO/KEGG。
4. SCENIC推断RNA调控网络，比较各类型top regulons。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| fgsea permutations | 1,000 | 置换次数 |
| 富集显著性 | BH adjusted P≤0.05 | FDR阈值 |
| DE筛选 | adjusted P≤0.05 | 输入排序基因 |
| 状态DEG | Wilcoxon | 细胞内比较 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| fgsea | 快速预排序基因集富集分析 |
| SCENIC | 基于共表达和motif的调控网络推断 |
| regulon | 转录因子及其靶基因集合 |

## 复现
- Seurat FindMarkers；fgsea；clusterProfiler；SCENIC（https://scenic.aertslab.org/）。
- 示例：`fgsea(pathways=msigdb_sets, stats=ranked_logFC, nperm=1000)`。

## 生物学意义
揭示LumHR、LumSec、免疫、成纤维等细胞的功能异质性和潜在调控因子；网络为推断而非因果验证。

## 涉及 Figures
- **Fig. 3e–l、4f–k、5b–d、6b–f/j–k**；Extended Data Fig. 1、5、7、9–11。
