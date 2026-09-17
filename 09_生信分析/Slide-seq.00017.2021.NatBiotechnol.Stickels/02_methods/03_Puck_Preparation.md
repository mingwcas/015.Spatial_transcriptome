# Method: Puck Preparation

## 原文（Methods）
> Puck preparation was performed as described previously1, with the following modification. Beads were pelleted and resuspended in water with 10% DMSO at a concentration between 20,000 and 50,000 beads per μl. Then, 10 μl of the resulting solution was pipetted into each position on the gasket. The coverslip gasket filled with beads was centrifuged at 850g for at least 30 min at 4 °C until the surface was dry.

## 解读

### 意义
Puck preparation是将barcoded beads铺成均匀单层用于空间转录组实验的关键步骤，确保每个bead位置固定且可被显微镜识别。

### 输入
- Barcoded beads (悬浮于水+DMSO)
- Gasket (硅胶垫片，带有圆形凹槽)
- 10% DMSO水溶液

### 输出
- 用于空间转录组的puck（beads紧密排列在glass substrate上）

### 核心步骤
1. **Bead重悬**: 将beads pellet重悬于含10% DMSO的水中，浓度20,000-50,000 beads/μl
2. **铺beads**: 取10 μl bead溶液加入gasket每个孔位
3. **离心**: 850g, 4°C离心至少30分钟
4. **干燥**: 直至表面干燥，beads紧密贴附

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| DMSO浓度 | 10% | 促进beads贴附 |
| Bead浓度 | 20,000-50,000 beads/μl | 优化覆盖度 |
| 铺液体积 | 10 μl/孔 | gasket规格 |
| 离心力 | 850 g | 轻柔离心 |
| 离心温度 | 4°C | 防止降解 |
| 离心时间 | ≥30 min | 确保干燥 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Puck | Barcoded bead array，贴附在玻璃表面的10μm beads阵列 |
| Gasket | 硅胶垫片，带有圆形凹槽孔位用于放置beads |
| DMSO | 二甲基亚砜，促进寡核苷酸和beads贴附玻璃表面 |

## 复现
- **设备**: Nikon Eclipse Ti microscope, Yokogawa CSU-W1 confocal scanner
- **耗材**: Bioptechs FCS2 flow cell, gasket from previous study
- **详细protocol**: 见原文献Slide-seq (Rodriques et al., Science 2019)

## 生物学意义
Puck是Slide-seq平台的核心组件。每个puck上的beads在空间中位置固定，通过后续sequencing确定每个bead的barcode，从而将RNA捕获与空间位置关联。均匀的单层beads铺排是获得高空间分辨率的前提。

## 涉及 Figures
- **Fig. 1a** — Puck preparation shown in method overview
