# Fig. 1 — Spatial-CITE-seq workflow design and application to diverse mouse tissue types and human tonsil for co-mapping of proteins and whole transcriptome

## Caption（原文）
> a, Scheme of spatial-CITE-seq. A cocktail of ADTs is applied to a PFA-fixed tissue section to label a panel of ~200–300 protein markers in situ. Next, a set of DNA barcodes A1–A50 is flowed over the tissue surface in a spatially defined manner via parallel microchannels, and reverse transcription is carried out inside each channel for in-tissue synthesis of cDNAs complementary to endogenous mRNAs and introduced ADTs. Then, a set of DNA barcodes B1–B50 is introduced using another microfluidic device with microchannels perpendicular to the first flow direction and subsequently ligated to barcodes A1–A50, creating a 2D grid of tissue pixels, each of which has a unique spatial address code AB. Finally, barcoded cDNA is collected, purified, amplified and prepared for paired-end NGS sequencing. b, Spatially resolved 189-plex protein and whole transcriptome co-mapping of mouse spleen, colon, intestine and kidney tissue with 25-µm pixel size. Upper row: bright-field optical images of the tissue sections. Middle row: unsupervised clustering of all pixels based on all 189 protein markers only and projection onto the tissue images. Lower row: unsupervised clustering of whole transcriptome of all pixels and projection to the tissue images. Colors correspond to different proteomic or transcriptomic clusters indicated on the right side of each panel. c, Image of a human tonsil tissue section. The region mapped by spatial-CITE-seq is indicated by a dashed box. d, Per-pixel UMI count and protein count histograms. e, UMAP plot of the clustering analysis of all pixels based on 273 proteins only. f, Spatial distribution of the clusters (0–6) indicated by the same colors as in e. g, UMAP plot of the clustering analysis of all pixels based on the mRNA transcriptome. h, Spatial distribution of the transcriptomic clusters (0–5) indicated by the same colors as in g. Pixel size: 25 µm. i, Differentially expressed proteins in the clusters shown in c and d. j, Tissue image of the mapped region (left), spatial proteomic clusters (right) and the overlay (middle). k, Individual surface protein markers related to B cells and follicular DCs. l, Functional protein markers such as immunoglobulins showing spatially distinct distribution of GC B cells (IgM), matured B cells (IgG) and naive B cells (IgD), in agreement with B cell maturation, class switch and migration. m, Individual protein markers enriched in the extracellular region (CD90, Notch3) and crypt (Mac2). n, Individual T cell protein markers CD3, CD4 and CD45RA showing T cell zones and subtypes. o, Individual protein markers CD32, CD9 and CD171. CD32 identified a range of immune cells, including platelets, neutrophils, macrophages and DCs, trafficking from vasculature. CD9 identified plasma cell precursors in GCs and crypt. CD171, a neural cell adhesion molecule, is found highly distinct in the GC dark zone. To our knowledge, this has not been reported previously and warrants further investigation. Color key: protein expression from high to low.

## Panel-by-Panel 解读

### Panel a — Spatial-CITE-seq工作流程
**结论**：展示spatial-CITE-seq的四步工作流程：ADT染色 → Barcode A原位逆转录 → Barcode B原位连接 → 测序文库构建
**关键数据**：50×50微通道网格，25 µm像素大小，~200-300种蛋白标记物

### Panel b — 小鼠多组织189-plex蛋白质和转录组共映射
**结论**：在小鼠脾、结肠、小肠和肾四种组织中成功实现189种蛋白质和全转录组的空间共映射
**关键数据**：189-plex蛋白质panel，25 µm像素大小，蛋白质聚类和转录组聚类在解剖区域上高度一致

### Panel c-d — 人扁桃体组织区域和数据质量
**结论**：展示人扁桃体2.5 mm × 2.5 mm映射区域，每像素平均蛋白质计数239，UMI计数4,309
**关键数据**：平均蛋白质计数/pixel = 239，平均UMI计数/pixel = 4,309

### Panel e-f — 人扁桃体273蛋白质聚类
**结论**：基于273种蛋白质的无监督聚类识别出7个主要空间域（clusters 0-6），空间分布高度distinct
**关键数据**：7个蛋白质聚类，清晰分辨生发中心明区/暗区、T细胞区、隐窝等结构

### Panel g-h — 人扁桃体转录组聚类
**结论**：转录组聚类识别8个clusters，与蛋白质聚类correlated但噪声更大、精度更低
**关键数据**：8个转录组聚类

### Panel i — 差异表达蛋白分析
**结论**：差异表达分析识别每个聚类中的主要细胞类型标记物
**关键数据**：展示了CD19、CD21、CD23、CD3、CD90等关键标记物的聚类特异性表达

### Panel j — 组织图像与蛋白质聚类叠加
**结论**：蛋白质聚类与解剖特征高度吻合，验证了spatial-CITE-seq的空间分辨能力

### Panel k — B细胞和滤泡树突状细胞标记物
**结论**：CD19富集于滤泡，CD21在所有成熟B细胞和滤泡树突状细胞中高表达，CD23限制在生发中心明区顶端区域
**关键数据**：CD19（B细胞标记），CD21/CR2（成熟B细胞+FDC），CD23（GC明区）

### Panel l — 免疫球蛋白标记物
**结论**：IgM限制在GC B细胞，IgG在成熟B细胞中表达（迁移出滤泡），IgD主要由naive B细胞产生
**关键数据**：IgM → GC B细胞，IgG → 成熟B细胞，IgD → naive B细胞，反映B细胞成熟和类别转换

### Panel m — 细胞外区域和隐窝标记物
**结论**：CD90广泛表达但GC中完全缺失，Notch3在鳞状上皮细胞中，Mac2/Galectin3富集在隐窝区
**关键数据**：CD90（Thy-1），Notch3，Mac2/Galectin3

### Panel n — T细胞标记物
**结论**：CD3识别所有主要T细胞区，CD4标记辅助T细胞，CD45RA标记naive/干细胞样T细胞
**关键数据**：CD3（总T细胞），CD4（辅助T细胞），CD45RA（naive T细胞）

### Panel o — 其他免疫标记物
**结论**：CD32（Fc受体）主要在GC外，CD9在滤泡和隐窝的浆细胞前体中，CD171（神经细胞粘附分子）高度特异性地富集在GC暗区——此前未报道
**关键数据**：CD171在GC暗区的高度特异性富集是新发现

## 总体结论
Fig. 1是本文的核心结果图，展示了spatial-CITE-seq技术的完整工作流程和在多种组织类型中的应用。关键发现包括：(1) 高plex蛋白质组（189-273种）能够在多种组织中实现空间域的精确识别；(2) 蛋白质聚类比转录组聚类更精确、噪声更少；(3) 人扁桃体中发现了CD171在生发中心暗区的高度特异性富集等新生物学发现。

## 关联 Figures / Extended Data
- **Extended Data Fig. 1** — Spatial-CITE-seq详细设计和工作流程
- **Extended Data Fig. 2** — 小鼠多组织的空间映射详情
- **Extended Data Fig. 3** — 免疫荧光验证
- **Extended Data Fig. 4** — 与scCITE-seq和免疫荧光的比较
- **Extended Data Fig. 5** — 人脾和胸腺的空间映射
- **Extended Data Table 1** — 基因和蛋白质计数汇总
