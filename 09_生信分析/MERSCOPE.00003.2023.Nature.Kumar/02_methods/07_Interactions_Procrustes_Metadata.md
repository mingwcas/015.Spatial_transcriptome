# Method: 细胞互作、左右乳房Procrustes与临床元数据统计

## 原文（Methods）
> In contralateral samples, we calculated Bray–Curtis dissimilarity ... using the vegdist function from the vegan package (v.2.5-6) ... Procrustes analysis using the protest function ... permutation test with 9,999 permutations.
> Wilcoxon rank-sum tests were used ... Fisher’s exact tests ... The P values from the two-tailed tests are reported ...
> We used CellPhoneDB v3 ... downsampled ... 23,584 cells ... threshold of 0.1 ... top 50 interactions ... P<0.05 and mean>0.5.

## 解读
### 意义
检验左右乳房组成一致性、临床变量关联及配体–受体通讯。
### 输入
细胞类型计数矩阵、临床元数据、表达矩阵和细胞状态标签。
### 输出
Bray–Curtis/MDS/Procrustes相关、临床比较P值、CellPhoneDB互作列表。
### 核心步骤
1. vegan::vegdist计算Bray–Curtis，cmdscale做MDS。
2. vegan::protest执行Procrustes，9,999次置换，Pearson评估前两轴。
3. CellPhoneDB下采样每类型≥2,000细胞、每状态≥100；threshold 0.1。
4. 排除integrin并按五类通讯分组，筛选top50（P<0.05且mean>0.5）。
5. Wilcoxon比较连续临床变量；Fisher检验每状态≥20细胞患者计数。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| Procrustes permutations | 9,999 | 显著性检验 |
| CellPhoneDB threshold | 0.1 | >10%细胞表达 |
| CellPhoneDB筛选 | P<0.05；mean>0.5 | 强互作 |
| 分组 | 5类 | epithelium、immune、stroma等 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| Bray–Curtis | 组成丰度差异度量 |
| Procrustes | 对齐两组多维构型 |
| CellPhoneDB | 配体–受体统计框架 |

## 复现
- vegan v2.5-6；CellPhoneDB v3（https://github.com/ventolab/CellPhoneDB）。
- 示例：`protest(cmdscale(vegdist(counts, method="bray")), permutations=9999)`。

## 生物学意义
区分技术/采样差异与真实生态差异，提出细胞通讯假说；配体–受体共表达不等于功能互作。

## 涉及 Figures
- **Fig. 1**；Fig. 4；Extended Data Fig. 1、2、7、12。
