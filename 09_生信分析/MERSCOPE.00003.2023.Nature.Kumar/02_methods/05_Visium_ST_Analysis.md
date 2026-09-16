# Method: Visium空间转录组分析

## 原文（Methods）
> Sequencing reads from Visium ST (10x Genomics) experiments were first preprocessed with Space Ranger (v.1.2.0; 10x Genomics) and mapped to the GRCh38 reference genome. ... We filtered out spots with total counts of less than 100. The UMI counts were normalized using SCTransform. ... anchor-based integration ... Differentially expressed genes ... two-sided Wilcoxon rank-sum test. P values were adjusted by Bonferroni correction ... Pearson correlation analysis between these two data modalities.

## 解读
### 意义
在55 μm spot尺度解析组织区域，并与单细胞标记表达进行对应验证。
### 输入
Visium测序读段、组织图像和4个样本；GRCh38参考。
### 输出
spot count矩阵、整合聚类、区域marker和ST–scRNA Pearson相关。
### 核心步骤
1. Space Ranger v1.2.0比对并生成spot表达矩阵。
2. 去除总counts<100的spot，SCTransform归一化。
3. Seurat anchor integration整合4样本，PCA和FindClusters聚类。
4. FindAllMarkers/Wilcoxon识别簇marker并Bonferroni校正。
5. 选scRNA marker（pct.1>0.25、avg_logFC>0.25），计算两模态均值并Pearson相关。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| 最低spot counts | 100 | spot质控 |
| marker pct.1 | >0.25 | scRNA marker筛选 |
| marker avg_logFC | >0.25 | 效应阈值 |
| 多重校正 | Bonferroni，adjusted P<0.05 | DE显著性 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| Visium spot | 10x空间捕获点，约55 μm |
| SCTransform | 基于正则化负二项模型的归一化 |
| Pearson r | 两模态marker均值线性相关 |

## 复现
- Space Ranger v1.2.0；Seurat v3；GRCh38。
- 示例：`Spatial <- SCTransform(Spatial); FindClusters(Spatial)`。

## 生物学意义
用无偏空间转录组把细胞类型信号定位到导管、叶和脂肪/结缔区域，但spot混合细胞限制单细胞分辨率。

## 涉及 Figures
- **Fig. 2a–c、3o、5h–i**；Extended Data Fig. 3、6。
