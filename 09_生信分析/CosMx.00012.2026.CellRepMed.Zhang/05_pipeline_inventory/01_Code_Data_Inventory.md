# 代码与数据清单 — CosMx_SCLC_TME_Heterogeneity

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| 本研究分析代码 | https://github.com/ZhoulabCPH/SCLC-LNM-SMI.git | 论文自带 | 空间坐标数据、细胞注释信息、分析代码 |
| Seurat | https://cran.r-project.org/web/packages/Seurat/index.html | 开源 (MIT) | 单细胞分析主工具 v5.1.0 |
| Harmony | https://cran.r-project.org/web/packages/harmony/index.html | 开源 (MIT) | 批次效应校正 v1.0 |
| clusterProfiler | http://bioconductor.org/packages/release/bioc/html/clusterProfiler.html | 开源 (Artistic-2.0) | GO/KEGG富集分析 v4.8.3 |
| CellChat | https://github.com/jinworks/CellChat.git | 开源 (MIT) | 配体-受体分析 v1.6.1 |
| ClusterR | https://cran.r-project.org/web/packages/ClusterR/index.html | 开源 (GPL-3) | MiniBatchKMeans聚类 v1.3.3 |
| DoubletFinder | https://github.com/chris-mcginnis-ucsf/DoubletFinder | 开源 (MIT) | 双细胞检测 v2.0.6 |
| GSVA | https://new.bioconductor.org/packages/devel/bioc/html/GSVA.html | 开源 (Artistic-2.0) | 单样本GSEA v2.0.7 |
| survival | https://cran.r-project.org/web/packages/survival/index.html | 开源 (GPL-2) | 生存分析 v3.5-7 |
| QuPath | https://qupath.github.io/ | 开源 (Apache 2.0) | 数字病理分析 v0.5.1 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| SCLC CosMx SMI原始数据 | Zenodo | https://doi.org/10.5281/zenodo.15104582 | 本研究产生的主要数据 |
| SCLC单细胞RNA-seq (Savchuk队列) | GEO | GSE303152 | 用于验证C5/C6/C9特异性 |
| SCLC bulk RNA-seq (George队列) | 原文补充 | Table S10 | 预后验证队列1 |
| SCLC bulk RNA-seq (Jiang队列) | GEO | GSE60052 | 预后验证队列2 |
| CosMx Human Universal Cell Characterization Panel | Bruker Spatial Biology | Cat#121500041 | 1,000-plex RNA panel |
| CellMarker 2.0数据库 | 在线资源 | https://doi.org/10.1093/nar/gkac947 | 细胞类型注释参考 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| CosMx SMI数据获取 | ⚠️ 部分受限 | 需CosMx仪器和试剂的商业许可 |
| 细胞分割 | ⚠️ 部分受限 | 需AtoMx SIP软件和Cellpose分割模型 |
| 批次校正和聚类分析 | ✅ 可完全复现 | Seurat/Harmony开源可用 |
| 差异表达分析 | ✅ 可完全复现 | Seurat标准流程 |
| GO/KEGG通路富集 | ✅ 可完全复现 | clusterProfiler开源可用 |
| 细胞间相互作用分析 | ✅ 可完全复现 | 置换检验方法可自行实现，CellChat开源 |
| 细胞邻里分析 | ✅ 可完全复现 | ClusterR开源可用 |
| 公共数据整合 | ✅ 可完全复现 | GEO数据可下载，Seurat流程可复现 |
| 生存分析 | ✅ 可完全复现 | R survival包开源可用 |
| mIF验证 | ⚠️ 部分受限 | 需Opal Polaris试剂和Vectra Polaris仪器 |
| IHC验证 | ⚠️ 部分受限 | 需BenchMark ULTRA染色机和相应抗体 |

**状态说明**：
- ✅ 可完全复现（工具/代码开源可获取）
- ⚠️ 部分受限（需注册/需商业许可）
- ❌ 无法直接复现（需原始样本/仪器）
