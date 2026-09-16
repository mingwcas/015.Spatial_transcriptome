# Method: CODEX空间蛋白组分割、聚类与区域比较

## 原文（Methods）
> StarDist trained on TissueNet dataset was used for cell segmentation. The average intensity of each protein was then calculated for individual cells using the segmentation masks and the protein images. ... Unsupervised clustering using Leiden algorithm was performed ... Tissue regions were manually annotated into lobules, ducts and connective tissue ... relative cell percentages and densities ... were compared.

## 解读
### 意义
将34抗体CODEX图像转换为单细胞蛋白表达和组织区域细胞组成。
### 输入
FFPE CODEX多轮荧光图像、34抗体panel、TissueNet训练StarDist模型。
### 输出
细胞/核/膜分割、蛋白强度、Leiden簇、人工细胞类型标签、区域密度。
### 核心步骤
1. StarDist分割细胞；核定位蛋白用核mask，膜蛋白用膜mask计算平均强度。
2. 所有细胞蛋白强度z-score；Leiden无监督聚类。
3. 按marker热图人工识别细胞类型；病理形态标注lobule/duct/connective。
4. 比较区域细胞比例与单位面积密度；免疫子集提高分辨率识别T/髓系亚群。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| 抗体数 | 34 | CODEX蛋白panel |
| 聚类 | Leiden | 单样本无监督聚类 |
| 强度标准化 | 跨细胞z-score | 消除量纲 |
| 成像面积 | 约1 cm² | CODEX空间覆盖 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| CODEX/PhenoCycler | 多轮寡核苷酸报告探针成像 |
| StarDist |星形多边形细胞分割模型 |
| Leiden | 图社区聚类算法 |

## 复现
- StarDist（TissueNet模型）、Leiden、PhenoCycler；原文未给完整脚本。
- 示例：`labels = stardist.predict_instances(image)`；对蛋白强度z-score后Leiden聚类。

## 生物学意义
提供与RNA空间结果正交的蛋白层验证；抗体panel和人工区域/标签可能带来主观性。

## 涉及 Figures
- **Fig. 2g–i、3n、4c–d/l/n、6h**；Extended Data Fig. 4、6、8、11。
