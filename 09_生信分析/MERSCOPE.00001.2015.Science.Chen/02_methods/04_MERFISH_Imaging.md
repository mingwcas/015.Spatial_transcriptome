# Method: MERFISH 成像（显微镜、激光、杂交轮次与光漂白）

## 原文（Methods）

> The sample coverslip was assembled into a Bioptech's FCS2 flow chamber, and the flow through this chamber was controlled via a home-built fluidics system composed of three computer-controlled 8-way valves (Hamilton, MVP and HVXM 8-5) and a computer-controlled peristaltic pump (Rainin, Dynamax RP-1). The sample was imaged on a home-built microscope constructed around an Olympus IX-71 body and a 1.45 NA, 100x oil immersion objective and configured for oblique incidence excitation.
>
> Illumination was provided at 641 nm, 561 nm, and 405 nm using solid state lasers (MPB communications, VFL-P500-642; Coherent, 561-200CWCDRH; and Coherent, 1069413/AT) for excitation of our Cy5-labeled readout probes, the fiducial beads, and nuclear counterstains, respectively. … imaged with an EMCCD camera (Andor, iXon-897). The camera was configured so that a pixel corresponds to 167 nm in the sample plane.
>
> 1 mL of 10 nM of the appropriate fluorescently labeled readout probe in readout hybridization buffer … was flown across the sample, flow was stopped, and the sample was incubated for 15 min. … approximately 75 to 100 regions were exposed to ~25 mW 642-nm and 1 mW of 561-nm light and imaged. Each region was 40 μm by 40 μm.
>
> After imaging, the fluorescence of the readout probes was extinguished via photobleaching. The sample was washed with 2 mL of photobleaching buffer (2xSSC and 2 mM vanadyl ribonucleoside complex), and each imaged region of the sample was exposed to 200 mW of 641-nm light for 3 s. … The above hybridization, imaging, and photobleaching process was repeated either 16 times for the 140-gene measurements using the MHD4 code or 14 times for the 1001-gene measurements using the MHD2 code. An entire experiment was typically completed in ~20 hours.

## 解读

### 意义
把"顺序杂交 + 成像 + 光漂白"完全自动化，形成一条可在约 20 小时内完成 14–16 轮的流水线；每轮用一条 Cy5 readout probe 读出 4 个"1"位之一，光漂白确保轮次之间信号不串扰。

### 输入
- 已完成 encoding probe 杂交并锚定 fiducial beads 的 coverslip 样品
- Readout hybridization buffer（2×SSC、10% v/v formamide、10% w/v dextran sulfate、2 mM vanadyl ribonucleoside complex）
- 10 nM Cy5 标记 readout probe（每轮一条，140 基因用 bit 1–16，1001 基因用 bit 1–14）
- Readout wash buffer、imaging buffer、photobleaching buffer
- Hoechst 核染色（ENZ-52401）

### 输出
- 每个成像区域 14 或 16 轮的单分子荧光图像（每轮 641 nm + 561 nm 双通道）
- 光漂白后的验证图像（bleach 1；确认信号已被清除）
- 405 nm 采集的 Hoechst 核图像（用于核分割与距离分析）
- 每张图约 75–100 个 40 μm × 40 μm 区域

