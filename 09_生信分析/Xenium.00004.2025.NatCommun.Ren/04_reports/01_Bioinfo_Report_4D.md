# 四维度生信分析报告 — Xenium 5K空间转录组基准测试

> **论文信息**：Systematic benchmarking of high-throughput subcellular spatial transcriptomics platforms across human tumors
> **DOI**: [10.1038/s41467-025-64292-3](https://doi.org/10.1038/s41467-025-64292-3)
> **平台**: Xenium 5K, CosMx 6K, Stereo-seq v1.3, Visium HD FFPE
> **期刊**: Nature Communications (2025)
> **完成日期**: 2025年

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 样本预处理 | 肿瘤组织三分处理 | - | FFPE/OCT/单细胞悬液分别处理 |
| sST数据生成 | Stereo-seq v1.3 | SAW v.8.0 | 0.5 μm分辨率，poly(dT)无偏捕获 |
| sST数据生成 | Visium HD FFPE | spaceranger v.3.0.0 | 2 μm分辨率，18,085基因 |
| iST数据生成 | Xenium 5K | Xenium Onboard Analysis v.3.1.0 | 5,001基因，多通道细胞分割 |
| iST数据生成 | CosMx 6K | Atomx v.1.3.2 | 6,175基因，单分子精度 |
| 蛋白组参考 | CODEX | PhenoCycler-Fusion 2.0 | 16-plex抗体，空间蛋白 ground truth |
| 单细胞参考 | scRNA-seq | cellranger v.7.0.0 | 10x Chromium 3' GEM v3.1 |
| 数据预处理 | 质量控制 | Python/OpenCV v.4.10.0 | 组织掩膜过滤，统一8 μm bin |
| 相关性分析 | ST vs scRNA-seq相关性 | Python (numpy, scipy) | Pearson相关，R=0.53-0.85 |
| 扩散控制评估 | 转录本扩散分析 | scikit-learn v.1.5.2 | Stereo-seq扩散3.4×于Visium HD |
| 图像配准 | 跨平台/跨模态对齐 | SimpleITK v.2.4.0 | 多阶段配准流程 |
| 细胞注释 | scRNA-seq注释 | Seurat v.5.1.0 + DoubletFinder v.2.0.3 | 两轮聚类+标记基因注释 |
| ST注释转移 | 五工具注释 | SELINA/Celltypist/Spoint/Tangram/TACCO | 多数投票整合 |
| CODEX注释 | KNN分类器 | QuPath v.0.5.1 + StarDist v.0.5.0 | 手动标注+机器学习 |
| 聚类评估 | 无监督聚类 | scanpy v.1.10.3 + Leiden | 轮廓宽度评估 |
| 空间聚类 | 空间域识别 | CellCharter | 多尺度grid分析 |
| 通路富集 | GO富集分析 | clusterProfiler v.4.6.2 | DEGs (p_adj≤0.05, FC≥2) |
| 降采样分析 | 测序饱和度 | pysam v.0.22.1 | 20%/40%/60%/80%降采样 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|-------------|
| Fig. 1 | 四平台基因检测敏感性比较 | 散点图、箱线图、饱和度曲线 |
| Fig. 2 | 假阳性（背景噪声/扩散控制）评估 | 空间热图、箱线图、散点图 |
| Fig. 3 | 转录本-蛋白（CODEX）空间一致性 | 空间热图、相关性条形图 |
| Fig. 4 | 细胞分割准确性比较 | 分割叠加图、密度图、箱线图 |
| Fig. 5 | 细胞聚类、注释准确性、与CODEX空间对齐 | UMAP、条形图、空间分布图 |
| Fig. 6 | 空间聚类一致性和恶性细胞分布 | 空间聚类图、相关性图 |
| Supplementary Fig. 1 | 基因面板重叠分析 | UpSet图 |
| Supplementary Fig. 2-4 | 敏感性详细分析 | 多类型图 |
| Supplementary Fig. 5 | 背景噪声详细分析 | 热图、箱线图 |
| Supplementary Fig. 6 | 图像配准流程 | 叠加图 |
| Supplementary Fig. 7-16 | 各维度详细补充分析 | 多种图形 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|-----------|
| scRNA-seq处理 | cellranger | v.7.0.0 | 商业（10x Genomics） |
| Visium HD FFPE处理 | spaceranger | v.3.0.0 | 商业（10x Genomics） |
| Stereo-seq v1.3处理 | SAW | v.8.0 | 商业（STOmics/BGI） |
| Xenium 5K分析 | Xenium Onboard Analysis | v.3.1.0 | 商业（10x Genomics） |
| CosMx 6K解码 | Atomx | v.1.3.2 | 商业（NanoString） |
| CosMx图像拼接 | napari-cosmx | - | 开源 |
| 单细胞聚类注释 | Seurat | v.5.1.0 | 开源 |
| 双细胞检测 | DoubletFinder | v.2.0.3 | 开源 |
| 空间数据分析 | scanpy | v.1.10.3 | 开源 |
| 图像处理 | OpenCV | v.4.10.0 | 开源 |
| 医学图像配准 | SimpleITK | v.2.4.0 | 开源 |
| 细胞核分割 | StarDist | v.0.5.0 | 开源 |
| 病理图像分析 | QuPath | v.0.5.1 | 开源 |
| 降采样分析 | pysam | v.0.22.1 | 开源 |
| 通路富集 | clusterProfiler | v.4.6.2 | 开源 |
| 空间聚类 | CellCharter | - | 开源 |
| ST注释 | SELINA | v.0.1 | 开源 |
| ST注释 | Celltypist | v.1.6.3 | 开源 |
| ST注释 | Spoint | v.1.1.7 | 开源 |
| ST注释 | Tangram | v.1.0.4 | 开源 |
| ST注释 | TACCO | v.0.4.0.post1 | 开源 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| DNB (DNA Nanoball) 阵列 | 空间barcode技术 | Stereo-seq空间编码 |
| 迭代荧光杂交成像 | 成像技术 | Xenium/CosMx空间转录组检测 |
| poly(dT) 探针捕获 | 靶向捕获 | Visium HD转录本捕获 |
| UMI (Unique Molecular Identifier) | 分子标签 | 原始分子计数定量 |
| Moran's I | 空间自相关统计 | 背景噪声空间聚集评估 |
| Pearson相关系数 | 相关性分析 | 基因表达和空间一致性评估 |
| Leiden算法 | 图聚类算法 | 单细胞无监督聚类 |
| UMAP | 降维算法 | 单细胞数据可视化 |
| Silhouette score | 聚类质量评估 | 细胞群体分离度量化 |
| StarDist | 深度学习分割 | CODEX细胞核自动分割 |
| KNN分类器 | 机器学习分类 | CODEX细胞类型注释 |
| SimpleITK相似性变换 | 图像配准 | 跨平台/跨模态空间对齐 |
| CellCharter空间聚类 | 空间域识别 | 组织空间结构解析 |

---

## 研究局限性

1. **样本量有限**：每种癌症类型仅1名患者（n=3 total），限制了统计推断的泛化能力
2. **CODEX非原位**：CODEX在相邻切片而非原始ST切片上进行，引入形态学差异
3. **Stereo-seq样本差异**：Stereo-seq使用新鲜冷冻组织，与FFPE组织比较受结构差异影响
4. **商业pipeline限制**：对齐和分割分析使用商业pipeline，可能存在自定义优化空间
5. **新鲜样本限制**：所有样本为新鲜收集，存档或长期保存样本的普适性未验证

---

## 平台推荐总结

| 应用场景 | 推荐平台 | 原因 |
|----------|----------|------|
| 单细胞水平分析 | Xenium 5K > CosMx 6K | 多通道分割减少转录本泄漏，注释准确性最高 |
| 免疫微环境研究 | Xenium 5K | 最高的空间一致性，TLS和免疫细胞检测最优 |
| 通路水平分析 | Stereo-seq v1.3 | 全转录组无偏检测，宿主-微生物互作 |
| 组织区域分析 | Visium HD FFPE | 更大基因面板，区域水平差异检测 |
| 肿瘤边界描绘 | Xenium 5K, Visium HD FFPE | 更连续的边界勾勒 |
