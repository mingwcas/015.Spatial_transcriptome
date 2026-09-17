# Method: Public Single-Cell RNA-Seq Data Processing

## 原文（Methods）
> Processed single-cell RNA-seq data of primary SCLC tumors and brain, kidney, liver, and pleural metastases (n = 24 samples) from Savchuk et al., were downloaded from Gene Expression Omnibus (GEO, GSE303152). Data were re-processed using a standard 'Seurat pipeline' (v5.1.0) with consistent QC filters (500–10,000 genes, 1,000–60,000 UMIs, <10% mitochondrial gene content). Potential doublets were identified and removed using 'DoubletFinder' (v2.0.6) with an expected doublet rate of 2.5%. Data normalization was performed using NormalizeData, followed by the identification of the top 2,000 highly variable genes via FindVariableFeatures. PCA was conducted on the scaled data of these variable genes, and the top 50 principal components were used for downstream analysis. A shared nearest neighbor graph was constructed using FindNeighbors (dims = 1:10), and graph-based clustering was performed with FindClusters at a resolution of 0.5. For visualization, UMAP was applied using the top 30 principal components. To integrate data across multiple samples and mitigate the batch effects, we used Seurat's canonical correlation analysis (CCA) based integration workflow prior to the final clustering and visualization steps.

## 解读

### 意义
利用公共单细胞RNA-seq数据（包含多器官转移灶）验证CosMx发现的转移相关恶性细胞亚群是否在其他转移位点也存在，还是淋巴结特异性的适应性程序。

### 输入
- Savchuk et al.的SCLC单细胞RNA-seq数据
- GEO数据库：GSE303152
- 24个样本：原发肿瘤、脑转移、肾转移、肝转移、胸膜转移

### 输出
- 整合后的单细胞RNA-seq数据
- 各转移位点的恶性细胞聚类注释
- C5、C6、C9特征基因在其他转移位点的表达情况

### 核心步骤
1. 从GEO下载GSE303152数据
2. 标准Seurat流程质控（500-10,000基因，1,000-60,000 UMIs，<10%线粒体）
3. DoubletFinder (v2.0.6)去除doublets（预期doublet率2.5%）
4. NormalizeData标准化
5. FindVariableFeatures识别top 2,000高变基因
6. PCA降维（top 50 PCs）
7. FindNeighbors (dims=1:10)和FindClusters (resolution=0.5)
8. UMAP可视化（top 30 PCs）
9. Seurat CCA整合多样本

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因数过滤 | 500-10,000 | 质控范围 |
| UMI过滤 | 1,000-60,000 | 质控范围 |
| 线粒体阈值 | <10% | 质控标准 |
| DoubletFinder版本 | v2.0.6 | doublet检测 |
| 预期doublet率 | 2.5% | DoubletFinder参数 |
| 高变基因数 | 2,000 | 下游分析 |
| 用于聚类的PCs | 50 | 降维维度 |
| FindNeighbors dims | 1:10 | 邻居构建 |
| 聚类分辨率 | 0.5 | 图聚类分辨率 |
| UMAP PCs | top 30 | 可视化降维 |
| 整合方法 | CCA | Seurat canonical correlation analysis |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DoubletFinder | 双细胞检测工具 |
| CCA | Canonical Correlation Analysis，典型相关分析 |
| UMI | Unique Molecular Identifier，唯一分子标签 |

## 复现
- 工具/代码/URL：
  - GEO: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE303152
  - DoubletFinder: https://github.com/chris-mcginnis-ucsf/DoubletFinder
  - Seurat: https://cran.r-project.org/web/packages/Seurat/index.html

## 生物学意义
该分析验证了C5、C6、C9亚群的特征基因在其他器官转移灶（脑、肝、肾、胸膜）中表达很低，表明这些亚群是淋巴结特异性的适应性程序，而非普遍性的转移驱动程序。这一发现强调了淋巴结作为免疫特化器官的独特微环境对肿瘤细胞转录组的影响。

## 涉及 Figures
- **Fig. S4A, S4B** — C5、C6、C9标记物在其他转移位点的低表达
