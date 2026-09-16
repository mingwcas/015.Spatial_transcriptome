# Method: Visium 与 Xenium 的 STalign 空间对齐比较

## 原文（Methods）
> To compare spatial gene expression patterns from Visium and Xenium technologies, we first mapped all the data to the same coordinate space. We used STalign (v1.0.1), a computational tool that utilizes affine transformations along with diffeomorphic metric mapping to align target and source datasets (Clifton et al., 2023). The initial alignment involved only affine transformations and eight manually determined landmarks to align the Visium histology image (source) to the Xenium histology image (target).
> Next, we used STalign to map the Xenium transcripts (source) onto their corresponding Xenium histology image (target) using both affine and diffeomorphic metric mapping. The transcripts were rasterized at 30 μm resolution, with an initial affine transformation guided by four manually defined landmarks. Diffeomorphic metric mapping was then performed with the following parameters: a = 2500, epV = 1, niter = 2000, sigmaA = 0.11, sigmaB = 0.10, sigmaM = 0.15, sigmaP = 50, muA = [1, 1, 1], muB = [0, 0, 0], with all other settings left at their defaults. We extracted the overlapping regions between the two datasets (Appendix 1—figure 3A), which reduced the total spots in the Visium dataset to 3958. Finally, we aggregated the Xenium gene expression data to ~55 μm × 55 μm patches that correspond to the spatial locations of the Visium spots, resulting in matched-resolution spatial gene expression for both technologies (Appendix 1—figure 3B).

## 解读

### 意义
把 Visium（55 μm spot，全转录组）与 Xenium（亚细胞分辨率，313 基因）两套不同平台、不同坐标系的数据映射到同一坐标空间并聚合到同一分辨率，从而能够逐基因、逐位置地定量比较两种平台的一致性，并检验 Xenium 信号是否被脱靶基因"污染"。

### 输入
- Visium CytAssist 数据集（同一乳腺癌组织块，Janesick et al.）：4992 spots，含 x–y 坐标，18,085 genes/spot
- Xenium 数据集（同一组织块）：转录本级坐标 + Xenium H&E 组织学图像
- 手工标注的 landmark 点（Visium↔Xenium 组织学图像 8 个；Xenium 转录本↔图像 4 个）

### 输出
- 统一坐标系下的 Visium spot 位置与 Xenium 转录本位置
- 重叠区域（overlap region）掩膜：Visium 保留 **3958 spots**
- Xenium 聚合为 ~55 μm × 55 μm patch 的匹配分辨率表达矩阵
- 逐基因比较指标：RMSE（相对 y = x）与 Pearson r

