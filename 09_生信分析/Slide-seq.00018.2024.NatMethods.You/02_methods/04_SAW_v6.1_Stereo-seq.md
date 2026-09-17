# Method: SAW v6.1 (Stereo-seq)

## 原文（Methods）
> Stereo-seq data were processed with SAW (v6.1).

## 解读

### 意义
SAW (Sterosep-seq Analysis Workflow)是华大基因开发的Stereo-seq专用分析管道，用于处理基于DNA纳米球（nanoball）技术的空间转录组数据。

### 输入
- 原始FASTQ文件
- Stereo-seq芯片的空间条码信息

### 输出
- 带有高分辨率空间坐标的基因表达矩阵
- 亚微米级分辨率的表达数据

### 核心步骤
1. 解析FASTQ中的Stereo-seq专用条码
2. 使用SAW流程进行数据处理
3. 生成高分辨率的spot-by-gene矩阵
4. 与组织图像对齐

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| SAW version | v6.1 | Stereo-seq专用分析管道 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DNA nanoball (DNB) | DNA纳米球，Stereo-seq的条码载体 |
| sub-micron resolution | 亚微米级分辨率 |

## 复现
- 工具/代码/URL：华大基因SAW管道（随Stereo-seq平台提供）

## 生物学意义
Stereo-seq在原始测序深度下具有最高的捕获效率，但由于强烈的分子横向扩散，其实际分辨率受到影响。在脑组织中观察到特别严重的扩散问题。此外，Stereo-seq对血细胞污染的影响相对较小。

## 涉及 Figures
- **Fig. 2** — 灵敏度比较：原始reads下Stereo-seq总counts最高
- **Fig. 3** — 扩散比较：Stereo-seq在脑组织和OB中扩散严重，但在眼球中控制最佳
- **Fig. 4** — 下游性能：成功识别所有预期细胞亚群
