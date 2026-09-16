# Method: Cryosectioning, fixation, H&E staining and imaging

## 原文（Methods）
> “The first stage ... is to place sections of fresh-frozen tissue on top of the microarray... the sections are formalin-fixed... stained with H&E... imaged at high resolution” (Methods/Experimental design, PDF pp.5, 17–18; Steps 1–24). “Acquire bright-field images ... using a 20× objective ... save ... .jpg files” (Step 24).

## 解读
### 意义
保留组织形态并建立后续空间定位的明场参考图。
### 输入
−80°C OCT包埋新鲜冷冻哺乳动物组织；条码oligo-dT微阵列（6个subarrays，每个1,007 spots，100 μm直径、200 μm间距）。
### 输出
固定、H&E染色组织切片及20× bright-field JPG图像。
### 核心步骤
1. 冷冻切片并附着到array；4% formaldehyde固定10 min。 2. 异丙醇、hematoxylin、bluing buffer、eosin染色。 3. 20×采集各subarray明场图。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| 固定 | 4% formaldehyde，10 min | 保存形态和RNA |
| 成像 | 20×，每subarray；JPG | 与spot图配准 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| spatial spot | 约100 μm的条码捕获圆区 |
| H&E | hematoxylin/eosin组织学染色 |

## 复现
- 工具/代码/URL：显微镜；视频 https://www.youtube.com/watch?v=ZsuGQRLpnbE
- 代码片段：不适用（实验步骤）。

## 生物学意义
形态图使表达矩阵可回投到组织区域；切片折叠、裂纹、条纹或染色不均会导致空间偏差。

## 涉及 Figures
- **Fig. 1、Fig. 6** — 组织形态与空间spot参照。
