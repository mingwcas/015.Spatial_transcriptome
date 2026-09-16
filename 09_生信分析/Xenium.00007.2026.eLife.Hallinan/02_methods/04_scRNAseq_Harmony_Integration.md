# Method: 单细胞 RNA-seq 比较（Harmony 整合）

## 原文（Methods）
> Both scRNA-seq and Xenium provide single-cell resolution data. To integrate these datasets, we first removed cells lacking detectable gene expression. We then normalized the combined gene expression data using CPM and applied a log transformation with a pseudocount of 1. Principal component analysis is then applied to the normalized data, and batch effects are corrected using Harmony (v1.2.3) on the top 30 PCs using default parameters except for theta, which was set to 8, to promote further mixing with clusters across technologies. Finally, UMAP is performed on the harmonized PCs, generating a shared 2D embedding across the two technologies, and the data is further facetted by technology for visualization (Appendix 1—figure 5).
> We first computed Leiden clusters on the harmonized PCs (resolution = 1.0) to identify transcriptionally similar groups of cells shared across both technologies. For each Leiden cluster, we calculated the mean expression of every gene present in both datasets. Clusters containing fewer than ten cells from either modality were excluded to ensure robust gene-level estimates.

## 解读

### 意义
把 scRNA-seq（全转录组、解离后测序）与 Xenium（原位、单细胞分辨率）整合到同一嵌入空间，用"跨技术共享的细胞簇"作为可比单元，从而绕开两平台细胞分割与定量方式的差异，定量检验 Xenium 的基因表达是否更接近目标基因本身、还是"目标基因 + 预测脱靶基因"的合并表达。

### 输入
- Chromium Next GEM 3′ scRNA-seq 数据集（同一乳腺癌组织块）：12,388 cells × 36,601 genes
- Xenium 单细胞级表达矩阵（313 基因，均存在于 scRNA-seq 中）
- 两数据集共同子集：313 个基因

### 输出
- Harmony 整合后的共享 UMAP 2D 嵌入（可按技术分面可视化）
- Leiden 簇（resolution = 1.0）及其跨技术细胞组成
- 每个簇的簇级平均表达向量（两平台各一套）
- 逐基因比较指标：RMSE（相对 y = x）与 Pearson r
- 脱靶检验结果："靶基因单独" vs "靶基因 + 预测脱靶聚合"的相关性对比

