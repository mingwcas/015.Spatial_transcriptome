# Method: Fluorescent Staining and Validation

## 原文（Methods）
> The CODEX imaging with six protein markers—CD21, CD31, CD3, CD90, CD279 and CD19—was conducted following standard PhenoCycler protocols with default settings. Highly multiplexed immunofluorescence imaging on a separate formalin-fixed, paraffin-embedded human tonsil tissue section was performed by sequential immunofluorescence staining on COMET using the FFeX technology previously described by Lunaphore Technologies.

## 解读

### 意义
使用多重免疫荧光成像独立验证spatial-CITE-seq的蛋白质空间分布结果。

### 输入
- 人扁桃体组织切片（邻近切片）
- 6种蛋白质标记物抗体（CD21, CD31, CD3, CD90, CD279, CD19）

### 输出
- 多重免疫荧光图像
- 与spatial-CITE-seq蛋白质表达图谱的比较

### 核心步骤
1. CODEX成像：使用PhenoCycler平台，6种蛋白质标记物（CD21, CD31, CD3, CD90, CD279, CD19）
2. 多重免疫荧光：使用Lunaphore Technologies的COMET平台和FFeX技术
3. 在FFPE人扁桃体组织切片上进行序贯免疫荧光染色
4. 与spatial-CITE-seq结果进行头对头比较

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| CODEX标记物 | CD21, CD31, CD3, CD90, CD279, CD19 | 6种验证抗体 |
| 成像平台 | PhenoCycler / COMET | 多重成像系统 |
| 技术 | FFeX（Lunaphore） | 序贯免疫荧光技术 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CODEX | CO-Detection by indEXing，基于索引的共检测多重成像技术 |
| PhenoCycler | Akoya Biosciences的多重蛋白质成像平台 |
| COMET | Lunaphore Technologies的自动化多重免疫荧光平台 |
| FFeX | Lunaphore的序贯免疫荧光染色技术 |
| FFPE | Formalin-Fixed Paraffin-Embedded，福尔马林固定石蜡包埋 |

## 复现
- 工具/代码/URL
  - Akoya Biosciences PhenoCycler
  - Lunaphore Technologies COMET + FFeX
- 代码片段：N/A（成像实验）

## 生物学意义
独立的多重免疫荧光成像验证了spatial-CITE-seq检测的蛋白质空间分布的准确性。CD21、CD279和CD19主要在生发中心内检测到，T细胞标记物CD90和CD3分布在生发中心周围区域，内皮细胞标记物CD31描绘了血管结构——这些模式与spatial-CITE-seq结果高度一致。

## 涉及 Figures
- **Extended Data Fig. 3** — COMET平台的序贯免疫荧光成像结果
- **Extended Data Fig. 4a** — 6种蛋白质的免疫荧光与spatial-CITE-seq的头对头比较
