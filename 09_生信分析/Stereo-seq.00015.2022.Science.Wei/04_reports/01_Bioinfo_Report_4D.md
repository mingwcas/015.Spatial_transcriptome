# 四维度生信分析报告 — 蝾螈大脑再生空间转录组研究

> **论文信息**
> - 论文标题: Single-cell Stereo-seq reveals induced progenitor cells involved in axolotl brain regeneration
> - DOI: [10.1126/science.abp9444](https://doi.org/10.1126/science.abp9444)
> - 平台: Stereo-seq (Spatial Enhanced Resolution Omics Sequencing)
> - 期刊: Science (2022)
> - 第一作者: Wei, Xiaoyu
> - 完成日期: 2024

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 空间转录组测序 | Stereo-seq | DNB sequencing, 220nm spot, 500/715nm center-to-center | 单细胞分辨率空间转录组，11页，~850 DNB/细胞，6291 UMI/细胞 |
| 单细胞分割 | Watershed algorithm | scikit-image | 核染色+转录本空间分离实现单细胞边界划定 |
| 空间聚类分析 | Spatially constrained clustering | 自定义算法 | 6个解剖区域，16个细胞簇 |
| 单细胞聚类注释 | Seurat | v4+ | 发育33种细胞类型，再生28种细胞类型 |
| 轨迹分析 | RNA Velocity | Dynamo | 发现reaEGC→rIPC→IMN→nptxEX分化轨迹 |
| 伪时间分析 | Pseudotime | Monocle2/3 | 跨再生阶段轨迹整合 |
| 验证实验 | RNA ISH | 传统实验方法 | Stereo-seq数据验证 |
| 细胞通讯分析 | Ligand-receptor | 自定义分析 | Tnc-Sdc1相互作用发现 |
| 细胞追踪 | BrdU labeling | 实验方法 | 新生神经元验证 |
| 基因模块分析 | Module scoring | 自定义分析 | NSC/Cell cycle/Translation模块评估 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|--------------|
| Fig.1 | Stereo-seq技术流程、单细胞分割、16种细胞类型、3种EGC亚型(wntEGC/sfrpEGC/ribEGC) | 模式图 + 空间分布图 + 小提琴图 |
| Fig.2 | 6个发育阶段(St.44→ metamorphosis)的细胞类型组成变化、33种细胞类型、NSC/细胞周期/翻译模块动态 | 气泡图 + 小提琴图 + 空间分布图 |
| Fig.3 | 7个再生阶段(2-60 DPI)的细胞类型分布、MCG和reaEGC响应、WSN发现、Tnc-Sdc1配体-受体对 | 空间分布图 + 折线图 + UMAP |
| Fig.4 | reaEGC→rIPC1→IMN→nptxEX谱系转换轨迹、RNA velocity和Monocle伪时间分析 | 流线图 + 热图 + 散点图 + UMAP |
| Fig.5 | 发育与再生神经发生的比较分析、平行轨迹发现、分子级联对比 | 空间分布图 + 热图 + 富集分析条形图 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 原始测序数据处理 | SAW pipeline | - | 开源 (https://github.com/BGIResearch/SAW) |
| 表达矩阵生成 | handleBam | - | 厂商内部工具 |
| 单细胞分割 | scikit-image | - | 开源 |
| 单细胞分析 | Seurat | 4.x | 开源 |
| RNA velocity | Dynamo | - | 开源 (https://github.com/aristoteleo/dynamo-release) |
| 伪时间分析 | Monocle2/3 | 2.x/3.x | 开源 |
| 空间聚类 | 自定义 | - | 自定义 |
| 降维可视化 | UMAP | - | 开源 |
| 细胞注释 | 已知Marker基因 | - | 文献参考 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| Watershed segmentation | 图像分割算法 | 单细胞边界划定 |
| Spatially constrained clustering | 聚类算法 | 空间信息约束的细胞聚类 |
| CCA (Canonical Correlation Analysis) | 多元统计 | 多截面数据整合 |
| SCTransform | 标准化方法 | 单细胞数据标准化 |
| DDRTree | 降维方法 | 轨迹构建 |
| RPCA (Robust PCA) | 降维方法 | 跨阶段数据整合 |
| RNA velocity | 动力学模型 | 细胞状态转换预测 |
| Pseudotime analysis | 轨迹推断 | 细胞分化时序重构 |
| Gene Ontology enrichment | 统计检验 | 功能富集分析 |

---

## 局限性/利益冲突

1. **厂商论文**: Stereo-seq技术由BGI研发，本文作者单位包含BGI研究人员，可能存在技术偏向性
2. **动物模型限制**: 蝾螈为两栖类动物，再生能力可能与哺乳动物存在种属差异
3. **短期追踪**: BrdU实验仅分析20 DPI，神经元的最终成熟和功能整合需要更长期验证
4. **空间分辨率**: 虽然 Stereo-seq 达到亚细胞水平，但仍受切片厚度(20µm)限制
5. **缺乏扰动实验**: VZ特异性标记和功能干扰实验是验证EGC来源的关键，本文未涉及
