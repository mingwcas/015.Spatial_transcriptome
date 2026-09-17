# Method: smFISH and Comparison with DBiT-seq

## 原文（Methods）
> Single molecular fish (smFISH) was performed using HCR v3.0 kit (Molecular Instruments, Inc) following manufacture protocols. Probes used in current study included Ttn, sfrp2, Trf and Dlk1. smFISH z stack images were taken using a ZEISS LSM 880 confocal microscope with a 60x oil immersion objective. The smFISH quantitation was performed using FISH-quant (https://biii.eu/fish-quant). mRNA transcript count was an average of three fields of view with each having a size of 306 × 306 μm. The sum of DBiT-seq transcript counts in the same locations were also calculated and compared side by side with smFISH counts.

## 解读

### 意义
该方法使用smFISH作为金标准验证DBiT-seq的转录本定量准确性，建立了技术间的相关性基准。

### 输入
- HCR v3.0 kit (Molecular Instruments)
- smFISH探针：Ttn, sfrp2, Trf, Dlk1
- ZEISS LSM 880共聚焦显微镜
- FISH-quant分析软件

### 输出
- smFISH图像和定量数据
- DBiT-seq与smFISH的对比数据

### 核心步骤
1. 按照Molecular Instruments HCR v3.0 kit说明书进行smFISH
2. 使用探针：Ttn, sfrp2, Trf, Dlk1
3. ZEISS LSM 880共聚焦显微镜60x油镜拍摄z-stack图像
4. FISH-quant软件定量smFISH信号
5. 计算3个视野的平均转录本数（每个视野306×306μm）
6. 计算DBiT-seq相同位置的转录本计数总和
7. 两者对比分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| smFISH方法 | HCR v3.0 | 杂交链式反应信号放大 |
| 探针基因 | Ttn, sfrp2, Trf, Dlk1 | 验证基因 |
| 显微镜 | ZEISS LSM 880, 60x油镜 | 高分辨率成像 |
| 视野大小 | 306×306μm | 3个视野取平均 |
| 分析软件 | FISH-quant | 定量分析 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| smFISH | Single molecule Fluorescent In Situ Hybridization，单分子荧光原位杂交 |
| HCR | Hybridization Chain Reaction，杂交链式反应，信号放大技术 |
| FISH-quant | smFISH定量分析工具 |

## 复现
- 工具/代码/URL：HCR v3.0 kit (Molecular Instruments); FISH-quant (https://biii.eu/fish-quant)
- 关键代码：NA

## 生物学意义
smFISH是转录本定量的金标准方法。通过与DBiT-seq对比，论文发现DBiT-seq检测到smFISH总转录本的约15.5%，这比Slide-seq高出1-2个数量级。这种验证建立了DBiT-seq定量准确性的信心，同时说明了不同技术间的检测效率差异。

## 涉及 Figures
- **Fig. S2F** — smFISH验证空间表达模式
- **Fig. S2G** — DBiT-seq与smFISH定量对比
