# Method: Imputation, embedding and clustering of Spatial-ATAC-Hi-C data

## 原文（Methods）
> ScHiCluster94 (v.1.3.5) (https://github.com/zhoujt1994/scHiCluster) was used to perform contact matrix imputation for individual spatial pixels at three different resolutions (100 kb (for compartment analysis), 25 kb (for visualization) and 10 kb). In brief, contacts from individual pixels were first filtered to exclude contacts overlapping the ENCODE blacklist regions. ScHiCluster then performed matrix imputation using linear convolution and random walk with restart, generating imputed sparse single-pixel contact matrices for each chromosome. To optimize storage efficiency, we output the imputed contact matrices for the whole chromosome only at 100 kb, for the 10.05-Mb window at 25 kb, and for the 5.05-Mb window at 10 kb for each pixel. The GAS and GAD scores were used for spatial data embedding and clustering. To compute the GAS, we first applied the make_gene_matrix function from SnapATAC295 (v.2.6.4), which counts Tn5 insertions within the promoter region of each gene (2 kb upstream of the TSS) and gene body region to generate a raw count matrix. The resulting raw count matrix was used as the gene activity score matrix and imported into Seurat93 (v.5.1.0) for embedding and clustering analysis. Similarly, to compute the GAD scores, we first converted the read pairs into a BED-like tabular file, with each line representing a unique fragment that was one end of the Hi-C pairs. Then, we applied the same analysis pipeline for the Hi-C data and generated the raw count matrix as the GAD score matrix. The GAD score matrix was further used for embedding and clustering analysis. For clustering of spatial data, we first identified highly variable features from the GAS matrix/GAD score matrix using the FindVariableFeatures function. Linear transformation (scaling) was then applied to these variable features and principal-component analysis (PCA) was performed on the scaled data. We then constructed a k-nearest neighbor (kNN) graph using the FindNeighbors function and applied the Louvain algorithm via the FindClusters function to iteratively group cells together. For visualization, pixels with fewer than 2,000 fragments (empirically threshold) were assigned the majority cluster label or mean GAS/GAD score of their six nearest neighboring pixels based on Euclidean distance.

## 解读

### 意义
对Spatial-ATAC-Hi-C数据进行插补、降维和聚类，识别空间像素中的细胞类型和基因调控模式

### 输入
- 质量控制后的pairs文件（Hi-C数据）
- fragment.tsv文件（ATAC-seq数据）
- 参考基因组注释（基因位置，ENCODE黑名单区域）

### 输出
- 插补后的接触矩阵（三种分辨率）
- Gene Activity Score (GAS)矩阵
- Gene Activity Distance (GAD)矩阵
- 空间聚类结果和细胞类型注释
- UMAP/t-SNE可视化

### 核心步骤
1. **Hi-C数据插补**：
   - 使用ScHiCluster (v.1.3.5)进行接触矩阵插补
   - 三种分辨率：100 kb（区室分析），25 kb（可视化），10 kb（详细分析）
   - 过滤ENCODE黑名单区域的接触
   - 使用线性卷积和随机游走重启进行插补
   - 优化存储：100 kb全染色体，25 kb 10.05-Mb窗口，10 kb 5.05-Mb窗口

2. **Gene Activity Score (GAS)计算**：
   - 使用SnapATAC2 (v.2.6.4)的make_gene_matrix函数
   - 计算Tn5插入事件：启动子区域（TSS上游2 kb）和基因体区域
   - 生成原始计数矩阵作为GAS矩阵

3. **Gene Activity Distance (GAD)计算**：
   - 将Hi-C read pairs转换为BED-like表格文件
   - 每行代表Hi-C pairs的一个末端片段
   - 应用与ATAC-seq相同的分析流程生成GAD矩阵

4. **聚类分析**：
   - 使用Seurat (v.5.1.0)进行嵌入和聚类
   - FindVariableFeatures识别高变异特征
   - 线性变换（缩放）和PCA降维
   - FindNeighbors构建k近邻图
   - FindClusters应用Louvain算法聚类

5. **低质量像素处理**：
   - 片段数<2000的像素被标记为低质量
   - 分配多数聚类标签或最近6个邻居的平均GAS/GAD分数（基于欧氏距离）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| ScHiCluster版本 | v.1.3.5 | Hi-C数据插补工具 |
| 插补分辨率 | 100 kb, 25 kb, 10 kb | 三种不同分辨率的接触矩阵 |
| SnapATAC2版本 | v.2.6.4 | ATAC-seq分析工具 |
| Seurat版本 | v.5.1.0 | 单细胞数据分析框架 |
| GAS计算窗口 | 启动子区域(TSS上游2 kb) + 基因体 | Tn5插入计数区域 |
| 低质量阈值 | <2000 fragments | 片段数阈值 |
| 邻居数量 | 6个最近邻居 | 低质量像素插补的邻居数 |
| 聚类算法 | Louvain | 图聚类算法 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| GAS | Gene Activity Score，基因活性分数，基于ATAC-seq信号的基因表达估计 |
| GAD | Gene Activity Distance，基因活性距离，基于Hi-C数据的基因活性估计 |
| ScHiCluster | Hi-C数据插补和聚类工具，使用卷积和随机游走方法 |
| ENCODE黑名单 | ENCODE项目定义的基因组区域，通常具有异常高信号，应过滤 |
| Louvain算法 | 基于模块度优化的图聚类算法 |
| kNN图 | k近邻图，用于表示数据点之间的局部相似性 |

## 复现
- 工具/代码/URL
  - ScHiCluster: https://github.com/zhoujt1994/scHiCluster
  - SnapATAC2: https://github.com/scverse/SnapATAC2
  - Seurat: https://github.com/satijalab/seurat
  - ENCODE黑名单: https://github.com/Boyle-Lab/Blacklist
- 代码片段
  ```bash
  # Hi-C数据插补（ScHiCluster）
  # Python环境
  from scHiCluster import scHiCluster
  # 过滤ENCODE黑名单区域
  # 插补接触矩阵
  # 输出三种分辨率的矩阵
  
  # GAS计算（R/SnapATAC2）
  library(SnapATAC2)
  # 计算Tn5插入矩阵
  # 启动子区域和基因体区域
  
  # 聚类分析（R/Seurat）
  library(Seurat)
  # 创建Seurat对象
  # FindVariableFeatures
  # ScaleData
  # RunPCA
  # FindNeighbors
  # FindClusters (Louvain)
  # RunUMAP
  ```

## 生物学意义
插补和聚类分析揭示了Spatial-ATAC-Hi-C数据的生物学意义：

**Hi-C数据插补**：
- 弥补单像素Hi-C数据的稀疏性
- 提高3D基因组结构分析的准确性
- 多分辨率分析允许不同尺度的生物学发现

**GAS和GAD分数**：
- GAS：ATAC-seq信号估计基因活性，反映染色质可及性
- GAD：Hi-C数据估计基因活性，反映3D基因组结构
- 联合使用提供多层次的基因调控信息

**聚类分析**：
- 识别空间像素中的细胞类型
- 发现组织区域和结构
- 揭示细胞类型的空间分布模式

该方法的技术优势：
- 整合ATAC-seq和Hi-C信息，提供全面的基因调控视角
- 多分辨率分析适应不同的生物学问题
- 标准化流程便于比较不同样本

局限性：
- 插补可能引入假阳性信号
- 聚类结果受参数选择影响
- 计算资源需求较高
- 需要生物学知识解释聚类结果

## 涉及 Figures
- **Fig. 2** — 空间聚类和细胞类型识别
- **Fig. 3** — GAS和GAD分数分析
- **Extended Data Fig. 6** — 插补效果验证和聚类质量评估
- **Supplementary Fig. 2** — 多分辨率分析结果
