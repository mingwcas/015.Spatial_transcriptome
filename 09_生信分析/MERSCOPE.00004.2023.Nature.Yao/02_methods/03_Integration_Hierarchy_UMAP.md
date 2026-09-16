# Method: 跨平台整合、层级taxonomy与UMAP

## 原文（Methods）
> Key steps ... select anchor cells; select high variance genes; compute KNN within and cross modality; compute Jaccard similarity; perform Leiden clustering; merge clusters based on conserved DEGs; repeat ... until no clusters can be found.

## 解读
### 意义
整合10xv2/v3并构建class–subclass–supertype–cluster四级分类。
### 输入
10xv2、10xv3、10xMultiome矩阵及marker基因。
### 输出
34 classes、338 subclasses、1,201 supertypes、5,322 clusters及UMAP。
### 核心步骤
1. 锚细胞和共享HVG。2. BiocNeighbors/Annoy跨模态KNN。3. Jaccard–Leiden和DEG合并迭代。4. 534 TF marker定义层级并人工校正。5. PCA后UMAP。
### 关键参数（本文设置）
|参数|值|含义|
|---|---|---|
|hierarchy KNN|5|层级聚类|
|TF markers|534|class/subclass特征|
|UMAP|nn.neighbors=25, md=0.4|降维|
|Annoy|v1.17.1|近邻索引|

## 名词/参数/指标
|名词|定义|
|---|---|
|Anchor|跨数据集参考细胞|
|Hierarchy|root→class→subclass→supertype→cluster|

## 复现
- scrattch.bigcat：https://github.com/AllenInstitute/scrattch.bigcat；BiocNeighbors v1.16.0；cirrocumulus v1.1.56
- `iter_clust_big()`；UMAP参数如上

## 生物学意义
建立可解释的全脑分层分类；人工校正和稀有群体缺失是潜在偏差。

## 涉及 Figures
- **Fig. 1–2**；Extended Data Fig. 4,6,7
