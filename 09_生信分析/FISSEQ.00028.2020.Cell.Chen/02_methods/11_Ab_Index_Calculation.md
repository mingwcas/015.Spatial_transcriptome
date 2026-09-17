# Method: Aβ Index Calculation and Amyloid Plaque Niche Analysis

## 原文（Methods）
> We used the standard deviation of Aβ fluorescence intensity of pixels in a TD as the Aβ index. This differentiates mild Aβ from intense Aβ accumulation. We grouped the cells in 5 concentric rings around the amyloid plaques. Ring 1, cells within 10 μm of Aβ-positive areas compared with tissue far from plaques (ring 5, the most distant ring is 195 pixels or 54.6 μm away from ring 1). The ROI of ring 1 (plaque cellular niche) is based on the area mask with boundary expansion by 10 μm. We compute 5 co-centroid circles (donuts) from the ROI of ring 1 in the plaque cellular niche to the ROI of ring 5 far from plaque with 18.2 μm extension per ring without overlap between plaques. To test if a gene of interest is significantly enriched in ring 1, we used two-sided binomial test to compare the fraction of puncta of the corresponding gene in ring 1 relative to the total number of puncta of the same gene in all rings (q) against the expected proportion (a), which is the proportion of the area of ring 1 to the area of all rings.

## 解读

### 意义
Aβ指数计算和斑块微环境分析是将基因表达变化与淀粉样病理关联的核心方法，通过量化每个TD的Aβ负荷和分析斑块周围的基因表达梯度来研究Aβ对周围细胞的影响。

### 输入
- 6E10免疫荧光图像
- ISS/RNAscope的puncta空间坐标
- 斑块二值mask

### 输出
- 每个TD的Aβ指数（像素强度标准差）
- 5个同心环的基因表达量化
- 每个基因在ring 1的富集L2OR和p值

### 核心步骤
1. Aβ指数计算：每个TD内6E10像素强度的标准差
2. 斑块mask生成：Triangle阈值法（ImageJ）二值化6E10信号
3. Ring 1定义：斑块mask边界扩展10 μm
4. 5个同心环计算：从ring 1到ring 5，每环扩展18.2 μm
5. 二项检验：测试基因在ring 1的富集
   - q：基因在ring 1的puncta比例
   - a：ring 1面积占所有环面积的预期比例
   - L2OR = log2(q(1-q) / a(1-a))
6. Bonferroni校正多重比较

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Aβ指数 | 像素强度标准差 | 最佳Aβ负荷指标 |
| Ring 1扩展 | 10 μm | 斑块边界扩展 |
| 环间距 | 18.2 μm (65 pixels) | 相邻环之间的距离 |
| Ring 5最远距离 | 195 pixels = 54.6 μm | 从ring 1到ring 5 |
| 阈值方法 | Triangle (ImageJ) | 斑块二值化方法 |
| 统计检验 | 两侧二项检验 | 富集检验 |
| 多重校正 | Bonferroni | 保守的多重比较校正 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Aβ index | Aβ指数，TD内6E10像素强度的标准差 |
| Plaque cellular niche | 斑块细胞微环境，ring 1区域 |
| Concentric rings | 同心环，围绕斑块的5个等距分析区域 |
| L2OR (Log2 Odds Ratio) | 以2为底的对数优势比 |
| Binomial test | 二项检验，比较观察比例与预期比例 |
| Triangle threshold | Triangle阈值法，图像二值化方法 |

## 复现
- 工具/代码/URL
  - ImageJ Triangle threshold
  - 自定义分析脚本
- 代码片段
```R
# Aβ指数计算
ab_index <- sd(pixel_intensity_in_TD)

# L2OR计算
L2OR <- log2((q*(1-q)) / (a*(1-a)))
# q: fraction of puncta in ring 1
# a: expected proportion (area ratio)
```

## 生物学意义
Aβ指数的计算方法（像素强度标准差）通过专家评估被证明是最能代表Aβ负荷的指标。同心环分析揭示了基因表达随距斑块距离的梯度变化，如51/54个PIGs在ring 1显著富集。这种方法使得研究者能够定量评估Aβ对周围微环境的分子影响。

## 涉及 Figures
- **Fig. 2B-C** — Aβ指数计算和区域分布
- **Fig. 4D-E** — ISS的5环分析
- **Fig. 6E-F** — OLIG的5环分析
- **Figure S4** — 补体成分的5环分析
- **Figure S5D-E** — OLIG的全切片5环分析
