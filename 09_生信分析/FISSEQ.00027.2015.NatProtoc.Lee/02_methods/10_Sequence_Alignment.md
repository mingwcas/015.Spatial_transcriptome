# Method: 序列比对（Sequence Alignment with Bowtie）

## 原文（Methods）
> Align reads to refseq_human using Bowtie 1.0 or earlier, and write mapped reads to bowtie_output.txt. bowtie -C -n 3 -l 15 -e 240 -a -p 12 -m 20 --chunkmbs 200 -f --best --strata --refidx refseq_human read_data_*.csfasta bowtie_output.txt

## 解读

### 意义
将颜色空间的测序读取比对到参考转录组，确定每个读取的基因来源

### 输入
- read_data_*.csfasta（碱基调用文件）
- refseq_human（Bowtie索引）

### 输出
- bowtie_output.txt（比对结果）

### 核心步骤
1. 下载RefSeq RNA FASTA文件和gene2refseq转换表
2. 使用bowtie-build -C构建颜色空间索引
3. 运行Bowtie比对（颜色空间模式）
4. 输出比对结果

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| -C | 颜色空间模式 | SOLiD颜色空间比对 |
| -n 3 | 最大错配数3 | 允许的错配 |
| -l 15 | 种子长度15 | 比对种子长度 |
| -e 240 | 最大质量值240 | 每次比对的最大质量值 |
| -a | 报告所有比对 | 多重比对报告 |
| -p 12 | 12线程并行 | 多线程 |
| -m 20 | 最多20个比对 | 过滤多重比对读取 |
| --best --strata | 最佳比对 | 仅报告最佳比对 |
| Bowtie版本 | 1.0或更早 | Bowtie 2.0+不支持SOLiD |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RefSeq | NCBI参考序列数据库 |
| gene2refseq | RefSeq ID到Gene ID的转换表 |
| Color space alignment | SOLiD颜色空间中的序列比对 |
| Bowtie | 短读取比对工具 |

## 复现
- 工具：Bowtie 1.0 (http://bowtie-bio.sourceforge.net)
- 关键：Bowtie 2.0或更高版本不支持SOLiD颜色空间比对
- 参考数据库：human.rna.fna, gene2refseq (NCBI FTP)

## 生物学意义
序列比对将测序读取映射到已知转录组，是基因鉴定的关键步骤。颜色空间比对可利用SOLiD双碱基编码的纠错特性。多重比对参数（-m 20）过滤高度重复序列，减少假阳性比对。

## 涉及 Figures
- **Fig. 5c** — 序列比对到RefSeq示意
- **Fig. 6** — 比对步骤48
