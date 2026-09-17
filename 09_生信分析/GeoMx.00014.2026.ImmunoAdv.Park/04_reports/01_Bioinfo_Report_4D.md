# 四维度生信分析报告 — GeoMx_dMMR_CRC_Immunotherapy

> 论文信息
> - 标题：Comprehensive spatial and immune profiling of metastatic mismatch repair–deficient colorectal cancer reveals response to immunotherapy
> - DOI: https://doi.org/10.1093/immadv/ltag001
> - 平台：GeoMx（空间多组学）
> - 完成日期：2025-09-24投稿，2025-12-16接受，2026-01-09发表

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| Bulk RNA-seq | 全转录组测序 | HiSeq 2500, STAR v2.6.1, RSEM v1.3.1 | 免疫高/低浸润分组，转录组特征区分响应 |
| 单细胞RNA-seq | scRNA-seq | 10× Chromium 5′ V(D)J, CellRanger v5.0, Seurat v4.0, Harmony | 17,970细胞，7个主要细胞群，NK细胞和M1/M2极化差异 |
| 多重免疫组化 | mIHC | Opal Polaris 7-color (Akoya), Leica BOND Rx, inForm, phenoptr v0.3.2 | 空间邻近性：敏感灶效应细胞-肿瘤距离近 |
| 细胞间通讯 | 配体-受体分析 | CellChat R v2.1.2 | 敏感灶免疫激活网络 vs 抵抗灶SPP1+ TAMs网络 |
| 免疫浸润反卷积 | 细胞类型比例估算 | EPIC (bulk RNA-seq) | CD8+/CD4+ T细胞、巨噬细胞比例差异 |
| 主成分分析 | 样本分群 | R base stats | PCA区分敏感/抵抗表型 |
| 差异表达分析 | DEG识别 | Seurat FindAllMarkers | 免疫高/低组差异基因 |
| 免疫组化 | dMMR/PD-L1检测 | Dako Autostainer Link 48, PD-L1 IHC 22C3 pharmDx | dMMR确认，CPS≥1为PD-L1阳性 |
| 统计检验 | 组间比较 | Wilcoxon, ANOVA, R v4.1.1 | 显著性阈值 P<0.05 |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|---------|-------------|
| Fig. 1 | 研究设计概览，多组学策略，样本采集，CT影像治疗前后对比 | 流程图 + CT图像 |
| Fig. 2 | Bulk RNA-seq：免疫分层、差异基因、火山图、PCA、基因表达热图、mIHC组织图 | 热图 + 火山图 + PCA散点图 + 组织图像 |
| Fig. 3 | mIHC空间分析：肿瘤-免疫距离量化（CD8、CD68、CD163等） | 组织图像 + 散点/柱状图 |
| Fig. 4 | scRNA-seq：UMAP、细胞组成、细胞毒性评分、巨噬细胞极化 | UMAP + 柱状图 + 热图 |
| Fig. 5 | CellChat通讯网络：Circle plots、sender-receiver热图、通路活性气泡图 | Circle plots + 热图 + 气泡图 |
| Fig. 6 | 整合空间-分子模型：敏感 vs 抵抗机制示意图 | 模式图 |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|---------|
| RNA提取 | QIAamp Mini Kit | - | 商业（Qiagen） |
| Bulk RNA-seq建库 | Illumina TruSeq Stranded Total RNA + Ribo-Zero Gold | - | 商业（Illumina） |
| Bulk RNA-seq测序 | HiSeq 2500 | - | 商业（Illumina） |
| Bulk RNA比对 | STAR | v2.6.1 | 开源 |
| Bulk表达定量 | RSEM | v1.3.1 | 开源 |
| 单细胞解离 | gentleMACS | - | 商业（Miltenyi） |
| 单细胞建库 | 10× Chromium 5′ V(D)J | - | 商业（10× Genomics） |
| 单细胞测序 | NovaSeq 6000 | - | 商业（Illumina） |
| 单细胞比对 | CellRanger | v5.0 | 商业（10× Genomics） |
| 单细胞分析 | Seurat | v4.0 | 开源 |
| 批次校正 | Harmony | - | 开源 |
| mIHC染色 | Opal Polaris 7-color kit | - | 商业（Akoya） |
| mIHC自动染色 | Leica BOND Rx | - | 商业（Leica） |
| mIHC图像分析 | inForm | - | 商业（PerkinElmer） |
| 空间分析 | phenoptr | v0.3.2 | 商业（PerkinElmer） |
| 细胞通讯 | CellChat | v2.1.2 | 开源 |
| 免疫组化 | PD-L1 IHC 22C3 pharmDx Kit | - | 商业（Dako） |
| IHC染色仪 | Dako Autostainer Link 48 | - | 商业（Dako） |
| 统计检验 | R base stats | v4.1.1 | 开源 |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| STAR | 比对算法（剪接比对） | RNA-seq reads比对至GRCh38 |
| RSEM | 期望最大化定量 | TPM表达量计算 |
| Harmony | 批次校正算法 | 单细胞多样本整合校正 |
| CellChat置换检验 | 统计框架 | 配体-受体相互作用显著性评估 |
| Seurat聚类 | 图聚类 | 单细胞细胞类型分群 |
| FindAllMarkers | 差异表达 | 细胞类型特征基因识别 |
| EPIC反卷积 | 细胞类型分数估算 | Bulk RNA-seq细胞组成预测 |
| 监督分类器（inForm） | 机器学习 | mIHC细胞 phenotype assignment |
| PCA | 降维 | 转录组样本分群可视化 |

---

## 利益冲突/局限性

- **利益冲突**：作者声明无利益冲突
- **主要局限**：
  1. **单病例研究**：仅纳入1例患者，限制了结果的泛化性
  2. **无配对对照**：缺乏健康组织或未治疗对照
  3. **商业平台依赖**：GeoMx空间转录组数据来自多平台整合，未使用GeoMx平台直接测序；多标mIHC依赖商业试剂和软件
  4. **数据可及性**：Bulk和scRNA-seq数据需联系作者获取，非公开可用
