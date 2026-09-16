# 代码与数据清单 — Xenium 探针脱靶结合 (OPT)

> 论文：Hallinan et al., eLife 14, RP107070 (2026) | DOI: [10.7554/eLife.107070](https://doi.org/10.7554/eLife.107070)

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| OPT (Off-target Probe Tracker) | https://github.com/JEFworks-Lab/off-target-probe-tracker | 开源（见仓库 LICENSE） | **本文核心自研工具**，Python；含 flip / track / stat / all 四模块 |
| OPT 归档快照 | https://archive.softwareheritage.org/swh:1:dir:ce72a180d5114de1d9a91109270eb45cef1a0dc8 | — | Software Heritage 永久归档，rev `8ca930d2` |
| nucmer (MUMmer) | https://github.com/mummer4/mummer | GPL | 序列比对引擎，OPT 的底层依赖 |
| gffread | https://github.com/gpertea/gffread | MIT | 从注释 + 基因组提取转录本序列 |
| STalign | https://github.com/JEFworks-Lab/STalign | MIT | 空间转录组结构对齐（v1.0.1） |
| Harmony | https://github.com/immunogenomics/harmony | GPL-3.0 | 单细胞批次整合（v1.2.3） |
| Scanpy / Seurat 生态 | https://scanpy.readthedocs.io | BSD-3 | PCA / UMAP / Leiden 等常规单细胞分析 |
| pyfaidx | https://github.com/mdshw5/pyfaidx | BSD-3 | 从 BED 坐标提取基因组序列，生成探针 FASTA |
| Integrative Genomics Viewer (IGV) | https://igv.org | MIT | 目视核对探针-转录本比对 |
| STcompare（思路参考） | https://github.com/JEFworks-Lab/STcompare | — | 跨平台差异空间模式基因比较方法学参考 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| Xenium 人乳腺数据集 | 10x Genomics | https://www.10xgenomics.com/products/xenium-in-situ/preview-dataset-human-breast | Janesick et al. 乳腺癌组织块，Xenium v1 面板 |
| Visium CytAssist 数据集 | 10x Genomics | 同上（同一页面） | 连续切片，原始 4992 spots × 18,085 基因 |
| Chromium 3′ scRNA-seq 数据集 | 10x Genomics | 同上（同一页面） | 12,388 细胞 × 36,601 基因 |
| Xenium 乳腺面板探针靶序列 FASTA | 论文补充材料 | **Supplementary file 1** | 2582 条 40 bp 探针靶序列，靶向 313 基因；由 10x Genomics 提供 |
| GENCODE basic v47 注释 | GENCODE | https://www.gencodegenes.org/human/ | GRCh38，10x 探针设计所用注释类型 |
| GENCODE comprehensive v47 注释 | GENCODE | https://www.gencodegenes.org/human/ | 含大量低质量注释，用于完整性分析 |
| RefSeq v110 注释 | NCBI | https://www.ncbi.nlm.nih.gov/refseq/ | GRCh38 |
| CHESS v3.1.3 注释 | CHESS | https://ccb.jhu.edu/chess/ | 映射到 GRCh38.p12 |
| 参考基因组 GRCh38 | Ensembl/NCBI | https://www.ensembl.org | p14（CHESS 用 p12）；剔除 alternative scaffolds |
| HuBMAP 胎盘定制面板 | HuBMAP Portal | https://portal.hubmapconsortium.org/browse/dataset/28fe8e4ac8a4193f82fdd9f4d4eb0bb2 | BED 格式，300 靶基因 |
| HuBMAP 多组织（心/肾/肺）定制面板 | HuBMAP Portal | https://portal.hubmapconsortium.org/browse/dataset/6f597ca43db80f2499443f5c5bfac97c | BED 格式，300 靶基因 |
| HuBMAP 胎盘 bulk RNA-seq | HuBMAP | https://doi.org/10.35079/HBM549.BBBQ.445 | 用于评估脱靶基因组织表达 |
| HuBMAP 心脏 scRNA-seq | HuBMAP | https://doi.org/10.35079/HBM378.WGXD.394 | 同上 |
| HuBMAP 肾脏 scRNA-seq | HuBMAP | https://doi.org/10.35079/HBM793.TLPP.486 | 同上 |
| HuBMAP 肺 scRNA-seq | HuBMAP | https://doi.org/10.35079/HBM826.BQLS.392 | 同上 |
| OPT 全量输出（所有公开 10x 面板） | 论文补充材料 | **Supplementary file 10**（ZIP） | 作者对全部公开 10x Genomics 预制面板运行 OPT 的结果 |
| 各分析完整 OPT 输出 | 论文补充材料 | Supplementary files 2–9 | 含跨注释结果与 HuBMAP 面板结果 |
| MDAR checklist | 论文补充材料 | eLife 附件 | 材料设计分析报告清单 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| OPT 脱靶预测（乳腺面板） | ✅ 可完全复现 | OPT 开源；探针 FASTA 见 Supplementary file 1；4 套注释公开可下载 |
| 跨注释一致性分析 | ✅ 可完全复现 | 仅需下载 4 套注释 + gffread，全部公开 |
| STalign 空间对齐 | ✅ 可完全复现 | STalign v1.0.1 开源；参数（a=2500, epV=1, niter=2000, sigmaA/B/M/P 等）论文已完整给出；输入数据 10x 公开 |
| Visium/Xenium 表达比较 | ✅ 可完全复现 | 两数据集均 10x 公开下载；RMSE/Pearson 计算逻辑论文已述 |
| scRNA-seq 整合比较 | ✅ 可完全复现 | Chromium 数据公开；Harmony v1.2.3 参数（30 PCs, theta=8）已给出 |
| HuBMAP 定制面板评估 | ⚠️ 部分受限 | 面板 BED 与 RNA-seq 均通过 HuBMAP Portal 公开，但需注册 Portal 账号并按 HuBMAP 数据使用条款访问 |
| IGV 比对可视化 | ✅ 可完全复现 | 输入序列与比对结果均可重建 |
| Xenium 原始成像数据再分析 | ❌ 无法直接复现 | 需 10x Xenium 仪器与配套试剂；本文未做新实验，但若要从原始图像验证脱靶需重新成像 |
| 探针脱靶的实验验证 | ❌ 无法直接复现 | 需定制探针、Xenium 仪器与配对样本，本文未开展 |

**状态说明**：
- ✅ 可完全复现（工具/代码开源可获取）
- ⚠️ 部分受限（需注册/需商业许可）
- ❌ 无法直接复现（需原始样本/仪器）
