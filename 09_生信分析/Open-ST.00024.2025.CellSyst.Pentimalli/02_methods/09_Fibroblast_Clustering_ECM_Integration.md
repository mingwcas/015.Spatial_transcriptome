# Method: Fibroblast Transcriptomic Clustering and ECM-Phenotype Integration

## 原文（Methods）
> To identify transcriptomic states of the ﬁbroblast in the TME, we selected cells annotated as ﬁbroblasts with more than 100 detected transcripts for unsupervised clustering, this time selecting the ﬁrst 5 PCs and identifying 6 clusters and a resolution= 0.15. We then identiﬁed marker genes enriched in each cluster for literature-based cluster annotation: 'matrix ﬁbroblasts' (LUM+ MGP+ TIMP1+), 'myoﬁbroblasts' (FN1+ COL11A1+ ACTA2+), 'activated ﬁbroblasts' (JUN+ FOS+ IGF1+), 'antigen-presenting' (CD74+ HLA-DRB1+), 'CCL19+ reticular' and 'CXCL10+ reticular' ﬁbroblasts.

## 解读

### 意义
鉴定成纤维细胞的6种转录组状态，并揭示它们与ECM区室和多细胞niche的空间关联。

### 输入
- 62,604个成纤维细胞（>100转录本的细胞）
- 基因表达矩阵

### 输出
- 6种成纤维细胞转录组状态
- 成纤维细胞表型与ECM区室的关联

### 核心步骤
1. 筛选>100转录本的成纤维细胞
2. SCTransform归一化，选前5个PC
3. 聚类分辨率0.15，识别6个聚类
4. 基于标记基因和文献注释6种状态
5. 量化每种状态在ECM区室中的富集
6. 分析成纤维细胞邻域的胶原和弹性蛋白含量

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 成纤维细胞数 | 62,604 | 分析的成纤维细胞总数 |
| 最低转录本数 | 100 | 细胞筛选阈值 |
| PC数 | 5 | 主成分维数 |
| 聚类分辨率 | 0.15 | 比全局聚类更保守的分辨率 |
| 聚类数 | 6 | 成纤维细胞状态数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CAF | 癌相关成纤维细胞（Cancer-Associated Fibroblasts） |
| Myofibroblasts | 肌成纤维细胞，FN1+ COL11A1+ ACTA2+，与ECM降解相关 |
| Activated fibroblasts | 活化成纤维细胞，JUN+ FOS+ IGF1+，与胶原沉积相关 |
| Matrix fibroblasts | 基质成纤维细胞，LUM+ MGP+ TIMP1+，与稳态ECM相关 |
| Antigen-presenting fibroblasts | 抗原呈递成纤维细胞，CD74+ HLA-DRB1+ |
| Reticular fibroblasts | 网状成纤维细胞，CCL19+或CXCL10+，与免疫niche相关 |

## 复现
- Seurat v4.0.4, R v4.1
- 代码: https://github.com/rajewsky-lab/3D_lung
- 文献参考: Kieffer et al., 2020; Lambrechts et al., 2018; Elyada et al., 2019; Fletcher et al., 2015

## 生物学意义
成纤维细胞是TME中最丰富的细胞类型，其功能异质性远超简单分类。6种状态的空间分布揭示了功能特化：
- 肌成纤维细胞限于降解ECM（肿瘤bed），与FN1/COL11A1表达一致
- 活化成纤维细胞在desmoplastic ECM中产生最高胶原信号
- 抗原呈递和网状成纤维细胞分别定位于macrophage和免疫niche，参与免疫调控而非ECM代谢
这表明成纤维细胞在TME中的角色远不止ECM产生，还包括免疫调节。

## 涉及 Figures
- **Fig. 5D-F** — 成纤维细胞UMAP、空间分布和ECM关联
- **Fig. S5D-F** — 标记基因和niche富集
