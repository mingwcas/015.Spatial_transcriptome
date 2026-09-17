# Method: Cell Segmentation

## 原文（Methods）
> With the observation that unspliced RNA signals for a cell are much more aggregated than those of spliced, we used method in Spateo to segment individual cells through unspliced RNA signals within spots. Specifically, we first aggregated unspliced RNA signals of all genes from a spot together to obtain total signals of the spot. Thus, we got a two-dimensional array with each element as a spot and value on each element as the total unspliced RNA signals on this spot. Second, we applied Gaussian blur with kernel size 21 on unspliced signal array to generate a smoothed array. After this step, we could see plenty of 'mountain-like' peaks and plains which indicates cell centroids and non-cell regions, respectively. Third, OTSU was used to find a cutoff to split array into cell and non-cell regions based on the smoothed array and we only considered cell regions in following steps. Fourth, we performed Watershed algorithm to split cell regions into individual cells until all cells have their unique labels with previous 'mountain-like' peaks as seeds. Fifth, since we only considered unspliced RNA signals above, the segmented cells would much more like cell nucleus rather than whole cells, so we expanded our segmentations with several iterations, each iteration only expanded one spot around cells, to include cytoplasm regions. Here each cell would be expanded at most 11 times unless the spot number it covered was larger than 600. Last, with the region information of each cell, we congregate RNA signals of all genes from all spots covered by a cell to be the gene expression profile of this cell, and generate a cell-to-gene AnnData object.

## 解读

### 意义
将空间转录组数据中的spot分割成单个细胞，实现单细胞分辨率的空间转录组分析。

### 输入
- 空间转录组表达矩阵
- unspliced RNA信号
- 空间坐标

### 输出
- 单细胞分割结果（每个细胞的边界和包含的spots）
- 单细胞基因表达矩阵（AnnData格式）

### 核心步骤
1. 聚合每个spot的所有unspliced RNA信号
2. 高斯模糊平滑（kernel size=21）
3. OTSU自动阈值分割细胞/非细胞区域
4. Watershed算法从"山峰"种子分割单个细胞
5. 迭代扩展包含细胞质区域（最多11次扩展）
6. 汇总每个细胞覆盖的所有spots的基因表达

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 高斯模糊kernel | 21 | 平滑unspliced信号 |
| 扩展迭代上限 | 11次 | 包含细胞质 |
| 最大spot数限制 | 600 | 单细胞最大大小 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Unspliced RNA | 未剪接RNA，留在细胞核内 |
| OTSU | 自动阈值分割算法 |
| Watershed | 分水岭图像分割算法 |
| AnnData | 单细胞数据标准格式 |

## 复现
- Spateo: https://github.com/aristoteleo/spateo-release
- OpenCV: Python cv2 library

## 生物学意义
细胞分割是实现单细胞分辨率空间转录组分析的关键步骤，使得可以研究细胞类型组成和空间分布。

## 涉及 Figures
- Fig. 2A, 2D, 2E (cell segmentation results)