### 核心步骤
1. 下载同一组织块的 Chromium 3′ scRNA-seq 数据（12,388 cells，36,601 genes）
2. 将 scRNA-seq 与 Xenium 同时子集到共有的 313 个基因
3. 去除无可检测基因表达的细胞（空液滴/空细胞）
4. 对合并矩阵做 **CPM** 归一化，再做 **log(x + 1)**（伪计数 1）变换
5. 对归一化数据做 **PCA**
6. 用 **Harmony (v1.2.3)** 在前 30 个 PC 上校正批次效应；除 `theta = 8` 外其余为默认参数（theta 提高以促进跨技术混合）
7. 在 harmonized PCs 上做 **UMAP**，得到两技术共享的 2D 嵌入，并按技术分面可视化（Appendix 1—figure 5）
8. 在 harmonized PCs 上做 **Leiden 聚类（resolution = 1.0）**，识别跨技术共享的转录相似细胞群
9. 计算每个 Leiden 簇中每个基因的平均表达；剔除任一模态细胞数 < 10 的簇，保证基因级估计稳健
10. 对每个基因，用两平台的簇级平均表达向量计算 RMSE（相对 y = x）与 Pearson r
11. 脱靶检验：在 scRNA-seq 中把某基因与其所有预测脱靶基因的 **raw counts 相加** → 重新 CPM → log(x + 1)，再算 RMSE 与 r，比较"目标基因单独"与"目标基因 + 脱靶"哪个与 Xenium 更吻合

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 整合工具 | Harmony v1.2.3 | 批次效应校正 |
| 输入 PC 数 | top 30 PCs | 用于 Harmony 的主成分数 |
| Harmony theta | 8（默认以外唯一改动） | 簇多样性惩罚强度，值越大混合越强 |
| 归一化 | CPM + log(x + 1) | 深度归一化 + 对数变换（伪计数 1） |
| 降维可视化 | UMAP | 基于 harmonized PCs |
| 聚类 | Leiden，resolution = 1.0 | 在 harmonized PCs 上 |
| 簇过滤阈值 | 每种模态 ≥ 10 cells | 低于此值的簇被排除 |
| scRNA-seq 规模 | 12,388 cells × 36,601 genes | Chromium Next GEM 3′ |
| 分析基因集 | 313（两平台共有） | Xenium 全部基因均在 scRNA-seq 中 |
| 比较指标 | RMSE（相对 y = x）、Pearson r | 簇级平均表达向量 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Harmony | 基于迭代聚类与线性校正的批次效应整合算法 |
| theta | Harmony 的多样性惩罚参数，越大越鼓励跨批次混合 |
| PC（Principal Component） | 主成分，PCA 降维后的坐标轴 |
| Harmonized PCs | 经 Harmony 校正后的主成分坐标 |
| UMAP | 非线性降维，用于 2D 可视化 |
| Leiden | 基于模块度的图聚类算法，resolution 控制簇粒度 |
| CPM | Counts per million，按测序深度归一化 |
| log1p / log(x+1) | 对数变换，伪计数 1，稳定低表达方差 |
| Cluster-level mean expression | 簇内细胞平均表达，跨平台比较的可比单元 |
| RMSE (relative to y = x) | 相对 y=x 的均方根误差 |

## 复现
- Harmony：https://github.com/immunogenomics/harmony （CRAN: `harmony`）
- Seurat / Scanpy（PCA、UMAP、Leiden）：https://satijalab.org/seurat/ ，https://scanpy.readthedocs.io/
- 数据下载：https://www.10xgenomics.com/products/xenium-in-situ/preview-dataset-human-breast
- 代码片段（关键调用，R）：
```r
obj <- NormalizeData(obj)                      # CPM + log1p (pseudocount = 1)
obj <- FindVariableFeatures(obj); obj <- ScaleData(obj); obj <- RunPCA(obj, npcs = 30)
obj <- RunHarmony(obj, group.by.vars = "technology", theta = 8)   # v1.2.3
obj <- RunUMAP(obj, reduction = "harmony", dims = 1:30)
obj <- FindClusters(obj, reduction = "harmony", resolution = 1.0) # Leiden
# 簇级均值 + 指标
r  <- cor(xen_mean, scrna_mean); rmse <- sqrt(mean((xen_mean - scrna_mean)^2))
```

## 生物学意义
解离 scRNA-seq 与 Xenium 是两套完全不同的测量物理过程（酶解离 + 逆转录 vs 原位探针杂交 + 滚环扩增），若两者在共享细胞簇上的基因表达高度相关，说明 Xenium 的定量在生物学上可信。本文的关键发现是：对于部分基因（如 TUBB2B，Xenium vs scRNA-seq r = 0.015），目标基因单独几乎不相关，而把预测脱靶基因（TUBB2A）并入后相关性跃升至 r = 0.793；ACTG2 由 r = 0.653 提升到 r = 0.813（并入 ACTB、POTEM、POTEE、POTEF、POTEI、POTEJ、ACTA1）。局限：Harmony/UMAP 属于非线性流形学习，簇的对应关系不是严格的一一映射；单细胞级 Xenium 数据依赖细胞分割质量；簇级均值会丢失细胞类型内部异质性；少于 10 细胞的簇被排除可能失去稀有细胞类型。

## 涉及 Figures
- **Fig. 4** — scRNA-seq 与 Xenium 整合后的跨技术比较及脱靶基因贡献
- **Appendix 1—figure 5** — Harmony 整合共享嵌入（按技术分面）
- **Appendix 1—figure 4** — 簇级表达比较与离群基因
