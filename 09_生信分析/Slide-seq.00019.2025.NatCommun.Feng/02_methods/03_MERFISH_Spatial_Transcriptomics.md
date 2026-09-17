# Method: MERFISH (Multiplexed Error-Robust FISH)

## 原文（Methods）
> Brain tissue was harvested from P0 and 6mo mice that were euthanized using CO2, immediately embedded using optimal cutting temperature (OCT) compound, and stored in −80 °C during short-term storage. Frozen-embedded samples were cryo-sectioned at −20 °C at 10 μm thickness prior to mounting on MERSCOPE beaded coverslips (Vizgen, Cat: 10500001). Following, tissue sections were refrozen for 5-15 min, fixed with 4% paraformaldehyde (PFA) diluted in 1X PBS for 15 min, washed three times with 1X PBS for 5 min each, and stored in 70% ethanol at 4 °C to allow for tissue permeabilization. Sections were stored in 70% ethanol for no longer than 3 weeks until all imaging from animals of the same age was completed. Sample preparation, including probe hybridization and gel embedding, was performed using Vizgen's sample preparation kit (Vizgen, Cat: 10400012) as detailed in Vizgen's manufacturer's instructions for unfixed tissue.

## 解读

### 意义
MERFISH是一种大规模平行单分子成像技术，可在原位测量数百种基因转录本的拷贝数和空间位置，研究Ts65Dn三体小鼠脑在发育和成熟过程中的细胞景观变化。

### 输入
- Ts65Dn和整倍体小鼠脑组织（P0和6月龄）
- Vizgen MERSCOPE平台
- 500基因MERFISH面板

### 输出
- >240,000个细胞的 простран transcriptomics数据
- 细胞类型空间分布
- 差异基因表达分析结果

### 核心步骤
1. CO2处死小鼠，迅速采集脑组织
2. OCT包埋，-80°C保存
3. -20°C条件下10 μm切片
4. 4% PFA固定15分钟
5. Vizgen样本准备试剂盒进行探针杂交和凝胶包埋
6. MERSCOPE成像（7个1.5 μm z平面）
7. Vizgen Post-processing Tool和Cellpose进行细胞分割
8. Scrublet去除doublets
9. 标准化：按细胞体积归一化并缩放

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 10 μm | 组织切片厚度 |
| z平面数 | 7 (1.5 μm each) | 捕获整个组织厚度 |
| MERFISH基因数 | 500 | 定制基因面板 |
| 细胞体积过滤 | <50 μm³ or >3×median | 排除异常细胞 |
| doublet过滤 | Scrublet | 去除双细胞 |
| 转录本标准化 | volume×1000/mean | 体积和样本间校正 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| MERFISH | Multiplexed Error-Robust Fluorescence In Situ Hybridization |
| MERSCOPE | Vizgen的空间转录组成像平台 |
| Cellpose | 基于机器学习的细胞分割算法 |
| Scrublet | 单细胞RNA-seq doublet检测工具 |

## 复现
- 平台：Vizgen MERSCOPE
- 软件：Vizgen Post-processing Tool, Cellpose 2.0
- 试剂盒：Vizgen #10500001, #10400012

## 生物学意义
MERFISH揭示了Ts65Dn小鼠脑中 trisomy相关的基因表达模式变化，包括WNT、SHH、NOTCH信号通路的改变，以及神经祖细胞自我更新、增殖和迁移相关基因的表达改变，为理解DS神经发育异常提供了空间分辨率的见解。

## 涉及 Figures
- **Fig. 5** — Cellular and spatial landscape of postnatal and mature trisomic mouse brains
- **Fig. 6** — Trisomy-associated transcriptional changes
