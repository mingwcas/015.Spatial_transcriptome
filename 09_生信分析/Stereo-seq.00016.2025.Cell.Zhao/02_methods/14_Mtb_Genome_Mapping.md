# Method: M. tb Genome Mapping

## 原文（Methods）
> The M. tb genome reference (ASM19595v2, https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000195955.2/) was concatenated with Mus musculus genome reference GRCm38. Then the raw sequence fastq files were aligned with SAW as described above. Only uniquely mapped reads are kept for the host and M. tb gene expression counting.

## 解读

### 意义
将测序reads同时比对到宿主小鼠基因组和结核分枝杆菌(Mtb)基因组，实现宿主-病原体转录组的共同分析。

### 输入
- 原始Fastq文件
- 小鼠参考基因组 (GRCm38)
- Mtb参考基因组 (ASM19595v2)

### 输出
- 宿主基因表达计数
- Mtb基因表达计数

### 核心步骤
1. 拼接Mtb和小鼠参考基因组
2. 使用SAW流程比对
3. 保留唯一比对的reads
4. 分别计数宿主和Mtb基因表达

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Mtb参考 | ASM19595v2 | |
| 小鼠参考 | GRCm38 | |
| 比对条件 | 唯一比对 | 宿主和Mtb |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Mtb | Mycobacterium tuberculosis，结核分枝杆菌 |
| 宿主-病原体共感染模型 | 同时分析两种生物的转录组 |

## 复现
- Mtb基因组：https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000195955.2/
- SAW pipeline (同Method 04)

## 生物学意义
同时捕获宿主和病原体转录组对于研究感染机制和免疫应答至关重要。

## 涉及 Figures
- Fig. 6 (host-Mtb transcriptomics)
- Fig. 7 (BCR repertoire)
