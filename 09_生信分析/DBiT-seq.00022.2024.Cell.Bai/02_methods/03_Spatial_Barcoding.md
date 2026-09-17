# Method: Spatial Barcoding with Microfluidic Devices

## 原文（Methods）
> Spatial barcoding with microfluidic devices. The platform capitalizes on RNA fragmentation naturally occurring in FFPE specimens and appends poly(A) tails to a broad spectrum of RNA species, thereby overcoming traditional barriers associated with FFPE samples.

## 解读

### 意义
使用微流控芯片对组织中的RNA进行空间编码，保留空间位置信息

### 输入
- 带有poly(A)尾的RNA分子
- 微流控芯片
- DNA条形码引物

### 输出
- 带有空间条形码的cDNA分子
- 空间位置信息

### 核心步骤
1. 微流控芯片设计与制造
2. DNA条形码退火
3. 微流控通道加载条形码引物
4. 逆转录过程中引入空间条形码
5. 空间位置编码

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 设备规格 | 10-20 μm像素 | 空间分辨率 |
| 条形码类型 | 确定性条形码 | 唯一标识每个像素 |
| 通道数量 | 多通道 | 覆盖组织区域 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 微流控设备 | 微米级流体控制芯片 |
| 确定性条形码 | 预先设计的唯一编码序列 |
| 空间像素 | 组织上的最小分析单位 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
该方法实现了RNA分子的空间定位，使研究者能够在组织背景下理解基因表达模式。

## 涉及 Figures
- **Fig. 1** — Patho-DBiT workflow and spatial whole transcriptome mapping of mouse embryo
