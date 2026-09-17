# 四维度生信分析报告 — Spatial-CITE-seq

> **论文**：High-plex protein and whole transcriptome co-mapping at cellular resolution with spatial CITE-seq  
> **期刊**：Nature Biotechnology, Volume 41, October 2023, 1405–1409  
> **DOI**：10.1038/s41587-023-01676-0  
> **平台**：DBiT-seq (Deterministic Barcoding in Tissue)  
> **完成日期**：2025-01

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 空间条码标记 | 微流控确定性条码（50×50网格） | 自制PDMS芯片 | 25 µm像素，2500个空间位置 |
| 蛋白质检测 | ADT（抗体衍生标签）测序 | BioLegend ADT cocktails | 人273-plex / 小鼠189-plex |
| 转录组比对 | STAR比对 | ST Pipeline v1.7.2 | 比对到GRCm38/GRCh38 |
| ADT计数 | UMI去重计数 | CITE-seq-Count v1.4.2 | 蛋白质表达矩阵 |
| 蛋白质标准化 | CLR变换 | Seurat v3.2 | 蛋白质聚类 |
| 转录组标准化 | SCTransform | Seurat v3.2 | 转录组聚类 |
| 聚类分析 | Louvain聚类 + UMAP | Seurat v3.2 | 7-10个空间域 |
| 多模态整合 | 加权最近邻（WNN） | Seurat v3.2 | RNA/蛋白质模态权重 |
| 空间-单细胞整合 | Label transfer | Seurat v3.2 | 细胞类型空间映射 |
| 空间去卷积 | SPOTlight | SPOTlight R包 | 细胞比例估计 |
| 批量相关性 | Pearson相关 | R | R = 0.78（spatial vs scCITE-seq） |
| 验证成像 | CODEX / COMET FFeX | PhenoCycler / Lunaphore | 6种蛋白免疫荧光验证 |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|-------------|
| Fig. 1a | Spatial-CITE-seq工作流程示意图 | 流程图/示意图 |
| Fig. 1b | 小鼠4种组织的189-plex蛋白质和转录组聚类 | 空间聚类图 |
| Fig. 1c-d | 人扁桃体映射区域和数据质量 | 明场图 + 直方图 |
| Fig. 1e-h | 人扁桃体273蛋白和转录组的UMAP及空间聚类 | UMAP + 空间图 |
| Fig. 1i | 差异表达蛋白热图 | 热图 |
| Fig. 1j | 组织图像与蛋白质聚类叠加 | 叠加图 |
| Fig. 1k-o | 单个蛋白质标记物的空间表达 | 空间表达图 |
| Fig. 2a | 皮肤活检明场图像 | 明场图 |
| Fig. 2b-c | 基因计数和转录组聚类 | 空间热图/聚类图 |
| Fig. 2d-f | 273蛋白质聚类和空间分布 | UMAP + 空间图 |
| Fig. 2g | scRNA-seq和空间转录组整合 | UMAP |
| Fig. 2i | 功能基因空间可视化 | 空间表达图 |
| Fig. 2j-n | Tph细胞鉴定和空间分布 | 差异表达 + 空间图 |
| ED Fig. 1 | ADT结构和详细工作流程 | 示意图 |
| ED Fig. 2 | 小鼠4组织数据质量 | 热图 + 箱线图 + 饱和度曲线 |
| ED Fig. 3 | COMET免疫荧光验证 | 荧光图像 |
| ED Fig. 4 | 与scCITE-seq和免疫荧光比较 | 散点图 + UMAP |
| ED Fig. 5 | 人脾和胸腺空间映射 | 空间图 + 热图 |
| ED Fig. 6 | 皮肤活检数据详情 | 空间热图 |
| ED Fig. 7 | scRNA-seq和去卷积分析 | UMAP + 饼图 |
| ED Table 1 | 基因和蛋白质计数汇总 | 表格 |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|-----------|
| 微流控芯片制备 | AutoCAD + PDMS | 2021 | 商业（设计）/自制（芯片） |
| DNA寡核苷酸合成 | IDT | — | 商业 |
| ADT抗体鸡尾酒 | BioLegend | cat. 99502/99833 | 商业 |
| 组织固定/染色 | 标准协议 | — | — |
| 原位逆转录 | Maxima H Minus RT | Thermo Fisher | 商业 |
| 原位连接 | T4 DNA Ligase | NEB | 商业 |
| cDNA纯化 | Zymo DNA kit + Streptavidin beads | ZD4014 / Invitrogen | 商业 |
| 文库构建 | Nextera XT | Illumina FC-131-1024 | 商业 |
| 测序 | NovaSeq 6000 | Illumina | 商业 |
| Read格式化 | 自定义Python脚本 | — | 自定义 |
| mRNA比对 | STAR | — | 开源 |
| mRNA处理 | ST Pipeline | v1.7.2 | 开源 |
| ADT计数 | CITE-seq-Count | v1.4.2 | 开源 |
| 聚类/可视化 | Seurat | v3.2 | 开源 |
| 热图绘制 | ggplot2 | — | 开源 |
| 去卷积 | SPOTlight | — | 开源 |
| 单细胞制备 | 10x Genomics Chromium | 5' Kit v1.1 | 商业 |
| 验证成像 | PhenoCycler / COMET | — | 商业 |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| SCTransform | 正则化负二项回归 | 转录组数据标准化 |
| CLR变换 | 居中对数比 | 蛋白质数据标准化 |
| Louvain聚类 | 图社区检测 | 空间域识别 |
| UMAP | 非线性降维 | 高维数据可视化 |
| Seurat Integration | 锚点整合 | 多数据集/多模态整合 |
| WNN (Weighted Nearest Neighbor) | 多模态学习 | RNA和蛋白质模态权重学习 |
| Label transfer | 监督学习 | 细胞类型注释转移 |
| SPOTlight | NMF回归 | 空间去卷积 |
| STAR | RNA-seq比对 | 读段基因组定位 |
