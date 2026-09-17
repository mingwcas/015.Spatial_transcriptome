# 代码与数据清单 — Stereo-seq V2

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|-------|------|
| SAW pipeline | https://github.com/STOmics/SAW | 商业 | STOmics官方分析流程 |
| SpaceFlow | https://github.com/hongleili/SpaceFlow | 开源 | 空间深度学习分割 |
| Spateo | https://github.com/aristoteleo/spateo-release | 开源 | 空间转录组分析，v1.1.0 |
| Scanpy | https://github.com/scverse/scanpy | 开源 | 单细胞分析，v0.10.7 |
| infercnvpy | https://github.com/icbi-lab/infercnvpy | 开源 | CNV推断，v0.5.0 |
| rMATS-turbo | https://github.com/Xinglab/rmats-turbo | 开源 | 可变剪接分析，v4.3.0 |
| MIXCR | https://github.com/milaboratory/mixcr | 开源 | 免疫repertoire，v4.5.0 |
| ST_BarcodeMap | https://github.com/STOmics/ST_BarcodeMap | 开源 | 条码匹配，v0.0.1 |
| Hotspot | https://github.com/willtownes/hotspot | 开源 | 空间自相关分析 |
| Metascape | https://metascape.org/gp/index.html | 免费在线 | GO富集分析 |
| Levenshtein | https://rapidfuzz.github.io/Levenshtein/ | 开源 | 序列距离计算 |
| ClustalW | http://www.clustal.org/clustal2/ | 开源 | 多序列比对，v2.1 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| Stereo-seq V1+V2新鲜鼠脑 | GSA | CRA018257 | 本研究 |
| Stereo-seq V2 FFPE鼠脑 | GSA | CRA016462 | 本研究 |
| Stereo-seq V2 TNBC FFPE | GSA | HRA007387 | 本研究，10例患者 |
| Stereo-seq V2 Mtb感染鼠肺 | GSA | CRA018250 | 本研究 |
| Stereo-seq V2 人结核肺 | GSA | HRA011927 | 本研究，3例患者 |
| Visium FFPE鼠脑 | 10X Genomics | https://www.10xgenomics.com/resources/datasets/mouse-brain-coronal-section-1-ffpe-2-standard | 对照数据 |
| Visium FF新鲜鼠脑 | 10X Genomics | https://www.10xgenomics.com/resources/datasets/adult-mouse-brain-coronal-section-fresh-frozen-1-standard | 对照数据 |
| MERFISH鼠脑 | Zhuang Lab | https://alleninstitute.github.io/abc_atlas_access/descriptions/Zhuang-ABCA-2.html | 细胞类型注释参考 |
| Stereo-seq V1鼠脑 | BSDC | https://doi.org/10.12412/BSDC.1699433096.20001 | 对照数据 |
| ABA ISH数据 | Allen Institute | https://mouse.brain-map.org/ | 基因表达验证 |
| Bulk RNA-seq 鼠 hippocampus/cortex | GEO | GEO: GSE206562 | 对照数据 |
| Bulk RNA-seq Mtb感染鼠 | GEO | GEO: GSE107991 | BCR验证 |
| Bulk RNA-seq TB患者PBMC | GEO | GEO: GSE107995 | BCR验证 |
| Mtb基因组 | NCBI | ASM19595v2 (GCF_000195955.2) | 病原体参考 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| FFPE文库构建 | ⚠️ 部分受限 | 需商业试剂盒(Stereo-seq Transcriptomics Set for FFPE) |
| 原始数据处理 | ✅ 可完全复现 | SAW开源，STAR/Scanpy等工具均可获取 |
| 空间聚类分析 | ✅ 可完全复现 | SpaceFlow/Spateo/Scanpy均开源 |
| 细胞分割 | ✅ 可完全复现 | Spateo开源可用 |
| CNV分析 | ✅ 可完全复现 | infercnvpy开源 |
| 可变剪接分析 | ✅ 可完全复现 | rMATS-turbo开源 |
| BCR库组装 | ✅ 可完全复现 | MIXCR开源 |
| Mtb基因组比对 | ✅ 可完全复现 | 参考基因组公开 |
| GO富集分析 | ✅ 可完全复现 | Metascape免费在线 |
| 图像分析(U-Net) | ⚠️ 部分受限 | 需预训练模型 |

**状态说明**：
- ✅ 可完全复现（工具/代码开源可获取）
- ⚠️ 部分受限（需注册/需商业许可）
- ❌ 无法直接复现（需原始样本/仪器）
