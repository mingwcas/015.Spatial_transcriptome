# Method: Hybridization and Counting (nCounter System)

## 原文（Methods）
> After collection of indexing oligos has been performed, they are hybridized to optical fluorescent barcodes or GeoMx Hyb codes. Then, they are digitally counted using the single-molecule counting nCounter System or analyzed using next generation according to manufacturer's instructions (NanoString, Seattle WA) (16, 17).

## 解读

### 意义
杂交和计数是 DSP 的定量检测环节，将从各 AOI 收集的 indexing oligos 与荧光条码杂交，然后在 nCounter 系统上进行单分子计数，实现对原始信号的高灵敏度数字化读取。

### 输入
- 各 AOI 收集的 indexing oligos（96 孔板）
- GeoMx Hyb codes（光学荧光条码）
- nCounter 系统或 NGS 测序平台

### 输出
- 各靶标在各 AOI 的原始计数（raw counts）
- 数据文件（.dcm 等格式，可导入 GeoMx Data Analysis Suite）

### 核心步骤
1. 将收集的 indexing oligos 与 GeoMx Hyb codes（光学荧光条码）杂交
2. 杂交产物在 nCounter 系统上运行：
   - 分子杂交 → 荧光条码可视化 → 相机成像计数
   - 每个荧光条码对应一个唯一 index，代表一个靶标
3. 或选择下一代测序（NGS）作为检测平台（按厂家说明）
4. 获得每个孔（对应每个 AOI）中各靶标的数字化计数

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 检测平台 | nCounter 系统（主要）/ NGS（备选） | 单分子计数 |
| 读取方式 | 荧光条码成像 | 每个靶标对应唯一彩色条码 |
| 板格式 | 96 孔板 | 每个 AOI 一孔 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| nCounter System | NanoString 单分子计数系统，基于荧光条码杂交和成像 |
| GeoMx Hyb codes | GeoMx 专有的光学荧光条码（对应各靶标 index） |
| NGS | Next Generation Sequencing，下一代测序（可选替代检测方案） |
| Raw counts | 原始计数，尚未进行 QC 和 normalization |

## 复现
- 工具/代码/URL：[NanoString nCounter Analysis System](https://nanostring.com/products/ncounter-systems/)
- GeoMx 蛋白分析：[https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-protein-assays/](https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-protein-assays/)

## 生物学意义
nCounter 系统是 NanoString 的核心专利技术，无需 PCR 扩增或酶切，直接对单分子进行计数，避免了传统 qPCR 的偏好性问题。这一"数字化"计数方式提供了宽动态范围和高度可重复性，特别适合处理高plex 数据。对 DSP 而言，nCounter 的读取为后续的 QC 和归一化提供了原始计数矩阵。

## 涉及 Figures
- **Fig. 1** — DSP assay workflow 中的 hybridization 和 counting 步骤
