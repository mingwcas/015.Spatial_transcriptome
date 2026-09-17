# Method: Xenium In Situ Workflow

## 原文（Methods）
> The Xenium In Situ technology uses targeted panels to detect gene expression. 313 genes for cell type identification (280 of which are included in the Xenium Human Breast Panel) were selected and curated primarily based on single-cell atlas data for human breast tissue. The probes were designed to contain two complementary sequences that hybridize to the target RNA and a third region encoding a gene-specific barcode, so that the paired ends of the probe bind to the target RNA and ligate to generate a circular DNA probe. If the probe experiences an off-target binding event, ligation should not occur, suppressing off-target signals and ensuring high specificity.

> The Xenium workflow (using in-development chemistry and a prototype instrument and consumables) began by sectioning 5 μm FFPE tissue sections onto a Xenium slide, followed by deparaffinization and permeabilization to make the mRNA accessible. The mRNAs were targeted by the 313 probes described above and two negative controls: (1) probe controls to assess non-specific binding and (2) genomic DNA (gDNA) controls to ensure the signal is from RNA. Probe hybridization occurred at 50 °C overnight with a probe concentration of 10 nM. After stringency washing to remove un-hybridized probes, probes were ligated at 37 °C for two hours. During this step, a rolling circle amplification (RCA) primer was also annealed. The circularized probes were then enzymatically amplified (for one hour at 4 °C followed by two hours at 37 °C), generating multiple copies of the gene-specific barcode for each RNA binding event, resulting in a strong signal-to-noise ratio. After washing, background fluorescence was quenched chemically.

> The Xenium Analyzer is fully automated and includes an imager (imageable area of about 12 × 24 mm per slide), sample handling, liquid handling, wide-field epifluorescence imaging, capacity for two slides per run, and an on-instrument analysis pipeline. The imager is a fast area scan camera featuring a high numerical aperture, a low read noise sensor, and ~200 nm per-pixel resolution. On the Xenium Analyzer, image acquisition was performed in cycles. The reagents, including fluorescently labeled probes for detecting RNA, were automatically cycled in, incubated, imaged, and removed by the instrument. Following the binding of fluorescent oligos to the amplified barcode sequence, the sample underwent 15 rounds of fluorescent probe hybridization, imaging, and probe removal. The Z-stacks were taken with a 0.75 μm step size across the entire tissue thickness.

> The Xenium Analyzer captured a Z-stack of images every cycle and in every channel, which needed to be processed and stitched to build a spatial map of the transcripts across the tissue section. Stitching was performed on the DAPI image, taking all of the stacks from different FOVs and colors to create a complete 3D morphology image (morphology.ome.tif) for each of the stained regions. First, the lens distortion in internal sensor data was corrected based on instrument calibration data. Next, the Z-stacks from the internal sensor data were further subsampled to a 3 μm step size, which was determined empirically to be a useful resolution for cell segmentation quality. Image features were then extracted from the regions where FOVs overlapped. Feature matching was performed to estimate the offsets between adjoining FOVs. The offsets were used to ensure consistent global alignment across the image. Finally, the 3D DAPI image volumes (Z-stacks) generated across FOVs were stitched together.

> The goal of RCA product image processing was to detect and filter puncta and correct distortion. A punctum is a point source in microscopy, smaller than a pixel, and is measured in units of observed photons. The 3D image volumes (Z-stacks) obtained for each FOV were processed, for four color channels and 15 cycles, to detect the puncta in 3D space that correspond to labeled RCA products. The RNA fluorescence images were scanned for punctum signals that stand out from the local background. The XYZ coordinates of each punctum were refined by examining local brightness. The signal intensity of the punctum was determined by fitting a Gaussian distribution to the observed emitted light to determine the center, size, and intensity of the point sources. We filtered out puncta that were unlikely to be from true RCA products (non-punctate or low-quality signals). Similar to DAPI images, curvature distortion was corrected.

> In order to proceed from puncta to transcripts, decoding was performed using a Xenium codebook—a collection of codewords that were assigned to genes in the gene panel (gene_panel.json). Each codeword was defined based on an expected pattern of fluorescent signals recorded across channels and cycles. Some codewords were reserved for negative controls. The fluorescent signals from all channels and cycles were compared to the codebook using a global (across all FOVs) maximum likelihood approach. This approach considered attributes such as puncta locations, their color and cycle of detections, and signal intensities.

> A Phred-style calibrated quality score (Q-Score) was assigned to each decoded transcript to signify the confidence in the decoded transcript identity. Raw Q-Scores were derived from the likelihood of the maximum likelihood codeword compared to the likelihood of other sub-optimal codewords. Codewords were mapped to targets using the gene panel information. Final Q-Scores were calculated by first binning the full range of raw Q-Scores, then the raw Q-Scores in each bin were calibrated by the proportion of "Negative Control Codewords" in the bin. A final Q-Score was assigned to each bin to ensure that each bin's Q-Scores were correctly calibrated. Three types of controls were used: 1. Negative control codewords; 2. Negative control probes; 3. Unassigned codewords. We only included transcripts with a Q-Score ≥20 in the cell-feature matrix and downstream analyses.

