# 代码与数据清单 — FISSEQ RNA原位测序

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| FISSEQ软件包 (fisseq.zip) | http://arep.med.harvard.edu/FISSEQ_Nature_Protocols_2014/ | 论文自带 | 包含MATLAB图像配准脚本和Python碱基判读/聚类脚本 |
| FISSEQ.py (Python模块) | 包含在fisseq.zip中 | 论文自带 | ImageData()和AlignmentData()函数 |
| register_FISSEQ_images.m (MATLAB) | 包含在fisseq.zip中 | 论文自带 | 图像配准函数 |
| 示例R session | http://arep.med.harvard.edu/FISSEQ_Nature_Protocols_2014/ | 论文自带 | 数据分析示例 |
| 示例数据集 | http://arep.med.harvard.edu/FISSEQ_Nature_Protocols_2014/ | 论文自带 | 30碱基测序的原始和反卷积图像 |
| Bowtie | http://bowtie-bio.sourceforge.net | 开源 | 必须使用1.0或更早版本 |
| Fiji/ImageJ | http://fiji.sc/Fiji | 开源 | 图像查看和裁剪 |
| Bio-Formats插件 | http://loci.wisc.edu/software/bio-formats | 开源 | Fiji插件，读取显微镜格式 |
| R/RStudio | http://www.r-project.org, http://www.rstudio.com | 开源 | 数据分析和可视化 |
| ggplot2 | CRAN | 开源 | R可视化包 |
| data.table | CRAN | 开源 | R数据处理包 |
| Enthought Canopy Python 2.7 | https://www.enthought.com/products/canopy/ | 免费学术版 | 必须使用此版本运行FISSEQ.py |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| 人类RefSeq RNA FASTA | NCBI FTP | ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/mRNA_Prot/human.rna.fna.gz | 参考转录组 |
| 小鼠RefSeq RNA FASTA | NCBI FTP | ftp://ftp.ncbi.nlm.nih.gov/refseq/M_musculus/mRNA_Prot/mouse.rna.fna.gz | 参考转录组 |
| 大鼠RefSeq RNA FASTA | NCBI FTP | ftp://ftp.ncbi.nlm.nih.gov/refseq/R_norvegicus/mRNA_Prot/rat.rna.fna.gz | 参考转录组 |
| gene2refseq转换表 | NCBI FTP | ftp://ftp.ncbi.nih.gov/gene/DATA/gene2refseq.gz | RefSeq ID到Gene ID映射 |
| 示例图像数据 | 论文补充材料 | http://arep.med.harvard.edu/FISSEQ_Nature_Protocols_2014/ | 原始和反卷积图像堆栈 |
| 示例结果数据 | 论文补充材料 | http://arep.med.harvard.edu/FISSEQ_Nature_Protocols_2014/ | results.tsv示例 |
| SOLiD测序试剂盒 | Applied Biosystems | cat. no. 4449388 | 商业试剂 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 样品固定与透化 | ⚠️ 部分受限 | 需要新鲜细胞/组织样品和标准实验室设备 |
| 原位RT | ⚠️ 部分受限 | 需要M-MuLV RT等酶和aminoallyl-dUTP |
| cDNA交联与环化 | ⚠️ 部分受限 | 需要BS(PEG)9和CircLigase II（商业试剂） |
| RCA扩增 | ⚠️ 部分受限 | 需要φ29 DNA聚合酶 |
| SOLiD测序 | ⚠️ 部分受限 | 需要SOLiD ToP测序试剂盒（Applied Biosystems）和共聚焦显微镜 |
| 分区测序 | ❌ 无法直接复现 | 需要自定义引物设计和自动化显微镜 |
| 3D反卷积 | ⚠️ 部分受限 | Huygens为商业软件；可用开源替代但效果可能不同 |
| 图像配准 | ✅ 可完全复现 | MATLAB脚本论文自带，但需要>100 GB RAM |
| 碱基判读 | ⚠️ 部分受限 | 必须使用Python 2.7 (Canopy)，该版本已过时 |
| 序列比对 | ⚠️ 部分受限 | Bowtie 1.0已停止维护，颜色空间模式仅旧版支持 |
| 空间聚类 | ✅ 可完全复现 | Python脚本论文自带 |
| R数据分析 | ✅ 可完全复现 | R/RStudio开源，示例数据和脚本可用 |
| 参考数据库构建 | ✅ 可完全复现 | NCBI RefSeq和gene2refseq免费下载 |

### 复现总结
- **完全可复现**：图像配准、空间聚类、R数据分析、参考数据库构建
- **部分受限**：大部分实验步骤需要商业试剂和专用设备；计算分析需要特定软件版本
- **无法直接复现**：分区测序需要自定义引物和自动化；SOLiD试剂盒可能已停产
- **主要障碍**：1）需要共聚焦显微镜（2-3周连续使用）；2）SOLiD试剂盒和Python 2.7已过时；3）需要>100 GB RAM计算资源
- **建议**：关注FISSEQ的后续发展版本（如结合Illumina测序的改进方案）
