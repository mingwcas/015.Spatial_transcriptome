# Method: Multiplex Immunofluorescence and Image Analysis

## 原文（Methods）
> FFPE sections were stained using the Opal Polaris 7-color kit (Akoya) on a Leica BOND Rx autostainer. Primary antibodies included panCK/Opal-620, PD-L1/Opal-480, CD8/Opal-780, CD68/Opal-690, CD11C/Opal-520, and CD163/Opal-570. Slides were counterstained with DAPI and imaged with spectral unmixing. Image analysis was performed using inForm software (PerkinElmer), with tissue segmentation into CK+ tumor and CK⁻ stromal regions. Cell segmentation was performed based on nuclear boundaries followed by phenotype assignment using a supervised classifier trained on representative tumor and stromal regions to minimize arbitrary intensity cut-offs. Spectral unmixing, background subtraction, and batch correction were conducted using optimized default parameters in inForm. Cells were not positive for any of the six markers designated as unassigned and are reported. Spatial proximity metrics were quantified using the phenoptr R package (v0.3.2). Centroid-to-centroid nearest-neighbor distances were calculated between CK+PD-L1+ tumor cells and immune subsets, and the number of neighboring cells within a fixed 15-µm radius was summarized to assess local immune–tumor interactions.

## 解读

### 意义
多重免疫荧光技术可在单张组织切片上同时检测6种蛋白标记，结合空间分析量化肿瘤-免疫细胞的空间相互作用，是本研究的核心空间组学方法。

### 输入
- FFPE组织切片
- Opal Polaris 7-color kit（Akoya）
- Leica BOND Rx自动染色机
- 一抗：panCK、PD-L1、CD8、CD68、CD11C、CD163
- inForm软件（PerkinElmer）
- phenoptr R包（v0.3.2）

### 输出
- 多光谱成像图片（6通道）
- 组织分割结果（CK+肿瘤区、CK-基质区）
- 细胞分型结果（各类免疫细胞亚群）
- 空间邻近数据（最近邻距离、15 μm半径内细胞数）

### 核心步骤
1. Leica BOND Rx自动染色机进行Opal Polaris 7色多标染色
2. DAPI复染核
3. 多光谱成像 + 光谱拆分
4. inForm软件分析：
   - 组织分割（CK+ vs CK-）
   - 细胞分割（基于核边界）
   - 监督学习分类器表型赋值
   - 光谱拆分、背景扣除、批次校正
5. phenoptr R包计算空间指标：
   - CK+PD-L1+肿瘤细胞与各类免疫细胞的质心最近邻距离
   - 15 μm半径内邻近细胞数

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 染色平台 | Leica BOND Rx | 自动染色机 |
| 多标试剂盒 | Opal Polaris 7-color (Akoya) | |
| 标记组合 | panCK/Opal-620, PD-L1/Opal-480, CD8/Opal-780, CD68/Opal-690, CD11C/Opal-520, CD163/Opal-570 | |
| 分析软件 | inForm (PerkinElmer) | |
| 空间半径 | 15 µm | 邻近细胞分析 |
| 空间工具 | phenoptr R v0.3.2 | |
| 细胞分类 | 监督分类器 | 减少主观阈值设定 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| mIHC | Multiplex immunohistochemistry，多重免疫组化 |
| Opal Polaris | Akoya多重荧光染色技术 |
| 光谱拆分 | Spectral unmixing，分离重叠荧光信号 |
| 最近邻距离 | Nearest-neighbor distance，质心间最短距离 |
| CK | Cytokeratin，细胞角蛋白（肿瘤上皮标记） |
| PD-L1 | 程序性死亡配体1 |
| CD8 | 细胞毒性T细胞标记 |
| CD68/CD163 | 巨噬细胞标记（CD68为泛巨噬细胞，CD163为M2型） |
| CD11C | 树突状细胞/巨噬细胞标记，常用于M1型巨噬细胞 |

## 复现
- 工具/URL：
  - inForm software: https://www.perkinelmer.com/informatics/products/image-analysis/inform
  - phenoptr: https://github.com/PerkinElmer/phenoptr
- 代码片段：
```R
library(phenoptr)
# 计算最近邻距离
nn_distances <- compute_neighbors(cell_data, cell_types, radius = 15)
# 计算15µm半径内细胞数
neighbor_counts <- count_neighbors_within_radius(cell_data, radius = 15)
```

## 生物学意义
多标空间分析揭示了PD-L1+肿瘤细胞与CD8+ T细胞、M1/M2型巨噬细胞的空间配置关系，是理解免疫检查点抑制剂响应异质性的关键。

## 涉及 Figures
- **Fig. 3** — 空间邻近分析，PD-L1+肿瘤细胞与免疫亚群的距离关系
- **Supplementary Figure S3-1 to S3-3** — 代表性分割输出和最近邻图
- **Supplementary Figure S4** — mIHC来源的细胞密度数据
