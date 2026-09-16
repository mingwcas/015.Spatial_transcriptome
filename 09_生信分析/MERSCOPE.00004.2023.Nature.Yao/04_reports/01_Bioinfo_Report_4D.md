# 四维度生信分析报告 — A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain

> Nature 624, 317–332 (2023), DOI: [10.1038/s41586-023-06812-z](https://doi.org/10.1038/s41586-023-06812-z)，平台：MERSCOPE/MERFISH。

## 维度一：分析方法 / Methods
|分析类型|方法|工具/版本|关键结果|
|---|---|---|---|
|scRNA处理|比对、QC、双细胞|CellRanger 6.1.1、DoubletFinder|约4.0M QC细胞|
|聚类整合|迭代Jaccard–Leiden、跨模态KNN|scrattch.bigcat 0.0.5、BiocNeighbors 1.16、Annoy 1.17.1|5,322 clusters层级taxonomy|
|空间转录组|MERSCOPE解码/Cellpose分割/映射|Vizgen v231、Cellpose|约4.3M细胞空间标签|
|配准统计|CCFv3 ANTs配准、Gini/Shannon|ANTS、DescTools、vegan|51切片/3,062,367细胞空间统计|
|调控分析|TF模块|WGCNA，power=6|52模块|

## 维度二：结果图表
|图|内容摘要|主要图形类型|
|---|---|---|
|Fig.1|全脑taxonomy与UMAP|树状图、UMAP|
|Fig.2|六个神经元邻域|UMAP、MERFISH|
|Fig.3|调节性递质及空间|UMAP、空间图|
|Fig.4|非神经元/未成熟神经元|UMAP、空间图|
|Fig.5|TF模块与分类准确度|热图、密度图、箱线/柱图|
|Fig.6|CCFv3区域特征|热图、散点图|

## 维度三：Pipelines
|阶段|工具|版本|开源/商业|
|---|---|---|---|
|测序比对|CellRanger/NovaSeq|6.1.1|商业软件/仪器|
|聚类|scrattch.bigcat|0.0.5|开源R包|
|映射|scrattch.mapping|0.2|开源|
|分割解码|Vizgen/Cellpose|v231|Vizgen商业+开源|
|配准|ANTs|未注明|开源|

## 维度四：算法与 AI
|算法/模型|类型|用途|
|---|---|---|
|Jaccard–Leiden|图聚类|细胞类型聚类与层级构建|
|Annoy KNN|近邻检索|跨模态整合、映射、imputation|
|UMAP/PCA|降维|可视化taxonomy|
|WGCNA|网络分析|TF共表达模块|
|Cellpose|深度学习分割|DAPI/PolyT细胞边界|

**局限**：空间结论依赖CCFv3配准；分割污染、稀有类型采样不足及部分软件/仪器商业化限制复现。