### 核心步骤
1. 用 STalign 以**仅仿射变换** + **8 个手工 landmark**，将 Visium 组织学图像（source）对齐到 Xenium 组织学图像（target）
2. 将学到的变换应用于 Visium spots 坐标，使其在两张图像上位置一致
3. 用 STalign 将 Xenium 转录本（source）映射到 Xenium 组织学图像（target），采用仿射 + 微分同胚度量映射（diffeomorphic metric mapping）
4. 转录本先以 **30 μm** 分辨率栅格化（rasterize），初始仿射由 4 个手工 landmark 引导
5. 用给定参数执行微分同胚映射（见下表）
6. 提取两数据集重叠区域，Visium spots 由 4992 降至 3958
7. 将 Xenium 表达聚合到与 Visium spot 位置对应的 ~55 μm × 55 μm patch
8. 对每个共享基因构建跨空间位置的 log-normalized 表达向量，计算 RMSE（相对 y = x）与 Pearson r
9. 检验脱靶假设：把 Xenium 靶基因与"Visium 中该基因 + 其预测脱靶基因"的合并表达比较（合并 raw counts → CPM → log(x+1)）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| STalign 版本 | v1.0.1 | 空间对齐工具版本 |
| 图像配准 landmark 数 | 8（手工） | Visium 图像 → Xenium 图像 |
| 转录本栅格化分辨率 | 30 μm | Xenium 转录本转图像的分辨率 |
| 转录本配准 landmark 数 | 4（手工） | Xenium 转录本 → Xenium 图像，初始仿射 |
| a | 2500 | 微分同胚映射的核带宽参数 |
| epV | 1 | 速度场更新相关参数 |
| niter | 2000 | 迭代次数 |
| sigmaA | 0.11 | 仿射变换正则化 |
| sigmaB | 0.10 | 平移/形变正则化 |
| sigmaM | 0.15 | 度量/图像匹配正则化 |
| sigmaP | 50 | 映射/prior 正则化 |
| muA | [1, 1, 1] | 仿射先验均值 |
| muB | [0, 0, 0] | 平移先验均值 |
| Visium 原始 spots | 4992 | 含 x–y 坐标 |
| Visium 重叠后 spots | 3958 | 与 Xenium 重叠区域内 |
| Xenium 聚合 patch 大小 | ~55 μm × 55 μm | 匹配 Visium spot 尺寸 |
| Visium 基因数 | 18,085 / spot | Xenium 313 基因中 307 个与之共享 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| STalign | 基于仿射变换 + 微分同胚度量映射（LDDMM）的空间转录组对齐工具 |
| Landmark | 手工标注的对应点，用于引导初始仿射变换 |
| Affine transformation | 仿射变换（平移/旋转/缩放/错切） |
| Diffeomorphic metric mapping | 微分同胚映射，可做非线性、拓扑保持的形变配准 |
| Rasterization | 栅格化，将转录本点转为固定像素分辨率的图像 |
| Spot / Patch | Visium 捕获点（55 μm）/ Xenium 聚合出的同尺寸方块 |
| RMSE (relative to y = x) | 相对 y=x 线的均方根误差，衡量两平台数值一致性与偏差 |
| Pearson r | 逐基因跨位置表达向量的皮尔逊相关系数 |
| CPM | Counts per million，测序深度归一化 |

## 复现
- STalign（v1.0.1）：https://github.com/JEFworks-Lab/STalign
- 数据下载：https://www.10xgenomics.com/products/xenium-in-situ/preview-dataset-human-breast
- 代码片段（关键调用）：
```r
# 1) 组织学图像仿射配准（8 landmarks）
L = STalign.Landmarks(visium_landmarks, xenium_landmarks)
out = STalign.STalign(image_vis, image_xen, XJ=L, YJ=L, T=STalign.affine(...))
# 2) 转录本 → 图像：仿射 + 微分同胚（30 μm 栅格，4 landmarks）
out = STalign.STalign(raster_xen, image_xen, XJ=L4, YJ=L4,
        a=2500, epV=1, niter=2000, sigmaA=0.11, sigmaB=0.10,
        sigmaM=0.15, sigmaP=50, muA=c(1,1,1), muB=c(0,0,0))
```

## 生物学意义
同一组织块、两套平台、逐基因比较，是验证"Xenium 测到的到底是不是目标基因"的最直接策略。对齐后误差与相关性显示：多数基因两平台一致（Xenium 可靠），但对存在脱靶的基因（如 ACTG2、TUBB2B），Xenium 与 Visium 单基因相关性极低（ACTG2 r = 0.088），而把 Visium 中靶基因 + 预测脱靶基因的计数合并后相关性显著提升——这是"脱靶结合污染真实信号"的空间层面关键证据。局限：微分同胚配准依赖手工 landmark 与参数选择，组织切片本身存在形变与组织学差异；聚合到 55 μm 会损失 Xenium 的亚细胞分辨率；Visium 基因覆盖不全（313 基因中 6 个缺失：AKR1C1、ANGPT2、BTNL9、CD8B、POLR2J3、TPSAB1）限制了可比较范围。

## 涉及 Figures
- **Fig. 2** — Visium 与 Xenium 逐基因比较（RMSE 与 r），脱靶基因一致性差
- **Fig. 3** — 合并靶基因 + 脱靶基因后一致性提升（ACTG2 等）
- **Appendix 1—figure 3A** — 两数据集重叠区域
- **Appendix 1—figure 3B** — Xenium 聚合为 55 μm patch 的匹配分辨率表达
