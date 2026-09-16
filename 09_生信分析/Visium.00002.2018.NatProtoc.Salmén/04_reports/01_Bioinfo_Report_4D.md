# 四维度生信分析报告 — Barcoded solid-phase RNA capture for Spatial Transcriptomics

> 论文：Salmén et al., *Nature Protocols* (2018), DOI [10.1038/s41596-018-0045-2](https://doi.org/10.1038/s41596-018-0045-2)；平台：Spatial Transcriptomics/Visium前身；依据：全文 Methods、Fig.1–7 captions。

## 维度一：分析方法 / Methods
| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---|---|---|---|
| 组织学 | 冷冻切片、4% formaldehyde固定、H&E、20×明场 | cryostat/显微镜 | 形态参考图 |
| 参数优化 | Cy3-dCTP cDNA footprint、pepsin梯度 | 532 nm扫描 | 选择强且不扩散条件 |
| 空间捕获 | 条码oligo-dT、表面RT、proteinase K去组织 | Superscript III | spot级空间cDNA |
| 建库 | USER释放、二链、CEL-Seq样T7 IVT、接头连接/二次RT | beads、Bioanalyzer | aRNA和paired-end文库 |
| QC/index | qPCR峰值−3/4定PCR循环；Qubit/Bioanalyzer | qPCR、Qubit | 成品约400–500 bp |
| 计算计数 | trimming→STAR比对/计数→barcode demultiplex→UMI filtering | ST Pipeline + STAR | TSV/BED/log |
| 图像定位 | 明场/Cy3配准、spot/tissue detection | ST Spot Detector | 坐标+3×3 affine matrix |
| 可视化 | spot矩阵与图像整合 | ST Viewer、R、Python | 空间探索分析 |

## 维度二：结果图表
| 图 | 内容摘要 | 主要图形类型 |
|---|---|---|
| Fig.1 | 阵列探针与实验总览、明场/spot图 | 示意图+显微图 |
| Fig.2 | 嗅球通透化优化 | 明场/荧光图 |
| Fig.3 | aRNA、qPCR、成品文库QC | Bioanalyzer/qPCR |
| Fig.4 | Day 1–6实验流程及暂停点 | 流程图 |
| Fig.5 | FASTQ至计数、图像配准、可视化 | 计算流程图 |
| Fig.6 | 嗅球/乳腺癌细胞密度与组织缺陷 | 明场图 |
| Fig.7 | genes和unique transcripts的spot分布 | 直方图+空间图 |

## 维度三：Pipelines
| 阶段 | 工具 | 版本 | 开源/商业 |
|---|---|---|---|
| FASTQ处理/计数 | ST Pipeline | 论文推荐；版本未在本文给出 | 开源 |
| 比对 | STAR | 论文引用v2概念；版本未给出 | 开源 |
| 图像配准 | ST Spot Detector | 论文推荐；版本未给出 | 开源web工具 |
| 可视化 | ST Viewer | 版本未给出 | 开源桌面工具 |
| 高级分析 | R/Python | 版本未给出 | 开源 |

## 维度四：算法与 AI
| 算法/模型 | 类型 | 用途 |
|---|---|---|
| quality trimming | 序列预处理 | 去除低质量序列 |
| STAR genome alignment | splice-aware比对 | reads定位到基因组 |
| gene counting | 计数算法 | 生成基因计数 |
| barcode demultiplexing | 条码解析 | 将分子分配到空间spot |
| UMI filtering | 去重复 | 去除扩增重复分子 |
| affine transform | 几何配准 | 对齐组织和spot图 |
| 限制/风险 | 非AI模型 | 100 μm spot通常5–100细胞；poly(A)偏好、FFPE灵敏度受限；结果依赖组织质量和细胞密度；作者涉及技术专利。 |
