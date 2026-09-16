# Method: MERSCOPE解码、细胞分割与scRNA映射

## 原文（Methods）
> Raw MERSCOPE data were decoded using Vizgen software (v231). Cell segmentation ... based on DAPI and PolyT staining using Cellpose. ... volume >100 µm3 and <3,000 µm3, at least 15 genes detected and ... 40 but no more than 3,000 mRNA molecules.

## 解读
### 意义
从空间成像获得单细胞表达并映射到scRNA taxonomy。
### 输入
59张200 µm间隔冠状切片；500-gene panel；DAPI/PolyT；10xv3参考。
### 输出
约4.3M QC细胞；cluster标签和空间坐标。
### 核心步骤
1. Vizgen v231解码。2. Cellpose在第4/7 z层分割并传播边界。3. 体积、基因数、mRNA过滤。4. 共享基因cluster centroid相关性最近邻映射，80% marker bootstrap。
### 关键参数（本文设置）
|参数|值|含义|
|---|---|---|
|体积|100–3,000 µm³|质量范围|
|检测基因|≥15|最低基因数|
|mRNA|40–3,000|去除低质/双细胞|
|bootstrap|80% marker|稳健映射|

## 名词/参数/指标
|名词|定义|
|---|---|
|Cellpose|DAPI/PolyT细胞分割算法|
|映射标签|最近scRNA cluster centroid的标签|

## 复现
- Vizgen MERSCOPE；Cellpose；https://github.com/AllenInstitute/scrattch.mapping
- `map_cells_knn_big(query, reference, marker_genes)`

## 生物学意义
将转录身份置于全脑空间；分割错误和邻近污染限制精度。

## 涉及 Figures
- **Fig. 1–6**；Extended Data Fig. 2,7,8
