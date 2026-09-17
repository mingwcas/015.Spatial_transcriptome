# Method: RNA Velocity Analysis (scVelo)

## 原文（Methods）
> BAM files from individual snRNA-seq replicates were preprocessed using the Velocyto command line in Velocyto v0.17.17. The human reference genome GRCh38/hg38 was retrieved from the UCSC genome browser. Output loom files from individual replicates were integrated to generate a new count matrix with the top 2000 variable features. Two additional count matrices were generated to separate the DS and euploid conditions. Following, scVelo v0.3.1 was used to compute expression dynamics and latent time for all three count matrices in Python.

## 解读

### 意义
RNA velocity分析通过计算剪接与未剪接mRNA的比例，预测单个细胞的未来状态和发育轨迹，揭示DS产前脑细胞分化方向的改变。

### 输入
- snRNA-seq的BAM文件（包含GN和CB标签）
- GRCh38/hg38参考基因组
- 10x Genomics数据

### 输出
- RNA速率矢量（方向和大小）
- 潜在时间（latent time）预测
- 细胞发育轨迹可视化

### 核心步骤
1. Velocyto v0.17.17预处理BAM文件
2. 生成loom文件（包含剪接/未剪接mRNA计数）
3. 整合所有样本的loom文件
4. 选择top 2000个可变特征
5. 分别生成DS和整倍体条件计数矩阵
6. scVelo v0.3.1计算表达动态和潜在时间
7. UMAP可视化发育轨迹

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 可变特征数 | Top 2000 | 速度分析特征选择 |
| scVelo版本 | v0.3.1 | 速度计算工具 |
| Velocyto版本 | v0.17.17 | BAM预处理工具 |
| 参考基因组 | GRCh38/hg38 | UCSC |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RNA velocity | 通过剪接/未剪接mRNA比率预测细胞未来状态 |
| spliced mRNA | 已剪接的成熟mRNA |
| unspliced mRNA | 未剪接的前体mRNA |
| latent time | 基于速度推断的细胞分化时间 |

## 复现
- 软件：Velocyto v0.17.17, scVelo v0.3.1
- 参考：https://scvelo.org/

## 生物学意义
RNA velocity分析揭示了DS产前脑中NPC分化轨迹的改变，包括DS NPC中RNA速度矢量方向性和长度降低，表明分化过程减速。这一发现为理解DS神经发育异常提供了动态的、发育轨迹层面的证据。

## 涉及 Figures
- **Fig. 4** — Altered differentiation trajectories in DS brain
