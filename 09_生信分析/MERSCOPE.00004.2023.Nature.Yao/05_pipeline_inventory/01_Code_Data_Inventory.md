# 代码与数据清单 — Mouse Brain Cell Atlas

## 一、代码清单
|资源|URL|许可证|备注|
|---|---|---|---|
|scrattch.bigcat|https://github.com/AllenInstitute/scrattch.bigcat|GitHub（许可证以仓库为准）|聚类、DEG、imputation|
|scrattch.mapping|https://github.com/AllenInstitute/scrattch.mapping|GitHub（许可证以仓库为准）|层级映射，v0.2|
|ABC atlas access|https://github.com/AllenInstitute/abc_atlas_access|GitHub|数据访问说明|
|cirrocumulus|https://cirrocumulus.readthedocs.io/en/latest/|开源|taxonomy可视化|

## 二、数据清单
|数据类型|存储位置|访问号/URL|说明|
|---|---|---|---|
|AIBS 10x FASTQ|NeMO|https://assets.nemoarchive.org/dat-qg7n1b0|scRNA-seq原始数据|
|10x scRNA-seq|GEO|GSE246717|亦见BioProject PRJNA1030397|
|10x scRNA-seq|BioProject|PRJNA1030397|测序数据|
|AIBS MERFISH|Brain Image Library|https://doi.org/10.35077/g.610|MERSCOPE空间数据|
|处理数据说明|ABC atlas|https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas|在线浏览scRNA/snRNA/MERFISH|
|MERFISH处理访问|GitHub|https://github.com/AllenInstitute/abc_atlas_access/blob/main/descriptions/MERFISH-C57BL6J-638850.md|下载说明|

## 三、复现可行性
|分析|状态|说明|
|---|---|---|
|scRNA比对/QC|✅ 可完全复现|FASTQ、参考和CellRanger流程公开；CellRanger需软件获取|
|聚类/DEG/映射|✅ 可完全复现|scrattch.bigcat与scrattch.mapping公开|
|MERFISH解码/成像|⚠️ 部分受限|原始空间数据公开，但Vizgen软件/仪器流程含商业组件|
|Cellpose分割|✅ 可完全复现|算法公开，需原始DAPI/PolyT图像|
|CCFv3配准/空间统计|✅ 可完全复现|ANTS、DescTools、vegan及CCFv3公开|
|实验取样|❌ 无法直接复现|需小鼠、MERSCOPE仪器及探针面板|
