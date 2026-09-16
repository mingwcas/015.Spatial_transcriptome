# Method: MERFISH 成像、三维切片与细胞分割（60 层等距切片，12 层成像）

## 原文（Methods）
> We sectioned the preoptic region into 60 evenly spaced slices along the anterior-posterior axis and performed three-dimensional MERFISH imaging on every fifth slice (29). Individual RNA molecules were clearly detected and identified (fig. S9), and individual cells were segmented based on 4′,6-diamidino-2-phenylindole (DAPI) and total mRNA staining (fig. S10) (29). In total, we profiled >400,000 cells from three to four replicates in naïve male and female animals, as well as >500,000 additional cells from three to five replicates of animals subjected to behavioral stimuli (29).
> Tissue fixation and sectioning as well as MERFISH probe construction, staining, and imaging were performed by using established protocols (26). ... Individual cells were segmented with a seeded watershed algorithm by using DAPI and total mRNA costains (29).

**来源**：正文 Results "MERFISH measurements of the preoptic region"（PDF p.6）与 Methods summary（PDF p.12）。

## 解读

### 意义
在保持组织完整的前提下，把"基因表达"变成"带坐标的单分子点云"，并通过分割把点云归到具体细胞体，使空间位置成为可分析变量。

### 输入
- 固定并切片的小鼠视前区组织（60 层等距切片）
- 155 基因探针组（135 组合 + 20 顺序）
- DAPI 与总 polyA mRNA 共染图像

### 输出
- 单分子级 RNA 定位点云（可解码到具体基因）
- 细胞体（soma）分割边界（seeded watershed）
- 细胞 × 基因矩阵 + 三维空间坐标
- naïve 动物 >400,000 细胞；行为刺激动物额外 >500,000 细胞

### 核心步骤
1. 组织固定、包埋，沿前后轴切成 60 层等距切片
2. 每隔 5 片取 1 片做三维 MERFISH 成像（共 12 片）
3. 135 基因组合 smFISH 多轮成像 → 解码 RNA 分子（纠错条形码）
4. 组合轮次后再做顺序多色 FISH，补测 20 个基因
5. DAPI + 总 mRNA 共染，用 seeded watershed 分割细胞体边界
6. 把 RNA 分子分配到细胞，生成细胞 × 基因 × 坐标矩阵

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片总数 | 60 evenly spaced slices | 沿前后轴等距切层 |
| 成像切片 | every 5th → 12 slices | 实际做 MERFISH 的层数 |
| 切片厚度 | 10 μm | MERFISH 成像切片厚度 |
| 成像区域 | 1.8 × 1.8 × 0.6 mm | Bregma +0.26 to –0.34 |
| 分割算法 | seeded watershed | 基于种子点的分水岭分割 |
| 分割依据 | DAPI + total mRNA costain | 细胞核 + 总 RNA 共染 |
| naïve 细胞数 | >400,000（3–4 replicates） | 未受行为刺激动物 |
| 行为刺激细胞数 | >500,000（3–5 replicates） | 行为刺激动物 |
| 灵敏度 | 6–8× transcript copies/cell | 相对 scRNA-seq 的检出拷贝数倍数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| MERFISH | 多重纠错荧光原位杂交，单分子级 RNA 成像 |
| 3D MERFISH | 在组织厚度方向同时成像，获得三维点云 |
| DAPI | 4′,6-diamidino-2-phenylindole，细胞核染料 |
| total mRNA costain | 总 polyA 染料共染，用于确定细胞质边界 |
| seeded watershed | 以核为种子、按强度梯度扩展的分水岭分割 |
| FOV | field of view，单次成像视野 |
| soma boundary | 细胞体（胞体）边界，非完整细胞含突起边界 |

## 复现
- 原始数据：Dryad **10.5061/dryad.8t8s248**
- 分析软件：https://github.com/ZhuangLab/MERFISH_analysis
- 实验协议：(26) Moffitt et al., PNAS 113, 14456–14461 (2016)

```python
# 概念性流程（MERFISH_analysis 流水线）
# 1) 解码：多轮图像 → 单分子定位与 barcode 纠错
# 2) 分割：DAPI 种子 + total mRNA 边界
# 3) 分配：RNA 分子 → 细胞
import merfish
rna   = merfish.decode(fov_images, codebook)      # 单分子点云
cells = merfish.segment(dapi, polya, method="seeded_watershed")
adata = merfish.assign(rna, cells)                # 细胞 × 基因 × 坐标
```

## 生物学意义
MERFISH 原位测量保留了 scRNA-seq 丢失的空间语境，并显著提升低表达基因（尤其是神经调质受体）的检出能力（每细胞拷贝数高 6–8 倍）。局限：分割边界只代表**细胞体**而非含突起的完整细胞，一部分 RNA 落在边界之外，只能是"神经/胶质突起中 RNA 的候选"；12/60 的抽样成像意味着前后轴信息是离散采样而非连续覆盖。

## 涉及 Figures
- **Fig. 3A** — MERFISH 成像与分割流程示意、单分子点云与分割边界
- **Fig. 3B / 3C** — ~500,000 个 naïve 细胞的基因表达热图与 tSNE
- **fig. S9** — 135 基因的原始与解码图像
- **fig. S10** — 总 mRNA / 核共染与分割边界
- **fig. S11 / S12** — 重复性、与 bulk RNA-seq 相关性、假检出率与灵敏度
