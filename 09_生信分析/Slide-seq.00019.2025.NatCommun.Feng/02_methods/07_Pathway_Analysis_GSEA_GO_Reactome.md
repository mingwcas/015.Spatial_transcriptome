# Method: Pathway Analysis (GSEA, GO, Reactome)

## 原文（Methods）
> Functional enrichment analysis was performed for DEGs within each cell subtype using GSEA. Pathway analysis was conducted using GO Biological Processes and Reactome databases with the ClusterProfiler package (v4.10.1). Statistically significant enrichment for GO pathways were determined with FDR ≤0.05.

## 解读

### 意义
通路分析将差异基因映射到生物学功能通路，揭示DS神经发育异常中受影响的核心生物学过程和信号通路。

### 输入
- 差异表达基因列表
- GO (Gene Ontology) Biological Processes数据库
- Reactome通路数据库
- 参考基因集

### 输出
- 标准化富集分数（NES）
- FDR校正的显著性通路
- 条形图和热图可视化

### 核心步骤
1. 使用GSEA对每个细胞亚型的DEGs进行功能富集分析
2. 使用ClusterProfiler v4.10.1进行GO生物过程富集分析
3. 使用Reactome数据库进行通路富集分析
4. FDR ≤ 0.05作为显著性阈值
5. 选择相关通路进行可视化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 富集方法 | GSEA | 基因集富集分析 |
| 分析工具 | ClusterProfiler v4.10.1 | R包 |
| 数据库 | GO BP, Reactome | 通路数据库 |
| FDR阈值 | ≤0.05 | 显著性阈值 |
| NES | Normalized Enrichment Score | 标准化富集分数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| GSEA | Gene Set Enrichment Analysis，基因集富集分析 |
| GO | Gene Ontology，基因本体论 |
| NES | Normalized Enrichment Score，标准化富集分数 |
| ClusterProfiler | 流行的富集分析R包 |

## 复现
- R包：ClusterProfiler v4.10.1
- 参考：https://yulab-smu.top/biomedical-knowledge-mining-book/

## 生物学意义
通路分析揭示了DS产前脑中的核心生物学主题：细胞周期通路下调、翻译和核糖体生物合成通路下调、染色质重塑改变、转座元件去抑制，以及特定细胞类型中SLIT-ROBO信号通路的受损。这些发现为理解DS神经发育异常的分子机制提供了系统层面的见解。

## 涉及 Figures
- **Fig. 2** — Reactome and GO pathway enrichment across cell subtypes
- **Fig. 4** — Proteomics pathway enrichment
