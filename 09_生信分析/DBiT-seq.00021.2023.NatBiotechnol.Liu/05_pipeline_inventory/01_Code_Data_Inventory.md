# 代码与数据清单 — Spatial-CITE-seq

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| Hiplex_proteome（主分析脚本） | https://github.com/edicliuyang/Hiplex_proteome | 未注明 | R脚本，用于空间CITE-seq数据分析 |
| ST Pipeline | https://github.com/SpatialTranscriptomicsResearch/st_pipeline | 开源 | v1.7.2，空间转录组数据处理 |
| CITE-seq-Count | https://github.com/Hoohm/CITE-seq-Count | 开源 | v1.4.2，ADT UMI计数 |
| Seurat | https://satijalab.org/seurat/ | 开源 | v3.2，聚类、整合、可视化 |
| SPOTlight | https://github.com/MarcElosua/SPOTlight | 开源 | 空间去卷积 |
| ggplot2 | CRAN | 开源 | 热图绘制 |
| STAR | https://github.com/alexdobin/STAR | 开源 | RNA-seq读段比对 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|-----------|------|
| 测序数据（FASTQ） | GEO | GSE213264 | 所有spatial-CITE-seq和scRNA-seq测序数据 |
| 高分辨率显微镜图像 | Figshare | https://doi.org/10.6084/m9.figshare.20723680 | 组织明场和通道图像 |
| ADT序列信息 | 补充材料 | Supplementary Table 1-2 | Barcode A/B和ADT序列 |
| 小鼠组织切片 | Zyagen | MF-701, MF-311, MF-308, MF-901 | 脾、结肠、小肠、肾 |
| 人扁桃体切片 | Zyagen | HF-707 | 冷冻切片 |
| 人皮肤活检 | Yale Neurology | — | COVID-19疫苗注射部位（IRB: 2000027055） |
| scCITE-seq参考数据 | 已发表 | King et al., Sci. Immunol. 2021 | 人扁桃体scCITE-seq |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 数据预处理（ST Pipeline + CITE-seq-Count） | ✅ 可复现 | 开源工具，数据公开于GEO |
| 聚类分析（Seurat） | ✅ 可复现 | 标准Seurat工作流，参数明确 |
| 整合分析（Seurat Integration） | ✅ 可复现 | 标准方法，参数已给出 |
| 空间去卷积（SPOTlight） | ✅ 可复现 | 开源R包 |
| 微流控芯片制备 | ⚠️ 需专业设备 | 需要洁净室、PDMS模具制作能力 |
| Spatial-CITE-seq实验 | ⚠️ 需专业设备 | 需要微流控芯片、NovaSeq测序、BioLegend ADT |
| CODEX/COMET验证成像 | ⚠️ 需专业设备 | 需要PhenoCycler或COMET平台 |
| 单细胞RNA-seq（10x Genomics） | ✅ 可复现 | 标准10x Genomics流程，数据公开 |
| 自定义Python脚本（Read格式化） | ⚠️ 未公开 | 论文未提供格式化脚本的详细代码 |
