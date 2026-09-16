# Method: 图像分析、spot 定位与二进制词解码

## 原文（Methods）

> Fluorescent spots were identified and localized in each image using a multi-Gaussian-fitting algorithm (38) assuming a Gaussian with a uniform width of 167 nm. This algorithm was used to allow partially overlapping spots to be distinguished and individually fit. RNA spots were distinguished from background signal, i.e., signal arising from probes bound non-specifically, by setting the intensity threshold required to fit a spot with this software.
>
> Images of the same sample region in different rounds of hybridization were registered by rotating and translating the image to align the two fiducial beads within the same image that were most similar in location after a coarse initial alignment via image correlation. … The quality of this alignment was determined from the residual distance between five additional fiducial beads, and alignment error was typically ~20 nm.
>
> Fluorescence spots in different hybridization rounds were connected into a single string, corresponding to a potential RNA molecule, if the distance between spots was smaller than 1 pixel (167 nm). For each string of spots, the on-off sequence of fluorescent signals in all hybridization rounds were used to assign a binary word to the potential RNA molecule … Measured words were then decoded into RNA species using the 16-bit MHD4 code or the 14-bit MHD2 code discussed in the main text.
>
> To determine the copy number per cell, the number of each RNA species was counted in individual cells within each 40 μm by 40 μm imaging area. … In the 1001-gene experiments, the cell nucleus generally contained too much fluorescent signal to allow identification of individual RNA molecules. These bright regions were excluded from all subsequent analysis.

## 解读

### 意义
把 14–16 轮二维荧光图像变成"每个 RNA species 在每个细胞中的拷贝数"这一可定量、带误差指标的终产物，并同时输出每个分子的亚细胞坐标（供空间分布分析使用）。

### 输入
- 每轮 641 nm（RNA）与 561 nm（fiducial beads）通道图像，40 μm × 40 μm 区域
- codebook（16-bit MHD4 / 14-bit MHD2，Tables S1 / S3）
- 核图像（405 nm Hoechst）

### 输出
- 每个细胞的 spot 定位与所属 RNA species（Fig. 2B、5A 的彩色点图）
- 每细胞每基因的拷贝数矩阵（→ Fig. 2E、3A、5C）
- 质量指标：每轮 1→0 / 0→1 错误率、每 species calling rate、confidence ratio
- 用于空间分析的分子坐标（→ Fig. 4）

