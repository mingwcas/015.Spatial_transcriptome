# 分区测序 (Partition Sequencing)

## 原文 (Methods)

To obtain a spot density that is high enough to yield statistically significant RNA localization, and yet sufficiently low for discerning individual molecules, we developed partition sequencing, in which preextended sequencing primers are used to reduce the number of molecular sequencing reactions through random mismatches at the ligation site. Progressively longer sequencing primers result in exponential reduction of the observed density, and the sequencing primer can be changed during imaging to detect amplicon pools of different density.

## 解读

### 意义
分区测序是解决高密度扩增产物成像难题的关键创新。通过控制测序引物的长度，可以指数级地降低观察到的分子密度，从而在保持统计显著性的同时，能够分辨单个分子。

### 输入
- 高密度的 cDNA 扩增产物
- 不同长度的预延伸测序引物

### 输出
- 不同密度的扩增产物池
- 可分辨的单分子信号

### 核心步骤
1. **引物设计**：设计不同长度的预延伸测序引物
2. **随机错配**：通过在连接位点引入随机错配来减少分子测序反应数量
3. **密度控制**：较长的测序引物导致观察到的密度呈指数级降低
4. **动态调整**：在成像过程中可以更换测序引物以检测不同密度的扩增产物池

### 关键参数
- 引物长度：1-4 个碱基的延伸
- 密度降低比例：1/4, 1/16, 1/256
- 可检测的扩增产物池：不同密度

## 名词/参数/指标

| 术语 | 定义 |
|------|------|
| Partition Sequencing | 分区测序，通过控制引物长度来调节分子密度 |
| 预延伸测序引物 | 比标准引物更长的测序引物 |
| 随机错配 | 在连接位点引入的碱基不匹配 |
| 密度降低因子 | 4^n，其中 n 是引物延伸的碱基数 |

## 复现

### 所需试剂
- 测序引物（不同长度）
- 连接酶
- 荧光标记的连接子

### 所需设备
- 荧光显微镜
- 共聚焦显微镜

## 生物学意义

分区测序使得在低放大倍数和宽场模式下检测基因表达模式成为可能，这对于：
- 组织水平的空间转录组学
- 高通量筛选
- 多尺度成像

具有重要应用价值。

## 涉及 Figures

- **Fig. 2A**: 分区测序原理示意图
- **fig. S5**: SOLiD 连接测序细节
