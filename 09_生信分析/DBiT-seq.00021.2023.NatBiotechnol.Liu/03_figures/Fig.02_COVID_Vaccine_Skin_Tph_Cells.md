# Fig. 2 — Integrated spatial and single-cell profiling of a human skin biopsy tissue at the site of COVID-19 mRNA vaccination injection revealed localized peripheral T cell activation

## Caption（原文）
> a, Bright-field image of skin section in the mapped region. A pilosebaceous unit is indicated by the dashed region. b, Gene count spatial map. c, Spatial clustering of all pixels based on whole transcriptome. Despite low gene count in the low cell density regions of dermal collagen, the clustering analysis revealed spatially distinct zones based on transcriptomic profiles. d, UMAP clustering of all 273 proteins. e, Protein count distribution. f, Spatial clustering of all pixels based on 273 proteins only, which is in high concordance with spatial clusters identified by spatial transcriptome co-mapped on the same tissue section. g, Integrated analysis of single-cell and spatial transcriptome. Left: The transcriptomes of spatial tissue pixels (red) conform to the clusters identified by joint analysis with scRNA-seq (blue). Middle: unsupervised clustering of the combined transcriptome dataset. Right: cell type annotation. i, Visualization of select genes associated with different gene oncology functions via integrated analysis and transfer learning. j, Differential protein expression in different cell types (APC, B cell and two subtypes of T cells). k, Spatial distribution of APCs, T cells and B cells. l, Expression of CD223 (LAG3) protein, a functional marker of activated T cells and other immune cell subsets. m, Identification of a highly localized population of Tph cells at the vaccine injection site. n, Spatial distribution of Tph gene score correlates with the cell localization. Pixel size: 25 µm.

## Panel-by-Panel 解读

### Panel a — 皮肤组织明场图像
**结论**：展示COVID-19 mRNA疫苗注射部位皮肤活检的明场图像，包含胶原丰富低细胞密度区和血管肉芽肿高细胞密度区
**关键数据**：虚线标注毛囊皮脂腺单位

### Panel b — 基因计数空间图
**结论**：基因计数与细胞密度相关，高细胞密度区域每像素411个基因
**关键数据**：高细胞密度区411 genes/pixel

### Panel c — 转录组空间聚类
**结论**：即使在低细胞密度的胶原区域，转录组聚类也能识别空间上distinct的区域
**关键数据**：低基因计数区域仍能产生有意义的聚类

### Panel d — 273蛋白质UMAP聚类
**结论**：273种蛋白质的UMAP聚类显示清晰的细胞群体分离

### Panel e — 蛋白质计数分布
**结论**：蛋白质计数在组织切片上变异较小，低密度区域仍可检测到~270种蛋白质
**关键数据**：低密度区域可检测~270种蛋白质

### Panel f — 蛋白质空间聚类
**结论**：基于273种蛋白质的空间聚类产生10个clusters，与转录组聚类高度一致
**关键数据**：10个蛋白质聚类

### Panel g — 单细胞与空间转录组整合分析
**结论**：空间像素数据（红）与scRNA-seq数据（蓝）的整合分析显示良好一致性，识别出13个主要clusters
**关键数据**：13个主要聚类，8种细胞类型注释（内皮细胞、成纤维细胞、角质形成细胞、巨噬细胞、黑色素细胞、肌肉细胞、T细胞等）

### Panel i — 功能基因可视化
**结论**：展示了与不同基因本体功能相关的基因空间表达，包括凋亡相关基因（CCNL2, NOL3）、脂蛋白代谢（APOC1）、连接蛋白（GJA1）等
**关键数据**：CCNL2/NOL3在血管区，APOC1/GJA1/PRDX2在血管区，TMEM132D/ALG5在真皮区，CYP4F8在大部分皮肤区域

### Panel j — 差异表达蛋白分析
**结论**：APC、B细胞和两种T细胞亚型的差异表达蛋白标记物
**关键数据**：展示了APC、B cell、T cell_1、T cell_2的特异性蛋白标记物

### Panel k — 免疫细胞空间分布
**结论**：APC和T细胞定位于空间上distinct的区域，B细胞分布在整个组织中
**关键数据**：APC和T细胞空间分离，B细胞广泛分布

### Panel l — CD223 (LAG3) 表达
**结论**：LAG3蛋白表达标记激活的T细胞和其他免疫细胞亚群
**关键数据**：CD223 (LAG3) 在特定免疫细胞群中表达

### Panel m — Tph细胞鉴定
**结论**：在疫苗注射部位鉴定出高度局部化的Tph（外周辅助T）细胞群体
**关键数据**：Tph细胞在注射部位富集

### Panel n — Tph签名评分空间分布
**结论**：Tph基因签名评分（LAG3, PD-1, CXCR6）的空间分布与细胞定位相关
**关键数据**：Tph signature score基于LAG3、PD-1、CXCR6表达水平

## 总体结论
Fig. 2展示了spatial-CITE-seq在临床样本中的应用——COVID-19 mRNA疫苗注射部位皮肤活检。通过整合空间高plex蛋白质组、转录组和配对scRNA-seq数据，研究者鉴定出在疫苗注射部位高度富集的Tph细胞群，这些细胞表达LAG3、PD-1和CXCR6等激活标志物，可能参与局部免疫激活和全身疫苗应答的启动。蛋白质聚类在低细胞密度区域仍表现出优越性，且与转录组聚类高度一致。

## 关联 Figures / Extended Data
- **Extended Data Fig. 6** — 皮肤活检的空间热图详情（基因、UMI、蛋白质）
- **Extended Data Fig. 7** — scRNA-seq数据质量、加权最近邻分析和SPOTlight去卷积
