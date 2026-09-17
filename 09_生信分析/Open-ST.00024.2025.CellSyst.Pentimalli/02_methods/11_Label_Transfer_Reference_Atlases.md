# Method: Data Integration with Reference scRNA-seq Atlases (Label Transfer)

## 原文（Methods）
> To compare gene expression proﬁles with published reference atlases, we performed label transfer using the standard Seurat pipeline. We integrated our data with the Human Lung Cell Atlas to annotate lung resident cell types and with a NSCLC single cell cohort to annotate tumor-speciﬁc cell types. For each reference dataset, we identiﬁed a subset of 900 shared 'features' using the SelectIntegrationFeatures function and pairs of 'anchors' between the reference and our query dataset using the FindTransferAnchors function. Then, we leveraged the TransferData function to score each cell in our query dataset for similarity with annotated cell types in the reference dataset.

## 解读

### 意义
将CosMx空间转录组数据与已发表的健康肺和NSCLC单细胞RNA-seq参考图谱整合，验证细胞类型注释的准确性。

### 输入
- CosMx单细胞数据（query）
- 健康肺细胞图谱（Travaglini et al., 2020）
- NSCLC单细胞队列（Kim et al., 2020）

### 输出
- 每个细胞与参考细胞类型的相似度评分
- 注释一致性的验证

### 核心步骤
1. 选择900个共享特征基因（SelectIntegrationFeatures）
2. 使用SCT归一化方法寻找参考和query数据集间的锚点（FindTransferAnchors）
3. 使用pcaproject降维方法
4. TransferData函数计算每个细胞与参考细胞类型的相似度
5. 可视化label transfer score的UMAP

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 共享特征基因 | 900 | SelectIntegrationFeatures nfeatures |
| 归一化方法 | SCT | reference和query均使用SCT assay |
| 降维方法 | pcaproject | 将query投影到参考PC空间 |
| PC维度 | 1:20 | 用于anchor寻找的PC范围 |
| NN方法 | rann | 近似最近邻方法 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Label transfer | 将参考数据集的细胞类型标签转移到query数据集的方法 |
| Anchor | 参考和query数据集中基因表达模式相似的细胞对 |
| SCT assay | SCTransform归一化后的表达矩阵 |

## 复现
- Seurat v4.0.4: Stuart et al., 2019 (Cell)
- 健康肺图谱: Travaglini et al., 2020 (Nature), Synapse: syn21041850
- NSCLC数据: Kim et al., 2020 (Nat Commun), GEO: GSE131907
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
与两个独立参考图谱的一致性验证增强了细胞类型注释的可信度。健康肺图谱验证了肺固有细胞类型（肺泡细胞、呼吸道上皮等），NSCLC图谱验证了肿瘤特异性细胞类型。这种交叉验证策略对于单panel空间转录组数据的细胞类型注释尤为重要。

## 涉及 Figures
- **Fig. 1E** — UMAP展示与健康肺和NSCLC参考图谱的label transfer score
