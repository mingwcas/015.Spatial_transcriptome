# 代码与数据清单 — Slide-seq空间转录组方法比较 (cadasSTre)

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| cadasSTre分析代码 | https://github.com/YOU-k/cadasSTre | CC-BY-NC-ND 4.0 | 论文自带分析脚本 |
| scPipe | https://bioconductor.org/packages/release/bioc/html/scPipe.html | Artistic-2.0 | Bioconductor包 |
| Seurat | https://satijalab.org/seurat/ | GPL-3.0 | 空间和单细胞分析 |
| SpaceRanger | https://www.10xgenomics.com/products/space-ranger | 商业许可 | 10X官方工具 |
| BSTMatrix | https://www.bmkgene.com/ | 商业许可 | BMKGENE产品 |
| SAW | 华大基因官方渠道 | 商业许可 | Stereo-seq分析 |
| DR.SC | Bioconductor | Artistic-2.0 | 空间聚类 |
| PRECAST | GitHub (待查) | 开源 | 空间整合分析 |
| CellChat | https://github.com/sqjin/CellChat | GPL-3.0 | 细胞通讯 |
| CellPhoneDB | https://github.com/ventolab/CellphoneDB | Apache 2.0 | 细胞通讯 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| 原始计数矩阵 | 国家基因组数据中心 (NGDC) | PRJCA020621 | BioProject accession |
| cadasSTre数据集 | genographix.com | 持续更新 | 跨平台sST基准数据集 |
| 标准切片protocol | protocols.io | dx.doi.org/10.17504/protocols.io.5qpvo379dv4o/v1 | 可复现的切片流程 |
| Slide-seq V2数据 (Puck) | 公开数据集 | Puck 190926_03, 191204_01, 200115_08 | 鼠标眼球和海马体 |
| 参考基因组 | - | Mouse GRCm39 | 基因组比对参照 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 数据获取 | ✅ 可完全复现 | 数据已公开存储于NGDC |
| 标准切片protocol | ✅ 可完全复现 | 详细protocol已发布于protocols.io |
| 数据预处理 | ⚠️ 部分受限 | 部分平台需要商业软件（SpaceRanger, SAW, BSTMatrix） |
| 聚类分析 | ✅ 可完全复现 | Seurat, DR.SC, PRECAST均开源 |
| 差异表达分析 | ✅ 可完全复现 | Seurat内置FindMarkers |
| 细胞通讯分析 | ⚠️ 部分受限 | CellChat/CellPhoneDB可复现但结果不一致 |
| 标记基因验证 | ⚠️ 部分受限 | 需要原位杂交实验验证 |

**状态说明**：
- ✅ 可完全复现（工具/代码开源可获取）
- ⚠️ 部分受限（需注册/需商业许可）
- ❌ 无法直接复现（需原始样本/仪器）
