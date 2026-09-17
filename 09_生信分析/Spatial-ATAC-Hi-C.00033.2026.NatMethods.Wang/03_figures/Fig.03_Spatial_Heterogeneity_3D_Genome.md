# Fig. 3 — Spatial-ATAC-Hi-C reveals spatial heterogeneity of 3D genome architectures in mouse brain

## Caption（原文）
> a, Heatmap of differential compartment regions (left) and GAS (right) of compartment region correlated genes (overlapped with the compartment regions and PCC of compartment score and GAS ≥ 0.3). b, GO term enrichment of compartment region correlated genes shown in a. IL, interleukin. c, Excitatory neuron-specific chromatin loop involving Satb2 gene. The loop anchors are highlighted in blue and orange shades. Pseudobulk Hi-C map of inhibitory neuron (top triangle) and excitatory neuron (bottom triangle) at genomic region chr1: 55.5–58.5 Mb (top). Virtual 4C interaction track anchored at Satb2 region (bottom). d, Excitatory neuron-specific chromatin loop involving Satb2 gene in snm3C dataset. The loop anchors are highlighted in blue and orange shades. Pseudobulk Hi-C map of CNU-LGE GABA (top triangle) and IT-ET Glut (bottom triangle) at genomic region chr1: 55.5–58.5 Mb (top). Virtual 4C interaction track anchored at Satb2 region (bottom). e, Spatial loop signal at single-pixel resolution for the differential loop involving Satb2 showed in c. f, Inhibitory neuron-specific chromatin loop involving Gpr88 gene. The loop anchors are highlighted in blue and orange shades. Pseudobulk Hi-C map of inhibitory neuron (top triangle) and excitatory neuron (bottom triangle) at genomic region chr3: 115.3–117.3 Mb (top). Virtual 4C interaction track anchored at Gpr88 region (bottom). g, Inhibitory neuron-specific chromatin loop involving the Gpr88 gene in the snm3C dataset. The loop anchors are highlighted in blue and orange shades. Pseudobulk Hi-C map of CNU-LGE GABA (top triangle) and IT-ET Glut (bottom triangle) at genomic region chr3: 115.3–117.3 Mb (top). Virtual 4C interaction track anchored at Gpr88 region (bottom). h, Spatial loop signal at single-pixel resolution for the differential loop involving Gpr88 showed in f. i, Aggregate peak analysis (APA) plots of cell-type-specific loops in mouse R6 sample (left) and GO term enrichment of genes located in the corresponding cell-type-specific loop anchors (right). j, Bubble plot of transcription factor motif enrichment at chromatin accessible regions located in cell-type-specific loops in i. Bubble size and color represent the significance of enrichment (−log10 P value). Significance of motif enrichment was assessed using hypergeometric test. The statistical significances of GO term enrichment in b and i were assessed using Fisher's exact test.

## Panel-by-Panel 解读

### Panel a — 差异A/B区室区域
**结论**：展示了细胞类型特异性A/B区室区域及其与基因活性评分的相关性，揭示了染色质区室化的细胞类型特异性。

**关键数据**：识别出1,683个细胞类型特异性A/B区室区域，其中765个显示出PC1值与GAS评分的高相关性（PCC > 0.3）。

### Panel b — 区室相关基因GO富集
**结论**：不同细胞类型特异性区室中的基因显示出生物学上一致的功能特征。

**关键数据**：兴奋性神经元特异性区室富集于突触功能相关术语；抑制性神经元特异性区室富集于GPCR信号和谷氨酸受体信号；非神经元特异性区室富集于免疫相关术语。

### Panel c — 兴奋性神经元特异性染色质环（Satb2）
**结论**：展示了Satb2基因启动子区域与远端染色质可及性区域（约1 Mb远）之间的兴奋性神经元特异性染色质环。

**关键数据**：基因组区域chr1: 55.5–58.5 Mb，兴奋性神经元的染色质相互作用信号显著高于抑制性神经元（ANOVA, P = 6.87 × 10−6）。

### Panel d — snm3C数据验证（Satb2环）
**结论**：snm3C单细胞3D基因组数据验证了Satb2基因的兴奋性神经元特异性染色质环。

**关键数据**：CNU-LGE GABA（抑制性）和IT-ET Glut（兴奋性）神经元的伪批量Hi-C图谱与Spatial-ATAC-Hi-C结果一致。

### Panel e — Satb2环的空间信号分布
**结论**：Satb2环在单像素水平上显示出空间特异性，信号在皮层区域特异性高表达。

**关键数据**：环信号在isocortex区域特异性富集。

### Panel f — 抑制性神经元特异性染色质环（Gpr88）
**结论**：展示了Gpr88基因的抑制性神经元特异性染色质环。

**关键数据**：基因组区域chr3: 115.3–117.3 Mb，抑制性神经元的染色质相互作用信号显著高于兴奋性神经元。

### Panel g — snm3C数据验证（Gpr88环）
**结论**：snm3C数据验证了Gpr88基因的抑制性神经元特异性染色质环。

**关键数据**：CNU-LGE GABA和IT-ET Glut神经元的伪批量Hi-C图谱与Spatial-ATAC-Hi-C结果一致。

### Panel h — Gpr88环的空间信号分布
**结论**：Gpr88环在单像素水平上显示出空间特异性，信号在纹状体区域特异性高表达。

**关键数据**：环信号在striatum区域特异性富集。

### Panel i — 细胞类型特异性环的APA分析和GO富集
**结论**：系统鉴定了细胞类型特异性染色质环，并分析了环锚定基因的功能富集。

**关键数据**：识别出268个兴奋性神经元特异性、556个抑制性特异性和41个非神经元特异性环。

### Panel j — 转录因子motif富集
**结论**：细胞类型特异性环锚定的开放染色质区域显示出不同的转录因子motif富集模式。

**关键数据**：兴奋性神经元富集Jun-AP1和Fosl2（活动依赖性转录程序），抑制性神经元富集Meis1（纹状体中型多棘神经元分化）。

## 总体结论
Fig. 3揭示了小鼠脑中3D基因组架构的空间异质性。通过分析细胞类型特异性A/B区室和染色质环，证明Spatial-ATAC-Hi-C能够在空间水平上识别细胞类型特异性的染色质结构特征。Satb2和Gpr88基因的细胞类型特异性染色质环通过snm3C数据得到验证，并在单像素水平上显示出明确的空间分布模式。系统分析识别出865个细胞类型特异性染色质环，其功能富集与已知的细胞生物学功能一致。

## 关联 Figures / Extended Data
- Extended Data Fig. 6（R8样本的A/B区室和染色质环分析，Neurod6基因的兴奋性神经元特异性环）
- Supplementary Table 7–9（细胞类型特异性区室和环的详细数据）
