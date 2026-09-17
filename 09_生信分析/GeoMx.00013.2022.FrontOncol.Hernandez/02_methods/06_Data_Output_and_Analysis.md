# Method: Data Output and Analysis (DSP Data Analysis Suite)

## 原文（Methods）
> The counts obtained are then mapped to the different areas selected in the GeoMx DSP device; the device has an analysis suite that facilitates quality control (QC) of DSP counts, and data visualization, normalization, and analysis. The QC of the initial dataset is the initial step for data analysis and comprises the assessment of parameters such as binding density, positive and limit of detection controls, positive control normalization, and minimum nuclei and surface area. The normalization step allows the normalization of the data using the counts from specific probes like "Housekeepers" or "IgGs" for background correction. The method of normalization should be decided based on the type of sample and the aim of the project. Data can be visualized in different ways including heatmaps, boxplots, and correlation plots. The platform also provides statistical test functions (18).

## 解读

### 意义
数据分析和 QC 是 DSP 工作流程的最后关键环节，GeoMx Data Analysis Suite 提供了一站式工具完成原始计数的质量控制、归一化和可视化分析，确保数据的可靠性和生物学可解释性。

### 输入
- nCounter 输出的原始计数数据（各 AOI × 各靶标矩阵）
- 样品注释信息（临床特征、分组等）

### 输出
- QC 通过的数据矩阵
- 归一化后的表达矩阵
- 可视化结果（热图、箱线图、相关性图）
- 统计检验结果（t-test, Mann-Whitney, 线性混合模型等）

### 核心步骤
1. **QC of Initial Dataset**：
   - Binding density（结合密度）
   - Positive and limit of detection controls（阳性对照和检测限对照）
   - Positive control normalization（阳性对照归一化）
   - Minimum nuclei and surface area（最小细胞核数和表面积）
2. **Normalization**：使用 Housekeepers（看家基因/蛋白）或 IgGs 进行背景校正
3. **Visualization**：
   - Heatmaps（热图）
   - Boxplots（箱线图）
   - Correlation plots（相关性图）
4. **Statistical Analysis**：
   - Unpaired t-test（两组独立样本）
   - Paired t-test（配对样本）
   - Mann–Whitney U-test（非正态分布数据）
   - Linear mixed models（重复测量数据）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| QC 参数 | Binding density, 阳性对照, LOD, 最小核数/面积 | 评估数据质量 |
| 归一化策略 | Housekeepers (蛋白: GAPDH, Histone H3, S6; RNA: UBB, OAZ1, SDHA, POLR2A) 或 IgGs | 基于研究目的选择 |
| 统计方法 | t-test, Mann-Whitney, 线性混合模型 | 根据数据结构选择 |
| 可视化 | 热图、箱线图、火山图 | 数据探索和结果展示 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Binding Density | 结合密度，反映探针与组织的结合效率 |
| LOD | Limit of Detection，检测限 |
| Housekeepers | 看家基因/蛋白，用作归一化的内参 |
| IgG | 免疫球蛋白同型对照，用于背景校正 |
| Linear Mixed Model | 线性混合模型，适用于多 ROI 嵌套数据结构 |
| GeoMx Data Analysis Suite | GeoMx 数据分析套件（内置于 GeoMx Data Center） |

## 复现
- 工具/代码/URL：[GeoMx Data Center](https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-data-center/)
- GeoScript Hub（自定义R脚本）：[https://nanostring.com/products/geomx-digital-spatial-profiler/geoscript-hub/](https://nanostring.com/products/geomx-digital-spatial-profiler/geoscript-hub/)

## 生物学意义
数据分析和 QC 确保 DSP 产生的数十至数百个靶标的数据质量可靠。归一化策略的选择对最终结果影响显著——不同组织类型、不同研究问题可能需要不同的归一化方法。该平台的内置统计功能使研究者能够快速比较不同临床亚组（如免疫治疗应答vs无应答）的 biomarker 差异，但复杂分析仍建议与生信专家合作。

## 涉及 Figures
- **Fig. 6** — 热图示例（用于初始数据集的 QC 可视化）
