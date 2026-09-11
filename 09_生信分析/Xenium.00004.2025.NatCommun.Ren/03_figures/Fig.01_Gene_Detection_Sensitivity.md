# Fig. 1 — Evaluation of Gene Detection Sensitivity Across ST Platforms

## Caption（原文）
> Fig. 1 | Evaluation of gene detection sensitivity across ST platforms. a Experimental workflow. For each tumor type (COAD, HCC, OV), samples were divided into three parts: (1) FFPE blocks were used for Visium HD FFPE, CosMx 6K, and Xenium 5K; (2) fresh-frozen OCT-embedded tissue was used for Stereo-seq v1.3; (3) dissociated tissue was subjected to scRNA-seq. Sections adjacent to each ST slide were profiled by 16-plex CODEX for spatial proteomics. b H&E staining and EPCAM expression from ST data, along with PanCK staining from adjacent CODEX sections of COAD samples across the four ST platforms. Color intensity reflects the transcript count per 8 μm bin. Scale bars, 1 mm. c Mean transcript count per 8 μm bin for selected marker genes, computed across all bins with non-zero expression values over the entire tissue sections. d Pearson correlation of gene expression levels between ST data and scRNA-seq data. For each gene, the total transcript counts across three cancer types were averaged and log10 transformed. Each data point represents one gene. The diagonal red line indicates a slope of 1, and color intensity corresponds to relative gene counts. R denotes the correlation coefficient, and n indicates the number of genes included in the analysis. e Log2-transformed total transcript count per gene across the ten selected regions (400 × 400 μm each) in HCC and OV. Each data point represents one gene (n = 17,134 for Stereo-seq v1.3 and Visium HD FFPE, n = 6175 for CosMx 6K, n = 5001 for Xenium 5K). Center lines indicate the median value, and lower and upper hinges represent the 25th and 75th percentiles, respectively. The whiskers denote 1.5× the interquartile range. f Log2-transformed gene and transcript counts per 8 μm bin within the ten selected regions in HCC and OV. Each data point represents one bin. Center lines indicate the median value, and lower and upper hinges represent the 25th and 75th percentiles, respectively. The whiskers denote 1.5× the interquartile range. g Mean sequencing saturation across the 10 selected regions for human transcripts detected by Stereo-seq v1.3 and Visium HD FFPE, calculated at stepwise increasing sequencing depths. Panel a created with BioRender.com. Source data are provided as a Source Data file.

## Panel-by-Panel 解读

### Panel a — Experimental Workflow
**结论**：实验设计采用统一处理流程，将每种癌症患者的肿瘤样本均分为三部分，分别用于四种ST平台、scRNA-seq和CODEX，确保平台间比较的可比性。
**关键数据**：每种癌症类型（COAD、HCC、OV）生成三个样本部分：
- FFPE块：Visium HD FFPE、CosMx 6K、Xenium 5K
- OCT块：Stereo-seq v1.3
- 单细胞悬液：scRNA-seq

### Panel b — EPCAM Expression Spatial Patterns
**结论**：所有四个ST平台均显示出清晰定义的EPCAM空间模式，与H&E染色和相邻CODEX切片的PanCK免疫染色一致。
**关键数据**：8 μm bin水平转录本计数（颜色强度），标尺1 mm

### Panel c — Marker Gene Detection Sensitivity
**结论**：Xenium 5K在多种标记基因上表现出最高的检测敏感性，超过了其他三个平台。
**关键数据**：每8 μm bin的平均转录本计数（所有非零表达bins计算）

### Panel d — Gene Expression Correlation with scRNA-seq
**结论**：Stereo-seq v1.3、Visium HD FFPE和Xenium 5K与scRNA-seq表现出高相关性（R分别为0.85、0.82、0.80），而CosMx 6K相关性较低（R=0.53）。
**关键数据**：
- Stereo-seq v1.3: R=0.85, n=6,098 genes
- Visium HD FFPE: R=0.82, n=4,963 genes
- CosMx 6K: R=0.80, n=16,935 genes
- Xenium 5K: R=0.53, n=16,948 genes

### Panel e — Transcript Count Distribution Across ROIs
**结论**：Stereo-seq v1.3、Visium HD FFPE和Xenium 5K表现出相当的分层分布，反映了有效的基因间差异检测能力。CosMx 6K的基因间变异较小，提示其差异表达解析能力有限。
**关键数据**：
- Stereo-seq v1.3 & Visium HD FFPE: n=17,134 genes
- CosMx 6K: n=6,175 genes
- Xenium 5K: n=5,001 genes

### Panel f — Transcript and Gene Counts Per Bin
**结论**：Visium HD FFPE在HCC和OV样本中表现出增强的检测能力。Xenium 5K在HCC中灵敏度高于CosMx 6K，但在OV中表现相反。
**关键数据**：每8 μm bin的Log2转录本和基因计数

### Panel g — Sequencing Saturation
**结论**：在相同测序深度下，Visium HD FFPE表现出比Stereo-seq v1.3更低的测序饱和度。
**关键数据**：Stereo-seq v1.3在不同测序深度下的饱和度曲线

## 总体结论
Fig. 1系统性地评估了四种高分辨率ST平台的基因检测敏感性。研究表明Xenium 5K在标记基因检测方面表现最优，而Stereo-seq v1.3、Visium HD FFPE和Xenium 5K与scRNA-seq的基因水平相关性均高于CosMx 6K，为后续平台选择提供了灵敏度的基准参考。

## 关联 Figures / Extended Data
- **Supplementary Fig. 2a, b** — 共享FFPE区域的敏感性分析
- **Supplementary Fig. 3a-e** — CosMx 6K相关性详细分析
- **Supplementary Fig. 4a-f** — 捕获效率和质量指标
