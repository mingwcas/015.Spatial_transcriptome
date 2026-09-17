# 代码与数据清单 — 蝾螈大脑再生空间转录组研究

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| ARTISTA (分析代码) | https://github.com/BGI-DEV-REG/ARTISTA | - | 论文自带分析代码 |
| SAW pipeline (原始数据处理) | https://github.com/BGIResearch/SAW | - | Stereo-seq官方处理流程 |
| Dynamo (RNA velocity) | https://github.com/aristoteleo/dynamo-release | - | 开源单细胞向量场分析 |
| Seurat | https://satijalab.org/seurat/ | MIT | 单细胞分析标准工具 |
| Monocle2 | http://cole-trapnell-lab.github.io/monocle-release/ | - | 伪时间分析 |
| Monocle3 | https://cole-trapnell-lab.github.io/monocle3/ | - | 伪时间分析 |
| scikit-image | https://scikit-image.org/ | BSD | 图像分割 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| 原始测序数据 | CNGB Nucleotide Sequence Archive (CNSA) | CNP0002068 | 蝾螈端脑空间转录组原始数据 |
| 交互式数据库 | https://db.cngb.org/stomics/artista/ | - | 可视化探索和下载 |
| 补充表格 | Science期刊Supplementary Materials | DOI: 10.1126/science.abp9444 | Table S1-S7 |
| 参考基因组 | - | - | 蝾螈基因组(需自行获取) |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| Stereo-seq数据获取 | ⚠️ 部分受限 | 需注册CNGB账号下载原始数据 |
| SAW pipeline运行 | ⚠️ 部分受限 | 开源但依赖BGI特定试剂盒和芯片 |
| Seurat分析 | ✅ 可完全复现 | 开源工具，标准流程 |
| RNA velocity分析 | ✅ 可完全复现 | Dynamo开源可用 |
| Monocle伪时间分析 | ✅ 可完全复现 | 开源工具可用 |
| 细胞注释验证 | ⚠️ 部分受限 | 需RNA ISH实验验证 |
| BrdU追踪实验 | ❌ 无法直接复现 | 需活体动物实验 |

---

## 状态说明

- ✅ **可完全复现**（工具/代码开源可获取）
- ⚠️ **部分受限**（需注册/需商业许可/需原始样本）
- ❌ **无法直接复现**（需原始样本/仪器/动物实验）

---

## 数据获取链接

- **论文DOI**: [10.1126/science.abp9444](https://doi.org/10.1126/science.abp9444)
- **代码仓库**: [ARTISTA GitHub](https://github.com/BGI-DEV-REG/ARTISTA)
- **SAW pipeline**: [SAW GitHub](https://github.com/BGIResearch/SAW)
- **交互式数据库**: [STORMS](https://db.cngb.org/stomics/artista/)
- **原始数据**: [CNGB CNSA](https://db.cngb.org/cnsa/) (Accession: CNP0002068)
