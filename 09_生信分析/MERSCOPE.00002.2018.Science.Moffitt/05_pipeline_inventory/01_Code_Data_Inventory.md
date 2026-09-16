# 代码与数据清单 — 下丘脑视前区 MERFISH 图谱

> 论文：Moffitt et al., Science 362, eaau5324 (2018) | DOI: [10.1126/science.aau5324](https://doi.org/10.1126/science.aau5324)

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| MERFISH analysis | https://github.com/ZhuangLab/MERFISH_analysis | 见仓库 | Zhuang Lab 公开分析代码 |
| GEO | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE113576 | 数据库条款 | scRNA-seq 数据 |
| Allen Brain Atlas | https://mouse.brain-map.org | 公开资源条款 | 核团边界与解剖定位参考 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| preoptic region scRNA-seq | GEO | GSE113576 | ~31,000 cells；Drop-seq 改良平台 |
| MERFISH 原始/处理数据 | Dryad | https://doi.org/10.5061/dryad.8t8s248 | 视前区 155-gene MERFISH 数据 |
| MERFISH code / pipeline | GitHub | https://github.com/ZhuangLab/MERFISH_analysis | 图像解码与分析生态 |
| 补充表 S1–S11 | Science Supplementary | https://science.sciencemag.org/content/362/6416/eaau5324/suppl/DC1 | cluster、marker、跨平台对应等 |
| Allen mouse brain reference | Allen Institute | https://mouse.brain-map.org | 解剖核团与 marker 空间定位 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| scRNA-seq 聚类与 marker 分析 | ✅ 可完全复现 | GEO GSE113576 公开；需按补充材料重建预处理细节 |
| MERFISH 表达矩阵与 cluster 对应 | ✅ 可完全复现 | Dryad 数据与分析代码公开 |
| 155-gene panel 设计复核 | ✅ 可完全复现 | 主文给出 135+20 组成；完整面板见补充材料 |
| 空间核团分布分析 | ⚠️ 部分受限 | 需 Dryad 空间坐标、切片 landmark 与 Allen Atlas 对齐参数 |
| cFos 行为激活统计 | ⚠️ 部分受限 | 数据公开，但行为动物切片较少（4 slices/animal），需补充材料的原始计数 |
| ISH 正交验证 | ❌ 无法直接复现 | 需原始脑组织、16 μm 切片、定制探针与成像实验 |
| MERFISH 实验 | ❌ 无法直接复现 | 需专用多轮杂交成像系统、155 基因探针与组织样本 |

**状态说明**：
- ✅ 可完全复现（工具/代码开源可获取）
- ⚠️ 部分受限（需注册/需商业许可）
- ❌ 无法直接复现（需原始样本/仪器）
