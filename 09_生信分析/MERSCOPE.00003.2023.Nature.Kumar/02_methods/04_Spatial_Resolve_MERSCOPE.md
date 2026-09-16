# Method: Resolve smFISH与MERSCOPE MERFISH空间分析

## 原文（Methods）
> We used QuPath (v.0.3.0) to segment cells on the basis of their DAPI images, then used ImageJ (v.1.52n) and the Molecular Cartography plug-in ... to count genes in each cell. ... cells with less than 10 gene counts were filtered ... A random-forest machine learning model with a default of 500 trees was trained ... top 20 principal components as predictors ...
> For each tissue section ... divided into different spatial regions ... We performed cell segmentation using CellPose based on ... DAPI signal and the cell membrane staining ... Cells were filtered with fewer than 20 UMIs or 10 genes detected ... random-forest model with a default of 500 trees ...

## 解读
### 意义
将靶向空间转录信号分配到单细胞并映射到导管、叶 lobule、脂肪和结缔组织。
### 输入
Resolve 100基因smFISH；MERSCOPE 266基因MERFISH；DAPI/膜图像；病理区域标注。
### 输出
细胞分割、细胞×基因矩阵、空间坐标、细胞类型/状态标签、邻域图和区域频率。
### 核心步骤
1. Resolve用QuPath DAPI分割、ImageJ/Molecular Cartography计数；MERSCOPE用CellPose分割。
2. 按低计数阈值过滤；Seurat NormalizeData、ScaleData、PCA、UMAP。
3. AddModuleScore按marker初注释，再以500树random forest、top20 PCs和投票阈值细化。
4. 病理学标注空间区域；CellTrek scoloc DT计算Resolve细胞邻域共定位。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| Resolve panel | 100 genes | scRNA marker设计 |
| Resolve过滤 | <10 gene counts剔除 | 低信号细胞 |
| MERSCOPE过滤 | <20 UMIs或<10 genes剔除 | 低质量细胞 |
| random forest | 500 trees；top 20 PCs | 监督分类 |
| 低置信度 | 最大分数/投票<0.5；MERSCOPE top1-top2<0.1 | 标签过滤 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| smFISH/MERFISH | 单分子/高复用荧光原位杂交 |
| AddModuleScore | 基因模块平均表达评分 |
| CellPose | 细胞图像分割算法 |

## 复现
- QuPath 0.3.0、ImageJ 1.52n、Seurat 3.2.3、CellPose、randomForest、CellTrek。
- 示例：`AddModuleScore(obj, features=marker_list)`；`randomForest(x=PC1:PC20, y=label, ntree=500)`。

## 生物学意义
验证scRNA marker在原位的空间生态位与细胞邻域；靶向panel和分割误差限制未覆盖细胞及边界细胞的解释。

## 涉及 Figures
- **Fig. 2d–f、3p–q、4e/m、5e、6g**；Extended Data Fig. 4、6、8、9、10、11。
