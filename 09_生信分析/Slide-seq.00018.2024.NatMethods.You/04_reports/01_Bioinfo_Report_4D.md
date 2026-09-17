# 四维度生信分析报告 — Slide-seq空间转录组方法比较

> 论文信息：Systematic comparison of sequencing-based spatial transcriptomic methods
> DOI: https://doi.org/10.1101/2023.12.03.569744
> 平台：Slide-seq / 多种sST平台比较
> 完成日期：2024

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 数据预处理 | 统一预处理管道 | scPipe v2.0.0 | 支持多平台数据统一处理 |
| Visium分析 | 空间转录组分析 | SpaceRanger v2.1.0 | 生成spot-by-gene矩阵 |
| BMKMANU分析 | 条码珠阵列分析 | BSTMatrix v2.3.j | 处理图案化阵列数据 |
| Stereo-seq分析 | 纳米球技术分析 | SAW v6.1 | 高灵敏度数据处理 |
| 聚类分析 | 转录组聚类 | Seurat v4.3.0 | 最稳定鲁棒的聚类方法 |
| 空间聚类 | 空间感知聚类 | DR.SC v3.3 | 联合降维和聚类 |
| 空间聚类 | 概率嵌入聚类 | PRECAST v1.6.2 | 整合空间信息 |
| 差异表达 | 标记基因检测 | FindMarkers (Wilcoxon) | 跨平台一致性较低 |
| 细胞通讯 | 配体-受体分析 | CellChat v1.6.1 | 无一致结果 |
| 细胞通讯 | 配体-受体分析 | CellPhoneDB v4 | 无一致结果 |
| 验证实验 | 原位杂交 | ExSeq简化版 | 验证标记基因表达 |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|--------------|
| Fig. 1 | 实验设计和数据处理流程概述 | 流程图 + 组织图像 |
| Fig. 2 | 六种sST平台灵敏度比较 | 饱和曲线 + 散点图 + 热图 |
| Fig. 3 | 分子横向扩散比较 | 表达模式图 + 密度曲线 + LWHM箱线图 |
| Fig. 4 | 下游性能：聚类、标记基因检测 | t-SNE/UMAP + 热图 + Upset图 |
| Fig. 5 | 六种sST方法总结和排名 | 排名表格 + 特征概述 |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|-----------|
| 数据获取 | 各平台官方pipeline | - | 混合 |
| 统一预处理 | scPipe | v2.0.0 | 开源 (Bioconductor) |
| 序列比对 | STAR | 2.7.10b | 开源 |
| Visium处理 | SpaceRanger | v2.1.0 | 商业 (10X Genomics) |
| BMKMANU处理 | BSTMatrix | v2.3.j | 商业 (BMKGENE) |
| Stereo-seq处理 | SAW | v6.1 | 商业 (华大基因) |
| 聚类分析 | Seurat | v4.3.0 | 开源 |
| 空间聚类 | DR.SC | v3.3 | 开源 |
| 空间聚类 | PRECAST | v1.6.2 | 开源 |
| 细胞通讯 | CellChat | v1.6.1 | 开源 |
| 细胞通讯 | CellPhoneDB | v4 | 开源 |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| Seurat聚类 | KNN + 层次聚类 | 单细胞/空间数据聚类 |
| DR.SC | 联合降维和空间聚类 | 空间感知聚类 |
| PRECAST | 概率嵌入 + 聚类 | 空间数据整合 |
| Wilcoxon秩和检验 | 非参数统计 | 差异表达分析 |
| LWHM | 半峰宽度量 | 分子扩散定量 |
| ECA/ECP | 熵度量 | 聚类质量和一致性评估 |
| CellChat | 配体-受体推断 | 细胞通讯网络分析 |
| CellPhoneDB | 配体-受体推断 | 细胞通讯分析 |

## 局限性说明

1. **参考组织选择局限**：对小鼠眼球发育的认知仍有限，难以构建完全准确的ground truth
2. **平台特异性偏好**：每个平台都有独特和共享的标记基因，跨平台比较存在挑战
3. **细胞通讯分析不稳定**：CellChat和CellPhoneDB均未产生一致结果
4. **空间感知方法优势不明显**：DR.SC和PRECAST并不总是优于传统Seurat
5. **DBiT-seq数据差异**：E10胚胎眼球数据与其他E12.5数据不完全可比
