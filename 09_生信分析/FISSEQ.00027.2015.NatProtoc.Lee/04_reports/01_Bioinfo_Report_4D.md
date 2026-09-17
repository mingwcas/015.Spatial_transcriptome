# 四维度生信分析报告 — FISSEQ RNA原位测序

> **论文**：Fluorescent in situ sequencing (FISSEQ) of RNA for gene expression profiling in intact cells and tissues
> **DOI**：10.1038/nprot.2014.191
> **期刊**：Nature Protocols, Vol.10 No.3, 2015
> **平台**：FISSEQ (Fluorescent In Situ Sequencing)
> **第一作者**：Lee JH, Daugharthy ER
> **通讯作者**：Church GM
> **完成日期**：2025年处理

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 样品制备 | 细胞固定与透化 | 10% formalin, Triton X-100, pepsin | 适用于培养细胞、组织切片、FFPE、3D类器官、果蝇胚胎 |
| 原位RT | 逆转录合成cDNA | M-MuLV RT, aminoallyl-dUTP | 随机六聚体引物实现全转录组覆盖 |
| cDNA交联 | BS(PEG)9胺交联 | BS(PEG)9 (NHS酯双功能团) | 将cDNA共价固定在细胞蛋白基质上 |
| cDNA环化 | CircLigase II连接 | CircLigase II (60°C, 1h) | 线性cDNA环化用于RCA |
| RCA扩增 | 滚环扩增 | φ29 DNA polymerase (30°C过夜) | 单分子→含数百拷贝的扩增子 |
| 扩增子交联 | BS(PEG)9交联 | BS(PEG)9 | 保持扩增子空间位置 |
| 测序 | SOLiD连接法测序 | T4 DNA ligase, SOLiD探针 | 5引物×7轮=35轮图像，~30bp读长 |
| 分区测序 | 随机条形码分区 | 自定义测序引物 | 解决光学分辨率限制下的扩增子计数 |
| 成像 | 共聚焦显微镜4色成像 | Zeiss LSM 710/Leica SP5/Yokogawa CSU-W1 | 20-50 cells/FOV, 15,000-40,000 reads/FOV |
| 3D反卷积 | CMLE反卷积 | SVI Huygens Professional | 减少离焦背景，提高碱基判读质量 |
| 图像配准 | 块间局部配准 | MATLAB (register_FISSEQ_images) | 校正色差和时间漂移 |
| 碱基判读 | 像素级颜色转换检测 | Python 2.7 (FISSEQ.ImageData) | 颜色空间FASTA输出 |
| 序列比对 | Bowtie颜色空间比对 | Bowtie 1.0 (-C模式) | 比对到人类RefSeq转录组 |
| 空间聚类 | 3×3膨胀核聚类 | Python 2.7 (FISSEQ.AlignmentData) | 生成results.tsv（基因ID、位置、质量） |
| 统计分析 | 数据过滤与富集分析 | R/RStudio, ggplot2, data.table | Fisher精确检验找空间富集基因 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|---|---------|------------|
| Fig. 1 | FISSEQ文库构建与测序原理示意 | 流程示意图 |
| Fig. 2 | FISSEQ vs 单细胞RNA-seq比较 | 概率密度散点图 |
| Fig. 3 | 分区测序计数分辨率受限扩增子 | 原理示意图+细胞图像 |
| Fig. 4 | SOLiD颜色编码与解码方案 | 编码表+示意图 |
| Fig. 5 | 图像分析、配准与序列聚类示例 | 3D渲染+配准+聚类图 |
| Fig. 6 | 实验与分析步骤概览 | 流程图 |
| Table 1 | 测试样品类型（6种） | 表格 |
| Table 2 | 显微镜平台比较（3种） | 表格 |
| Table 3 | 故障排除指南 | 表格 |
| Box 1 | SOLiD测序化学详细说明 | 文本框 |
| Supplementary Fig. 1-6 | 温度敏感固定、酸处理、RNA降解、反卷积、配准、RStudio界面 | 各类补充图 |
| Supplementary Videos 1-4 | 配准效果展示 | 视频 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 图像预处理 | Fiji/ImageJ | — | 开源 |
| 3D反卷积 | SVI Huygens Professional | — | 商业 |
| 3D可视化 | Bitplane Imaris | — | 商业 |
| 图像配准 | MATLAB (自定义脚本) | — | 商业+论文自带 |
| 碱基判读 | Python 2.7 (FISSEQ.py) | Canopy 2.7 | 论文自带 |
| 序列比对 | Bowtie | 1.0 | 开源 |
| 空间聚类 | Python 2.7 (FISSEQ.py) | Canopy 2.7 | 论文自带 |
| 数据分析 | R/RStudio | 最新版 | 开源 |
| 统计可视化 | ggplot2, data.table | — | 开源 |
| 参考数据库 | NCBI RefSeq, gene2refseq | — | 免费 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| SOLiD颜色空间编码 | 测序化学算法 | 双碱基探测，每个碱基检测两次降低错误率 |
| CMLE反卷积 | 图像处理算法 | 约束最大似然估计3D反卷积 |
| 块间局部配准 | 图像配准算法 | 校正色差和时间漂移 |
| 像素级颜色转换检测 | 碱基判读算法 | 基于特定颜色转换模式识别真实信号 |
| 3×3膨胀核空间聚类 | 空间聚类算法 | 将邻近相似像素聚类为扩增子 |
| 分区测序外推 | 计数算法 | 从不同分区大小的计数外推实际扩增子数 |
| Fisher精确检验 | 统计检验 | 空间富集分析 |

### 论文局限性
1. **rRNA污染**：rRNA reads占50-80%，缺乏rRNA去除步骤，限制mRNA读取深度
2. **读长短**：~30 bp，受SOLiD连接法限制
3. **检测灵敏度低**：当前检测阈值~200-400 mRNA分子/细胞
4. **需要专用设备**：共聚焦显微镜需预留2-3周；4色成像设备升级~$20,000
5. **计算资源需求高**：需要>100 GB RAM的高性能计算集群
6. **软件兼容性**：必须使用Python 2.7 (Canopy)和Bowtie 1.0
7. **富集机制不明**：FISSEQ为何富集活性转录本的分子机制不清楚
8. **厂商论文**：Nature Protocols方法论文，侧重实验操作而非生物学发现
9. **商业软件依赖**：Huygens反卷积和Imaris可视化为商业软件
10. **手动操作多**：试剂更换手动进行，需要显微镜持续2-3周
