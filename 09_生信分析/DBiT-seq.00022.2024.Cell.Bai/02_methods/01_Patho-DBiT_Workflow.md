# Method: Patho-DBiT Workflow

## 原文（Methods）
> Patho-DBiT integrates in situ polyadenylation, microfluidic in tissue barcoding, and computational innovations to decode rich RNA biology inherent in FFPE samples. The platform capitalizes on RNA fragmentation naturally occurring in FFPE specimens and appends poly(A) tails to a broad spectrum of RNA species, thereby overcoming traditional barriers associated with FFPE samples and even outperforming the assays conducted with frozen tissues.

## 解读

### 意义
解决临床FFPE组织样本中RNA降解和交联问题，实现空间转录组学分析

### 输入
- FFPE组织切片
- 微流控芯片
- DNA条形码引物
- 逆转录试剂

### 输出
- 空间转录组数据
- 多种RNA类型的空间表达谱
- 组织空间位置信息

### 核心步骤
1. FFPE组织脱蜡和去交联
2. 组织透化
3. 酶促原位多聚腺苷酸化
4. 逆转录合成cDNA
5. 微流控空间条形码标记
6. 组织裂解和cDNA提取
7. cDNA纯化、模板转换和PCR扩增
8. 核糖体RNA去除、文库制备和测序

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 像素大小 | 10-20 μm | 空间分辨率 |
| 测序深度 | 高深度 | 覆盖全转录组 |
| 组织类型 | FFPE | 临床存档样本 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| FFPE | 福尔马林固定石蜡包埋组织 |
| 原位多聚腺苷酸化 | 在组织中为RNA添加poly(A)尾 |
| 微流控条形码 | 使用微流控芯片进行空间编码 |
| Patho-DBiT | 病理兼容的确定性组织条形码技术 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
该方法使临床存档的FFPE组织样本能够进行空间转录组学分析，为回顾性研究和临床病理学研究提供了新的可能性。

## 涉及 Figures
- **Fig. 1** — Patho-DBiT workflow and spatial whole transcriptome mapping of mouse embryo
