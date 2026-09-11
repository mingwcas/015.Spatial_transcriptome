# Method: Spatial Pathway Enrichment

## 原文（Methods）
> To assess pathway-level differences across spatial regions, differentially expressed genes (DEGs) were identified using the scanpy Python package. Comparisons were made between immune-infiltrated versus tumor regions and tumor versus normal epithelial regions. Genes with adjusted p-value ≤0.05 and fold change ≥2 were defined as DEGs and subsequently subjected to GO enrichment analysis (R package clusterProfiler, v.4.6.2). Pathways with adjusted p-value ≤0.05 were retained for downstream comparisons across platforms.

## 解读

### 意义
通过空间分辨的差异表达分析和GO通路富集，评估各ST平台在识别区域特异性生物学通路方面的能力。这是跨平台功能通路检测能力的重要基准测试。

### 输入
- 各ST平台表达矩阵
- 解剖学对齐的区域选择（免疫浸润区、肿瘤区、正常上皮区）

### 输出
- 各区域类型的差异表达基因列表
- GO富集通路（adjusted p ≤ 0.05）
- 跨平台通路富集比较

### 核心步骤
1. 从相邻连续切片选择三种区域类型：
   - 免疫浸润区
   - 肿瘤区
   - 正常上皮区
2. 使用scanpy识别差异表达基因：
   - 免疫浸润区 vs 肿瘤区
   - 肿瘤区 vs 正常上皮区
3. 筛选条件：adjusted p-value ≤ 0.05 且 fold change ≥ 2
4. 使用clusterProfiler (v.4.6.2)进行GO富集分析
5. 保留adjusted p-value ≤ 0.05的通路
6. 跨平台比较通路富集结果

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| DEG阈值 | adjusted p-value ≤ 0.05 且 fold change ≥ 2 |  |
| 富集分析工具 | clusterProfiler v.4.6.2 | R包 |
| 通路显著性 | adjusted p-value ≤ 0.05 |  |
| 分析工具 | scanpy v.1.10.3 | Python |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DEG | Differentially Expressed Genes，差异表达基因 |
| GO | Gene Ontology，基因本体论 |
| fold change | 表达量倍数变化 |
| clusterProfiler | R语言通路富集分析包 |

## 复现
- scanpy: v.1.10.3 (Python)
- clusterProfiler: v.4.6.2 (R)

## 生物学意义
研究发现Xenium 5K在免疫浸润区识别出最多的DEGs和通路，包括独特的T细胞激活和白细胞介导细胞毒性通路。相比之下，CosMx 6K富集到的通路较少，主要与代谢相关，提示其检测敏感性可能受限。

## 涉及 Figures
- **Supplementary Fig. 16** — 空间通路富集分析详细结果
