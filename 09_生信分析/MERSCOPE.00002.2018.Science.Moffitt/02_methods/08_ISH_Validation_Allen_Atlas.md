# Method: 原位杂交验证与 Allen Brain Atlas 比较

## 原文（Methods）
> These clusters were each associated with different hormonal modulations, ranging from cluster i20:Gal/Moxd1, predicted to lie in the sexually dimorphic nucleus of the POA... to cluster e24:Gal/Rxfp1, expressing no sex steroid receptor (Fig. 2A).
> These data were validated with two-color in situ hybridization (fig. S7A).
> Predicted locations for the clusters on the basis of spatial expression patterns of their marker genes observed in the Allen Brain Atlas (35) and our own in situ hybridization data (fig. S7) suggest that excitatory clusters tended to be grouped on the tree by anatomical structures or nuclei (Fig. 1D).
> We validated, by use of two- or three-color in situ hybridization, all clusters that could be specifically defined by two marker genes and spatial location (Fig. 8C).

**来源**：正文 Results（PDF p.3、p.10–11）。原文将 Allen Brain Atlas（35）与本研究 ISH 作为 marker 空间定位的互补证据。

## 解读

### 意义
验证 scRNA-seq/MERFISH 推断的 marker 空间位置是否符合已知脑图谱，并用独立的 ISH 图像确认关键集群的基因共表达与核团定位。

### 输入
- scRNA-seq 集群 marker 基因与预测核团
- MERFISH 集群的 marker 表达与细胞坐标
- Allen Brain Atlas（文献 35）的原位表达图谱
- 新制备的双色/三色 ISH 图像
- 行为激活验证用 16 μm 厚组织切片

### 输出
- marker 基因的核团空间定位证据
- Gal、Th、Bdnf/Adcyap1 等集群的双色验证图（fig. S7）
- cFos 与集群 marker 的双色/三色共表达图（Fig. 8C）
- scRNA-seq 预测位置与 MERFISH 实测位置的定性匹配

### 核心步骤
1. 从 scRNA-seq 每个集群选取差异表达 marker，结合 Allen Brain Atlas 表达图谱预测核团
2. 在相邻组织切片上做双色或三色 ISH，检测两个 marker 的共定位
3. 用 marker 共表达 + 空间位置判断某集群能否被特异定义
4. 将 ISH 定位与 MERFISH 集群坐标及参考核团边界对照
5. 对 Gal、Th、Adcyap1/Bdnf 等已知功能 marker 做系统验证
6. 对行为激活集群在 16 μm 切片中检测 cFos 与 marker 共表达
7. 记录不确定性：图谱分辨率低、marker 空间模式有歧义时只做粗略预测

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| ISH 验证类型 | 2-color / 3-color | 检测 marker 共表达及 cFos |
| 行为验证切片厚度 | 16 μm | Fig. 8C 的 ISH 切片 |
| MERFISH 切片厚度 | 10 μm | 主空间测量切片 |
| Atlas 来源 | Allen Brain Atlas (Lein et al., 2007) | marker 空间表达参考 |
| 直接验证条件 | 2 marker + spatial location | 能唯一界定的行为集群才验证 |
| 典型 marker | Gal、Th、Sncg、Cplx3、Moxd1、Adcyap1、Bdnf | 集群与功能验证基因 |
| 预测局限 | 低分辨率、空间模式歧义 | scRNA-seq 位置只是粗略近似 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ISH | in situ hybridization，原位杂交 |
| Two-color / three-color ISH | 同一切片同时检测 2 / 3 个 RNA marker |
| Allen Brain Atlas | 小鼠脑基因表达空间参考图谱 |
| Spatial prediction | 由 marker 的已知表达模式推定集群所在核团 |
| Co-expression | 同一细胞同时出现两个或多个 marker 信号 |

## 复现
- Allen Brain Atlas：https://portal.brain-map.org/ 
- 数据/代码：https://github.com/ZhuangLab/MERFISH_analysis
- MERFISH 数据：Dryad **10.5061/dryad.8t8s248**

```python
# 概念性验证逻辑
atlas = load_allen_atlas(marker_genes)
predicted_nuclei = infer_nuclei(atlas, cluster_markers)
ish = quantify_colocalization("markerA", "markerB", thickness_um=16)
compare_spatial(predicted_nuclei, ish, merfish_cluster_coordinates)
```

## 生物学意义
ISH 与 Allen 图谱为单细胞聚类提供了独立空间证据：例如 Gal 的 7 个 scRNA-seq 集群、Th 的 6 个集群及 Adcyap1/Bdnf 的 9 个集群并非单一细胞类型，而可由不同 marker 组合与核团位置区分。该验证也帮助确认 E-3（Sncg+）是热敏神经元相关集群。局限：Allen 图谱和 ISH 的空间分辨率低于 MERFISH；marker 可能在多个核团表达，不能单独确定细胞身份；因此作者明确指出 scRNA-seq 预测位置只是粗略近似，且集群内异质性会使对应关系仅代表部分细胞。

## 涉及 Figures
- **Fig. 1C / 1D** — 结合 Allen 图谱与 ISH 的集群位置预测
- **Fig. 2A–C** — marker 集群细分；双色 ISH 验证见 fig. S7
- **Fig. 6** — Cyp19a1、Esr1、Oxtr、Gnrh1 集群的空间组织
- **Fig. 7F** — 热应激动物 cFos、Sncg、Adcyap1 的 ISH 图像
- **Fig. 8C** — 16 μm 切片中行为激活集群的 cFos + marker ISH 验证
- **fig. S7** — Gal、Th 及其他 marker 的双色原位杂交
