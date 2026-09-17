# Method: Tissue Histology and H&E Staining

## 原文（Methods）
> An adjacent tissue section was also requested from the same commercial resource which could be used to perform tissue histology examination using H&E staining. Basically, the fixed tissue slide was first cleaned by DI water, and the nuclei were stained with the alum hematoxylin (Sigma) for 2 minutes. Afterward, the slides were cleaned in DI water again and incubated in a bluing reagent (0.3% acid alcohol, Sigma) for 45 s at room temperature. Finally, the slides were stained with eosin for 2 more minutes. The stained embryo slide was examined immediately or stored at –80°C fridge for future analysis.

## 解读

### 意义
H&E染色提供组织形态学参考，用于将空间组学数据与解剖学结构对应，是空间映射的关键对照。

### 输入
- 固定的组织载玻片
- 蒸馏水（DI water）
- 明矾苏木精（Sigma）
- 0.3%酸酒精（Sigma）
- 伊红

### 输出
- H&E染色的组织载玻片
- 用于形态学参考的图像

### 核心步骤
1. 固定组织载玻片用DI水清洗
2. 明矾苏木精染核2分钟
3. DI水清洗
4. 0.3%酸酒精处理45秒（室温）
5. 伊红染色2分钟
6. 立即镜检或-80°C储存

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 苏木精染色时间 | 2分钟 | 细胞核着色 |
| 酸酒精处理时间 | 45秒 | 苏木精分化 |
| 伊红染色时间 | 2分钟 | 细胞质着色 |
| 储存温度 | -80°C | 长期保存 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| H&E staining | Hematoxylin and Eosin staining，苏木精-伊红染色，标准组织学染色 |
| Alum hematoxylin | 明矾苏木精，碱性染料染细胞核 |
| Eosin | 伊红，酸性染料染细胞质 |
| DI water | 去离子水 |

## 复现
- 工具/代码/URL：Sigma染色试剂
- 关键调用：NA

## 生物学意义
H&E染色提供了解剖学参考，使空间组学数据能够与特定组织结构关联。由于DBiT-seq需要破环组织（消化后收集cDNA），相邻切片的H&E染色是恢复空间定位的关键参考。

## 涉及 Figures
- **Fig. 2A** — H&E image from adjacent tissue section
- **Fig. 3B** — H&E image of mouse embryo brain region
- **Fig. 4B** — H&E staining on adjacent tissue section
