# Method: Ligand Spatial Activity Score Computation and Cell-Cell Communication Analysis

## 原文（Methods）
> To estimate the spatial activity of a speciﬁc ligand, we ﬁrst downloaded manually-curated, literature-supported receptor ligand pairs from the CellChat Human database and selected those in which both the receptor and the ligand were present in our 960-gene panel. For each center cell, we quantiﬁed the spatial activity of 164 ligands in its 2D and 3D cellular neighborhoods. To quantify the activity of each ligand in a given cellular neighborhood, we ﬁrst evaluated single pairs of interacting cells comprising the center cell and one of its neighbors. For each pair, we computed the geometric mean of receptor expression in the center cell and ligand expression in the neighbor cell. We then compute the overall ligand activity score for a speciﬁc cellular neighborhood summing all the pair scores having the center cell as receiver.

## 解读

### 意义
在3D细胞邻域中系统量化受体-配体相互作用的空间活性，揭示niche特异性的细胞间通讯网络。

### 输入
- CellChat数据库中480对受体-配体对（筛选panel中存在的）
- 3D细胞邻域中每个细胞的受体和配体表达量
- 邻域半径50μm

### 输出
- 164个配体的3D空间活性评分
- 96个配体在至少1个niche中富集（log2FC > 0.5）
- niche特异性通讯网络

### 核心步骤
1. 从CellChat数据库下载人工整理的受体-配体对
2. 筛选960基因panel中同时检测到受体和配体的480对
3. 对每对相互作用，计算中心细胞（接收方）受体表达与邻居细胞（发送方）配体表达的几何平均
4. 仅受体和配体同时非零表达时才有正分
5. 将同一配体与多个受体的活性求和
6. 比较每个niche内外的配体活性，识别niche富集的配体

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 数据库 | CellChat Human | 手工整理的受体-配体数据库 |
| 受体-配体对数 | 480 | 在panel中检测到的对数 |
| 配体轴数 | 165 | 按配体分组的通讯轴 |
| 富集阈值 | log2FC > 0.5 | niche内vs外的配体活性差异 |
| 富集配体数 | 96 | 至少在1个niche中富集的配体 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Ligand spatial activity score | 量化特定配体在细胞邻域中空间活性的指标 |
| CellChat | 细胞间通讯分析R包，提供手工整理的受体-配体对 |
| 几何平均 | sqrt(R×L)，要求受体和配体同时表达才有正分 |

## 复现
- CellChat: Jin et al., 2021 (Nat Commun)
- http://www.cellchat.org/
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
空间邻域约束的通讯分析相比空间无关的分析（如仅基于表达量）具有更高的灵敏度和特异性。1-2 molecules/cell的检测灵敏度使得低表达配体/受体也能被检测。该方法成功鉴定出niche特异性的通讯轴：如PDGFB限于血管niche，CDH1和EFNA1限于肿瘤bed，CCL19标记树突状细胞和T细胞niche。在树突状细胞niche中，该方法揭示了免疫检查点相互作用（PD-L1/PD-1, Galectin-9/Tim-3, CD80-CTLA4），为免疫治疗靶点提供了分子基础。

## 涉及 Figures
- **Fig. 4A-E** — 配体空间活性分析流程、niche特异性配体热图和3D渲染
- **Fig. 4F-G** — 树突状细胞niche通讯网络和免疫检查点示意图
- **Fig. S4** — 通讯分析细节
