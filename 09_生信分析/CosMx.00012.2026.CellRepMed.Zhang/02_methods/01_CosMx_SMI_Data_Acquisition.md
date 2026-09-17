# Method: CosMx SMI Data Acquisition and Processing

## 原文（Methods）
> Spatial molecular imaging was conducted using the CosMx SMI platform (Bruker Spatial Biology) according to company manuals. Sample selection and preparation: FFPE blocks of primary and lymph node metastases were reviewed by two board-certified pathologists to confirm the diagnosis, and assess the quality of the tissue and tumor content. Representative tumor regions identified via H&E staining were selected to construct two tissue microarrays (TMAs). For TMA construction, 1 mm cores from each sample were arrayed into a recipient block. Serial 5 μm sections were cut from the TMA blocks and adhered onto VWR Superfrost Plus slides for subsequent CosMx SMI analysis and H&E staining. SMI library preparation and hybridization: The CosMx Human Universal Cell Characterization Panel (1000-plex RNA panel) was used for spatial transcriptomic profiling, strictly following the manufacturer's protocol (MAN-10184-02, Bruker Spatial Biology). The workflow included deparaffinization, target retrieval at 100°C for 15 min, protease digestion at 40°C for 30 min, overnight hybridization with the 1000-plex gene-specific probe panel, and serial rounds of fluorescent reporter hybridization, imaging, and cleavage (16 cycles) to decode all targets. Morphological staining and imaging: Following RNA readout, the samples were stained with a five-fluorophore-conjugated antibody panel for cellular segmentation: DAPI (nuclei), PanCK (epithelium), CD45 (immune cells), CD68 (macrophages), and a cocktail of B2M/CD298 (membrane). z-stack images (eight slices at 0.8 μm intervals) were acquired for each field of view (FOV, 260,100 μm²) using the CosMx SMI instrument. Image processing and cell segmentation: Raw image data were processed using the AtoMx Spatial Informatics Platform (v1.3). Single-cell segmentation was performed using the 'Cellpose' pretrained neural network model. This algorithm leverages the nuclear (DAPI), membrane (B2M/CD298), and protein morphology (PanCK, CD45 and CD68) signals to delineate cell boundaries. Transcripts were then assigned to cells based on their spatial coordinates relative to the segmented boundaries. Data preprocessing and quality control: Following the quality control pipeline, cells with negative probe counts ≥1 or total detected genes ≤20 were removed. Cells co-expressing high levels of both PanCK and CD45 protein (likely due to segmentation errors) were excluded. After quality control, 604,230 high-quality cells (81.5% of the total number of cells) were retained for downstream analysis. Gene expression counts were log-normalized (log1p) using Seurat (v5.1.0). Technical batch effects across samples were corrected using 'Harmony' (v1.0) applied to the top 50 principal components.

## 解读

### 意义
该方法通过CosMx Spatial Molecular Imager平台对SCLC原发肿瘤和淋巴结转移样本进行高plex空间转录组学分析，在单细胞分辨率下获取细胞的转录组信息和空间位置信息。

### 输入
- FFPE组织样本（105例来自75位SCLC患者）
- CosMx Human Universal Cell Characterization Panel (1000-plex RNA panel)
- 用于细胞分割的抗体混合液（DAPI, PanCK, CD45, CD68, B2M/CD298）

### 输出
- 604,230个高质量单细胞数据
- 294 million转录本
- 384个FOV（每个FOV覆盖510μm × 510μm面积）
- Harmony批次校正后的表达矩阵

### 核心步骤
1. 样本收集与TMA构建（1mm直径组织芯）
2. 切片脱蜡、目标物Retrieval（100°C 15min）、蛋白酶消化（40°C 30min）
3. 过夜杂交1000-plex基因特异性探针
4. 16轮荧光报告子杂交-成像-切割循环
5. 五色荧光抗体染色用于细胞分割
6. z-stack成像（8层，0.8μm层厚）
7. AtoMx Spatial Informatics Platform处理原始图像
8. Cellpose预训练神经网络进行细胞分割
9. 转录本根据空间坐标分配到对应细胞
10. 质控过滤（去除负探针计数≥1或基因数≤20的细胞）
11. Seurat log-normalization (log1p)
12. Harmony批次校正

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 探针panel | CosMx 1000-plex RNA panel | 1000个基因 |
| 循环轮数 | 16 cycles | 解码所有靶标 |
| FOV大小 | 260,100 μm² | 约510μm × 510μm |
| z-stack层数 | 8层 @ 0.8μm间隔 | 0.8μm × 8 = 6.4μm总深度 |
| 质控过滤-负探针 | ≥1 | 剔除 |
| 质控过滤-基因数 | ≤20 | 剔除 |
| Harmony PCs | top 50 | 批次校正 |
| 最终保留细胞数 | 604,230 (81.5%) | 质控后高质量细胞 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CosMx SMI | Bruker Spatial Biology的空间分子成像平台 |
| FOV (Field of View) | 成像视野，本研究中每个FOV约510μm × 510μm |
| Cellpose | 预训练的细胞分割神经网络模型 |
| AtoMx SIP | AtoMx Spatial Informatics Platform，数据处理软件 |
| Harmony | 批次效应校正工具 |
| TMA | 组织芯片，1mm直径组织芯构建 |
| Ro/e | Ratio of observed to expected，观察值/期望值比值 |

## 复现
- 工具/代码/URL：AtoMx Spatial Informatics Platform (v1.3), Cellpose segmentation
- 代码片段：
```r
# Seurat + Harmony batch correction
library(Seurat)
library(harmony)
pbmc <- NormalizeData(pbmc)
pbmc <- FindVariableFeatures(pbmc)
pbmc <- ScaleData(pbmc)
pbmc <- RunPCA(pbmc, npcs = 50)
pbmc <- RunHarmony(pbmc, group.by.vars = "sample", dims.use = 1:50)
```

## 生物学意义
该方法实现了在FFPE组织样本上进行高plex空间转录组学分析，保持了组织的空间架构信息。单细胞分辨率使得能够精确定位每个细胞的转录组特征及其在组织中的空间位置，为研究肿瘤微环境中细胞间空间相互作用提供了技术基础。1,000-plex panel覆盖了主要的细胞类型标志物和疾病相关基因，能够满足系统性研究需求。

## 涉及 Figures
- **Fig. 1** — CosMx SMI工作流和单细胞空间转录组学分析框架
