# 四维度生信分析报告 — Stereo-seq V2

> 论文:Stereo-seq V2: Spatial mapping of total RNA on FFPE sections with high resolution
> DOI: https://doi.org/10.1016/j.cell.2025.08.008
> 平台: Stereo-seq (STOmics)
> 完成日期: 2025

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 芯片制备 | Chip N preparation | Exonuclease I处理 | 改造Chip T产生新捕获探针 |
| FFPE文库构建 | Stereo-seq FFPE library | Random primer捕获 | 5μm切片，95°C去交联，0.01μM dimer |
| 新鲜冷冻文库 | Stereo-seq FF library | Tn5片段化 | 10μm切片，13 cycles PCR |
| 原始数据处理 | SAW pipeline | STOmics | CID/UMI解析，STAR比对，MAPQ>10 |
| 边界检测 | Boundary detection | SpaceFlow + Spateo + OpenCV | 400μm扩展，10μm/层 |
| 分子扩散分析 | Molecule diffusion | Numpy convolve | LWHM量化，V2比V1扩散更少 |
| 基因体覆盖分析 | Gene body coverage | RseQC | V2均匀覆盖，V1/Visium 3'偏倚 |
| 空间聚类 | Spatial clustering | scVI + Leiden | 30邻域平滑，PCA降维 |
| 细胞分割 | Cell segmentation | Spateo | unspliced RNA信号，Gaussian blur，Watershed |
| 细胞类型注释 | Cell type annotation | Scanpy + marker genes | Leiden聚类，MERFISH标签转移 |
| CNV分析 | inferCNV | infercnvpy v0.5.0 | lfc_clip=3, window=250 |
| 空间可变剪接 | Alternative splicing | rMATS-turbo v4.3.0 | FDR≤0.05，5种AS类型 |
| Mtb基因组比对 | Mtb mapping | SAW + 拼接参考基因组 | Mtb ASM19595v2 + mm10 |
| 空间自相关模块 | Gene modules | Hotspot | FDR<0.01, k=30 |
| GO富集 | GO enrichment | Metascape | 感染/免疫相关通路 |
| BCR库组装 | BCR repertoire | MIXCR v4.5.0 | 物种mmu/hsa, ST_BarcodeMap |
| BCR-Mtb共定位 | Colocalization | Scipy KDTree | UMI>1过滤，NNS |
| CDR3聚类 | CDR3 clustering | Levenshtein + ClustalW | 距离<7, 层次聚类 |
| 染色图像分析 | Image analysis | U-Net | Mtb阳性区域自动识别 |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|---------|------------|
| Fig.1 | Stereo-seq V2分子扩散性能 | 散点图、线图、柱状图 |
| Fig.2 | 小鼠脑单细胞分辨率分析 | 空间可视化、Venn图、热图 |
| Fig.3 | 全基因体覆盖分析 | 折线图、饼图、柱状图、热图 |
| Fig.4 | 临床FFPE样本分析(TNBC) | H&E图像、回归图、热图 |
| Fig.5 | 肿瘤相关可变剪接事件 | 火山图、 sashimi图、热图 |
| Fig.6 | 宿主-Mtb转录组同时捕获 | 点图、空间可视化、柱状图 |
| Fig.7 | BCR克隆动态变化 | KDE图、散点图、Venn图、箱线图 |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 原始数据处理 | SAW pipeline | - | 商业(STOmics) |
| 比对 | STAR | v1.11 | 开源 |
| 质量控制 | RseQC | v5.0.1 | 开源 |
| 单细胞分析 | Scanpy | v0.10.7 | 开源 |
| 降维 | scVI | - | 开源 |
| 空间分割 | SpaceFlow | - | 开源 |
| 空间分析 | Spateo | v1.1.0 | 开源 |
| CNV分析 | infercnvpy | v0.5.0 | 开源 |
| 可变剪接 | rMATS-turbo | v4.3.0 | 开源 |
| 免疫 repertoire | MIXCR | v4.5.0 | 开源 |
| 数据可视化 | matplotlib/seaborn | v3.7.1/v0.12.2 | 开源 |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| SpaceFlow | 深度学习(空间正则化) | 空间分割与边界检测 |
| U-Net | 深度学习(图像分割) | 抗酸染色图像中Mtb区域识别 |
| scVI | 变分推断 | 批次效应校正与降维 |
| Leiden算法 | 图聚类 | 细胞/空间域聚类 |
| Hotspot | 空间自相关分析 | 空间基因模块鉴定 |
| inferCNV | 拷贝数推断 | 恶性/正常细胞区分 |
| rMATS-turbo | 统计模型 | 可变剪接事件检测 |
| KDTree | 空间最近邻搜索 | BCR克隆与感染区域共定位 |
| Gaussian blur + OTSU + Watershed | 图像分割 | 细胞分割 |
| Levenshtein distance + hierarchical clustering | 序列分析 | CDR3相似性聚类 |

## 局限性与利益冲突说明

1. **厂商论文**：作者来自BGI Research和STOmics，可能存在利益冲突
2. **商业产品依赖**：Stereo-seq芯片和试剂盒为商业产品（STOmics）
3. **技术局限**：DV200极低(<18)的样本性能未知；需要足够cDNA产量
4. **样本量**：TNBC样本n=10，Mtb感染小鼠模型n=3-10
5. **无配对对照**：部分分析缺少直接对照
