# 代码与数据清单 — MERFISH 原始方法

> 论文：Chen et al., Science 348, aaa6090 (2015) | DOI: [10.1126/science.aaa6090](https://doi.org/10.1126/science.aaa6090)

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| MERFISH analysis（ZhuangLab） | https://github.com/ZhuangLab/MERFISH_analysis | 见仓库 | 后续分析代码与 MERFISH 数据处理生态；本文原始实现为论文自带 |
| BLAST+ | https://blast.ncbi.nlm.nih.gov/Blast.cgi | 公共软件 | 引物/readout 正交性与人类基因组脱靶筛选 |
| Cufflinks | http://cole-trapnell-lab.github.io/cufflinks/ | 见项目 | bulk RNA-seq isoform abundance 定量 |
| Gene Ontology | http://geneontology.org | CC BY 4.0 | 基因群功能富集 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| 140-gene MHD4 codebook | 论文补充表 | Table S1 | 16-bit，140 个码字 |
| 1001-gene MHD2 codebook | 论文补充表 | Table S3 | 14-bit，1001 个码字 |
| Encoding probe 模板序列 | 论文补充表 | Table S5 | 编码探针模板与引物序列 |
| 140-gene MERFISH 数据 | 论文补充材料 | Science supplementary files | IMR90，~400 cells，7 个独立实验 |
| 1001-gene MERFISH 数据 | 论文补充材料 | Science supplementary files | IMR90，~200 cells，3 个独立实验 |
| Bulk RNA-seq | 论文补充材料 | Science supplementary files | 用于与 MERFISH 表达相关性比较 |
| smFISH 验证数据 | 论文补充材料 | Science supplementary files | 15 个基因，48 probes/RNA |
| IMR90 细胞 | ATCC | https://www.atcc.org/products/ccl-186 | 人胚肺成纤维细胞系 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| MHD4/MHD2 码本生成与理论性能 | ✅ 可完全复现 | 论文给出编码规则、位数、汉明距离与误差率；Table S1/S3 可用 |
| Encoding probe 设计 | ✅ 可完全复现 | 模板序列在 Table S5；PCR/IVT/逆转录流程已描述 |
| 140/1001 基因实验数据分析 | ⚠️ 部分受限 | 需要原始多轮荧光图像、定制流体系统与探针库；补充数据可用于部分再分析 |
| 单分子定位与解码 | ⚠️ 部分受限 | 算法原理公开，但原始代码与图像处理参数不完整 |
| smFISH 验证 | ⚠️ 部分受限 | 需合成 Biosearch Quasar 670 探针并建立成像系统 |
| Bulk RNA-seq 相关性 | ✅ 可完全复现 | 若取得补充 RNA-seq 数据，Cufflinks 与相关性分析可重跑 |
| UPGMA / GO 富集 | ✅ 可完全复现 | 输入表达矩阵与公开 GO 数据库即可 |
| MERFISH 实验整体 | ❌ 无法直接复现 | 需自定义显微镜（Olympus IX71）、EMCCD、流体/杂交系统、20 小时多轮成像与专用探针 |

**状态说明**：
- ✅ 可完全复现（工具/代码开源可获取）
- ⚠️ 部分受限（需注册/需商业许可）
- ❌ 无法直接复现（需原始样本/仪器）
