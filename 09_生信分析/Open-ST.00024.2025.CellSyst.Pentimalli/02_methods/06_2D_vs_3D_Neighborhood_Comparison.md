# Method: 2D vs 3D Neighborhood Comparison and Immune Niche Analysis

## 原文（Methods）
> By design, 3D neighborhoods included cells from the sections immediately above and below the z plane, comprising a 2.28-fold larger area than their 2D counterparts. As expected, 2D neighborhoods featured a lower number of neighbors and lower cell type diversity than their 3D counterparts (median of 71 cells from 9 cell types/neighborhood in 3D vs. 32 cells from 7 cell types in 2D, p < 0.005), conﬁrmed by a lower alpha diversity (median Chao index 3D: 10.5 vs. 2D: 8, p < 0.005).

## 解读

### 意义
系统比较2D和3D细胞邻域在TME空间组织表征上的差异，验证3D分析在免疫niche识别上的优势。

### 输入
- 同一数据集的2D和3D邻域矩阵
- 18种细胞类型注释

### 输出
- 2D/3D邻域比较量化指标
- 3D特有niche（树突状细胞niche）的鉴定
- 2D/3D一致性分析

### 核心步骤
1. 2D邻域：50μm半径的圆形区域；3D邻域额外包含上下切片各40μm半径区域
2. 量化邻居数量和细胞类型多样性（alpha多样性用Chao指数衡量）
3. 比较2D和3D niche分配的一致性
4. 验证3D特有niche（dendritic cell niche）通过IF染色

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 3D中位邻居数 | 71 cells / 9 cell types | 3D邻域的中位细胞数和类型数 |
| 2D中位邻居数 | 32 cells / 7 cell types | 2D邻域的中位细胞数和类型数 |
| 3D Chao指数 | 10.5 | 3D邻域的alpha多样性 |
| 2D Chao指数 | 8 | 2D邻域的alpha多样性 |
| 2D-3D总一致性 | 64.1% | 同一niche分配的细胞比例 |
| T cell niche一致性 | 46.2% | 最低一致性的niche |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Alpha多样性 | 生态学中的物种丰富度指标，此处用于衡量细胞类型多样性 |
| Chao指数 | 一种非参数物种丰富度估计量 |
| 2D-3D一致性 | 同一细胞在2D和3D分析中被分配到相同niche的比例 |

## 复现
- 自定义Python脚本 + Seurat v4.0.4
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
3D邻域包含2.28倍于2D的面积，捕获了更丰富的细胞多样性。关键发现：
1. 树突状细胞niche仅在3D中被鉴定，并经IF验证
2. T细胞niche一致性最低（46.2%），3D分析恢复了看似不连续的T细胞niche的空间连续性
3. 在2D中被错误分配到desmoplastic stroma的35.3%的T细胞niche细胞，在3D中被正确识别
这表明3D分析对免疫niche的准确表征至关重要。

## 涉及 Figures
- **Fig. 3A-E** — 2D/3D邻域设计、alpha多样性比较、niche一致性、T细胞niche 3D渲染
- **Fig. S3A-D** — 2D niche UMAP、一致性细节、IF验证
