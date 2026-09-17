# Method: 2D and 3D Cellular Neighborhood Identification and Multicellular Niche Annotation

## 原文（Methods）
> Cellular neighborhoods in 2D and 3D were computed with a custom Python script. First, for a given cell, the Euclidean distances in 2 or 3D between that cell and all other cells in the dataset were computed. This set of distances was then ﬁltered to remove distances greater than r=50 μm, resulting in a list of neighboring cells. This list was ﬁnally used to construct the 2D and 3D neighborhood matrices by counting the number of cells for each of the 18 cell types present in each cellular neighborhood. To identify 2D/3D multicellular niches in the TME, we imported the 2D/3D neighborhood matrix as a new assay in Seurat. We excluded cells with incomplete 3D neighborhoods. We then performed UMAP dimensionality reduction and clustering (resolution = 0.3).

## 解读

### 意义
定义每个细胞的2D和3D邻域（50μm半径），通过无监督聚类识别肿瘤微环境中的10种多细胞niche，揭示TME的空间组织架构。

### 输入
- 340,644个细胞的空间坐标和细胞类型注释
- 2D邻域：以目标细胞为中心，50μm半径的圆形区域
- 3D邻域：2D邻域 + 上下各40μm半径的邻近切片区域

### 输出
- 200,000+个细胞邻域
- 10种3D多细胞niche：tumor core, tumor surface, airways, alveoli, desmoplastic stroma, vascular stroma, smooth muscle, macrophage niche, dendritic cell niche, T cell niche

### 核心步骤
1. 计算每个细胞与其他所有细胞的2D/3D欧氏距离
2. 过滤>50μm的距离，构建18种细胞类型的邻域计数矩阵
3. 将邻域矩阵导入Seurat作为新assay
4. 排除不完整3D邻域的细胞（sections 4和34，以及边缘50μm内的细胞）
5. UMAP降维 + 聚类（分辨率0.3）
6. 合并相似聚类，注释10种多细胞niche
7. 与病理学家H&E标注进行比较验证

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 2D邻域半径 | 50 μm | 中心细胞到邻域边界的距离 |
| 3D邻域Z半径 | 40 μm | 上下切片邻域的半径 |
| 切片间距 | 30 μm | 3D邻域的Z轴跨度 |
| 3D邻域面积比2D | 2.28× | 3D邻域比2D邻域大2.28倍 |
| 聚类分辨率 | 0.3 | 多细胞niche聚类的分辨率 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 细胞邻域 | 以特定细胞为中心、给定半径内的所有邻近细胞的集合 |
| 多细胞niche | 共享相似邻域组成的细胞群落，代表TME中的功能单元 |
| Desmoplastic stroma | 促结缔组织增生性基质，富含成纤维细胞和浆细胞 |
| TME | 肿瘤微环境（Tumor Microenvironment） |

## 复现
- 工具: Seurat v4.0.4 + 自定义Python脚本
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
3D邻域分析揭示了TME由10种重复出现、空间有序的多细胞niche组成，涵盖了肺组织固有结构（气道、肺泡、平滑肌）和TME特有结构（肿瘤核心、肿瘤表面、纤维化基质、免疫niche）。niche注释与病理学家手动H&E标注高度一致，验证了方法的可靠性。3D分析相比2D在免疫niche识别上有显著优势（见方法06）。

## 涉及 Figures
- **Fig. 2B-E** — 3D邻域设计、niche UMAP、组成热图和空间定位
- **Fig. S2B-D** — 聚类结果和细胞多样性
