# Method: ISS Segmentation-Independent Cell Type Assignment

## 原文（Methods）
> We developed a segmentation-independent method to assign a candidate cell type to individual punctum by its proximal markers. Calculation performed directly on all puncta from a full section instead of puncta counts per cell, increases statistical power, and proved to be much more robust. The first step is to transform the distances between the investigated punctum (dp) and each cell type marker punctum p into distance scores (Vp) using a logistic function. The next step is to calculate a cell type score (Sct) for each punctum by combining the distance scores per cell type. The last step is to assign a cell type to a punctum based on a cutoff (0.75). By choosing a cutoff > 0.5, we ensure only one cell type can be assigned to a punctum. By taking k = 2, we enforce that at least two marker genes need to be close to the punctum in question for a cell type to be assigned.

## 解读

### 意义
传统的细胞分割方法依赖于DAPI核染色确定细胞边界，在ISS稀疏数据中容易出错。本方法开发了一种无分割的细胞类型分配策略，直接基于单个RNA分子与周围细胞类型标记的距离关系来推断其细胞来源。

### 输入
- 每个荧光斑点（punctum）的空间坐标
- 细胞类型标记基因的puncta坐标
  - 小胶质细胞：Itgam, Cx3cr1, Csf1r
  - 星形胶质细胞：Slc1a3, Gfap, Clu
  - 神经元：Syp
  - 少突胶质细胞：Plp1

### 输出
- 每个punctum的细胞类型分配（神经元/小胶质/星形胶质/少突胶质/未分配）
- 细胞类型得分（Sct）
- Fisher精确检验的富集结果

### 核心步骤
1. 计算距离分数（Vp）：使用logistic函数将距离转换为0-1分数
   - Vp = 1 / (1 + e^(s*(dp-r)))
   - dp：到标记punctum的距离
   - r：半径参数（小鼠15像素=4.875μm，人30像素=9.75μm）
   - s：曲线陡度（s=0.9）
2. 计算细胞类型得分（Sct）：
   - Sct = ΣVp / max(k=2, ΣVp)
   - 要求至少2个标记基因在附近
3. 基于阈值（0.75）分配细胞类型
4. Fisher精确检验评估基因在各细胞类型的富集

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 半径r（小鼠） | 15 pixels = 4.875 μm | 调查半径 |
| 半径r（人） | 30 pixels = 9.75 μm | 调查半径 |
| 陡度s | 0.9 | logistic曲线陡度 |
| 分配阈值 | 0.75 | 细胞类型分配cutoff |
| 最小标记数k | 2 | 至少需要2个标记基因 |
| 最大距离 | 307 pixels ≈ 100 μm | 超过此距离不计入 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Segmentation-independent | 无分割方法，不依赖细胞边界识别 |
| Logistic function | logistic函数，将距离转换为概率分数 |
| Distance score (Vp) | 距离分数，0-1之间的权重 |
| Cell type score (Sct) | 细胞类型得分，综合多个标记的信号 |
| Fisher's exact test | Fisher精确检验，评估富集显著性 |
| FDR-BH | Benjamini-Hochberg假发现率校正 |

## 复现
- 工具/代码/URL
  - 自定义方法（论文补充材料详细描述）
  - Figure S7提供参数敏感性分析
- 代码片段
```python
# 距离分数计算
def distance_score(dp, r=15, s=0.9):
    return 1 / (1 + np.exp(s * (dp - r)))

# 细胞类型得分
def cell_type_score(punctum, markers, k=2):
    scores = {}
    for ct, marker_puncta in markers.items():
        ct_score = sum(distance_score(dist(punctum, m)) for m in marker_puncta)
        total = sum(distance_score(dist(punctum, m)) for m in all_markers)
        scores[ct] = ct_score / max(k, total)
    return scores
```

## 生物学意义
该方法的创新在于避免了传统细胞分割的局限性，直接利用分子空间邻近关系进行细胞类型推断。参数敏感性分析（Figure S7）证明了方法的稳健性。该方法成功地将PIG响应主要归因于小胶质细胞和星形胶质细胞，少突胶质细胞也参与了部分PIGs的表达。

## 涉及 Figures
- **Fig. 4F-H** — PIGs的细胞类型分配
- **Fig. 7D-E** — 人脑PIGs和OLIGs的细胞类型分配
- **Figure S7** — 方法参数敏感性分析
