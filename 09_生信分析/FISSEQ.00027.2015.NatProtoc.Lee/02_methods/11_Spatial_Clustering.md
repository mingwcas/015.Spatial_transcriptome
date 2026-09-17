# Method: 空间聚类（Spatial Clustering）

## 原文（Methods）
> Spatially cluster the Bowtie reads, annotate clusters using gene2refseq and write to results.tsv. The default kernel size of 3 performs a 3 × 3 dilation before clustering. FISSEQ.AlignmentData('bowtie_output.txt', 3, G, 'results.tsv', 'human.rna.fna', 'gene2refseq', '9606')

## 解读

### 意义
将空间邻近且序列高度相似的像素聚类为单一对象（扩增子），生成包含基因ID、共识序列、空间位置等信息的最终数据集

### 输入
- bowtie_output.txt（比对结果）
- 基因组参考文件（human.rna.fna, gene2refseq）

### 输出
- results.tsv（最终结果表，包含基因ID、聚类大小、共识序列、x-y位置、错配数、碱基质量、比对质量）

### 核心步骤
1. 加载配准后的图像数据（FISSEQ.ImageData）
2. 运行FISSEQ.AlignmentData进行空间聚类
3. 默认3×3膨胀核进行邻域分析
4. 使用gene2refseq注释聚类
5. 输出结果到results.tsv

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| kernel size | 3 (默认) | 3×3膨胀核 |
| 物种 | 9606 (人类) | NCBI分类ID |
| 输出格式 | TSV | 制表符分隔文本 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Spatial clustering | 空间邻近像素的聚类 |
| Dilation | 膨胀操作，扩展邻域范围 |
| Consensus sequence | 聚类内多个像素的共识序列 |
| Cluster size | 聚类中的像素数 |

## 复现
- 工具：Python 2.7 + FISSEQ.py模块
- 代码：`FISSEQ.AlignmentData('bowtie_output.txt', 3, G, 'results.tsv', 'human.rna.fna', 'gene2refseq', '9606')`
- 物种支持：人类(9606), 小鼠(10090), 大鼠(10116)

## 生物学意义
空间聚类将来自同一扩增子的多个像素合并，提高序列准确性并减少噪声。聚类大小反映了扩增子的物理大小，可用于区分真正的扩增子和背景噪声。最终数据集包含每个基因的空间坐标，可用于亚细胞定位分析。

## 涉及 Figures
- **Fig. 5c** — 空间聚类示意（连接的像素聚类）
- **Fig. 6** — 聚类步骤49
