# Method: SRT Platform Comparison

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 4 SRT 平台比较
> Comparison of Xenium with SRT platforms. SRT/scRNA-seq gene efficiency ratios of different SRT methods in the hippocampal and thalamic regions.

## 解读

### 意义
空间转录组（SRT）平台比较研究系统性地评估了多种空间转录组技术（MERSCOPE, MERFISH, CosMx, Xenium, HS-ISS, Molecular Cartography）的检测效率、转录本分配准确性和基因特异性，为平台选择提供参考依据。

### 输入
- 多种 SRT 平台的数据（MERSCOPE, MERFISH, CosMx, Xenium, HS-ISS, Molecular Cartography）
- scRNA-seq 参考数据
- 组织区域注释

### 输出
- 检测效率比较
- 转录本分配比例
- 负共表达纯度（NCP）
- 基因效率比

### 核心步骤
1. 收集不同 SRT 平台的数据
2. 对齐 scRNA-seq 参考数据
3. 计算检测效率（SRT/scRNA-seq ratio）
4. 评估转录本分配比例
5. 计算负共表达纯度（NCP）
6. 平台间配对比较

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| MERSCOPE | Vizgen 平台 | 基于 MERFISH 技术 |
| MERFISH | 原始 MERFISH 数据 | Vizgen MERFISH |
| CosMx | NanoString 平台 | FFPE 数据集 |
| Xenium | 10X Genomics 平台 | In situ sequencing |
| HS-ISS | 原位测序 | 杂交测序 |
| Molecular Cartography | Resolve Biosciences | 多重荧光原位杂交 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SRT | Spatial Resolved Transcriptomics，空间转录组 |
| Detection efficiency | 检测效率，转录本/基因检测能力 |
| NCP | Negative Coexpression Purity，负共表达纯度 |
| SRT/scRNA ratio | SRT 与单细胞 RNA-seq 的基因效率比 |
| Transcript assignment | 转录本分配到细胞的比例 |

## 复现
- 工具/代码/URL：https://github.com/Moldia/Xenium_benchmarking v1.2.0
- 数据来源：
  - MERSCOPE: https://vizgen.com/data-release-program/
  - CosMx: https://nanostring.com/products/cosmx-spatial-molecular-imager/ffpe-dataset/
  - Molecular Cartography: https://resolvebiosciences.com/datasets/
  - MERFISH/HS-ISS: 原始发表文献

## 生物学意义
平台比较研究为空间转录组技术的选择提供了科学依据，不同平台在检测效率、空间分辨率和基因覆盖度方面各有优势，需要根据研究目的进行选择。

## 涉及 Figures
- **ED Fig. 4** — 多种 SRT 平台综合比较，包括检测效率、转录本分配和 NCP 等指标
