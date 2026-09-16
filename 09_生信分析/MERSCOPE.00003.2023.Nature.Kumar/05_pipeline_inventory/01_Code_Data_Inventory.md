# 代码与数据清单 — Human Breast Cell Atlas

## 一、代码清单
| 资源 | URL | 许可证 | 备注 |
|---|---|---|---|
| HBCA分析脚本 | https://github.com/navinlabcode/HumanBreastCellAtlas | 未在论文中注明 | Code availability明确提供 |
| CellPhoneDB | https://github.com/ventolab/CellPhoneDB | 开源许可见仓库 | v3，配体–受体分析 |
| SCENIC | https://scenic.aertslab.org/ | 开源工具 | 调控网络推断 |
| Protocols.io：细胞悬液 | https://www.protocols.io/view/dissociation-of-single-cell-suspensions-from-human-bp2l641bkvqe/v1 | 平台条款 | scRNA样本制备 |
| Protocols.io：核悬液 | https://www.protocols.io/view/dissociation-of-nuclear-suspensions-from-human-bre-x54v98ym4l3e/v1 | 平台条款 | snRNA样本制备 |

## 二、数据清单
| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---|---|---|---|
| HBCA转录组数据 | GEO | GSE195665 | scRNA、snRNA及空间相关数据（以仓库实际内容为准） |
| 细胞/核数据 | CELLxGENE/CZI | https://cellxgene.cziscience.com/collections/4195ab4c-20bd-4cd3-8b3d-65601277e731 | CZI整理的细胞数据 |
| 项目门户 | HBCA website | http://www.breastatlas.org | 图谱浏览与资源入口 |
| 参考基因组 | Ensembl/10x | GRCh38.p12（sc/snRNA）；GRCh38（Visium） | 比对参考 |
| CODEX/Resolve/MERSCOPE图像 | 论文/补充数据 | 论文未给独立原始图像URL | 需从GEO/作者资源核实 |

## 三、复现可行性
| 分析 | 状态 | 说明 |
|---|---|---|
| sc/snRNA定量与QC | ⚠️ 部分受限 | 代码公开，但原始FASTQ需从GEO下载并按版本配置 |
| Seurat整合/聚类 | ✅ 可完全复现 | 方法、版本和关键参数明确 |
| fgsea/SCENIC | ✅ 可完全复现 | 使用公开工具；SCENIC需按在线说明配置 |
| Visium分析 | ⚠️ 部分受限 | Space Ranger为厂商软件，需原始BCL/FASTQ及图像 |
| Resolve/MERSCOPE空间分析 | ⚠️ 部分受限 | 算法与阈值公开；原始图像/厂商软件与panel资源不完整 |
| CODEX空间蛋白 | ⚠️ 部分受限 | StarDist/Leiden方法明确，但原始多轮图像和抗体信息需补充材料 |
| CellPhoneDB互作 | ✅ 可完全复现 | CellPhoneDB v3和筛选阈值公开 |
| 组织制备/仪器成像 | ❌ 无法直接复现 | 依赖MERSCOPE、Resolve、CODEX等专用仪器和样本 |
