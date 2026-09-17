# Method: CNV Analysis of Spatial-ATAC-Hi-C Data

## 原文（Methods）
> The copy number (CN) ratio was calculated from Hi-C data using the 'calculate-cnv' module in NeoLoopFinder. All samples used in this paper were assumed to be diploid and the CN ratio here means the copy number divided by two copies. For each single pixel, the CN ratio at 5-Mb resolution was estimated, and the results were directly used for genome-wide heatmap visualization and clustering. The regional CN ratio visualization was plotted at 100-kb resolution. At sample level, the CN ratio was estimated at 100-kb resolution and a hidden Markov model-based segmentation was further performed using the 'segment-cnv' module to determine the boundaries of CN ratio segments. For spatial visualization of CNVs, we used MAGIC (Markov Affinity-based Graph Imputation of Cells) to further smooth the CN ratio.

## 解读

### 意义
从空间Hi-C数据中推断拷贝数变异（CNV），揭示肿瘤样本中基因组水平的空间异质性和克隆进化。

### 输入
- 空间Hi-C接触矩阵（单像素或伪批量）
- 参考基因组（mm10或GRCh38）
- NeoLoopFinder CNV模块

### 输出
- 单像素CNV谱（5-Mb分辨率）
- 伪批量CNV谱（100-kb分辨率）
- CNV分段边界（HMM分割）
- 空间CNV可视化图
- 基于CNV的聚类结果

### 核心步骤
1. 使用NeoLoopFinder的'calculate-cnv'模块从Hi-C数据计算拷贝数比值
2. 假设所有样本为二倍体，CN ratio = 拷贝数/2
3. 在5-Mb分辨率下估计每个像素的CN ratio
4. 在100-kb分辨率下估计样本水平的CN ratio
5. 使用HMM进行CN ratio分段以确定边界
6. 使用MAGIC算法平滑单像素CN ratio以去噪
7. 基于CNV谱进行聚类分析识别肿瘤克隆

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 单像素分辨率 | 5 Mb | 用于全局CNV可视化和聚类 |
| 样本水平分辨率 | 100 kb | 用于精细CNV检测 |
| 分段方法 | HMM | Hidden Markov Model分割CNV边界 |
| 平滑算法 | MAGIC | 图像去噪和空间模式增强 |
| 假设 | 二倍体 | CN ratio = 拷贝数/2 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CNV | Copy Number Variation，拷贝数变异 |
| CN ratio | 拷贝数比值，拷贝数除以2（二倍体参考） |
| NeoLoopFinder | 从Hi-C数据检测增强子劫持事件和CNV的工具 |
| HMM | Hidden Markov Model，用于CNV边界分割 |
| MAGIC | Markov Affinity-based Graph Imputation of Cells，用于去噪和平滑 |
| ecDNA | Extrachromosomal DNA，染色体外DNA |

## 复现
- 工具/代码/URL
  - NeoLoopFinder: https://github.com/XiaoTaoWang/NeoLoopFinder
  - EagleC: https://github.com/XiaoTaoWang/EagleC
  - MAGIC: https://github.com/KrishnaswamyLab/MAGIC
  - 代码: https://github.com/wangjuan001/Spatial-ATAC-Hi-C (MIT License)
- 代码片段（关键调用，≤10 行）
```python
from neoloopfinder import calculate_cnv, segment_cnv
# 计算伪批量CNV
cnv_ratio = calculate_cnv(hic_file='pseudobulk.hic', resolution=100000)
# HMM分段
segments = segment_cnv(cnv_ratio)
# 单像素CNV
pixel_cnv = calculate_cnv(pixel_contacts, resolution=5000000)
```

## 生物学意义
CNV是肿瘤基因组不稳定的主要表现，也是肿瘤异质性的重要来源。通过空间分辨的CNV分析，可以：
1. **识别肿瘤克隆**：不同CNV谱代表不同的肿瘤克隆群体
2. **追踪克隆进化**：空间CNV分布揭示肿瘤克隆的地理分布和演化关系
3. **鉴定癌基因扩增**：如本研究中发现的EGFR、MDM2和CDK4扩增
4. **检测ecDNA**：Hi-C图上的条纹模式提示染色体外DNA的存在
5. **临床意义**：CNV模式与肿瘤分级、预后和治疗反应相关

本研究展示了Spatial-ATAC-Hi-C在GBM和星形细胞瘤样本中检测空间CNV的能力，揭示了EGFR/CDK4/MDM2扩增的空间异质性。

## 涉及 Figures
- **Fig. 4a-f** — Spatial-ATAC-Hi-C捕获空间拷贝数差异
- **Fig. 5b** — GBM样本的CNV谱和焦点扩增
- **Fig. 5e-h** — EGFR、MDM2、CDK4扩增的空间分布
- **Extended Data Fig. 7** — 结构变异(SVs)检测
