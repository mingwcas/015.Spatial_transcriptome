# Method: Transposable Element Analysis (SoloTE)

## 原文（Methods）
> BAM files from individual snRNA-seq replicates, containing GN and CB tags, were used as input files for the SoloTE (v1.09) tool. To optimize our alignment for the detection of multi-mapped reads, the STAR parameters were set to --winAnchorMultimapNmax 100 and --outFilterMultimapNmax 100. SoloTE selected reads that were not mapped to known genes to avoid false identification of gene-associated TEs as independent transcriptional units. Dual analysis, where reads mapped to genes, were also included in our analysis. BEDtools was used to assess the overlap between filtered reads and transposable element annotations. Expression levels were quantified at the locus level for reads with high mapping quality, while multi-mapped reads were aggregated at the subfamily level. The Dfam and Repbase databases were used to categorize the TEs into subfamilies of DNA transposons and retrotransposons. Following, DEG analysis using the MAST framework with two-sided testing and FDR correction using BH (|log2FC| > 0; FDR ≤0.05) was performed between conditions to identify DS-specific enrichment of TEs. Granular cell subtype-specific enrichment of TEs was performed using GSEA.

## 解读

### 意义
SoloTE分析识别细胞类型特异性的转座元件（TE）表达变化，揭示DS神经发育异常中染色质重塑异常导致的TE去抑制现象。

### 输入
- snRNA-seq BAM文件（包含GN和CB标签）
- Dfam和Repbase转座元件注释数据库
- SoloTE v1.09

### 输出
- 细胞类型特异性TE表达变化
- TE亚家族富集热图
- LINE1等特定TE的分析结果

### 核心步骤
1. 使用--winAnchorMultimapNmax 100和--outFilterMultimapNmax 100参数进行STAR比对
2. SoloTE v1.09选择未比对到已知基因的reads
3. 同时包含比对到基因的reads进行双重分析
4. BEDtools评估reads与TE注释的重叠
5. 高质量reads在基因座水平定量，多映射reads在亚家族水平聚合
6. Dfam和Repbase数据库分类TE为DNA转座子和逆转座子
7. MAST框架进行DEG分析
8. GSEA进行细胞亚型特异性TE富集分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| SoloTE版本 | v1.09 | TE分析工具 |
| STAR multimap参数 | --winAnchorMultimapNmax 100 | 优化多映射reads检测 |
| TE注释数据库 | Dfam, Repbase | 转座元件数据库 |
| DEG阈值 | \|log2FC\| > 0, FDR ≤0.05 | 差异TE阈值 |
| 富集方法 | GSEA | 细胞类型特异性分析 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SoloTE | 单细胞RNA-seq数据中转座元件分析工具 |
| TE | Transposable Element，转座元件 |
| LINE1 | Long Interspersed Nuclear Element 1 |
| Dfam | 转座元件家族数据库 |
| Repbase | 重复序列数据库 |

## 复现
- 软件：SoloTE v1.09
- 参考：https://github.com/ValdebenitoMaturana/SoloTE
- 数据库：https://www.dfam.org/, https://www.girinst.org/repbase/

## 生物学意义
TE分析揭示了DS产前脑中LINE1等转座元件在NPC和兴奋性神经元中的选择性去抑制，与染色质调节因子（如HDAC2, EZH2）的下调相一致。这一发现提示TE去抑制可能成为DS的一个新标志，与神经命运决定、皮层发育异常和免疫激活相关。

## 涉及 Figures
- **Fig. 4** — Transposable element de-repression in DS brain
- **Supplementary Fig. 3** — TE subfamily analysis
