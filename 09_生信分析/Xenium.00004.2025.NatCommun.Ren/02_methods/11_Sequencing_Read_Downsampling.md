# Method: Sequencing Reads Downsampling for Stereo-seq v1.3 and Visium HD FFPE

## 原文（Methods）
> The --unmapped-fastq option was used in SAW to retain unmapped reads for Stereo-seq v1.3. We selected ten regions characterized by a high density of cancer cells in each dataset based on H&E staining. BAM files were filtered to isolate the reads with valid UMI information. The valid reads with spatial coordinates mapped to the ten regions were downsampled to fixed proportions (20%, 40%, 60%, and 80%) using the Python package pysam (v.0.22.1).

## 解读

### 意义
通过reads降采样分析，评估测序深度对Stereo-seq v1.3和Visium HD FFPE饱和度的影响，为平台间的公平比较提供测序饱和度视角的参考。

### 输入
- Stereo-seq v1.3原始FASTQ文件（含unmapped reads）
- Visium HD FFPE原始BAM文件
- 十个高密度癌细胞区域的坐标

### 输出
- 不同降采样比例（20%, 40%, 60%, 80%, 100%）下的饱和度曲线

### 核心步骤
1. Stereo-seq v1.3: 使用SAW的--unmapped-fastq选项保留未比对reads
2. 基于H&E染色选择十个高密度癌细胞区域
3. 过滤BAM文件，保留具有有效UMI信息的reads
4. 对落入十个区域的有效reads使用pysam进行降采样至20%、40%、60%、80%
5. 计算各降采样水平下的平均测序饱和度

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 降采样比例 | 20%, 40%, 60%, 80% | 相对于原始深度 |
| 区域选择 | 10个高密度癌细胞区域 | 基于H&E染色 |
| 分析工具 | pysam v.0.22.1 | Python包 |
| Stereo-seq工具 | SAW v.8.0 (--unmapped-fastq选项) |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 测序饱和度 | 检测到的唯一转录本数与理论最大值的比值 |
| 降采样 (Downsampling) | 按比例随机减少测序reads数量 |
| UMI | Unique Molecular Identifier，唯一分子标签 |

## 复现
- Python包：pysam v.0.22.1
- Stereo-seq分析：SAW v.8.0 (STOmics)
- 原始数据保留：--unmapped-fastq选项

## 生物学意义
降采样分析表明Visium HD FFPE在相同测序深度下表现出较低的测序饱和度，提示其测序效率相对较低。这为平台间的公平比较提供了重要参考。

## 涉及 Figures
- **Fig. 1g** — 10个选定区域的平均测序饱和度曲线
