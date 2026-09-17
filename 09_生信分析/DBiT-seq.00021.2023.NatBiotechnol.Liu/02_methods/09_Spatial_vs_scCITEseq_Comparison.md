# Method: Spatial-CITE-seq Comparison with scCITE-seq

## 原文（Methods）
> The scCITE-seq dataset was obtained from a published study. It was first cleaned by removing cells with fewer than ten total ADT UMIs and further randomly downsampled to 10,000 cells. scCITE-seq and spatial-CITE-seq datasets were combined, normalized with 'SCTransform' in Seurat version 3.2 and then integrated into a single dataset to perform clustering analysis.

## 解读

### 意义
将spatial-CITE-seq数据与已发表的scCITE-seq数据进行比较和整合，验证空间蛋白质组数据的准确性。

### 输入
- 已发表的scCITE-seq数据集（人扁桃体）
- 本文的spatial-CITE-seq数据（人扁桃体）

### 输出
- 伪批量数据的相关性分析（R = 0.78）
- 整合UMAP显示共享的蛋白质表达模式

### 核心步骤
1. 获取已发表的scCITE-seq数据集
2. 质控：去除ADT UMI总数<10的细胞
3. 随机下采样至10,000个细胞
4. 与spatial-CITE-seq数据合并
5. SCTransform标准化
6. Seurat v3.2整合和聚类分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| ADT UMI阈值 | ≥10 | 质控过滤阈值 |
| 下采样数量 | 10,000 cells | scCITE-seq细胞数 |
| 整合方法 | Seurat SCTransform | 标准化后整合 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| scCITE-seq | Single-cell CITE-seq，单细胞CITE测序 |
| Pseudo-bulk | 伪批量，将单细胞数据聚合为bulk水平用于相关性分析 |
| R = 0.78 | 伪批量数据的Pearson相关系数 |

## 复现
- 工具/代码/URL
  - Seurat v3.2：https://satijalab.org/seurat/
  - 参考scCITE-seq数据：King et al., Sci. Immunol. 2021
- 代码片段：
```r
# scCITE-seq质控和整合
scCITE <- subset(scCITE, nCount_ADT >= 10)
scCITE <- subset(scCITE, cells = sample(Cells(scCITE), 10000))
combined <- merge(spatial_CITE, scCITE)
combined <- SCTransform(combined)
```

## 生物学意义
spatial-CITE-seq与scCITE-seq的高度相关性（R=0.78）验证了空间蛋白质组数据的可靠性。整合UMAP分析显示两种方法在2D空间中共享高度一致的蛋白质表达模式，即使是低频细胞群体也能被准确捕获。这证明了spatial-CITE-seq作为高plex蛋白质空间映射工具的有效性。

## 涉及 Figures
- **Extended Data Fig. 4a** — 多重免疫荧光成像与spatial-CITE-seq的比较
- **Extended Data Fig. 4b** — 伪批量数据的Pearson相关性（R=0.78）
- **Extended Data Fig. 4c** — scCITE-seq和spatial-CITE-seq整合UMAP
