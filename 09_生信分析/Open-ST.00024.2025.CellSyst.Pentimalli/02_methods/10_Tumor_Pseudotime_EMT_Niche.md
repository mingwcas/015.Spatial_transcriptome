# Method: Tumor Pseudotime Analysis and EMT Niche Characterization

## 原文（Methods）
> To reconstruct their molecular dynamics, we ordered tumor cells according to their pseudotime. We ﬁrst generated a Seurat object including only tumor cells using the subset function and then re-normalized gene expression counts using SCTransform. We then selected the top 400 variable genes and grouped them in 5 PCs using the RunPCA function for downstream analyses. These included UMAP embedding and pseudotime analysis. For the latter, we converted the Seurat object into SingleCellExperiment format and then used the slingshot function to compute tumor cell pseudotime. Finally, we converted pseudotime scores to ranks (between 0 and 1) and added them as metadata in the Seurat object for plotting.

## 解读

### 意义
利用伪时间分析重建肿瘤细胞的上皮-间充质转化（EMT）动态过程，鉴定肿瘤表面的EMT niche及其分子驱动机制。

### 输入
- 38,804个肿瘤细胞的基因表达矩阵
- 3D niche分配信息

### 输出
- 肿瘤细胞伪时间排序（0-1）
- EMT相关基因的动态表达模式
- EMT niche的鉴定和分子特征

### 核心步骤
1. 提取肿瘤细胞子集，SCTransform重新归一化
2. 选择top 400高变异基因，计算5个PC
3. 使用slingshot计算伪时间轨迹
4. 伪时间转换为排名（0到1）
5. 结合3D niche分配，分析伪时间的空间分布
6. 识别伪时间与"pseudospace"（距肿瘤bed的距离）的关系
7. 鉴定EMT niche中差异表达基因

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 肿瘤细胞数 | 38,804 | 分析的肿瘤细胞总数 |
| 高变异基因数 | 400 | 用于伪时间分析的基因数 |
| PC数 | 5 | 主成分维数 |
| 工具 | Slingshot v2.2.1 | 伪时间轨迹推断工具 |
| 伪时间范围 | 0（早期/上皮）到 1（晚期/间充质） |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Pseudotime | 伪时间，根据基因表达相似性排列细胞，重建动态过程 |
| EMT | 上皮-间充质转化（Epithelial-to-Mesenchymal Transition） |
| Pseudospace | 伪空间，肿瘤细胞距肿瘤bed的空间距离 |
| EMT niche | 肿瘤表面中EMT预先激活的特定区域 |
| NDRG1 | N-myc下游调控基因1，脑转移标志物 |
| LGALS1 | 半乳糖凝集素1，伤口愈合和炎症调节因子 |

## 复现
- Slingshot v2.2.1: Street et al., 2018 (BMC Genomics)
- Seurat v4.0.4, SingleCellExperiment v1.16.0
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
伪时间分析揭示了关键发现：EMT不仅发生在浸润到desmoplastic stroma的肿瘤细胞中，更早在肿瘤表面的一个特定区域（EMT niche）就已预先激活。该niche中：
- NDRG1（脑转移标志物）几乎完全限于EMT niche肿瘤细胞
- LGALS1（伤口愈合开关）也在该区域富集
- 肌成纤维细胞、SPP1+巨噬细胞和肿瘤细胞形成伤口愈合样通讯网络
- 多条配体（IGF2, THBS1, SPP1, FN1, THBS2, COL1A2, COL6A3）汇聚于肿瘤整合素受体（ITGB1, ITGB4, ITGB6）

这与"肿瘤是永不愈合的伤口"理论一致，为整合素信号抑制剂（如FAK抑制剂）提供了治疗靶点依据。

## 涉及 Figures
- **Fig. 6A-F** — 肿瘤浸润、EMT伪时间、空间分布和ECM关联
- **Fig. 7A-I** — EMT niche标志物、伤口愈合样通讯网络和整合素信号
- **Fig. S6-S7** — 3D渲染和通讯网络细节