> In order to assign mRNA transcripts to cells, we first segment nuclei based on the signal in the DAPI morphology image and then assign transcripts to the closest nucleus within a maximum distance of 15 µm. Transcript assignment was performed using a 2D segmentation mask that was the result of combining multiple 2D segmentations taken at different Z-planes. Individual nuclei were detected and nuclei that were close in X, Y, and Z were identified as a single nucleus. The final 2D segmentation did not allow for overlapping nuclei. DAPI-based nucleus segmentation was achieved using a deep-neural-network approach. This approach is conceptually similar to the popular CellPose algorithm in that an encoder-decoder neural network does not directly solve for the segmentation mask, but instead solves a related problem that is easier to learn and allows for the imposition of geometric constraints. The training data is based on hundreds of thousands of hand-drawn cells covering a wide range of tissues imaged on the Xenium instrument. Segmentation quality was judged by holding back a subset of hand-labeled images for benchmarking purposes. We adopted the evaluation methodology used by Greenwald et al., 2021 and first proposed in Moen et al., 2019. We trained to achieve an F1 score of greater than 0.80 on benchmark datasets using an overlap threshold of 0.5 for detection.

> A variety of output files were produced by the on-instrument pipeline. The essential files used downstream were the feature-cell matrix (HDF5 and MEX formats identical to those output by Cell Ranger and Space Ranger for Chromium and Visium data, respectively), the transcripts (listing each mRNA, its 3D coordinates, and a quality score), and the cell boundaries CSV file.

## 解读

### 意义
以亚细胞空间分辨率检测靶向基因表达，实现转录本到单细胞的精确空间定位，揭示肿瘤微环境中的精细细胞组成和空间关系

### 输入
- 5 μm FFPE组织切片（连续切片）
- Xenium Human Breast Panel（280基因）+ 33个附加基因 = 313基因
- 两种阴性对照：探针对照和基因组DNA（gDNA）对照

### 输出
- feature-cell matrix（HDF5和MEX格式）
- 转录本列表（每个mRNA的3D坐标和质量分数）
- 细胞边界CSV文件
- 3D形态学图像（morphology.ome.tif）

### 核心步骤

#### Gene Panel Design
1. 基于人类乳腺组织单细胞图谱数据选择313个基因（280来自Xenium Human Breast Panel + 33附加基因）
2. 设计探针：包含两个互补序列（杂交靶标RNA）和一个基因特异性条码区
3. 探针与靶标RNA杂交后连接形成环形DNA探针，非靶标结合事件不会发生连接，确保高特异性

#### Sample Preparation
4. 将5 μm FFPE切片置于Xenium载玻片上
5. 去蜡和透化处理，使mRNA可及
6. 探针杂交（50°C过夜，探针浓度10 nM）
7. 严格洗涤去除未杂交探针
8. 探针连接（37°C，2小时），同时退火RCA引物
9. 环形探针酶促扩增（4°C 1小时 + 37°C 2小时），产生多个基因特异性条码拷贝
10. 洗涤后化学猝灭背景荧光

#### Analyzer Instrument
11. 将载玻片放入Xenium Analyzer仪器（全自动，成像面积约12×24 mm）
12. 进行15轮荧光探针杂交、成像和探针去除
13. Z-stack成像，步长0.75 μm，覆盖整个组织厚度
14. 像素分辨率~200 nm

#### Image Pre-processing
15. 根据仪器校准数据校正镜头畸变
16. Z-stack重采样至3 μm步长
17. 提取FOV重叠区域的图像特征
18. 特征匹配估计相邻FOV间的偏移量
19. 3D DAPI图像拼接，生成完整形态学图像

#### RCA Product Processing
20. 在4色通道×15循环的3D图像中检测puncta（点源信号）
21. 扫描RNA荧光图像，识别突出于局部背景的punctum信号
22. 通过局部亮度优化punctum的XYZ坐标
23. 拟合高斯分布确定点源的中心、大小和强度
24. 过滤非punctate或低质量信号
25. 校正曲率畸变

#### Decoding
26. 使用Xenium codebook将puncta解码为转录本
27. 每个codeword定义为跨通道和循环的预期荧光信号模式
28. 全局（跨所有FOV）最大似然方法比较观测信号与codebook
29. 考虑puncta位置、颜色、循环检测和信号强度

#### Q-Scores
30. 为每个解码转录本分配Phred风格校准质量分数（Q-Score）
31. 原始Q-Score基于最大似然codeword与次优codeword的似然比
32. 通过阴性控制codeword比例校准最终Q-Score
33. 三种控制类型：阴性控制codewords、阴性控制探针、未分配codewords
34. 仅保留Q-Score ≥20的转录本用于下游分析

