# 四维度生信分析报告 — Xenium敏感性、特异性和信号污染

> 论文信息
> - 论文标题：Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics
> - DOI：10.1038/s41592-026-03089-8
> - 平台：Xenium
> - 完成日期：2026-06-01

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| snRNA-seq预处理 | SCTransform标准化，SNN聚类，层级注释 | Seurat v5.0.1, R 4.3.2 | 四级细胞类型注释（Level 1-4，Level 2.1用于IHC验证） |
| Xenium分割 | 默认5µm核扩展，多模态分割（5K） | 10x Xenium, Baysor v0.7.0, ProSeg v2, Segger | 默认分割作为基线，ProSeg提高分辨率 |
| 细胞类型注释 | RCTD双细胞模式解卷积 | RCTD | w1/w2权重定量污染，singlet/doublet分类 |
| 空间溢出定量 | 邻域组成分析，余弦相似度 | 自定义Python/R | 恶性细胞溢出指数最高 |
| SPLIT校正 | 基于RCTD权重的转录本重新分配 | SPLIT R包 | 提升细胞类型分离和生物学保真度 |
| 替代校正方法 | ResolVI（变分推断），ovrlpy（垂直切片） | ResolVI, ovrlpy | ResolVI/ovrlpy降低基因数，SPLIT更优 |
| 批次效应评估 | iLISI, Silhouette Batch | scib-metrics | Xenium批次效应低 |
| 污染特异性评估 | Logistic回归预测空间邻近 | scikit-learn | SPLIT显著减少恶性标记在T细胞中的富集 |
| 数据质量评估 | Pseudo-bulk余弦相似度与Chromium比较 | 自定义 | SPLIT提高与snRNA-seq的相似度 |
| 工作流管理 | Snakemake管道 | Snakemake | 48线程，1TB内存，72小时超时 |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|---------|-------------|
| Fig. 1 | 实验设计和关键指标：41样本，19乳腺癌+22肺癌 | 热图，密度分布，UMAP |
| Fig. 2 | Xenium 5K vs 靶向面板比较：敏感性权衡 | UMAP，散点图，箱线图 |
| Fig. 3 | 转录本溢出和SPLIT原理：空间依赖性污染 | 细胞分割可视化，示意图，散点图 |
| Fig. 4 | SPLIT性能验证：最佳细胞类型分离 | UMAP，条形图，GSEA热图 |
| ED Fig. 1 | 外部参考注释一致性验证 | 热图，UMAP |
| ED Fig. 2 | 批次整合评分 | 热图 |
| ED Fig. 3 | 跨面板一致性分析 | 散点图，UMAP |
| ED Fig. 4 | 细胞类型表达谱相似性 | 散点图 |
| ED Fig. 5 | 各面板溢出指数 | 点图，条形图 |
| ED Fig. 6 | 样本级溢出指数 | 条形图 |
| ED Fig. 7 | SPLIT和SPLIT-shift效果 | UMAP，示意图 |
| ED Fig. 8 | Doublets和特异表型处理 | UMAP，IHC图像 |
| ED Fig. 9 | 乳腺癌panel SPLIT验证 | UMAP，多指标比较 |
| ED Fig. 10 | Top预测基因详情 | 热图 |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|-----|------|------|----------|
| Xenium分析主管道 | Snakemake | - | 开源 |
| 单细胞RNA-seq分析 | Seurat | 5.0.1 | 开源 |
| 细胞类型注释 | RCTD | - | 开源 |
| 分割（默认） | Xenium默认分割 | - | 商业 |
| 分割（替代） | Baysor | 0.7.0 | 开源 |
| 分割（替代） | ProSeg | v2 | 开源 |
| 分割（替代） | Segger | - | 开源 |
| 校正方法 | SPLIT | - | 开源 |
| 校正方法 | ResolVI | - | 开源 |
| 校正方法 | ovrlpy | - | 开源 |
| 指标计算 | scib-metrics | - | 开源 |
| 机器学习 | scikit-learn | - | 开源 |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| SCTransform | 归一化方法 | 单细胞RNA-seq方差稳定化 |
| RCTD (Poisson regression) | 概率解卷积模型 | 空间转录组细胞类型分解 |
| SPLIT | 参考基础信号分解 | 转录本污染校正 |
| ResolVI | 变分推断模型 | 空间转录组校正 |
| Logistic Regression | 分类模型 | 预测细胞空间邻近关系 |
| UMAP | 降维可视化 | 单细胞数据可视化 |
| GSEA | 富集分析 | 基因集富集检验 |
| Cosine similarity | 相似度度量 | 表达谱和污染指标比较 |

## 利益冲突/局限性

1. **厂商关联**：作者团队收到10x Genomics研究经费支持，R.G.从多家生物技术公司获得咨询收入
2. **样本局限性**：主要分析限于乳腺癌和肺癌，对其他组织的适用性需进一步验证
3. **参考依赖**：SPLIT依赖snRNA-seq参考，缺少参考的细胞类型可能导致错误分解
4. **IHC样本有限**：仅5个样本有成功的IHC验证
5. **5K panel敏感性**：5K panel敏感性较低，可能影响某些应用场景
