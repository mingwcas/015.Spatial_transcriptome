# Method: Cell-Type Separation and Batch Effect Assessment

## 原文（Methods）
> Biological conservation of cell types and batch effect strength were assessed using metrics proposed by Luecken et al., as implemented in the scib-metrics package and Calinski-Harabasz, Davies-Bouldin scores from scikit-learn. Higher scores indicate improved biological conservation or batch integration.
> Datasets were downsampled to a maximum of 100,000 cells to speed up calculations. Malignant cells were excluded before computing these metrics because they are often sample specific.

## 解读

### 意义
评估不同分割和校正方法对细胞类型分离效果和批次效应的影响，为方法选择提供定量依据。

### 输入
- 原始或校正后的单细胞表达矩阵
- 细胞类型注释标签
- 样本/面板来源信息

### 输出
- Calinski-Harabasz指数（越高越好）
- Davies-Bouldin指数（越低越好）
- iLISI评分（批次混合度，越高越好）
- Silhouette Batch评分

### 核心步骤
1. 合并所有样本数据
2. 下采样至≤100,000细胞
3. 排除恶性细胞（患者特异性）
4. 计算SCIB指标（iLISI、Silhouette Batch）
5. 计算聚类指标（Calinski-Harabasz、Davies-Bouldin）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| max_cells | 100,000 | 下采样细胞数上限 |
| exclude_malignant | TRUE | 排除恶性细胞 |
| n_neighbors (UMAP) | 50 | UMAP邻居数 |
| scib-metrics | 来自Luecken et al. | 批次效应评估工具包 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Calinski-Harabasz | 聚类间/内方差比，越高分离越好 |
| Davies-Bouldin | 聚类相似性，越低分离越好 |
| iLISI | 局部邻域批次混合度，越高越好 |
| Silhouette Batch | 全局批次分离度 |

## 复现
- 工具：scikit-learn, scib-metrics (https://github.com/YosefLab/scib-metrics)
- 代码：https://github.com/bdsc-tds/xenium_analysis_pipeline

## 生物学意义
这些指标综合评估了校正方法的效果：良好的细胞类型分离意味着生物学信号更清晰；保持低批次效应意味着数据可重复性强。恶性细胞被排除因为它们天然具有患者特异性。

## 涉及 Figures
- **Fig. 4b** — SCIB指标比较
- **ED Fig. 2** — 批次整合评分
