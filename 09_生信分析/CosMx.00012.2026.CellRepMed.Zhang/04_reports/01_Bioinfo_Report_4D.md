# 四维度生信分析报告 — CosMx_SCLC_TME_Heterogeneity

> 论文信息
> - 论文标题：Single-cell spatial transcriptomics reveals tumor microenvironment heterogeneity in primary and lymph node-metastatic small cell lung cancer
> - DOI: https://doi.org/10.1016/j.xcrm.2026.102713
> - 平台: CosMx Spatial Molecular Imager (SMI)
> - 期刊: Cell Reports Medicine (2026)
> - 完成日期: 2026-04-21

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 空间转录组数据获取 | CosMx SMI 1,000-plex panel | Bruker Spatial Biology, AtoMx SIP v1.3 | 604,230 cells, 294M transcripts, 384 FOVs |
| 细胞分割 | Cellpose预训练神经网络 | AtoMx SIP整合 | DAPI/PanCK/CD45/CD68/B2M/CD298信号 |
| 批次效应校正 | Harmony | v1.0 | Top 50 PCs校正 |
| 降维聚类 | PCA + UMAP + Graph-based clustering | Seurat v5.1.0 | 分辨率0.8，共13个恶性亚群 |
| 细胞类型注释 | Canonical markers + CellMarker 2.0 | 手动注释 | 4 compartments, 7 broad cell types |
| 组织分布偏好 | Ro/e分析 | Fisher精确检验 | C5/C6/C9特异富集于LNMT |
| 差异表达分析 | FindAllMarkers | log2FC>1, adj.p<0.001 | C5: 5 DEGs, C6: 28 DEGs, C9: 7 DEGs |
| 通路富集分析 | GO/KEGG富集 | clusterProfiler v4.8.3 | 细胞迁移、代谢重编程、NF-κB通路 |
| 空间相互作用分析 | 置换检验 | 6μm阈值, 1000次置换 | Fisher combined probability test |
| 配体-受体分析 | CellChat | v1.6.1 | p<0.01显著性 |
| 细胞邻里分析 | MiniBatchKMeans | ClusterR v1.3.3 | PT:11 CNs, PT-LNM:13 CNs, LNMT:15 CNs |
| 公共数据整合 | Seurat CCA | v5.1.0 | 多器官转移验证 |
| 生存分析 | Kaplan-Meier + Cox回归 | survival v3.5-7 | PIHs-1独立预后因素 |
| 单样本GSEA | ssGSEA | GSVA v2.0.7 | 20-gene PIHs-1 signature |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|--------------|
| Fig. 1 | CosMx SMI工作流和604,230单细胞图谱建立 | UMAP, Bar plot, Spatial maps |
| Fig. 2 | 13个恶性细胞亚群及C5/C6/C9 LN转移相关亚群 | UMAP, Heatmap, mIF images |
| Fig. 3 | T细胞(6亚群)和B细胞(4亚群)免疫景观重编程 | UMAP, Stacked bar, Lollipop plot, Venn diagram |
| Fig. 4 | 细胞空间相互作用/回避及血管-免疫niche重编程 | Heatmap, Boxplot |
| Fig. 5 | CN分析与PIHs-1预后价值 | Voronoi diagram, Forest plot, Kaplan-Meier |
| Fig. S1-S4 | 方法验证和C5/C6/C9特异性验证 | Various |
| Fig. S5-S6 | 免疫细胞亚群详细分析 | Various |
| Fig. S7-S10 | Extended interaction analysis | Various |
| Fig. S11-S12 | CN验证和预后signature验证 | Various |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|------------|
| 空间成像 | CosMx SMI | - | 商业 (Bruker Spatial Biology) |
| 图像处理 | AtoMx Spatial Informatics Platform | v1.3 | 商业 |
| 细胞分割 | Cellpose | 预训练模型 | 开源 |
| 批次校正 | Harmony | v1.0 | 开源 (MIT) |
| 单细胞分析 | Seurat | v5.1.0 | 开源 (Seurat) |
| 通路富集 | clusterProfiler | v4.8.3 | 开源 (Bioconductor) |
| 细胞间通信 | CellChat | v1.6.1 | 开源 (MIT) |
| 聚类 | ClusterR | v1.3.3 | 开源 (GPL-3) |
| 双细胞检测 | DoubletFinder | v2.0.6 | 开源 (MIT) |
| 生存分析 | survival | v3.5-7 | 开源 (GPL-2) |
| 病理分析 | QuPath | v0.5.1 | 开源 (Apache 2.0) |
| 多重荧光 | Vectra Polaris | - | 商业 (AKOYA) |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| Cellpose | 深度学习(卷积神经网络) | 单细胞图像分割 |
| Harmony | 批次效应校正算法 | 整合多样本数据 |
| UMAP | 非线性降维 | 单细胞数据可视化 |
| Seurat FindClusters | 图聚类算法 | 细胞类型分群 |
| MiniBatchKMeans | 聚类算法 | 细胞邻里分析 |
| ssGSEA | 基因集富集分析 | PIHs-1 signature评分 |
| Kaplan-Meier | 生存分析 | 生存曲线估计 |
| Cox比例风险模型 | 回归模型 | 多变量预后分析 |
| Fisher精确检验 | 统计检验 | 富集显著性 |
| Spearman相关 | 等级相关 | 表达相关性 |

## 局限性

1. **平台局限性**：CosMx 1,000-plex panel基因覆盖有限，限制了发现新生物学程序的能力；未来可采用CosMx 6K或Xenium 5K获得更全面的转录组覆盖
2. **样本局限性**：仅聚焦于淋巴结转移，未涵盖脑、肝、骨等内脏转移；淋巴结特异的TME可能不适用于其他转移位点
3. **分割算法**：尽管使用Cellpose和严格质控，高度 multiplex成像技术固有的细胞分割不准确性可能影响细粒度空间指标
4. **临床验证**：需要更大规模队列或临床试验验证PIHs-1作为治疗靶点的稳健性和临床应用价值
