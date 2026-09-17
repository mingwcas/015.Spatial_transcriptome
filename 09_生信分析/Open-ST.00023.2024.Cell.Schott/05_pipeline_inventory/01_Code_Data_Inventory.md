# 代码与数据清单 — Open-ST: High-resolution spatial transcriptomics in 3D

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| openst | https://github.com/rajewsky-lab/openst | 开源 | 核心计算工具包 |
| spacemake | https://github.com/rajewsky-lab/spacemake | 开源 | 空间转录组数据处理管道 |
| STIM | https://github.com/PreibischLab/STIM | 开源 | 3D重建框架 |
| Cellpose | https://github.com/MouseLand/cellpose | 开源 | 细胞分割算法 |
| scanpy | https://github.com/scverse/scanpy | 开源 | 单细胞分析框架 |
| squidpy | https://github.com/scverse/squidpy | 开源 | 空间组学分析 |
| scvi-tools | https://github.com/scverse/scvi-tools | 开源 | 批次校正和标签转移 |
| liana-py | https://github.com/saezlab/liana-py | 开源 | 细胞间通讯分析 |
| decoupler-py | https://github.com/saezlab/decoupler-py | 开源 | 基因集活性分析 |
| ParaView | https://www.paraview.org/ | 开源 | 3D可视化 |
| Fiji | https://imagej.net/software/fiji/ | 开源 | 图像处理 |
| Drop-seq tools | https://github.com/broadinstitute/Drop-seq | 开源 | 转录本定量 |
| STAR | https://github.com/alexdobin/STAR | 开源 | 序列比对 |
| Bowtie2 | https://github.com/BenLangmead/bowtie2 | 开源 | 快速比对 |
| samtools | https://github.com/samtools/samtools | 开源 | BAM文件处理 |
| microfilm | https://github.com/guiwitz/microfilm | 开源 | 伪图像生成 |
| scikit-image | https://github.com/scikit-image/scikit-image | 开源 | 图像处理算法 |
| scipy | https://github.com/scipy/scipy | 开源 | 科学计算 |
| kornia | https://github.com/kornia/kornia | 开源 | 可微计算机视觉 |
| pydeseq2 | - | 开源 | 差异表达分析 |
| kneed | https://github.com/arvkevi/kneed | 开源 | 肘部法检测 |
| RSeQC | https://rseqc.sourceforge.net | 开源 | RNA-seq质量控制 |
| napari | https://napari.org/stable/ | 开源 | 多维图像查看器 |
| QuPath | https://qupath.github.io/ | 开源 | 数字病理分析 |
| CellCharter | - | 开源 | 空间细胞生态位分析 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| Open-ST RNA-seq数据 | GEO | GSE251926 | 本研究生成的所有Open-ST数据 |
| 10x Xenium数据 | GEO | GSE263498 | HNSCC和转移性淋巴结Xenium数据 |
| 免疫荧光图像 | Zenodo | https://doi.org/10.5281/zenodo.11395256 | 转移性淋巴结IF图像 |
| Slide-seqV2数据 | GEO | GSE197353 | E9.5小鼠脑数据 |
| Seq-Scope数据 | GEO | GSE169706 | 小鼠肝数据 |
| Stereo-seq数据 | CNGB | CNX0422301 | Stereo-seq数据 |
| 10x Visium数据 | 10x Genomics | https://www.10xgenomics.com/resources/datasets/ | 小鼠脑数据 |
| DBiT-seq数据 | GEO | GSE137986 | E11小鼠胚胎数据 |
| 单细胞RNA-seq | GEO | GSE103322 | HNSCC原发和转移肿瘤 |
| Allen发育小鼠脑图谱 | Allen Institute | http://developingmouse.brain-map.org/ | ISH数据 |
| 3D打印切割指南 | 开放资源 | https://rajewsky-lab.github.io/openst | NovaSeq S4 flow cell切割工具 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 捕获区域制备 | ⚠️ 部分受限 | 需要Illumina NovaSeq 6000 S4 flow cell和自定义测序试剂盒 |
| 组织处理和文库制备 | ✅ 可完全复现 | 标准实验室设备，详细协议公开 |
| H&E染色和成像 | ✅ 可完全复现 | 标准组织学方法 |
| 细胞分割 | ✅ 可完全复现 | Cellpose开源，微调模型可复现 |
| 多模态配准 | ✅ 可完全复现 | openst包开源 |
| 3D重建 | ✅ 可完全复现 | STIM框架开源 |
| 聚类和细胞类型注释 | ✅ 可完全复现 | scanpy等标准工具 |
| 基因集和通讯分析 | ✅ 可完全复现 | decoupler-py和liana-py开源 |
| 与Xenium比较 | ⚠️ 部分受限 | 需要Xenium仪器和试剂 |
| 3D可视化 | ✅ 可完全复现 | ParaView开源 |

### 状态说明
- ✅ 可完全复现：工具/代码开源可获取
- ⚠️ 部分受限：需注册/需商业许可/需专用仪器
- ❌ 无法直接复现：需原始样本/仪器

### 复现建议
1. **实验部分**：需要访问Illumina测序平台，建议与有NovaSeq 6000的机构合作
2. **计算部分**：所有分析工具开源，可在标准计算环境复现
3. **数据获取**：所有数据已存入公共数据库，可自由下载
4. **3D重建**：需要足够的连续切片（建议≥10个切片）
