# 四维度生信分析报告 — Spatial-ATAC-Hi-C

> **论文**: Spatial chromatin architecture and accessibility co-profiling of mammalian tissues  
> **DOI**: 10.1038/s41592-026-03217-4  
> **平台**: Spatial-ATAC-Hi-C (基于DBiT-seq的微流控空间多组学技术)  
> **期刊**: Nature Methods | 2026 | 第一作者: Wang  
> **完成日期**: 2026

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 原始数据质控 | Adapter trimming, 质量过滤 | TrimGalore v0.6.10 | 去除低质量序列和接头污染 |
| 序列比对 | 短读长比对到参考基因组 | BBMap v39.01 | 高效定位测序reads |
| ATAC-seq处理 | 单细胞ATAC数据处理 | Cell Ranger ATAC v2.0 | 生成染色质可及性矩阵 |
| Hi-C数据处理 | 空间Hi-C配对数据处理 | runHiC pipeline, pairtools v0.3.0 | 构建空间分辨的3D基因组互作图谱 |
| 染色质可及性分析 | 单细胞ATAC降维、聚类、可视化 | ArchR | 识别细胞类型特异性开放染色质区域 |
| 多组学整合 | 多模态数据整合与聚类 | Seurat v5.1.0, SnapATAC2 v2.6.4 | 神经元vs非神经元细胞群的染色质状态差异 |
| 3D基因组聚类 | 单细胞Hi-C接触图谱聚类 | ScHiCluster v1.3.5 | 识别空间分辨的3D基因组结构变异 |
| 多尺度3D基因组分析 | 染色质域、区室、环检测 | Higashi, cooltools | 揭示组织特异性拓扑结构域 |
| 染色质环检测 | Hi-C互作环识别 | Peakachu | 鉴定增强子-启动子互作 |
| 结构变异检测 | 基因组结构变异识别 | NeoLoopFinder, EagleC | 检测空间分辨的SVs和CNVs |
| 拷贝数变异检测 | 基因组拷贝数变异分析 | Delly, Lumpy | 发现肿瘤组织中的CNVs |
| 数据平滑/插补 | 空间数据降噪 | MAGIC | 提高空间信号的信噪比 |
| 组织病理学分析 | H&E图像分析与细胞分割 | QuPath v0.6.0 | 配合空间条形码的组织学注释 |
| 空间条形码处理 | 微流控芯片条形码映射 | AtlasXbrowser | 将测序数据映射到组织空间坐标 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|---|---------|-------------|
| Fig. 1 | Spatial-ATAC-Hi-C技术原理与实验流程 | 示意图、微流控芯片示意图 |
| Fig. 2 | 小鼠脑组织空间染色质可及性图谱 | 空间散点图、UMAP、热图 |
| Fig. 3 | 人脑组织3D基因组空间结构 | 接触矩阵、TADs、A/B区室分布图 |
| Fig. 4 | 神经元与非神经元细胞的染色质状态比较 | 火山图、基因组浏览器截图 |
| Fig. 5 | GBM和星形细胞瘤样本的CNVs/SVs检测 | 拷贝数图谱、结构变异环形图 |
| Fig. 6 | 空间分辨的3D基因组改变与肿瘤异质性 | 空间热图、变异频率分布 |
| Fig. 7 | 技术验证与重复性评估 | 相关性散点图、重复性箱线图 |
| Supp. | 数据质量、参数优化、额外验证 | QC统计图、基准比较图 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 质控 | TrimGalore | v0.6.10 | 开源 (GPL-3.0) |
| 比对 | BBMap | v39.01 | 开源 (BSD-3) |
| ATAC处理 | Cell Ranger ATAC | v2.0 | 商业 (10x Genomics) |
| Hi-C处理 | runHiC pipeline | - | 开源 |
| Hi-C配对 | pairtools | v0.3.0 | 开源 (MIT) |
| ATAC分析 | ArchR | - | 开源 (MIT) |
| 多组学整合 | Seurat | v5.1.0 | 开源 (GPL-3.0) |
| ATAC分析 | SnapATAC2 | v2.6.4 | 开源 (MIT) |
| Hi-C聚类 | ScHiCluster | v1.3.5 | 开源 |
| 3D基因组分析 | Higashi | - | 开源 (MIT) |
| 基因组分析 | cooltools | - | 开源 (MIT) |
| 环检测 | Peakachu | - | 开源 |
| SV检测 | NeoLoopFinder | - | 开源 |
| SV检测 | EagleC | - | 开源 |
| CNV检测 | Delly | - | 开源 (GPL-2.0) |
| CNV检测 | Lumpy | - | 开源 (MIT) |
| 数据平滑 | MAGIC | - | 开源 (Apache-2.0) |
| 病理分析 | QuPath | v0.6.0 | 开源 (GPL-3.0) |
| 条形码映射 | AtlasXbrowser | - | 开源 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| ScHiCluster | 无监督聚类算法 | 单细胞Hi-C接触图谱的细胞类型聚类 |
| Higashi | 图神经网络/张量分解 | 多尺度3D基因组特征提取与细胞特异性分析 |
| MAGIC | 流形学习/数据插补 | 稀疏空间组学数据的降噪与信号恢复 |
| Peakachu | 机器学习分类器 | 染色质环（chromatin loops）的从头检测 |
| EagleC | 深度学习模型 | 基于Hi-C数据的拷贝数变异和结构变异检测 |
| NeoLoopFinder | 计算算法 | 检测与结构变异相关的新型染色质环 |
| ArchR | 降维/聚类框架 | 单细胞ATAC-seq数据的低维表示与细胞类型注释 |
| Seurat | 多组学整合框架 | 多模态单细胞数据的加权最近邻分析 |

---

*报告生成日期：2026*
