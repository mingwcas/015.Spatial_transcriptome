# 代码与数据清单 — GeoMx_dMMR_CRC_Immunotherapy

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|-------|------|
| STAR | https://github.com/alexdobin/STAR | GPL v3 | Bulk RNA-seq比对 |
| RSEM | https://github.com/deweylab/RSEM | GPL v3 | 表达量定量 |
| CellRanger | https://support.10xgenomics.com/single-cell-gene-expression/software | 商业许可 | 10×单细胞测序分析（需购买许可证） |
| Seurat | https://satijalab.org/seurat/ | R (GPL v3) | 单细胞数据分析 |
| Harmony | https://portals.broadinstitute.org/hartmann/Harmony/ | BSD | 单细胞批次校正 |
| CellChat | https://github.com/sqjin/CellChat | R (GPL v3) | 细胞间通讯分析 |
| phenoptr | https://github.com/PerkinElmer/phenoptr | 商业许可 | 空间分析（R包，需商业许可） |
| inForm | https://www.perkinelmer.com/informatics/products/image-analysis/inform | 商业许可 | mIHC图像分析软件 |
| Opal Polaris | https://www.akoyabio.com/phenoclear/opal-polaris/ | 商业许可 | 多重荧光染色试剂盒 |
| PD-L1 IHC 22C3 pharmDx | https://www.agilent.com/en/product/pharmaceutical-diagnostics/pd-l1-ihc-22c3-pharmdx | 商业许可 | PD-L1免疫组化检测 |
| Dako Autostainer Link 48 | https://www.agilent.com/en/product/automated-ihc-ish/dako-autostainer-link-48 | 商业许可 | 自动免疫组化染色仪 |
| R base stats | https://cran.r-project.org/ | GPL v2 | 统计分析 |
| **论文自带代码** | 无 | - | 论文未声明代码公开 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| Bulk RNA-seq数据 | 需联系作者 | 不公开 | 需机构伦理批准后申请获取 |
| Single-cell RNA-seq数据 | 需联系作者 | 不公开 | 需机构伦理批准后申请获取 |
| 多重免疫组化图像 | 需联系作者 | 不公开 | 仅正文图3展示部分数据 |
| CT影像 | 需联系作者 | 不公开 | 治疗前后对比图像 |
| 补充材料 | https://doi.org/10.1093/immadv/ltag001 | 可下载 | 包含补充Figure S2-S8 |
| Crossref元数据 | https://api.crossref.org/works/10.1093/immadv/ltag001 | 公开API | 论文基础元数据 |
| PDF全文 | 原始PDF | 本地存储 | /tmp目录下处理 |
| 政策 | Creative Commons Attribution (CC BY 4.0) | https://creativecommons.org/licenses/by/4.0/ | 可自由共享和改编，需注明来源 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| Bulk RNA-seq比对定量 | ⚠️ 部分受限 | STAR、RSEM为开源工具，但原始数据需向作者申请 |
| 单细胞RNA-seq分析 | ⚠️ 部分受限 | CellRanger需商业许可，Seurat/Harmony开源可用，原始数据需申请 |
| 多重免疫组化 | ⚠️ 部分受限 | Opal Polaris、inForm、phenoptr均为商业产品，需采购 |
| 空间邻近分析 | ⚠️ 部分受限 | 商业软件依赖，商业许可需购买 |
| CellChat通讯分析 | ✅ 可完全复现 | R包开源，示例数据可从CellChat官网获取 |
| EPIC反卷积 | ✅ 可完全复现 | R包开源，可使用其他bulk RNA-seq数据集复现 |
| 统计检验 | ✅ 可完全复现 | R base stats免费开源 |
| 免疫组化dMMR/PD-L1 | ⚠️ 部分受限 | Dako平台和22C3抗体为商业产品 |

### 状态说明

- ✅ **可完全复现**：工具/代码开源可获取
- ⚠️ **部分受限**：需注册/需商业许可，或数据需向作者申请
- ❌ **无法直接复现**：需原始样本/仪器

### 整体评估

**复现可行性：⚠️ 部分受限**

本研究的关键湿实验（mIHC、scRNA-seq建库测序）依赖商业平台和试剂，原始数据未公开存储库，需联系作者获取。干分析流程中的开源工具（Seurat、Harmony、CellChat）可完整复现方法学，但需准备类似的空间蛋白组学或单细胞转录组数据。

### 建议

1. 联系作者获取Bulk和scRNA-seq原始数据
2. 使用开源CellChat工具进行方法学复现
3. 如需空间蛋白组学数据，考虑使用akoya或类似商业平台
