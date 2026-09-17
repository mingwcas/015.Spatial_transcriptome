# 四维度生信分析报告 — 多技术整合解析乳腺癌肿瘤微环境

> **论文信息**：High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis  
> **DOI**: [10.1038/s41467-023-43458-x](https://doi.org/10.1038/s41467-023-43458-x)  
> **平台**: IlluminaSpatial (10x Genomics: Chromium scFFPE-seq, Visium CytAssist, Xenium In Situ)  
> **期刊**: Nature Communications (2023)  
> **完成日期**: 2023年12月

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 单细胞RNA测序 | Chromium Single Cell Gene Expression Flex (scFFPE-seq) | Cell Ranger v7.0.1 | FFPE样本单细胞转录组分析 |
| 空间转录组 | Visium CytAssist | Space Ranger v2022.0705.1 | 全转录组空间表达分析 |
| 原位分析 | Xenium In Situ | Xenium Ranger | 313基因靶向原位检测 |
| 数据预处理 | 质量控制与过滤 | scanpy 1.19 | 细胞/基因过滤，标准化 |
| 细胞类型注释 | 无监督聚类 | scanpy 1.19 + Seurat v4.3/v5 | 多轮聚类和标记基因注释 |
| 空间反卷积 | RCTD (Robust Cell Type Decomposition) | spacexr 2.0.1 | Visium spots细胞类型组成推断 |
| 图像配准 | 多平台空间对齐 | cv2 4.5.4 (OpenCV) | Visium-Xenium空间坐标对齐 |
| 差异表达分析 | 区域特异性DEGs | Seurat v4.3/v5 | DCIS vs IDC差异基因鉴定 |
| 细胞邻域分析 | 空间细胞共定位 | monet v0.3.2 | 细胞微环境组成分析 |
| 可视化分析 | 交互式数据浏览 | Loupe Browser v6.4.1 / Xenium Explorer | 空间数据可视化和探索 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|-------------|
| Fig. 1 | 三平台整合实验设计和数据概览 | 流程图、UMAP、空间热图 |
| Fig. 2 | scFFPE-seq单细胞聚类和细胞类型鉴定 | UMAP、条形图、热图 |
| Fig. 3 | Visium CytAssist空间表达模式 | 空间热图、H&E叠加图 |
| Fig. 4 | Xenium In Situ单细胞空间分辨率 | 空间散点图、细胞类型分布图 |
| Fig. 5 | 三平台数据整合和交叉验证 | 相关性散点图、空间叠加图 |
| Fig. 6 | DCIS亚型鉴定和分子特征 | 空间分布图、差异表达热图 |
| Fig. 7 | 三阳性受体区域（ERBB2+/ESR1+/PGR+） | 空间共表达图、箱线图 |
| Fig. 8 | 边界细胞（boundary cells）鉴定 | 空间散点图、共表达分析图 |
| Supplementary Fig. 1-15 | 质量控制、技术验证、补充分析 | 多种图形类型 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|-----------|
| scFFPE-seq处理 | Cell Ranger | v7.0.1 | 商业（10x Genomics） |
| Visium CytAssist处理 | Space Ranger | v2022.0705.1 | 商业（10x Genomics） |
| Xenium In Situ分析 | Xenium Ranger | - | 商业（10x Genomics） |
| 单细胞分析 | scanpy | 1.19 | 开源 |
| 单细胞分析 | Seurat | v4.3/v5 | 开源 |
| 空间反卷积 | spacexr (RCTD) | 2.0.1 | 开源 |
| 细胞邻域分析 | monet | v0.3.2 | 开源 |
| 图像配准 | cv2 (OpenCV) | 4.5.4 | 开源 |
| 交互式浏览 | Loupe Browser | v6.4.1 | 商业（10x Genomics） |
| 交互式浏览 | Xenium Explorer | - | 商业（10x Genomics） |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| RCTD (Robust Cell Type Decomposition) | 统计反卷积 | Visium spots细胞类型组成推断 |
| Leiden聚类算法 | 图聚类 | 单细胞无监督聚类 |
| UMAP | 降维算法 | 单细胞数据可视化 |
| Moran's I | 空间自相关 | 空间表达模式识别 |
| 多平台整合算法 | 数据整合 | scFFPE-seq/Visium/Xenium数据整合 |
| 图像配准算法 | 计算机视觉 | 多模态空间对齐 |
| 差异表达分析 | 统计检验 | 区域特异性基因鉴定 |
| 细胞邻域分析 | 空间统计 | 细胞微环境组成分析 |

---

## 研究亮点

1. **三技术整合**：首次系统整合scFFPE-seq、Visium CytAssist和Xenium In Situ三种10x Genomics平台
2. **FFPE样本适用性**：展示了在FFPE临床样本上的强大分析能力
3. **DCIS亚型发现**：鉴定出两种分子不同的DCIS亚型
4. **边界细胞发现**：识别出稀有的边界细胞共表达肿瘤和肌上皮标记
5. **三阳性区域**：发现ERBB2+/ESR1+/PGR+三阳性受体区域

---

## 研究局限性

1. **样本量有限**：仅分析了乳腺癌FFPE样本，需更多癌种验证
2. **商业软件依赖**：Cell Ranger、Space Ranger、Xenium Ranger为商业软件
3. **基因面板限制**：Xenium In Situ仅检测313个基因
4. **技术平台特异性**：整合方法可能需要针对其他平台调整
5. **临床验证缺失**：发现的生物标志物需独立队列验证

---

## 技术创新点

1. **多平台整合框架**：建立了scFFPE-seq + Visium + Xenium的标准化整合流程
2. **空间反卷积优化**：使用RCTD提高Visium数据的细胞类型分辨率
3. **图像配准方法**：开发了跨平台空间对齐的计算方法
4. **边界细胞鉴定**：提出了识别稀有边界细胞的分析策略
