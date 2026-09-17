# Method: Trajectory Analysis with scVelo

## 原文（Methods）
> Trajectory analysis was performed using scVelo29. We first loaded intronic and exonic gene expression matrices, UMAP coordinates created in Seurat from the original clustering of the Slide-seqV2 data, cluster IDs, and spatial coordinates of each bead from Slide-seqV2 into a scanpy object using a custom Python environment. We next applied the LT method developed in scVelo to our Slide-seqV2 expression data...

## 解读

### 意义
scVelo通过RNA velocity分析，利用spliced/unspliced mRNA比例推断细胞发育轨迹，将时间维度引入空间数据。

### 输入
- Intronic and exonic gene expression matrices (Slide-seqV2 DGE)
- UMAP coordinates from Seurat clustering
- Cluster IDs
- Spatial coordinates of each bead

### 输出
- Latent time (LT) values per bead
- Velocity genes (179 genes with significant velocity loadings)
- Trajectory-associated genes

### 核心步骤
1. **Load data**: Create scanpy object with exonic+intronic counts
2. **Run scVelo**: Apply velocity model to estimate LT
3. **Project to space**: Plot LT values onto Slide-seqV2 spatial coordinates
4. **Identify velocity genes**: Genes with likelihood >0.1

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 软件版本 | scvelo 0.1.25 | GitHub版本 |
| Velocity likelihood cutoff | >0.1 | 选择velocity genes |
| 数据整合 | scanpy object | Python环境 |
| LT projection | 3D surface fitting | MATLAB |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RNA velocity | 通过spliced/unspliced mRNA比率预测细胞未来状态 |
| Latent time (LT) | scVelo推断的细胞成熟时间 |
| Spliced/unspliced ratio | 反映基因表达动态变化 |
| Velocity genes | 对 trajectory有显著贡献的基因 |

## 复现
- **URL**: https://github.com/theislab/scvelo (v0.1.25)
- **代码**: 
```python
import scvelo as scv
adata = scv.read('slide-seqV2_data.h5ad')
scv.tl.velocity(adata)
scv.tl.velocity_graph(adata)
scv.tl.latent_time(adata)
```

## 生物学意义
RNA velocity与空间转录组结合，使我们能够在发育中的大脑皮层重建从 ventricular zone到cortical plate的径向发育轨迹，为理解空间发育程序提供了新工具。

## 涉及 Figures
- **Fig. 3b** — LT projected onto spatial coordinates
- **Supplementary Fig. 7c** — Monocle3 trajectory comparison
- **Supplementary Fig. 8** — Overlap with scVelo/Monocle3 genes
