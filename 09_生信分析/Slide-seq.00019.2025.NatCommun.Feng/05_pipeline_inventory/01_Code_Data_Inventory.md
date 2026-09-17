# 代码与数据清单 — Molecular cartography of the human down syndrome and trisomic mouse brain

---

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|-------|------|
| 微环境分析代码 | https://github.com/annaminyifeng/Molecular-Cartography-of-DS-Brain | - | GitHub |
| Code Ocean | https://doi.org/10.24433/CO.4591687.v2 | - | 可复现结果 |
| Seurat | https://www.satijalab.org/seurat | 开源(R PACKAGE) | snRNA-seq分析 |
| SCTransform | Seurat内置 | 开源 | 标准化 |
| Harmony | https://github.com/immunogenomics/harmony | 开源 | 批次校正 |
| RCTD | https://github.com/dmcable/spacexr | 开源 | 空间去卷积 |
| scVelo | https://scvelo.org/ | 开源 | RNA速率分析 |
| MAST | https://github.com/RGLab/MAST | 开源 | 差异表达分析 |
| ClusterProfiler | https://yulab-smu.top/biomedical-knowledge-mining-book/ | 开源 | 通路富集分析 |
| SoloTE | https://github.com/ValdebenitoMaturana/SoloTE | 开源 | TE分析 |
| Spectronaut | https://biognosys.com/software/spectronaut/ | 商业 | 质谱数据分析 |
| Cellpose | https://www.cellpose.org/ | 开源 | 细胞分割 |

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| 人类snRNA-seq | GEO | GSE280175 | 产前人脑snRNA-seq原始数据 |
| 人类Slide-seq | GEO | GSE280170 | 产前人脑Slide-seq原始数据 |
| 小鼠MERFISH | GEO | GSE280177 | Ts65Dn小鼠MERFISH原始数据 |
| 蛋白质组学 | MassIVE | MSV000096108 | 产前人脑蛋白质组学数据 |
| 补充数据 | 论文网站 | DOI: 10.1038/s41467-025-63752-0 | 完整补充数据文件 |
| 交互式网页 | https://neurodevelopment.shinyapps.io/Downsyndrome/ | - | DS神经发育数据可视化 |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| snRNA-seq分析 | ✅ 可完全复现 | 原始数据公开，分析工具均为开源 |
| Slide-seq分析 | ✅ 可完全复现 | Curio Seeker流程公开，原始数据可获取 |
| MERFISH分析 | ✅ 可完全复现 | Vizgen流程公开，Cellpose开源，原始数据可获取 |
| 蛋白质组分析 | ⚠️ 部分受限 | Spectronaut商业软件，但原始数据公开 |
| RNA速率分析 | ✅ 可完全复现 | scVelo开源，原始数据可获取 |
| TE分析 | ✅ 可完全复现 | SoloTE开源，原始数据可获取 |
| 微环境分析 | ✅ 可完全复现 | 自定义代码公开于GitHub和Code Ocean |
| 免疫荧光验证 | ❌ 无法直接复现 | 需要原始组织样本和抗体 |

---

## 状态说明

- ✅ **可完全复现**：工具/代码开源可获取，原始数据公开
- ⚠️ **部分受限**：需商业许可（如Spectronaut），但原始数据公开
- ❌ **无法直接复现**：需原始样本/仪器（如免疫荧光验证）
