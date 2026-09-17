# 代码与数据清单 — DBiT-seq Spatial Multi-Omics

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| DBiT-seq分析代码 | https://github.com/rongfan8/DBiT-seq | - | 论文自带 |
| ST Pipeline | https://github.com/SpatialTranscriptomicsResearch/st_pipeline (v1.7.2) | MIT | 序列比对和矩阵生成 |
| SpatialDE | https://github.com/Teichlab/SpatialDE | - | 空间差异表达分析 |
| Seurat | https://satijalab.org/seurat/ (V3.2) | - | 单细胞/空间数据分析 |
| SingleR | https://github.com/drisso/SingleR (v1.2.3) | - | 自动化细胞类型注释 |
| ToppGene Suite | https://toppgene.cchmc.org/ | - | GO和通路富集分析 |
| FISH-quant | https://biii.eu/fish-quant | - | smFISH定量 |
| HCR v3.0 kit | Molecular Instruments, Inc | 商业 | smFISH实验 |

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| 测序数据 (DBiT-seq) | GEO | GSE137986 | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE137986 |
| scRNA-seq参考数据 (E9.5-E13.5) | GEO | GSE109071 | Cao et al., 2019小鼠胚胎单细胞数据 |
| ENCODE bulk RNA-seq | ENCODE Project | - | E11.5小鼠胚胎liver, heart, neural tube |
| 抗体序列信息 | 论文Table S1 | - | 22种蛋白的ADT序列 |
| DNA barcode序列 | 论文Table S2 | - | A1-A50, B1-B50 barcode序列 |
| 关键试剂列表 | 论文Table S3 | - | 酶、缓冲液等 |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 微流控芯片制备 | ⚠️ 部分受限 | PDMS软光刻需实验室设备，但设计文件可索取 |
| 组织条码实验 | ⚠️ 部分受限 | 需微流控经验和试剂，但流程已详细描述 |
| 测序数据分析 | ✅ 可完全复现 | 代码开源，数据公开可下载 |
| SpatialDE分析 | ✅ 可完全复现 | Python包开源可用 |
| Seurat/SingleR分析 | ✅ 可完全复现 | R包开源，数据可从GEO下载 |
| 与scRNA-seq整合 | ✅ 可完全复现 | 参考数据GSE109071公开 |
| smFISH验证 | ⚠️ 部分受限 | 需购置HCR kit和共聚焦显微镜 |
| 免疫荧光验证 | ⚠️ 部分受限 | 需荧光显微镜和抗体 |

### 状态说明
- ✅ **可完全复现**: 工具/代码开源可获取
- ⚠️ **部分受限**: 需注册/需商业许可/需特定设备
- ❌ **无法直接复现**: 需原始样本/仪器

---

## 四、补充说明

### 1. 数据获取
- **GEO测序数据**: GSE137986 包含11个DBiT-seq样本的原始测序数据
- **scRNA-seq参考**: Cao et al., 2019 Nature 使用已发布的单细胞数据

### 2. 关键试剂
- PDMS微流控芯片和设计文件可从耶鲁大学材料转让协议(MTA)获取
- 抗体-DNA结合物 (TotalSeq) 商业购买自BioLegend
- DNA条码和引物商业合成 (IDT)

### 3. 代码使用
```python
# ST pipeline 基本用法
st_pipeline --input INPUT.fastq --output OUTPUT_DIR --genome GRCh38

# SpatialDE 分析
from SpatialDE import SpatialDE
results = SpatialDE.run(counts_df, coords_df)

# Seurat 整合分析
integrated <- RunHarmony(object, group.by.vars = "batch")
```

---

*报告生成日期: 2024*
*平台: DBiT-seq*
*论文: Liu et al., Cell 2020*