#### Cell Segmentation
35. 基于DAPI形态学图像进行细胞核分割
36. 使用深度神经网络方法（概念类似CellPose），编码器-解码器架构
37. 结合多个Z平面的2D分割结果生成最终2D分割掩膜
38. 将转录本分配到最近的细胞核，最大距离15 μm
39. 训练基于数十万手工标注细胞，F1 score > 0.80（overlap threshold 0.5）

#### Output File Export
40. 导出feature-cell matrix（HDF5/MEX格式）、转录本列表（含3D坐标和Q-Score）、细胞边界CSV

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因面板 | 313 genes（280 Human Breast Panel + 33附加） | 靶向检测基因数 |
| 探针杂交温度 | 50°C，过夜 | 探针与靶标RNA杂交条件 |
| 探针浓度 | 10 nM | 杂交反应中的探针浓度 |
| 连接温度/时间 | 37°C，2小时 | 探针连接条件 |
| RCA扩增 | 4°C 1h + 37°C 2h | 滚环扩增条件 |
| 成像循环数 | 15 rounds | 荧光探针杂交-成像-去除的循环次数 |
| Z-stack步长 | 0.75 μm（原始），3 μm（重采样） | 组织厚度方向的成像分辨率 |
| 像素分辨率 | ~200 nm | XY平面空间分辨率 |
| 可成像面积 | ~12×24 mm/slide | 每张载玻片的最大成像区域 |
| Q-Score阈值 | ≥20 | 用于下游分析的转录本质量过滤 |
| 细胞分割最大距离 | 15 μm | 转录本分配到最近细胞核的最大距离 |
| 分割F1 score | >0.80（overlap threshold 0.5） | 深度学习分割模型性能标准 |
| 阴性控制探针占比 | 0.026% of total counts (Q≥20) | 评估非特异性结合 |
| 解码控制占比 | 0.01% of total counts (Q≥20) | 评估解码特异性 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Xenium In Situ | 10x Genomics的原位空间转录组技术，基于显微镜读取的靶向基因检测 |
| RCA | Rolling Circle Amplification，滚环扩增，将单个RNA结合事件放大为多个基因条码拷贝 |
| punctum | 显微镜中的点源信号，小于一个像素，以观测光子数衡量 |
| codebook | Xenium的编码本，定义每个基因对应的跨通道和循环的荧光信号模式 |
| codeword | codebook中的编码词，每个基因对应一个特定的荧光信号模式 |
| Q-Score | Phred风格质量分数，衡量解码转录本身份的置信度 |
| FOV | Field of View，视场，Xenium Analyzer成像的单个视野 |
| cell segmentation | 将转录本分配到细胞的过程，基于DAPI核信号和深度学习 |
| gene_panel.json | 基因面板配置文件，定义靶向基因和探针信息 |

## 复现
- 工具/代码/URL：Xenium Analyzer仪器（10x Genomics，商业产品）；Xenium Explorer软件；开发版本软件套件
- 代码片段：N/A（主要由Xenium Analyzer on-instrument pipeline自动完成）

## 生物学意义
Xenium是本研究提供最高分辨率空间信息的技术。在Sample #1中，Xenium检测到167,885个细胞和36,944,521个转录本（Q≥20），中位166个转录本/细胞。相比scFFPE-seq（中位34基因/细胞，限于313基因面板），Xenium中位62基因/细胞，灵敏度更高。Xenium的关键发现包括：(1) 识别出scFFPE-seq和Visium未检测到的三阳性受体区域（ERBB2+/ESR1+/PGR+）；(2) 在Sample #2中发现共表达肿瘤和肌上皮标记的罕见"边界细胞"；(3) 在病理学家标注为正常的导管中发现肿瘤细胞标记。Xenium的非破坏性特性允许后续H&E和IF染色，实现分子与形态学的直接对应。

## 涉及 Figures
- **Fig. 1** — 实验设计示意图，展示Xenium工作流
- **Fig. 3** — Xenium数据的高分辨率单细胞信息（空间定位、细胞分割、注释）
- **Fig. 4** — 整合scFFPE-seq和Xenium解读DCIS亚型差异
- **Fig. 5** — Xenium识别三阳性受体区域
- **Fig. 6** — Xenium发现边界细胞
- **Supp. Fig. 2** — 转录本复杂度和阴性控制评估
- **Supp. Fig. 3-4** — Xenium热图和空间图
- **Supp. Fig. 5** — 两个连续切片的重复性验证
- **Supp. Fig. 6b-f** — Xenium检测脂肪细胞标记
- **Supp. Fig. 8** — Xenium与Visium定量比较
- **Supp. Fig. 9** — Xenium RNA与IF蛋白表达的对应
