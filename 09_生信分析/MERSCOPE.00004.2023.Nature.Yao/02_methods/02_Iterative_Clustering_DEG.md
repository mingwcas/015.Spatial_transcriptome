# Method: scrattch.bigcat迭代聚类与差异基因

## 原文（Methods）
> Clustering ... was performed using scrattch.bigcat (v0.0.5). We used automatic iterative clustering, iter_clust_big ... Jaccard–Leiden clustering proceeded as before.

## 解读
### 意义
对数百万细胞进行可扩展逐级聚类。
### 输入
QC后10xv2/v3矩阵；parquet稀疏分块。
### 输出
初始5,283 clusters；去噪后5,200 clusters/4,041,289 cells。
### 核心步骤
1. HVG/PCA抽样。2. KNN-Jaccard图。3. Leiden递归细分。4. DEG判据停止/合并。
### 关键参数（本文设置）
|参数|值|含义|
|---|---|---|
|版本|v0.0.5|大规模聚类|
|parquet bin|50,000 cells×500 genes|磁盘分块|
|10xv2 q1/q.diff/de.score/min|0.4/0.7/150/10|聚类DEG阈值|
|10xv3|0.5/0.7/150/4|聚类DEG阈值|

## 名词/参数/指标
|名词|定义|
|---|---|
|Binary DEG|表达比例、|log2FC|>1、adj P<0.01及比例差标准共同定义|
|Jaccard–Leiden|共享邻居图聚类|

## 复现
- https://github.com/AllenInstitute/scrattch.bigcat；Arrow v12.0.1
- `iter_clust_big(..., de.score.th=150)`

## 生物学意义
提供全脑细胞类型分辨率；抽样和阈值可能低估稀有类型。

## 涉及 Figures
- **Fig. 1**；Extended Data Fig. 1,4
