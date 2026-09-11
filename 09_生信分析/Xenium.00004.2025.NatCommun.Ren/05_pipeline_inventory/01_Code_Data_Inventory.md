# 代码与数据清单 — Xenium 5K空间转录组基准测试

---

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| SPATCH分析代码 | https://github.com/zenglab-pku/SPATCH | MIT License | 论文自带，含数据处理和分析全流程 |
| napari-cosmx | https://github.com/Nanostring-Biostats/CosMx-Analysis-Scratch-Space | - | CosMx图像拼接 |
| SELINA | v.0.1 | - | 细胞注释转移 |
| Celltypist | v.1.6.3 | - | 细胞注释转移 |
| Spoint | v.1.1.7 | - | 细胞注释转移 |
| Tangram | v.1.0.4 | - | 细胞注释转移 |
| TACCO | v.0.4.0.post1 | - | 细胞注释转移 |
| DoubletFinder | v.2.0.3 | - | 双细胞检测（CRAN） |
| Seurat | v.5.1.0 | - | 单细胞分析（R） |
| scanpy | v.1.10.3 | BSD | 空间转录组分析（Python） |
| clusterProfiler | v.4.6.2 | - | GO通路富集（R） |
| CellCharter | - | - | 空间聚类分析 |

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| 原始测序数据 | GSA/National Genomics Data Center | HRA011129 | 原始测序reads |
| 图像数据 | BioImage Archive | S-BIAD1900 | 原始显微镜图像 |
| 处理后数据 | SPATCH网站 | http://spatch.pku-genomics.org/ | 可视化和下载 |
| CODEX数据 | SPATCH网站 | http://spatch.pku-genomics.org/ | 蛋白表达和注释 |
| ST数据 | SPATCH网站 | http://spatch.pku-genomics.org/ | 空间转录组数据 |
| 辅助数据1 | 论文Supplementary | Supplementary Data 1 | 患者临床信息 |
| 辅助数据2 | 论文Supplementary | Supplementary Data 2 | 样本处理时间线 |
| 辅助数据3 | 论文Supplementary | Supplementary Data 3 | 平台技术比较 |
| 辅助数据4 | 论文Supplementary | Supplementary Data 4 | 基因面板列表 |
| 辅助数据5 | 论文Supplementary | Supplementary Data 5 | 基因面板重叠 |
| 辅助数据6 | 论文Supplementary | Supplementary Data 6 | 互斥标记基因对 |
| 辅助数据7 | 论文Supplementary | Supplementary Data 7 | CODEX抗体稀释比例 |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 原始数据获取 | ✅ 可完全复现 | GSA: HRA011129; BioImage Archive: S-BIAD1900 |
| 处理后数据获取 | ✅ 可完全复现 | SPATCH网站提供完整下载 |
| 细胞ranger/scRNA-seq分析 | ✅ 可完全复现 | cellranger v.7.0.0为商业软件但可获取 |
| spaceranger/Visium HD分析 | ⚠️ 部分受限 | spaceranger v.3.0.0商业许可需10x Genomics |
| SAW/Stereo-seq分析 | ⚠️ 部分受限 | SAW v.8.0商业许可需STOmics/BGI |
| Xenium Onboard Analysis | ⚠️ 部分受限 | 商业软件，10x Genomics许可 |
| Atomx/CosMx解码 | ⚠️ 部分受限 | 商业软件，NanoString许可 |
| napari-cosmx图像拼接 | ✅ 可完全复现 | 开源工具 |
| CODEX分析（QuPath/StarDist） | ✅ 可完全复现 | 开源工具 |
| ST注释转移工具 | ✅ 可完全复现 | 均为开源 |
| scRNA-seq/Seurat分析 | ✅ 可完全复现 | Seurat开源，cellranger商业 |
| 图像配准（SimpleITK） | ✅ 可完全复现 | 开源工具 |
| 空间聚类/通路分析 | ✅ 可完全复现 | 开源工具 |
| **完整复现** | ⚠️ **部分受限** | 需多个商业平台软件许可 |

---

## 状态说明

- ✅ **可完全复现**：工具/代码开源可获取
- ⚠️ **部分受限**：需注册/需商业许可
- ❌ **无法直接复现**：需原始样本/仪器

---

## SPATCH网站功能

SPATCH（http://spatch.pku-genomics.org/）提供以下功能：

1. **数据可视化**：交互式浏览基因表达和细胞类型注释
2. **数据下载**：原始和处理后数据均可下载
3. **跨平台比较**：支持四平台数据的可视化对比
4. **注释查询**：查看各类细胞的标记基因表达
5. **空间坐标文件**：提供转录本水平空间坐标文件
6. **形态学图像**：高分辨率H&E和免疫荧光图像
7. **分割掩膜**：平台专用pipeline和人工注释的分割结果

---

## 代码复现备注

1. **商业软件**需从相应厂商获取许可（10x Genomics, STOmics/BGI, NanoString）
2. **SPATCH GitHub仓库**（https://github.com/zenglab-pku/SPATCH）提供了主要分析流程
3. **图像配准**使用SimpleITK手动标注地标，实验记录对于复现很重要
4. **CODEX分类器**需要手动标注训练数据，需参考原文描述的训练过程
5. **阈值参数**在方法部分有详细描述，可直接用于复现
