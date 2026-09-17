# Fig. 2 — Spatial-ATAC-Hi-C reveals spatially resolved cell types of mouse brain

## Caption（原文）
> a, An unsupervised clustering analysis was performed based on the gene-associated domain score derived from spatial Hi-C data. An overlay of clusters with tissue image reveals the spatial distribution of the clusters (left). Uniform manifold approximation and projection (UMAP) embedding of the clustering analysis from spatial Hi-C data (right). b, An unsupervised clustering analysis was performed based on the GAS derived from spatial-ATAC-seq data. An overlay of clusters with tissue image reveals the spatial distribution of the clusters (left). UMAP embedding of the clustering analysis from spatial-ATAC-seq data (right). c, Mouse brain region anatomy annotation from Allen Brain Institute (https://mouse.brain-map.org/static/atlas). d, Mouse brain class annotation from Allen Brain Institute (https://mouse.brain-map.org/static/atlas). e, Projection of mouse brain R6 spatial-ATAC-seq data (right) to single-cell ATAC-seq data from mouse brain (left). f, Spatial distribution of each cell type from e in mouse brain R6 sample. g, Spatial distribution of GAD scores (top), GAS (middle) and MERFISH (bottom) for selected marker genes. h, Heatmap of genes with differential activity scores in excitatory neuron, inhibitory neuron and non-neuron cell types. i, GO term enrichment of excitatory neuron marker genes. The statistical significance of GO term enrichment was assessed using Fisher's exact test.

## Panel-by-Panel 解读

### Panel a — 基于Hi-C数据的无监督聚类
**结论**：基于基因关联域（GAD）评分的聚类分析识别出8个空间分布明确的聚类，与脑区解剖结构高度吻合。

**关键数据**：识别出8个聚类（H0–H7），空间分布与Allen Brain Atlas的解剖区域一致。

### Panel b — 基于ATAC-seq数据的无监督聚类
**结论**：基于基因活性评分（GAS）的聚类分析识别出7个聚类，与Hi-C聚类结果高度一致。

**关键数据**：识别出7个聚类（A0–A6），与Hi-C聚类结果显示出强一致性。

### Panel c — Allen Brain Atlas解剖注释
**结论**：展示了小鼠脑的解剖区域注释，包括纹状体、丘脑、下丘脑等区域，作为聚类结果的参考标准。

**关键数据**：来自Allen Brain Institute的标准解剖注释。

### Panel d — 细胞类型类别注释
**结论**：展示了MERFISH数据的细胞类型类别注释，用于验证Spatial-ATAC-Hi-C的细胞类型鉴定结果。

**关键数据**：包括兴奋性神经元、抑制性神经元和非神经元细胞等主要类别。

### Panel e — 单细胞ATAC-seq数据投影
**结论**：将空间ATAC-seq数据投影到已发表的单细胞ATAC-seq小鼠脑图谱数据上，实现细胞类型注释。

**关键数据**：投影到BICCN小鼠脑图谱的单细胞ATAC-seq数据。

### Panel f — 细胞类型空间分布
**结论**：展示了从单细胞ATAC-seq投影获得的细胞类型在组织中的空间分布，与MERFISH注释高度一致。

**关键数据**：15种细胞类型的空间分布模式。

### Panel g — 标记基因的空间模式
**结论**：展示了已知标记基因（Adora2a, Penk, Cldn11, Satb2）的GAD评分、GAS和MERFISH信号空间分布，三者高度一致。

**关键数据**：Adora2a和Penk在纹状体区域高表达，Cldn11在少突胶质细胞区域高表达，Satb2在皮层兴奋性神经元高表达。

### Panel h — 差异活性基因热图
**结论**：识别出915个主要细胞类型特异性基因，包括兴奋性神经元标记Satb2和Neurod6，抑制性神经元标记Adora2a和Gad2，非神经元标记Mpo和Nfia。

**关键数据**：n = 915个细胞类型特异性基因。

### Panel i — 兴奋性神经元标记基因GO富集
**结论**：兴奋性神经元标记基因富集于神经系统发育和谷氨酸能突触信号传导相关通路。

**关键数据**：富集通路包括突触组装、离子型谷氨酸受体信号通路、兴奋性突触后电位正调控等。

## 总体结论
Fig. 2证明Spatial-ATAC-Hi-C能够在小鼠脑组织中空间分辨复杂的细胞身份。通过Hi-C和ATAC-seq两种数据模态的聚类分析，以及与单细胞ATAC-seq图谱和MERFISH数据的系统比较，该技术成功鉴定了兴奋性神经元、抑制性神经元和非神经元细胞类型，并识别出915个细胞类型特异性基因和1,006个细胞类型特异性开放染色质区域。

## 关联 Figures / Extended Data
- Extended Data Fig. 5（R8样本的聚类分析和细胞类型注释）
- Supplementary Fig. 1（Gad2和Neurod6基因区域的伪批量轨迹，细胞类型特异性开放染色质区域）
