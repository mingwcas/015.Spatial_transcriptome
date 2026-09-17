# Method: Data Normalization Strategies

## 原文（Methods）
> Data normalization must be performed based on certain features of samples, strategies for ROI selection and segmentation, and the expression of housekeepers or isotype biomarkers. For this task, the platform has different options: Scale to nuclei, Scale to area, Housekeepers (reference normalization, RN), Background correction (SNR)... Protein or RNA profiles of single or few cells can be difficult to define the above background. Markers with low counts should be looked at with caution (e.g., PD-L1), especially since counts below 1 (found, for example, in immunologically cold areas) are equalized to 1 in the initial dataset, which can alter the final data when normalized by SNR (86).

## 解读

### 意义
DSP 数据归一化策略的选择直接影响最终数据的生物学解释。根据样本类型、ROI 特征和实验目的选择正确的归一化方法，是避免人为引入偏差或掩盖真实生物学信号的关键步骤。

### 输入
- 各 AOI 的原始计数（raw counts）
- 细胞核数、表面积等形态学数据
- Housekeeper 基因/蛋白表达量
- 阴性对照（IgG / 阴性探针）表达量

### 输出
- 归一化后的表达矩阵
- 可用于组间比较的标准化数据

### 核心步骤
1. **Scale to Nuclei**（按细胞核数归一化）：
   - 适用场景：研究每细胞 biomarker 表达
   - 方法：用检测到的细胞核数几何均值调整计数
   - 注意：当前 nuclei count 算法因组织异质性准确性有限，暂不推荐
2. **Scale to Area**（按面积归一化）：
   - 适用场景：ROI 面积差异较大的情况
   - 方法：用各 AOI 面积的几何均值调整计数
3. **Housekeepers / Reference Normalization (RN)**：
   - RNA panel：UBB, OAZ1, SDHA, POLR2A
   - 蛋白 panel：GAPDH, Histone H3, S6
   - 方法：评估各 housekeeper 的相关性，选取相关性好的取几何均值
4. **Background Correction (SNR, Signal-to-Noise Ratio)**：
   - 蛋白：IgG1, IgG2a, Rabbit IgG（三种同型对照）
   - RNA：8个阴性探针
   - 方法：评估各阴性对照/IgG 的相关性，选取表现好的用于背景校正
5. 选择合适的归一化策略（建议与生信分析师合作）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Scale to Nuclei | 暂不推荐 | nuclei count 算法准确性不足 |
| Housekeepers (蛋白) | GAPDH, Histone H3, S6 | 蛋白 panel 内参 |
| Housekeepers (RNA) | UBB, OAZ1, SDHA, POLR2A | RNA panel 内参 |
| IgG 同型对照 (蛋白) | IgG1, IgG2a, Rabbit IgG | 蛋白背景校正 |
| 阴性探针 (RNA) | 8个 | RNA 背景校正 |
| 最低计数值 | <1的计数值统一为1 | 影响 SNR 归一化结果 |
| 低丰度标记物 | 例：PD-L1 | 免疫冷区域信号可能失真 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Scale to Nuclei | 按细胞核数归一化 |
| Scale to Area | 按ROI面积归一化 |
| Reference Normalization (RN) | 看家基因归一化（内参归一化） |
| SNR | Signal-to-Noise Ratio，信噪比归一化 |
| Geometric Mean | 几何均值，用于归一化的聚合统计量 |
| LOD | Limit of Detection，检测限 |

## 复现
- 工具/代码/URL：GeoMx Data Analysis Suite（内置）
- GeoScript Hub（自定义 R 脚本）：[https://nanostring.com/products/geomx-digital-spatial-profiler/geoscript-hub/](https://nanostring.com/products/geomx-digital-spatial-profiler/geoscript-hub/)
- 参考：Decalf J et al., J Pathol 2019 (doi: 10.1002/path.5223)

## 生物学意义
归一化策略对 DSP 数据质量有决定性影响。选择不当可能导致真实信号被掩盖或人为引入批次效应。例如，SNR 归一化对于低表达biomarker（如 PD-L1）存在风险，因为免疫冷区域的<1计数值被统一设为1，会在SNR归一化后被放大。建议在初始数据探索阶段测试多种归一化策略，结合生物学预期（如肿瘤区域应有更高 panCK，免疫区域应有更高 CD45）进行验证。跨实验室数据比较时，标准化流程尤为重要。

## 涉及 Figures
- **Fig. 6** — 热图用于初始数据集 QC，辅助归一化策略选择
