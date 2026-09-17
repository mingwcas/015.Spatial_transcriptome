# 四维度生信分析报告 — Open-ST 3D TME Multimodal Profiling

> **论文**：Combining spatial transcriptomics and ECM imaging in 3D for mapping cellular interactions in the tumor microenvironment
> **DOI**：10.1016/j.cels.2025.101261
> **期刊**：Cell Systems (2025)
> **平台**：CosMx Spatial Molecular Imager (NanoString) + SHG
> **完成日期**：2025

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 空间转录组数据采集 | CosMx 1000-plex RNA ISH | CosMx SMI (NanoString) | 960基因，340,644细胞，155M转录本 |
| H&E组织分割 | 深度学习语义分割 | U-Net + ResNet101 | F1≈0.93，自动识别肿瘤/基质/正常区域 |
| 单细胞聚类 | 无监督SNN聚类 | Seurat v4.0.4, SCTransform | 24聚类→18种细胞类型 |
| 参考图谱整合 | Label transfer | Seurat v4.0.4 | 与健康肺和NSCLC scRNA-seq图谱一致 |
| 3D配准 | SIFT特征+全局优化 | STIM v0.2.0 | 中位配准精度42μm |
| 2D/3D邻域分析 | 空间邻域构建+聚类 | 自定义Python + Seurat | 10种多细胞niche，200,000+邻域 |
| 细胞间通讯 | 受体-配体空间活性评分 | CellChat + 自定义脚本 | 164配体轴，96个niche富集配体 |
| ECM成像 | 二次谐波生成(SHG) | Zeiss LSM 880 NLO | 胶原/弹性蛋白定量，3个ECM区室 |
| 成纤维细胞亚聚类 | 无监督聚类 | Seurat v4.0.4 | 6种转录组状态 |
| 肿瘤伪时间 | Pseudotime轨迹推断 | Slingshot v2.2.1 | EMT动态，EMT niche鉴定 |
| 免疫荧光验证 | 多重IF + 图像配准 | Zeiss Axioscan7, wsireg 0.3.7 | 蛋白水平验证 |
| 3D渲染 | 体素插值+可视化 | ParaView v5.10 | 3D niche和基因表达可视化 |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|---|---------|------------|
| Fig. 1 | 实验设计、ROI选择、18种细胞类型鉴定、参考图谱验证 | UMAP、空间图、H&E对照 |
| Fig. 2 | 3D邻域设计、10种多细胞niche鉴定、niche与病理标注对应 | 3D图、UMAP、热图、空间对照 |
| Fig. 3 | 2D vs 3D邻域比较、树突状细胞niche仅3D可检、T细胞niche连续性 | 分布图、alluvial图、3D渲染 |
| Fig. 4 | Niche特异性配体分析、树突状细胞niche免疫检查点通讯网络 | 热图、3D渲染、dotplot、示意图 |
| Fig. 5 | SHG ECM成像、3个ECM区室、6种成纤维细胞表型与ECM关联 | SHG图、散点图、UMAP、boxplot、3D渲染 |
| Fig. 6 | 肿瘤浸润、EMT伪时间、EMT niche鉴定、ECM硬度与EMT关系 | 3D渲染、UMAP、boxplot、空间图 |
| Fig. 7 | EMT niche分子标志物、伤口愈合样通讯网络、整合素信号汇聚 | 散点图、3D渲染、示意图 |
| ED Fig. S1-S7 | 数据质量、3D配准、通讯分析、ECM验证等补充数据 | 各类补充图 |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|-----|------|------|----------|
| 空间转录组采集 | CosMx SMI | — | 商业 (NanoString) |
| 细胞分割 | Cellpose | — | 开源 |
| 单细胞分析 | Seurat | v4.0.4 | 开源 |
| 归一化 | SCTransform | — | 开源 (Seurat内置) |
| 3D配准 | STIM | v0.2.0 | 开源 |
| 通讯分析 | CellChat | — | 开源 |
| 伪时间分析 | Slingshot | v2.2.1 | 开源 |
| SHG成像 | Zeiss LSM 880 NLO | — | 商业 (Zeiss) |
| IF扫描 | Zeiss Axioscan7 | — | 商业 (Zeiss) |
| IF拼接 | ASHLAR | v1.17.0 | 开源 |
| IF配准 | wsireg | v0.3.7 | 开源 |
| 3D可视化 | ParaView | v5.10 | 开源 |
| H&E分割 | U-Net + ResNet101 | — | 开源 (PyTorch) |
| 降维/可视化 | UMAP | — | 开源 |
| 图像处理 | Fiji | v1.53t | 开源 |
| 统计/可视化 | R (ggplot2, ggpubr) | v4.1 | 开源 |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| U-Net + ResNet101 | 深度学习语义分割 | H&E全切片组织区域自动识别 |
| SCTransform | 统计归一化 | 单细胞基因表达归一化和方差稳定 |
| SIFT (STIM内) | 计算机视觉特征匹配 | 3D切片对齐的特征点匹配 |
| Convolutional Wasserstein barycenters | 最优传输插值 | 3D体素数据中间层插值 |
| Slingshot | 伪时间轨迹推断 | 肿瘤细胞EMT轨迹重建 |
| CellChat | 细胞通讯推断 | 受体-配体相互作用数据库 |
| k-means | 无监督聚类 | ECM区室鉴定 |
| SNN + Louvain | 图聚类 | 细胞类型和niche聚类 |

## 局限性与利益冲突

**局限性**：
1. 单个患者样本（proof-of-principle），非大队列验证
2. 960基因预设panel，非全转录组无偏检测
3. 3D邻域定义（50μm半径、30μm切片间距）为经验参数，最优值可能因组织/样本而异
4. FFPE样本DV200=60%，RNA质量中等
5. 通讯分析基于转录本共检测，不能直接证明蛋白水平的相互作用

**利益冲突**：
- S.S. 是 Aignostics 顾问；L.R. 和 G.D. 是 Aignostics 员工
- S.M., M.G., Y.L. 是 NanoString Technologies 现任/前任员工和股东
- F.K. 是 Aignostics 联合创始人和顾问
- 部分作者与 NanoString (CosMx 平台厂商) 有利益关系
