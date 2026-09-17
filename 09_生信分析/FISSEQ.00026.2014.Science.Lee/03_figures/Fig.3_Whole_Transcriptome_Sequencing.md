# Fig. 3: 原代成纤维细胞全转录组原位 RNA-seq (Whole-Transcriptome in Situ RNA-seq in Primary Fibroblasts)

## Caption（原文）

(A) From deconvolved confocal images, 27-base reads are aligned to the reference, and alignments are spatially clustered into objects. (B) Of the amplicons, 90.6% align to the annotated (+) strand. (C) mRNA and noncoding RNA make up 43.6% and 6.9% of the amplicons, respectively. (D) GO term clustering for the top 90 ranked genes. (E) FISSEQ of 2710 genes from fibroblasts compared with RNA-seq for fibroblast, B cell, and iPS cells. Pearson's correlation is plotted as a function of the gene expression level. (F) Subcellular localization enrichment compared to the whole transcriptome distribution. (G) Of the amplicons, 481 map to the FN1 mRNA, showing an alternatively spliced transcript variant and a single-nucleotide polymorphism (arrow).

## Panel-by-Panel 解读

### Panel A: 分析流程
- **内容**：从去卷积共聚焦图像到序列比对和空间聚类
- **关键步骤**：
  1. 去卷积共聚焦图像
  2. 27 碱基读数比对到参考序列
  3. 比对结果空间聚类为对象
- **意义**：展示了 FISSEQ 的完整分析流程

### Panel B: 链特异性比对
- **内容**：扩增子比对到正确注释链的比例
- **关键数据**：90.6% 比对到正链
- **意义**：验证了测序的准确性和链特异性

### Panel C: RNA 类型分布
- **内容**：mRNA 和非编码 RNA 的比例
- **关键数据**：
  - mRNA：43.6%
  - 非编码 RNA：6.9%
- **意义**：展示了 FISSEQ 检测不同 RNA 类型的能力

### Panel D: GO 术语聚类
- **内容**：前 90 个高表达基因的 GO 术语聚类
- **关键信息**：成纤维细胞相关功能富集
- **意义**：验证了 FISSEQ 检测细胞类型特异性基因的能力

### Panel E: 与 RNA-seq 相关性
- **内容**：FISSEQ 与 RNA-seq 的相关性分析
- **关键数据**：
  - 成纤维细胞：Pearson's r = 0.57
  - B 细胞：Pearson's r = 0.47
  - iPS 细胞：Pearson's r = 0.23
- **意义**：展示了 FISSEQ 与传统方法的一致性

### Panel F: 亚细胞定位富集
- **内容**：不同 RNA 类型的亚细胞定位
- **关键信息**：非编码 RNA 核富集，mRNA 质定位
- **意义**：展示了 FISSEQ 的亚细胞定位能力

### Panel G: FN1 选择性剪接
- **内容**：FN1 mRNA 的选择性剪接变体
- **关键信息**：
  - 481 个扩增子比对到 FN1
  - 显示 EDA 和 IIICS 变体
  - 检测到单核苷酸多态性
- **意义**：展示了 FISSEQ 检测选择性剪接的能力

## 总体结论

Fig. 3 全面展示了 FISSEQ 技术的性能：
1. **高准确性**：90.6% 正链比对率
2. **全面性**：检测 mRNA 和非编码 RNA
3. **一致性**：与 RNA-seq 相关性良好
4. **亚细胞分辨率**：可以分析 RNA 的亚细胞定位
5. **剪接分析**：可以检测选择性剪接变体

## 关联 Figures / Extended Data

- **fig. S8**: 测序错误率分析
- **fig. S9**: 自动化分析流程
- **fig. S10**: 扩增子比对统计
- **fig. S11**: 与基因表达芯片比较
- **fig. S12**: 高表达基因功能分析
- **table S1**: 基因表达数据
- **table S2**: MALAT1 和 NEAT1 定位数据
- **table S3**: mRNA 亚细胞定位数据
