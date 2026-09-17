# 代码与数据清单 — 多技术整合解析乳腺癌肿瘤微环境

---

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| janesick_nature_comms_2023_companion | https://github.com/10XGenomics/janesick_nature_comms_2023_companion | MIT License | 论文配套代码，含完整分析流程 |
| Cell Ranger | https://www.10xgenomics.com/support/software/cell-ranger | 商业许可 | scFFPE-seq数据处理 |
| Space Ranger | https://www.10xgenomics.com/support/software/space-ranger | 商业许可 | Visium CytAssist数据处理 |
| Xenium Ranger | https://www.10xgenomics.com/support/software/xenium-ranger | 商业许可 | Xenium In Situ数据处理 |
| Loupe Browser | https://www.10xgenomics.com/support/software/loupe-browser | 商业许可 | 交互式数据可视化 |
| Xenium Explorer | https://www.10xgenomics.com/support/software/xenium-explorer | 商业许可 | Xenium数据交互式浏览 |
| scanpy | https://github.com/scverse/scanpy | BSD License | 单细胞分析（Python） |
| Seurat | https://github.com/satijalab/seurat | MIT License | 单细胞分析（R） |
| spacexr (RCTD) | https://github.com/dmcable/spacexr | MIT License | 空间反卷积分析 |
| monet | https://github.com/10XGenomics/monet | - | 细胞邻域分析 |
| OpenCV (cv2) | https://github.com/opencv/opencv | Apache 2.0 | 图像配准和处理 |

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| 原始测序数据 | GEO | GSE243280 | scFFPE-seq、Visium、Xenium原始数据 |
| 10x Genomics预览数据集 | 10x Genomics官网 | https://www.10xgenomics.com/resources/datasets | 预处理后的示例数据 |
| 交互式数据浏览器 | 10x Genomics | https://www.10xgenomics.com/resources/datasets | 可视化探索平台 |
| Chromium scFFPE-seq数据 | GEO | GSE243280 | FFPE单细胞RNA测序数据 |
| Visium CytAssist数据 | GEO | GSE243280 | 全转录组空间表达数据 |
| Xenium In Situ数据 | GEO | GSE243280 | 313基因靶向原位数据 |
| 图像数据 | GEO | GSE243280 | H&E染色和荧光图像 |
| 元数据 | 论文补充材料 | Supplementary Data | 样本信息和实验设计 |
| 313基因panel | 10x Genomics | Xenium In Situ平台 | 靶向基因列表 |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 原始数据获取 | ✅ 可完全复现 | GEO: GSE243280公开可用 |
| Cell Ranger/scFFPE-seq处理 | ⚠️ 部分受限 | 商业软件，需10x Genomics许可 |
| Space Ranger/Visium处理 | ⚠️ 部分受限 | 商业软件，需10x Genomics许可 |
| Xenium Ranger/Xenium处理 | ⚠️ 部分受限 | 商业软件，需10x Genomics许可 |
| scanpy单细胞分析 | ✅ 可完全复现 | 开源工具，pip/conda安装 |
| Seurat单细胞分析 | ✅ 可完全复现 | 开源工具，CRAN安装 |
| spacexr/RCTD反卷积 | ✅ 可完全复现 | 开源工具，GitHub安装 |
| monet邻域分析 | ✅ 可完全复现 | 开源工具 |
| OpenCV图像配准 | ✅ 可完全复现 | 开源工具，pip安装 |
| Loupe Browser可视化 | ⚠️ 部分受限 | 商业软件，需10x Genomics许可 |
| Xenium Explorer可视化 | ⚠️ 部分受限 | 商业软件，需10x Genomics许可 |
| 配套代码运行 | ✅ 可完全复现 | GitHub公开，MIT许可 |
| **完整复现** | ⚠️ **部分受限** | 需10x Genomics商业软件许可 |

---

## 状态说明

- ✅ **可完全复现**：工具/代码开源可获取
- ⚠️ **部分受限**：需注册/需商业许可
- ❌ **无法直接复现**：需原始样本/仪器

---

## 数据访问详情

### GEO数据集 (GSE243280)

数据集包含以下子系列：
- **GSE243279**：Chromium scFFPE-seq原始数据
- **GSE243278**：Visium CytAssist原始数据  
- **GSE243277**：Xenium In Situ原始数据
- **GSE243276**：图像数据

访问链接：https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE243280

### 10x Genomics预览数据集

10x Genomics提供了预处理后的示例数据，可用于快速测试分析流程：
- Chromium scFFPE-seq示例数据
- Visium CytAssist示例数据
- Xenium In Situ示例数据

访问链接：https://www.10xgenomics.com/resources/datasets

---

## 代码复现备注

1. **商业软件**：Cell Ranger、Space Ranger、Xenium Ranger需从10x Genomics获取许可
2. **配套代码**：GitHub仓库提供了完整的分析流程和文档
3. **环境配置**：建议使用conda环境管理Python依赖
4. **R包依赖**：Seurat、spacexr等R包需从CRAN或GitHub安装
5. **图像配准**：OpenCV版本需与代码兼容（cv2 4.5.4）
6. **内存需求**：大型空间数据处理需要充足内存（建议>32GB）
7. **计算资源**：单细胞聚类和反卷积分析计算密集，建议使用高性能计算集群
8. **参数调整**：聚类分辨率、反卷积参数等需根据数据特性调整

---

## 论文配套资源

### GitHub仓库结构
```
janesick_nature_comms_2023_companion/
├── notebooks/          # Jupyter notebooks
├── scripts/            # 分析脚本
├── data/               # 示例数据
├── figures/            # 图表生成代码
└── README.md           # 使用说明
```

### 交互式数据浏览器
10x Genomics提供了在线交互式数据浏览器，可直接探索论文中的数据：
- 支持基因表达查询
- 细胞类型注释浏览
- 空间坐标可视化
- 多平台数据对比

---

## 技术平台详情

### Chromium Single Cell Gene Expression Flex (scFFPE-seq)
- **用途**：FFPE样本单细胞RNA测序
- **分辨率**：单细胞水平
- **基因覆盖**：全转录组
- **样本类型**：FFPE组织

### Visium CytAssist
- **用途**：全转录组空间表达分析
- **分辨率**：55 μm spot直径
- **基因覆盖**：全转录组
- **样本类型**：FFPE/Frozen组织

### Xenium In Situ
- **用途**：靶向原位基因表达分析
- **分辨率**：亚细胞水平
- **基因覆盖**：313基因panel
- **样本类型**：FFPE/Frozen组织

---

## 引用信息

如果使用本论文的数据或代码，请引用：

```bibtex
@article{janesick2023high,
  title={High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis},
  author={Janesick, Amanda and Shelansky, Robert and Gottscho, Andrew D. and Wagner, Florian and Williams, Stephen R. and Rouault, Morgane and Beliakoff, Ghezal and Morrison, Carolyn A. and Oliveira, Michelli F. and Sicherman, Jordan T. and others},
  journal={Nature Communications},
  volume={14},
  number={1},
  pages={7676},
  year={2023},
  publisher={Nature Publishing Group},
  doi={10.1038/s41467-023-43458-x}
}
```
