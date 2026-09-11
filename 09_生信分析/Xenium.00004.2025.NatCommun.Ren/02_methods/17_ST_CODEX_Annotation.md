# Method: Annotation of ST and CODEX Data

## 原文（Methods）
> The latest versions of SELINA (v.0.1), Celltypist (v.1.6.3), Spoint (v.1.1.7), Tangram (v.1.0.4), and TACCO (v.0.4.0.post1) were used to transfer the annotations from scRNA-seq data to the filtered ST data. We utilized two metrics to evaluate the annotation consistency across different tools: (1) the proportion of cells that were consistently annotated as the same cell type by different tools; (2) the entropy of cell numbers detected by different tools for each cell type, which was calculated with the following formula:
> pi = Ni / ΣNn i=1 Ni
> H = -Σn i=1 pi log2(pi)
> where the number of cells detected by the i-th tool was denoted with Ni and its ratio over all tools was denoted as pi. Each cell was assigned a final cell type based on majority voting across annotation tools. For cells with inconsistent annotations across five tools, the label from the method showing the highest overall concordance with other tools was used to resolve conflicts.
> For the CODEX data, we first performed nuclear segmentation using StarDist (v.0.5.0) in QuPath (v.0.5.1). Cell boundaries were defined by expanding the nuclear boundaries by 5 μm. CODEX data exhibited prominent non-specific binding signals in tumor regions and background signals across entire sections, which could bias cell annotation if based solely on the average signal intensity. To address this challenge, we manually labeled hundreds of positive cells for each marker and trained a k-nearest neighbor (KNN) classiﬁer in QuPath. For membrane markers, cells with fluorescent signals surrounding the nuclei were defined as truly positive cells. For transcription factors, cells with fluorescent signals confined exclusively to the nuclei were defined as truly positive cells. Cells lacking any marker signal were categorized as negative cases. We trained the classifier using various signal statistics, including mean, median, minimum, maximum, and standard deviation for signals in the nucleus, cytoplasm, membrane, and the entire cell. This classifier was then applied to annotate the remaining cells across the entire section.

## 解读

### 意义
通过五种注释工具（SELINA, Celltypist, Spoint, Tangram, TACCO）将scRNA-seq注释转移到ST数据，并使用多数投票和熵评分评估注释一致性。CODEX数据使用StarDist分割和KNN分类器进行细胞类型注释，作为跨模态比较的ground truth。

### 输入
- scRNA-seq注释标签
- 各ST平台过滤后的表达矩阵
- CODEX蛋白表达数据

### 输出
- 各ST平台细胞类型注释
- 注释一致性评分（比例、熵）
- CODEX细胞类型注释

### 核心步骤
1. 使用5种工具将scRNA-seq注释转移到ST数据：
   - SELINA v.0.1, Celltypist v.1.6.3, Spoint v.1.1.7, Tangram v.1.0.4, TACCO v.0.4.0.post1
2. 评估注释一致性：
   - 指标1：被所有工具一致注释为同一细胞类型的细胞比例
   - 指标2：各工具检测细胞数的熵（H）
3. 多数投票确定最终细胞类型
4. 冲突解决：使用与其他工具一致性最高的工具标签
5. CODEX注释：
   - StarDist (v.0.5.0)核分割（QuPath v.0.5.1）
   - 核边界扩展5 μm定义细胞边界
   - 手动标注每种marker的数百个阳性细胞
   - 训练KNN分类器（使用核、质、膜、全细胞各信号统计量）
   - 应用分类器注释所有细胞

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 注释工具 | SELINA, Celltypist, Spoint, Tangram, TACCO | 5种工具 |
| CODEX分割 | StarDist v.0.5.0 + QuPath v.0.5.1 |  |
| 核扩展 | 5 μm | 细胞边界定义 |
| CODEX分类器 | KNN | 手动标注训练 |
| 质膜marker | 核周荧光信号 | 阳性判定 |
| 转录因子 | 仅核内荧光 | 阳性判定 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 注释转移 | 从reference数据（scRNA-seq）将标签迁移到query数据（ST） |
| 熵 (Entropy) | 衡量分布均匀性的指标，高熵=各工具检测差异大 |
| KNN分类器 | k-最近邻分类器 |
| majority voting | 多数投票，最终注释 |

## 复现
- SELINA: v.0.1
- Celltypist: v.1.6.3
- Spoint: v.1.1.7
- Tangram: v.1.0.4
- TACCO: v.0.4.0.post1
- StarDist: v.0.5.0
- QuPath: v.0.5.1

## 生物学意义
Xenium 5K在五种工具中表现出最高的注释一致性，表明其细胞类型识别稳健性最强。研究还发现iST平台比sST平台具有更高的注释熵，提示前者在推断细胞类型组成方面具有更高的一致性。

## 涉及 Figures
- **Fig. 5c** — 五种工具注释一致性比较
- **Supplementary Fig. 11a, b** — 注释细胞类型数和熵评分