### 核心步骤
1. coverslip 装入 Bioptechs FCS2 流室，由三只电脑控制 8-way 阀（Hamilton MVP / HVXM 8-5）与蠕动泵（Rainin Dynamax RP-1）驱动流路。
2. 物镜加热至 37°C；开启自建自动对焦系统维持全程合焦。
3. 通入 1 mL 10 nM readout probe（readout hybridization buffer），停流孵育 15 min。
4. 通入 2 mL readout wash buffer（2×SSC、20% v/v formamide、2 mM vanadyl ribonucleoside complex），停流孵育 3 min。
5. 通入 2 mL imaging buffer（2×SSC、50 mM Tris-HCl pH 8、10% w/v glucose、2 mM Trolox、0.5 mg/mL glucose oxidase、40 μg/mL catalase），停流。
6. 每个 40 μm × 40 μm 区域以 ~25 mW 642 nm + 1 mW 561 nm 曝光成像（每次实验约 75–100 个区域）。
7. 通入 2 mL photobleaching buffer，每区域以 200 mW 641 nm 照射 3 s 淬灭信号；重新通入 imaging buffer 后再成像一次以确认漂白效果。
8. 重复步骤 3–7 共 16 次（140 基因，MHD4）或 14 次（1001 基因，MHD2）。
9. 成像结束后通入 Hoechst（1:1000 in 2×SSC）染核，2×SSC 与 imaging buffer 各洗一次，每区域以 ~1 mW 405 nm 再成像一次。
10. 整个实验约 20 小时完成；imaging buffer 全程现配并储存于矿物油层下（>24 h 稳定）。

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 显微镜 | 自建，Olympus IX-71 机身 | 宽场 + 斜入射激发 |
| 物镜 | 1.45 NA, 100× 油浸 | 高收集效率、单分子灵敏度 |
| 照明 | oblique-incidence（斜入射） | 降低背景、照亮细胞全深 |
| 激发激光 | 641 nm（Cy5）/ 561 nm（fiducial beads）/ 405 nm（Hoechst） | 三通道 |
| 相机 | EMCCD（Andor iXon-897） | 单分子成像 |
| 像素尺寸 | 167 nm/pixel | 成像采样 |
| 成像区域 | 40 μm × 40 μm | 每区域计数范围 |
| 区域数 | ~75–100 regions/轮 | 每次实验覆盖范围 |
| Readout probe 浓度 | 10 nM | 1 mL/轮 |
| 杂交时间 | 15 min | 读出杂交 |
| 洗涤 | 3 min（readout wash buffer） | 去除非特异结合 |
| 成像激光功率 | ~25 mW @ 642 nm + 1 mW @ 561 nm | 背端口测得 |
| 光漂白 | 200 mW @ 641 nm, 3 s | 每区域每轮淬灭 Cy5 |
| 轮次 | 16（MHD4）/ 14（MHD2） | 与位数一致 |
| 总时长 | ~20 hours | 整次实验 |
| 核染色 | Hoechst 1:1000，~1 mW 405 nm | 最后一次成像 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Oblique-incidence illumination | 斜入射照明，减少激发体积从而降低背景荧光 |
| Readout hybridization | 荧光 readout probe 与 encoding probe 上 readout sequence 的杂交 |
| Photobleaching | 用强 641 nm 光不可逆淬灭 Cy5，使下一轮读出不受上一轮残留影响 |
| Bleach image | 漂白后采集的图像，用于验证信号清除效率 |
| Imaging buffer | 含葡萄糖/glucose oxidase/catalase 的除氧+抗氧化体系，抑制 Cy5 闪烁与光损伤 |
| Fiducial channel | 561 nm 通道，采集固定微球用于跨轮次配准 |
| QuadView | 荧光分光模块，把发射光分成 4 个通道同时成像 |

## 复现
- 硬件：Bioptechs FCS2 流室 + 物镜加热器；Hamilton MVP/HVXM 8-5 阀；Rainin Dynamax RP-1 泵；Olympus IX-71；1.45 NA 100× 油镜；MPB VFL-P500-642、Coherent 561-200CWCDRH、Coherent 1069413/AT 激光；Chroma zy405/488/561/647/752RP-UF1、ZET405/488/561/647-656/752m、T560lpxr、T650lpxr、750dcxxr、ET525/50m、WT59550m-2f、ET700/75m、HQ770lp；Photometrics QuadView；Andor iXon-897
- 关键流程（伪代码）：

```text
for bit in 1..16:              # 14 for the 1001-gene MHD2 experiment
    flow 1 mL 10 nM readout probe;  incubate 15 min
    flow 2 mL readout wash buffer;  incubate 3 min
    flow 2 mL imaging buffer
    image ~75-100 regions of 40x40 um @ 25 mW 642 nm + 1 mW 561 nm
    flow 2 mL photobleaching buffer; 200 mW 641 nm for 3 s per region
    image again to confirm bleaching
# then Hoechst 1:1000, 2xSSC wash, image @ ~1 mW 405 nm
```

## 生物学意义
成像几何与流程决定了 MERFISH 的可测密度上限。作者估算 IMR90 全转录组 RNA 密度约 200 molecules/μm³，而当前成像与分析手段每轮可分辨 2–3 molecules/μm³，32 轮后可达约 20 molecules/μm³ —— 足以同时覆盖除表达量最高 10% 以外的全部基因；若用压缩感知类算法可再提升约 4 倍，超分辨成像理论上可达 ~10⁵ molecules/μm³。局限：宽场无光学切片的几何使约 15% 分子落在焦平面外；核区（1001 基因实验中尤其严重）信号过密无法分辨单分子，被整体排除。

## 涉及 Figures
- **Fig. 2A** — 单细胞 16 轮杂交图像（hyb 1–hyb 16）与漂白后图像（bleach 1）。
- **Fig. 2C** — boxed 子区域在各轮杂交中的荧光图像。
- **Fig. 5A**（及 fig. S9A）— 14 轮杂交的 1001 基因测量。
- **Fig. S4** — 跨轮次 spot 数与亮度的稳定性检验。
