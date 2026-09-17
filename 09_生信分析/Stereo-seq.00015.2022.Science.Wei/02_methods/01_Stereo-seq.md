# Method: Stereo-seq (Spatial Enhanced Resolution Omics Sequencing)

## 原文（Methods）
> We performed spatial enhanced resolution omics sequencing (Stereo-seq) to capture spatially resolved single-cell transcriptomes of axolotl telencephalon sections during development and regeneration. Considering the average size of axolotl cells, we prepared cryosections of the adult axolotl telencephalon at 20-µm thickness to capture roughly a single-cell layer of tissue for Stereo-seq analysis on the entire section. Because Stereo-seq is based on DNA nanoball (DNB) sequencing technology, for which each DNB spot on the chip is 220 nm in diameter and the center-to-center distance of two adjacent spots is 500 or 715 nm, we were able to capture transcripts at the sub-cellular level.

## 解读

### 意义
Stereo-seq是一种基于DNA纳米球（DNB）测序技术的高分辨率空间转录组学方法，能够在亚细胞水平捕获转录本，实现真正的单细胞空间分辨率分析。

### 输入
- 20 µm厚度的冰冻切片（蝾螈端脑）
- Stereo-seq芯片（DNB模式）

### 输出
- 空间单细胞转录组数据
- 每个细胞约850个DNB位点
- 平均6291个UMI和1680个基因

### 核心步骤
1. 样本收集：收集发育阶段和再生阶段的蝾螈端脑组织
2. 冰冻切片：制备20 µm厚度的切片以覆盖近乎单细胞层
3. 原位RNA捕获：在Stereo-seq芯片上进行组织加载和原位RNA捕获
4. cDNA扩增：进行cDNA扩增和文库构建
5. 测序：进行高通量测序
6. 数据处理：使用SAW pipeline进行原始测序数据处理

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 20 µm | 近似单细胞层厚度 |
| DNB位点直径 | 220 nm | 每个DNB斑点大小 |
| 相邻DNB中心距 | 500或715 nm | 芯片密度 |
| 每细胞DNB位点数 | ~850 | 单细胞分割基础 |
| 平均UMI/细胞 | 6291 | 检测灵敏度 |
| 平均基因数/细胞 | 1680 | 基因检出率 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DNA nanoball (DNB) | DNA纳米球，Stereo-seq核心技术 |
| UMI | Unique Molecular Identifier，唯一分子标签 |
| Stereo-seq | 空间增强分辨率组学测序 |
| DNB sequencing | DNA纳米球测序技术 |

## 复现
- **工具/代码/URL**: 
  - SAW pipeline: https://github.com/BGIResearch/SAW
  - Stereo-seq分析流程: https://db.cngb.org/stomics/artista/
- **代码片段**: 无（厂商技术）

## 生物学意义
Stereo-seq技术实现了高分辨率的空间转录组分析，使得能够在亚细胞水平解析基因表达的空间分布。这对于理解复杂脑结构中不同细胞类型的空间组织和分子特征至关重要。该技术揭示了蝾螈端脑在发育和再生过程中的细胞类型组成、空间分布和分子动态。

## 涉及Figures
- **Fig. 1** — Stereo-seq技术流程和端脑空间转录组图谱构建
- **Fig. 3** — 再生过程中空间细胞类型动态变化
