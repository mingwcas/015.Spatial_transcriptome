# Method: Quality control of Spatial-ATAC-Hi-C data

## 原文（Methods）
> For Spatial-ATAC-Hi-C data, we used the pairtools stats (v.0.3.0) (https://github.com/open2c/pairtools) to compute summary statistics for all the pairs files in each sample, quantifying cis, trans and long-range (≥10 kb) contacts in single pixels. TSS enrichment of ATAC-seq signal was used to quantify the spatial-ATAC data quality. The ArchR74 package was used to calculate the TSS enrichment scores. Specifically, TSS positions were obtained from the precompiled version of hg38 genome for human and mm10 for mouse in ArchR. To approximate a TSS enrichment score for each single pixel, we calculated the average accessibility within the 50-bp window centered on each TSS and normalized this by the average accessibility of the TSS flanking regions (±1,900–2,000 bp).

## 解读

### 意义
评估Spatial-ATAC-Hi-C数据的质量，包括Hi-C接触统计和ATAC-seq信号质量，确保数据适合下游分析

### 输入
- 2500个空间像素的pairs文件（Hi-C数据）
- fragment.tsv文件（ATAC-seq数据）
- 参考基因组注释（TSS位置）

### 输出
- Hi-C接触统计数据（cis, trans, long-range contacts）
- TSS富集分数（ATAC-seq质量指标）
- 数据质量报告和过滤标准

### 核心步骤
1. **Hi-C数据质量控制**：
   - 使用pairtools stats (v.0.3.0)计算每个像素的接触统计
   - 量化cis接触（同一条染色体内的相互作用）
   - 量化trans接触（不同染色体间的相互作用）
   - 量化长程接触（≥10 kb）

2. **ATAC-seq数据质量控制**：
   - 使用ArchR包计算TSS富集分数
   - TSS位置来源：hg38（人类）或mm10（小鼠）预编译版本
   - 计算方法：
     - 50-bp窗口中心TSS的平均可及性
     - 标准化：除以TSS侧翼区域（±1,900-2,000 bp）的平均可及性

3. **质量评估**：
   - 评估Hi-C接触质量（cis/trans比例，长程接触比例）
   - 评估ATAC-seq信号质量（TSS富集分数）
   - 识别低质量像素用于后续过滤

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| pairtools版本 | v.0.3.0 | Hi-C接触统计工具 |
| TSS窗口大小 | 50 bp | 计算TSS富集的核心区域 |
| 侧翼区域 | ±1,900-2,000 bp | TSS富集计算的标准化区域 |
| 长程接触阈值 | ≥10 kb | 长程相互作用的定义 |
| 参考基因组TSS | hg38 (人类), mm10 (小鼠) | TSS位置来源 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| cis接触 | 同一条染色体内的DNA相互作用 |
| trans接触 | 不同染色体间的DNA相互作用 |
| 长程接触 | 基因组距离≥10 kb的相互作用 |
| TSS富集分数 | 转录起始位点附近的染色质可及性富集程度，ATAC-seq质量指标 |
| TSS | Transcription Start Site，转录起始位点 |
| pairtools | Hi-C数据处理和统计工具包 |

## 复现
- 工具/代码/URL
  - pairtools: https://github.com/open2c/pairtools
  - ArchR: https://github.com/GreenleafLab/ArchR
  - 参考基因组注释：ArchR预编译版本
- 代码片段
  ```bash
  # Hi-C质量控制
  for pixel in pixels/*.pairs; do
    pairtools stats $pixel > ${pixel%.pairs}.stats
  done
  
  # ATAC-seq TSS富集计算（R/ArchR）
  library(ArchR)
  # 加载参考基因组TSS位置
  TSS <- getTSS(genome = "hg38")  # 或 "mm10"
  # 计算每个像素的TSS富集分数
  # 具体代码见ArchR文档
  ```

## 生物学意义
质量控制是Spatial-ATAC-Hi-C数据分析的关键环节：

**Hi-C数据质量指标**：
- **cis/trans比例**：高质量数据通常具有较高的cis/trans比例
- **长程接触比例**：反映3D基因组结构的复杂性和质量
- **单像素接触数**：影响后续分析的统计功效

**ATAC-seq数据质量指标**：
- **TSS富集分数**：衡量染色质可及性信号的特异性
- **TSS富集模式**：高质量数据在TSS附近显示清晰的富集峰
- **信号噪声比**：影响后续peak calling和差异分析

**质量控制的生物学意义**：
- 确保数据反映真实的生物学信号
- 识别技术偏差和批次效应
- 指导后续分析参数的设置

该质量控制方法的优势：
- 使用成熟工具（pairtools, ArchR），结果可靠
- 多维度质量评估，全面反映数据质量
- 标准化流程便于比较不同样本和实验

局限性：
- 质量阈值需要根据具体实验调整
- 某些质量指标可能受生物学因素影响（如细胞类型组成）
- 需要人工判断和解释质量指标
- 计算资源需求较高

## 涉及 Figures
- **Extended Data Fig. 5** — 数据质量控制指标和分布
- **Fig. 2a** — 空间ATAC-seq和Hi-C数据质量展示
- **Supplementary Fig. 1** — 质量控制指标详细分析
