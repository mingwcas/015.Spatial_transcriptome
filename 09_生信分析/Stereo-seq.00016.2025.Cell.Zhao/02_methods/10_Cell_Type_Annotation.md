# Method: Cell Type Annotation

## 原文（Methods）
> We employed scanpy in Python for cell annotation, beginning with preprocessing that involved discarding cells with less than 200 genes, followed by data normalization and logarithmic transformation. We used the Leiden algorithm for cell clustering and annotated these clusters using classical markers to identify cell types. For further refinement, we followed a similar process for each primary cell type, combining manual subdivision based on known marker genes and spatial distribution.

## 解读

### 意义
对分割后的细胞进行类型注释，识别组织中的不同细胞类型。

### 输入
- 单细胞基因表达矩阵（AnnData）
- 已知的标记基因列表

### 输出
- 每个细胞的类型注释
- 细胞类型特异性标记基因

### 核心步骤
1. 预处理：过滤<200基因的细胞
2. 数据标准化和对数转换
3. Leiden算法聚类
4. 使用经典标记基因注释细胞类型
5. 对主要类型进一步细分

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因过滤阈值 | <200 genes | 过滤低质量细胞 |
| 聚类算法 | Leiden | |
| 注释方法 | 标记基因 + 空间分布 | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Leiden算法 | 社区检测聚类算法 |
| Marker genes | 细胞类型特异性标记基因 |

## 复现
- Scanpy: https://scanpy.readthedocs.io/
- 版本：0.10.7

## 生物学意义
细胞类型注释是理解组织细胞组成的基础，对于研究细胞类型空间分布和相互作用至关重要。

## 涉及 Figures
- Fig. 2D, 2E (cell type annotation)
