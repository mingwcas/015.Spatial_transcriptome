# 代码与数据清单 — Open-ST 3D Spatial Transcriptomics Protocol

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| openst | https://github.com/rajewsky-lab/openst | 开源 | 核心流程包，v.0.2.3 |
| spacemake | https://github.com/rajewsky-lab/spacemake | 开源 | 数据处理流程，v.0.7.9 |
| stimwrap | https://github.com/rajewsky-lab/stimwrap | 开源 | STIM Python绑定 |
| STIM | https://github.com/PreibischLab/STIM | 开源 | 3D对齐工具，v.0.3.0 |
| Cellpose | https://github.com/MouseLand/cellpose | 开源 | 细胞分割，v.2.2 |
| STAR | https://github.com/alexdobin/STAR | 开源 | 序列比对，v.2.7.10b |
| Bowtie2 | https://github.com/BenLangmead/bowtie2 | 开源 | rRNA过滤，v.2.5.1 |
| Drop-seq tools | https://github.com/broadinstitute/Drop-seq | 开源 | 数据处理工具，v.2.5.1 |
| scanpy | https://github.com/scverse/scanpy | 开源 | 下游分析，v.1.9.3 |
| scikit-image | https://github.com/scikit-image/scikit-image | 开源 | 图像处理，v.0.19.3 |
| samtools | https://github.com/samtools/samtools | 开源 | 序列处理，v.1.17 |
| scipy | https://github.com/scipy/scipy | 开源 | 科学计算，v.1.10.0 |
| Kornia | https://github.com/kornia/kornia | 开源 | 可微计算机视觉，v.0.7.0 |
| napari | https://napari.org | 开源 | 多维图像查看器，v.0.4.19 |
| Fiji | https://imagej.net/software/fiji/ | 开源 | 图像处理，v.1.53t |
| ParaView | https://www.paraview.org | 开源 | 3D可视化，v.5.11.0 |
| Open-ST 文档 | https://rajewsky-lab.github.io/openst | 开源 | 协议和教程 |
| Open-ST 包归档 | https://doi.org/10.5281/zenodo.14197712 | 开源 | v.0.2.3归档 |
| 3D打印文件 | https://rajewsky-lab.github.io/openst | 开源 | 切割导板设计文件 |
| Jupyter notebooks | https://github.com/rajewsky-lab/openst | 开源 | 分析教程 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| Open-ST RNA-seq数据 | GEO | GSE251926 | 转移性淋巴结数据集 |
| 显微镜成像数据 | GEO | GSE251926 | H&E染色图像 |
| 示例数据集 | GitHub | https://github.com/rajewsky-lab/openst | 3个连续切片，每个50M reads |
| 参考基因组 | 用户配置 | 自定义 | 物种特异性基因组和注释 |
| Flow cell tile信息 | GitHub | https://github.com/rajewsky-lab/openst | 坐标系统文件 |
| 预期输出 | GitHub | https://github.com/rajewsky-lab/openst | h5ad文件和QC报告 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 捕获区域生成 | ⚠️ 部分受限 | 需要Illumina NovaSeq 6000 flow cell和测序仪 |
| 3D打印切割导板 | ✅ 可完全复现 | .stl文件公开可用 |
| 组织切片和染色 | ✅ 可完全复现 | 标准分子生物学设备 |
| 透化和逆转录 | ✅ 可完全复现 | 商业试剂盒 |
| 文库构建 | ✅ 可完全复现 | 标准NGS文库构建 |
| 条形码测序 | ⚠️ 部分受限 | 需要Illumina测序仪和自定义测序方案 |
| 文库测序 | ⚠️ 部分受限 | 需要Illumina测序仪 |
| spacemake流程 | ✅ 可完全复现 | 开源软件，公开教程 |
| openst流程 | ✅ 可完全复现 | 开源软件，公开教程 |
| 细胞分割 | ✅ 可完全复现 | Cellpose开源 |
| 3D对齐 | ✅ 可完全复现 | STIM开源 |
| 下游分析 | ✅ 可完全复现 | scanpy/ParaView开源 |
| 数据访问 | ✅ 可完全复现 | GEO公开数据 |

**总体复现评估**：
- **实验部分**：⚠️ 部分受限（需要Illumina测序仪和flow cell，约$2/捕获区域）
- **计算部分**：✅ 可完全复现（所有软件开源，教程公开）
- **数据部分**：✅ 可完全复现（GEO公开数据）

**复现建议**：
1. 计算部分可在任何Linux工作站复现（推荐128GB RAM，2TB存储，24线程CPU）
2. 实验部分需要访问Illumina测序平台和标准分子生物学实验室
3. 建议先使用提供的示数据集熟悉计算流程
4. 完整复现需要约$1000-2000的flow cell和试剂成本（不含测序仪）
