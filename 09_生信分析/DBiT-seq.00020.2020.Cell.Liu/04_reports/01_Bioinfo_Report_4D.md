# 四维度生信分析报告 — DBiT-seq Spatial Multi-Omics

> **论文信息**
> - **标题**: High-Spatial-Resolution Multi-Omics Sequencing via Deterministic Barcoding in Tissue
> - **平台**: DBiT-seq (Deterministic Barcoding in Tissue for Spatial Omics Sequencing)
> - **DOI**: https://doi.org/10.1016/j.cell.2020.10.026
> - **期刊**: Cell 183, 1–17 (2020)
> - **第一作者**: Liu, Yang
> - **完成日期**: 2024

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 微流控芯片制造 | PDMS软光刻 | SU-8光刻胶, GE RTV PDMS | 10/25/50μm三种通道宽度 |
| 空间条码递送 | 微流控两步流动条码 | 正交PDMS芯片 + T4 DNA连接酶 | A1-A50 × B1-B50 = 2500像素 |
| 原位逆转录 | 原位cDNA合成 | Maxima H Minus逆转录酶 | Barcode A与cDNA共价连接 |
| cDNA纯化 | 生物素-链霉亲和素磁珠 | Dynabeads MyOne Streptavidin C1 | 高效回收空间标记cDNA |
| 文库构建 | Nextera XT tagmentation | Illumina Nextera XT Kit | paired-end 100×100测序 |
| 序列比对 | ST pipeline | ST pipeline v1.7.2 | pixels × genes表达矩阵 |
| 数据标准化 | SCTransform | Seurat V3.2 | 正则化负二项回归 |
| 空间变异基因鉴定 | SpatialDE | SpatialDE | 自动识别空间表达模式 |
| 聚类分析 | NMF + tSNE/UMAP | NNLM, Rtsne | 10-25个spatial domains |
| GO富集分析 | ToppGene | ToppGene Suite | 生物学通路注释 |
| 细胞类型注释 | SingleR + Seurat整合 | SingleR v1.2.3, Seurat V3.2 | 自动细胞类型鉴定 |
| 与ENCODE比较 | Pseudo-bulk相关性 | Pearson相关 | r > 0.784 |
| smFISH验证 | HCR v3.0 | Molecular Instruments | DBiT-seq检测效率~15.5% |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|--------------|
| Fig. 1 | DBiT-seq技术设计与验证 | 流程图 + 荧光图像 + 散点图 |
| Fig. 2 | 全胚胎空间多组学映射 | 空间热图 + UMAP + 条形图 |
| Fig. 3 | 胚胎脑空间多组学 | 空间热图 + 共定位图 |
| Fig. 4 | 早期眼部发育基因表达 | 空间热图 + UMAP |
| Fig. 5 | 11个胚胎全局聚类分析 | tSNE + 热图 |
| Fig. 6 | E11内部器官映射 | UMAP + 空间热图 |
| Fig. 7 | SpatialDE自动特征识别 | 空间热图 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 原始数据处理 | ST pipeline | v1.7.2 | 开源 |
| 标准化 | SCTransform (Seurat) | V3.2 | 开源 |
| 聚类 | NMF, tSNE/UMAP | NNLM, Rtsne | 开源 |
| 细胞类型注释 | SingleR | v1.2.3 | 开源 |
| 空间差异表达 | SpatialDE | - | 开源 |
| GO富集 | ToppGene | - | 开源 |
| 测序文库 | Nextera XT | - | 商业 |
| 测序平台 | HiSeq 4000 | - | 商业 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| SCTransform | 正则化负二项回归 | 单像素标准化和方差稳定 |
| NMF | 非负矩阵分解 | 空间domain聚类 |
| tSNE | 降维可视化 | 二维展示像素/细胞分布 |
| UMAP | 降维可视化 | 全局结构保持的二维映射 |
| SpatialDE | 统计模型 | 空间变异基因识别 |
| SingleR | 相关性分类 | 自动化细胞类型注释 |
| Seurat整合 | 锚点整合 | scRNA-seq与空间数据整合 |
| Pearson相关性 | 线性相关分析 | mRNA-蛋白相关性、跨技术比较 |

---

## 技术局限与利益冲突

### 技术局限
1. **非真正单细胞分辨率**: 10μm像素平均含~1.7个细胞，虽接近但不完全等于单细胞
2. **可映射面积受限**: 10μm像素时仅1mm×1mm，需增加条码数量或使用蛇形通道设计
3. **扩散限制理论极限**: 约5μm为可实现最小像素大小

### 利益冲突声明
- Rong Fan是IsoPlexis、Singleron Biotechnologies和AtlasXomics的联合创始人，并担任科学顾问委员会成员
- 作者已披露并由耶鲁大学 Provost's Office管理利益冲突

---

## 总结

DBiT-seq是一项创新性的空间多组学技术，通过微流控限域递送和正交条码连接实现甲醛固定组织的高分辨率空间转录组和蛋白质组联合分析。核心技术优势包括：(1) 10μm像素接近单细胞级别；(2) 兼容甲醛固定组织；(3) NGS-based方法易于推广；(4) 多组学联合检测。该技术为发育生物学、神经科学、癌症生物学和临床病理提供了新的研究工具。
