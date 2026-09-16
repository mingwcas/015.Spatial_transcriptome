# 四维度生信分析报告 — A spatially resolved single-cell genomic atlas of the adult human breast

> 论文：Kumar et al., Nature (2023)；DOI: [10.1038/s41586-023-06252-9](https://doi.org/10.1038/s41586-023-06252-9)；平台：MERSCOPE/MERFISH、Visium、Resolve、CODEX；依据：Methods及Fig. 1–6图注。

## 维度一：分析方法 / Methods
| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---|---|---|---|
| sc/snRNA预处理 | Cell Ranger比对、Seurat QC | Cell Ranger 3.1.0；Seurat 3.2.3；GRCh38.p12 | 714,331 cells、117,346 nuclei |
| 主类型整合 | CCA anchors、PCA/UMAP、聚类 | Seurat；SingleR | 10 cell clusters、11 nucleus clusters |
| 细胞状态 | 类型内重聚类、Wilcoxon | Seurat FindMarkers | 上皮11 states等 |
| 通路/调控 | fgsea、clusterProfiler、SCENIC | fgsea 1,000 permutations | pathway与regulon |
| Visium | Space Ranger、SCTransform、anchor integration | Space Ranger 1.2.0 | 4样本ST；9 clusters |
| Resolve | DAPI分割、marker评分、随机森林 | QuPath 0.3.0、ImageJ 1.52n、randomForest 500 trees | 12 tissues/5 women |
| MERSCOPE | CellPose分割、Seurat、随机森林 | Seurat；CellPose；randomForest 500 trees | 266-gene panel |
| CODEX | StarDist分割、Leiden、蛋白z-score | TissueNet模型；Leiden | 34-antibody panel，8 tissues |
| 互作/统计 | CellPhoneDB、Procrustes、Wilcoxon/Fisher | CellPhoneDB v3；vegan 2.5-6 | 配体受体、左右乳房一致性 |

## 维度二：结果图表
| 图 | 内容摘要 | 主要图形类型 |
|---|---|---|
| Fig. 1 | HBCA workflow及主要细胞类型 | UMAP、marker heatmap、流程图 |
| Fig. 2 | ST/Resolve/CODEX空间邻域 | 空间图、共定位网络、频率图 |
| Fig. 3 | 上皮类型、状态及导管–叶差异 | UMAP、表达图、空间图 |
| Fig. 4 | 免疫生态与血管邻近 | UMAP、组织空间、频率图 |
| Fig. 5 | 成纤维细胞与脂肪细胞 | UMAP、signature、ST/Resolve |
| Fig. 6 | 血管、淋巴和周血管谱系 | UMAP、组织学、空间验证 |

## 维度三：Pipelines
| 阶段 | 工具 | 版本 | 开源/商业 |
|---|---|---|---|
| 10x测序定量 | Cell Ranger/CASAVA | 3.1.0/1.8.1 | 商业厂商软件 |
| scRNA整合 | Seurat | 3.2.3 | 开源 |
| ST定量 | Space Ranger | 1.2.0 | 商业厂商软件 |
| 空间RNA | QuPath/ImageJ/CellPose | 0.3.0/1.52n | 开源；CellPose开源 |
| CODEX | PhenoCycler/Open平台、StarDist | 未注明 | 仪器/开源模型 |
| 通路/调控 | fgsea、clusterProfiler、SCENIC | 未注明 | 开源 |
| 互作 | CellPhoneDB | v3 | 开源 |

## 维度四：算法与 AI
| 算法/模型 | 类型 | 用途 |
|---|---|---|
| CCA anchor integration | 多样本整合 | 跨患者批次校正 |
| UMAP/PCA | 降维 | 细胞状态可视化 |
| Random forest（500 trees） | 监督机器学习 | Resolve/MERSCOPE细胞标签细化 |
| CellPose | 深度学习图像分割 | MERSCOPE细胞边界 |
| StarDist/TissueNet | 深度学习分割 | CODEX细胞分割 |
| Leiden | 图聚类 | CODEX蛋白表达聚类 |
| SCENIC | 调控网络推断 | TF–target regulon |

**局限与注意：** CellPhoneDB与空间共定位仅提示潜在互作；ST spot混合细胞；靶向panel存在检测范围限制；CODEX区域和类型标注含人工判断；研究样本族群以Caucasian/African American为主。
