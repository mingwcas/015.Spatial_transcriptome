# 代码与数据清单 — FISSEQ 2020 Cell Chen

> **论文**: Spatial Transcriptomics and In Situ Sequencing to Study Alzheimer's Disease
> **DOI**: 10.1016/j.cell.2020.06.038

---

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| WGCNA R包 | https://cran.r-project.org/web/packages/WGCNA/ | GPL-2 | 加权基因共表达网络分析 |
| limma R包 | https://bioconductor.org/packages/limma/ | GPL-2 | 差异表达分析 |
| edgeR R包 | https://bioconductor.org/packages/edgeR/ | GPL-2 | 差异表达分析 |
| STAR aligner | https://github.com/alexdobin/STAR | MIT | RNA-seq数据比对 |
| ImageJ/FIJI | https://fiji.sc/ | GPL-2 | 图像分析和Aβ负荷定量 |
| ggplot2 | https://cran.r-project.org/web/packages/ggplot2/ | GPL-2 | 数据可视化 |
| Circos | http://circos.ca/ | GPL-2 | 共表达网络可视化 |
| GOrilla | http://cbl-gorilla.cs.technion.ac.il/ | 学术免费 | GO功能富集分析 |
| DAVID | https://david.ncifcrf.gov/ | 学术免费 | 功能注释和通路分析 |
| R base | https://www.r-project.org/ | GPL-2 | 统计计算环境 |
| 自定义ISS分析脚本 | 论文补充材料 | 未明确 | 细胞类型分配和空间分析 |
| 自定义ST预处理脚本 | 论文补充材料 | 未明确 | ST数据预处理和质量控制 |

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| ST原始测序数据 | NCBI GEO | GSE153855 | AppNL-G-F和WT小鼠ST数据 |
| ISS原始图像 | 作者提供 | 未公开 | 84个基因的ISS成像数据 |
| Aβ负荷定量数据 | 论文补充材料 | Table S1-S6 | Aβ指数和基因表达关联 |
| WGCNA模块数据 | 论文补充材料 | Table S3-S4 | PIG和OLIG模块基因列表 |
| 人类AD ISS数据 | 作者提供 | 未公开 | 6个个体的ISS验证数据 |
| 免疫染色图像 | 论文补充材料 | Figure S1-S7 | 组织学验证图像 |
| 基因本体注释 | GO数据库 | http://geneontology.org/ | 功能注释 |
| 人类AD小胶质细胞标记物 | Mathys et al., 2019 | 原始文献 | Mic1标记物列表 |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| ST数据预处理 | ✅ 可完全复现 | 使用STAR和标准RNA-seq流程 |
| Aβ负荷定量 | ✅ 可完全复现 | 使用ImageJ和公开脚本 |
| WGCNA分析 | ✅ 可完全复现 | R WGCNA包，公开代码 |
| 差异表达分析 | ✅ 可完全复现 | R limma/edgeR包 |
| 功能富集分析 | ✅ 可完全复现 | 使用GOrilla和DAVID |
| ST数据可视化 | ✅ 可完全复现 | 使用ggplot2 |
| ISS细胞类型分配 | ⚠️ 部分受限 | 需要自定义脚本（论文补充材料） |
| ISS成像分析 | ⚠️ 部分受限 | 需要Cartana AB试剂和共聚焦显微镜 |
| RNAscope验证 | ⚠️ 部分受限 | 需要ACD Bio RNAscope试剂盒 |
| 人类样本验证 | ❌ 无法直接复现 | 需要人类AD大脑样本和伦理批准 |
| 纵向时间点分析 | ❌ 无法直接复现 | 需要不同年龄的AppNL-G-F小鼠 |
| 多重免疫染色 | ⚠️ 部分受限 | 需要特异性抗体和成像设备 |

---

## 状态说明

- ✅ **可完全复现**: 工具/代码开源可获取，数据公开可用
- ⚠️ **部分受限**: 需要商业试剂、专业设备或注册访问
- ❌ **无法直接复现**: 需要原始样本、特殊设备或伦理批准

---

## 关键资源获取

### 商业试剂
1. **Spatial Transcriptomics阵列**: Spatial Transcriptomics AB (现为10x Genomics)
2. **RNAscope试剂盒**: ACD Bio (Advanced Cell Diagnostics)
3. **ISS探针**: Cartana AB (现为10x Genomics)
4. **Illumina测序**: Illumina NextSeq500

### 开源工具
1. **R环境**: https://www.r-project.org/
2. **STAR aligner**: https://github.com/alexdobin/STAR
3. **ImageJ/FIJI**: https://fiji.sc/
4. **WGCNA**: https://cran.r-project.org/web/packages/WGCNA/

### 数据库
1. **NCBI GEO**: https://www.ncbi.nlm.nih.gov/geo/
2. **Gene Ontology**: http://geneontology.org/
3. **DAVID**: https://david.ncifcrf.gov/

---

## 复现建议

### 完全复现路线
1. 下载GSE153855 ST数据
2. 使用STAR进行比对和预处理
3. 使用R脚本进行WGCNA和差异表达分析
4. 使用ImageJ进行Aβ负荷定量
5. 使用ggplot2和Circos进行可视化

### 部分复现路线
1. 使用公开的ST数据重现主要分析
2. 替换ISS分析为其他空间技术（如MERFISH, seqFISH）
3. 使用公开的AD数据集验证发现

### 局限性
1. ISS需要专门的设备和试剂
2. 人类样本验证无法替代
3. 纵向设计需要大量时间和资源
