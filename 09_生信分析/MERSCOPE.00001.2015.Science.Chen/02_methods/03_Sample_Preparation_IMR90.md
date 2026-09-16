# Method: 细胞培养、固定与 encoding probe 杂交（IMR90）

## 原文（Methods）

> Human primary fibroblasts (American Type Culture Collection, IMR90), a commonly used cell line with a previously determined transcriptome (46), were used in this work. These cells are relatively large and flat, facilitating wide-field imaging without the need for optical sectioning. Cells were cultured with Eagle's Minimum Essential Medium.
>
> Cells were plated on 22-mm, #1.5 coverslips (Bioptechs, 0420-0323-2) at 350,000 cells/coverslip and incubated at 37°C with 5% CO2 for 48-96 hours within petri dishes. Cells were fixed for 20 min in 4% paraformaldehyde (Electron Microscopy Sciences, 15714) in 1x phosphate buffered saline (PBS; Ambion, AM9625) at room temperature, reduced for 5 min with 0.1% w/v sodium borohydride (Sigma, 480886) in water to reduce background fluorescence, washed three times with ice-cold 1x PBS, permeabilized for 2 min with 0.5% v/v Triton (Sigma, T8787) in 1x PBS at room temperature, and washed three times with ice cold 1x PBS.
>
> 10 μL of 100 μM (140-gene experiments) or 200 μM (1001-gene experiments) encoding probes in encoding hybridization buffer was added to the cell-containing coverslip and spread uniformly by placing another coverslip on top of the sample. Samples were then incubated in a humid chamber inside a 37°C-hybridization oven for 18-36 hours.
>
> A 1:1000 dilution of 0.2-μm-diameter carboxylate-modified orange fluorescent beads (Life Technologies, F-8809) in 2xSSC was sonicated for 3 min and then incubated with the sample for 5 min.

## 解读

### 意义
建立一套 RNase-free、低自发荧光的样本制备流程，在保持细胞形态（用于后续空间分布分析）的同时让 ~192 条/基因的 encoding probe 在 18–36 小时内充分杂交到胞内 RNA，并把 fiducial beads 锚定在样本上以支持后续多轮图像配准。

### 输入
- IMR90 人胚肺原代成纤维细胞（ATCC）
- 22-mm #1.5 coverslip（Bioptechs 0420-0323-2）、Eagle's Minimum Essential Medium
- 100 μM（140 基因）或 200 μM（1001 基因）encoding probes
- Encoding wash / hybridization buffer（2×SSC、30% formamide、2 mM vanadyl ribonucleoside complex、1 mg/mL yeast tRNA、10% dextran sulfate）
- 0.2-μm carboxylate-modified orange fiducial beads（Life Technologies F-8809）

### 输出
- 已固定、透化、完成 encoding probe 杂交并 post-fix 的 coverslip 样本
- 表面锚定 fiducial beads 的成像样品（可立即成像，或 4°C 保存不超过 12 小时）