### 核心步骤
1. 用多高斯拟合算法在每张图中定位荧光 spot，固定高斯宽度 167 nm，允许部分重叠的 spot 被分别拟合。
2. 通过调整拟合所需的强度阈值区分真信号与背景（非特异结合探针）；140 基因实验以最小化 1→0 与 0→1 错误率之和为准逐轮调整，1001 基因实验以最大化"4 个'1'位词 / 3 或 5 个'1'位词"的比值为准。
3. 用更快的单高斯拟合算法在每帧中识别 fiducial beads 位置。
4. 图像配准：先由图像相关做粗对齐，再旋转+平移使两枚位置最接近的微球重合；所有图像统一对齐到第一轮建立的坐标系；用额外 5 枚微球的残差距离评估，配准误差典型 ~20 nm。
5. 跨轮次连接 spot：若相邻轮次 spot 间距 <1 pixel（167 nm）则串成一个"string"，代表一个候选 RNA 分子。
6. 按 string 在各轮的 on/off 模式赋二进制词：高于阈值记 '1'，否则记 '0'。
7. 解码：MHD4 下"精确匹配或仅差 1 bit"归入对应 RNA（差 1 bit 即纠错，Fig. 2D 红叉）；MHD2 下仅精确匹配才归入。
8. 按 code word 逐 bit 统计错误率（利用 MHD4 的纠错信息反推每轮 p₁ 与 p₀），加权平均得每轮错误率，再由 Eq. 7 估计每个 species 的 calling rate。
9. 计算 confidence ratio = 精确匹配数 / 一位错纠错匹配数，与 misidentification control words 的分布比较。
10. 在 40 μm × 40 μm 区域内逐细胞计数；将信号过亮的核区排除（1001 基因实验中核区基本整体排除）。

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| spot 定位 | multi-Gaussian fitting，高斯宽度 167 nm | 允许重叠 spot 分别拟合 |
| 阈值策略（140 基因） | 最小化 1→0 与 0→1 错误率之和 | 逐轮调整 |
| 阈值策略（1001 基因） | 最大化 4 个"1"位词 / 3 或 5 个"1"位词之比 | 逐轮调整 |
| 配准方法 | 2 枚最相似 fiducial beads 的旋转+平移 | 以第一轮坐标系为基准 |
| 配准误差 | ~20 nm（由 5 枚额外微球残差评估） | 决定连接容差 |
| String 连接阈值 | <1 pixel = 167 nm | 跨轮次同一分子判定 |
| 解码判据（MHD4） | 精确匹配 或 差 1 bit | 单比特纠错 |
| 解码判据（MHD2） | 仅精确匹配 | 只能检错 |
| 平均 1→0 错误率 | ~10% | 每轮每 bit |
| 平均 0→1 错误率 | ~4% | 每轮每 bit |
| Calling rate（MHD4） | ~80% | 纠错后 |
| Calling rate（MHD2） | 约 1/3 of MHD4（~27%） | 无纠错 |
| Confidence ratio 阈值 | > controls 最大值 | 140 基因保留 91%；1001 基因保留 73% |
| 计数区域 | 40 μm × 40 μm | 每细胞计数范围 |
| 细胞核处理 | 过亮核区排除 | mRNA 主要富集于胞质 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Multi-Gaussian fitting | 用多个高斯函数同时拟合重叠 spot 的定位算法 |
| Fiducial registration | 以荧光微球为基准的跨轮次图像对齐 |
| String | 跨轮次按 <167 nm 距离串起的 spot 序列，对应一个候选 RNA 分子 |
| Measured word | 由 string 的 on/off 模式得到的实测二进制词 |
| Exact match / error-correctable match | 与码字完全相同 / 差 1 bit 且可被纠正的匹配 |
| Confidence ratio | 精确匹配数 ÷ 一位错匹配数，越大越可信 |
| Misidentification control | blank word / no-target word，用于给出错误率基线 |
| Calling rate | 被正确解码的分子占该 RNA species 真实分子数的比例 |

## 复现
- 论文未公开源代码；核心组件（多高斯拟合、fiducial 配准、字符串连接、汉明解码）均可自行实现。
- 解码关键逻辑：

```python
bit = [1 if spot_present[r] else 0 for r in range(N)]     # N = 16 (MHD4) or 14 (MHD2)
for word, gene in codebook.items():
    d = hamming(bit, word)
    if d == 0:                       exact_match(gene)      # both codes
    elif d == 1 and code == "MHD4":  corrected_match(gene)    # MHD4 only
# else: double-bit error word -> discarded (detected, not corrected)
conf_ratio = n_exact / max(n_one_bit_corrected, 1)
```

## 生物学意义
该分析链条把物理层的单分子检测误差显式量化并传播到生物学结论上：~80% calling rate 而非 100%，意味着所有拷贝数都被系统性低估约 20%，但因为该比例在全丰度范围内基本恒定（MERFISH/smFISH 比值 0.82 ± 0.06），细胞间与基因间的**相对**比较仍然可靠。confidence ratio 筛选（140 基因保留 91%、1001 基因保留 73%）进一步把假阳性高的基因排除在后续相关分析之外。局限：string 连接阈值 167 nm 低于单分子光学分辨极限，密集区域会漏检或误连；核区整体排除使核富集 RNA（尤其非编码 RNA）无法测量。

## 涉及 Figures
- **Fig. 2, B–D** — 实测二进制词、boxed 子区域各轮图像、以及 red crosses 标示的纠错位。
- **Fig. 2F** — confidence ratio 分布与 misidentification controls 的比较。
- **Fig. 5A** — 1001 基因测量中检测到的分子定位与红色圆圈标示的不可识别分子。
- **Fig. S6** — 每轮 1→0 / 0→1 错误率与 calling rate 估计。
