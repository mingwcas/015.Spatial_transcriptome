# 代码与数据清单 — Barcoded solid-phase RNA capture for Spatial Transcriptomics

## 一、代码清单
| 资源 | URL | 许可证 | 备注 |
|---|---|---|---|
| ST Pipeline | https://github.com/SpatialTranscriptomicsResearch/st_pipeline | 论文称open-source；具体LICENSE需以仓库为准 | FASTQ合并、trim、STAR、计数、demultiplex、UMI；需STAR和GFF3 |
| ST Spot Detector | https://github.com/SpatialTranscriptomicsResearch/st_spot_detector | 论文称open-source；具体LICENSE需以仓库为准 | 图像配准、spot/tissue检测 |
| Spot Detector Singularity | https://github.com/SpatialTranscriptomicsResearch/st_spot_detector_singularity | 仓库许可 | 可本地容器部署 |
| ST Viewer | https://github.com/jfnavarro/st_viewer | 论文称open-source；具体LICENSE需以仓库为准 | 桌面可视化（Linux/Mac/Windows） |
| ST Viewer manual | https://github.com/jfnavarro/st_viewer/wiki | 文档 | 使用说明 |
| STAR | https://github.com/alexdobin/STAR | 开源 | ST Pipeline所需比对器 |
| Protocol video | https://www.youtube.com/watch?v=rz-Evzk94o0 | 平台视频 | 实验流程 |

## 二、数据清单
| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---|---|---|---|
| 原始测序FASTQ | 论文未提供 accession | 未声明 | 每index合并为R1/R2；需自备样本 |
| 组织明场图 | 实验产生 | 无公共链接 | JPG，20× |
| Cy3空间spot图 | 实验产生 | 无公共链接 | JPG，与明场图同区域 |
| spot/gene矩阵 | ST Pipeline输出 | 无公共链接 | TSV；行spot、列gene、值unique molecules |
| 分子空间位置 | ST Pipeline输出 | 无公共链接 | BED |
| 处理日志 | ST Pipeline输出 | 无公共链接 | 每步统计 |

## 三、复现可行性
| 分析 | 状态 | 说明 |
|---|---|---|
| ST Pipeline计算 | ✅ 可完全复现 | 代码公开；需R1/R2、STAR index、GFF3、ids-file |
| 图像配准 | ✅ 可完全复现 | Spot Detector代码/容器公开；需两类图像 |
| Viewer分析 | ✅ 可完全复现 | ST Viewer仓库和手册公开 |
| 原始样本建库 | ⚠️ 部分受限 | 需新鲜冷冻组织、商业微阵列、实验设备和组织优化 |
| 论文典型Fig.7 | ❌ 无法直接复现 | 文中未给原始FASTQ、图像或accession |
| 组织优化 | ⚠️ 部分受限 | 需要每类组织重新确定pepsin/去组织条件 |

> 依据：PDF pp.5–7、11、17、27–28、31–34；metadata中明确DOI但未扫描到Data/Code availability段落，因此不臆造公共数据 accession。
