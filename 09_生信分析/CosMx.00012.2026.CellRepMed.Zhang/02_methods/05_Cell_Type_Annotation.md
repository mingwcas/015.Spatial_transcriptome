# Method: Cell Type Annotation

## 原文（Methods）
> Putative marker genes for each cluster were identified using FindAllMarkers (only.pos = TRUE). Cell identities were assigned manually by cross-referencing these markers with canonical lineage-specific genes, the CellMarker 2.0 database, and annotations from previous studies on SCLC.

## 解读

### 意义
细胞类型注释是将无监督聚类结果转化为生物学意义的关键步骤，通过标志基因将每个细胞群映射到特定的细胞类型。

### 输入
- 每个聚类的差异表达基因（FindAllMarkers结果）
- 经典细胞类型标志基因
- CellMarker 2.0数据库
- 已发表的SCLC研究注释

### 输出
- 每个细胞的细胞类型注释
- 四大细胞compartment：上皮(Epithelial)、内皮(Endothelial)、成纤维细胞(Fibroblast)、免疫细胞(Immune)
- 7种broad cell type：B细胞、T细胞、浆细胞、巨噬细胞、内皮细胞、成纤维细胞、恶性细胞
- 详细免疫细胞亚型

### 核心步骤
1. 使用FindAllMarkers (only.pos=TRUE)识别每个聚类的标志基因
2. 手动交叉参考：
   - 经典谱系特异性基因（如EPCAM上皮、KRT18恶性、PTPRC免疫）
   - CellMarker 2.0数据库
   - 已发表SCLC研究
3. 分配细胞类型标签

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| FindAllMarkers参数 | only.pos = TRUE | 仅返回上调基因 |
| 数据库 | CellMarker 2.0 | 细胞类型标志物数据库 |
| 参考注释 | 已发表SCLC研究 | 领域特异性注释 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| EPCAM | 上皮细胞标志物 |
| VWF, CD34 | 内皮细胞标志物 |
| COL1A2, ACTA2 | 成纤维细胞标志物 |
| PTPRC (CD45) | 免疫细胞标志物 |
| CD68 | 巨噬细胞标志物 |
| JCHAIN | 浆细胞标志物 |
| CD19, MS4A1 | B细胞标志物 |
| CD2, CD3D, CD3E | T细胞标志物 |
| SFN, KRT8, KRT18, KRT19 | 恶性上皮细胞标志物 |

## 复现
- 工具/代码/URL：CellMarker 2.0: https://doi.org/10.1093/nar/gkac947
- 代码片段：
```r
# Cell type annotation
markers <- FindAllMarkers(pbmc, only.pos = TRUE)
# Manual annotation based on canonical markers
Idents(pbmc) <- "RNA_snn_res.0.8"
new_ids <- c("T cell", "B cell", "Macrophage", "Malignant", ...)
names(new_ids) <- levels(pbmc)
pbmc <- RenameIdents(pbmc, new_ids)
```

## 生物学意义
细胞类型注释建立了单细胞转录组数据与生物学意义的桥梁。本研究识别了四个主要细胞compartment和七种broad cell type，为后续分析肿瘤微环境异质性和空间相互作用奠定了基础。

## 涉及 Figures
- **Fig. 1B, 1C** — 细胞类型注释结果
- **Fig. 2A** — 恶性细胞亚群注释
- **Fig. 3A, 3B** — T细胞和B细胞亚型注释