### 核心步骤
1. IMR90 以 Eagle's Minimum Essential Medium 培养，按 350,000 cells/coverslip 接种到 22-mm #1.5 coverslip，37°C、5% CO₂ 培养 48–96 小时。
2. 室温 4% PFA（1×PBS）固定 20 min。
3. 0.1% w/v sodium borohydride 水溶液还原 5 min，降低背景自发荧光；冰 1×PBS 洗 3 次。
4. 室温 0.5% v/v Triton（1×PBS）透化 2 min；冰 1×PBS 洗 3 次。
5. Encoding wash buffer 预平衡 5 min。
6. 加 10 μL encoding probes，盖上另一片 coverslip 使均匀铺展，湿盒内 37°C 杂交 18–36 小时。
7. Primary encoding wash buffer 洗 3 次，每次 47°C 10 min。
8. 加入经 3 min 超声的 1:1000 fiducial beads（2×SSC），孵育 5 min；2×SSC 洗 1 次。
9. 4% v/v PFA / 2×SSC 室温 post-fix 30 min；2×SSC 洗 3 次；立即成像或 4°C 保存 ≤12 小时。
10. 所有溶液按 RNase-free 配制。

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 细胞系 | IMR90 人原代成纤维细胞 | 大而扁平，适合无光学切片的宽场成像 |
| 接种密度 | 350,000 cells/coverslip | 22-mm #1.5 coverslip 上的细胞数 |
| 培养条件 | 37°C, 5% CO₂, 48–96 h | 贴壁与形态伸展 |
| 固定 | 4% PFA / 1×PBS, 20 min, RT | 交联固定 RNA 与蛋白 |
| 还原 | 0.1% w/v NaBH₄, 5 min | 降低背景荧光 |
| 透化 | 0.5% v/v Triton / 1×PBS, 2 min, RT | 允许探针进入细胞 |
| Encoding probe 浓度 | 100 μM（140 基因）/ 200 μM（1001 基因） | 10 μL/样品 |
| Encoding 杂交时长 | 18–36 h, 37°C | 探针杂交到细胞 RNA |
| Wash | 47°C × 10 min × 3 | 去除未结合探针 |
| Fiducial beads | 0.2 μm, 1:1000, 5 min | 多轮图像配准基准 |
| Post-fix | 4% PFA / 2×SSC, 30 min, RT | 固定已杂交探针 |
| 保存 | 4°C ≤12 h | 上机前限制 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Encoding hybridization buffer | encoding wash buffer + 1 mg/mL yeast tRNA + 10% w/v dextran sulfate |
| Encoding wash buffer | 2×SSC + 30% v/v formamide + 2 mM vanadyl ribonucleoside complex |
| Vanadyl ribonucleoside complex | RNase 抑制剂，保护 RNA 不被降解 |
| Dextran sulfate | 增加大分子有效浓度、加速杂交的拥挤剂 |
| Fiducial bead | 固定在样品上的荧光微球，用作多轮成像配准的参考点 |
| Post-fixation | 杂交后再次 PFA 固定，防止探针在后续多轮洗涤中脱落 |

## 复现
- 试剂清单：ATCC IMR90；Bioptechs 0420-0323-2 coverslip；EMS 15714 PFA；Sigma 480886 NaBH₄；Sigma T8787 Triton；Ambion AM9763 20×SSC；Ambion AM9342 formamide；NEB S1402S vanadyl ribonucleoside complex；Life Technologies 15401-011 yeast tRNA；Sigma D8906-50G dextran sulfate；Life Technologies F-8809 beads
- 关键调用（实验台流程摘要）：

```text
plate 3.5e5 IMR90 / 22-mm #1.5 coverslip; 37C, 5% CO2, 48-96 h
4% PFA 20 min -> 0.1% NaBH4 5 min -> 0.5% Triton 2 min (all RT, 1x PBS washes)
encoding wash buffer 5 min -> 10 uL 100-200 uM encoding probes
37C humid chamber 18-36 h -> wash 47C x10 min x3
fiducial beads 1:1000 (sonicated 3 min) 5 min -> post-fix 4% PFA/2xSSC 30 min
```

## 生物学意义
样本制备直接决定 MERFISH 的两类关键质量指标：信号背景比（NaBH₄ 还原与严格洗涤）和 RNA 保有率（RNase-free 与 vanadyl ribonucleoside complex）。作者用 conventional smFISH 的 z 层扫描验证了两点：只有 15% ± 1% 的 RNA 分子位于固定焦平面之外（说明斜入射宽场照明覆盖了细胞全深），且仅 5% ± 2% 的 mRNA 位于细胞核内（因此排除核区造成的损失很小）。局限：无光学切片与 z 扫描意味着厚细胞或组织必须改用光学切片方法才能用于 MERFISH。

## 涉及 Figures
- **Fig. 2A / Fig. 5A** — 本流程制备的 IMR90 细胞在 16 轮 / 14 轮杂交中的成像结果。
- **Fig. S4** — 样本在 16 轮迭代标记成像中的稳定性（spot 数随轮次的变化与亮度趋势）。
