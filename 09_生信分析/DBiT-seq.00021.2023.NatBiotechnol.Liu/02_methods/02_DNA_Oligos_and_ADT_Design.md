# Method: DNA Oligos and ADT Design

## 原文（Methods）
> DNA oligos used were all synthesized by Integrated DNA Technologies with high-performance liquid chromatography (HPLC) purification. All DNA oligos received were dissolved in RNase-free water at a 100 µM concentration and stored at −20 °C until use. All the DNA oligos used are listed in Supplementary Table 2. The barcode A and B oligos are listed in Supplementary Table 1. Barcode A contains three functional regions: a poly(T) region, a spatial barcode region and a ligation linker region. Poly(T) region hybrids with poly(A) tail of mRNA serve as the RT primer. The spatial barcode defines the row locations, and the ligation linker region was to be ligated with barcode B. Barcode B includes four functional regions: one ligation linker region, a spatial barcode region, a UMI region and a PCR primer region. The ligation linker region was to be ligated to barcode A. The spatial barcode region shows the column locations. Barcode B was also functionalized with 5′ biotin. ADTs for membrane proteins were purchased from BioLegend and are listed in Supplementary Table 2. Three antibody cocktail products are 273 antibodies cocktail for humans with nine isotype control antibodies (cat. no. 99502) and 189 antibodies cocktail for mice with nine isotype control antibodies (cat. no. 99833).

## 解读

### 意义
设计并制备空间条码DNA寡核苷酸和抗体衍生标签（ADT），实现蛋白质和mRNA的空间共索引。

### 输入
- IDT合成的HPLC纯化DNA寡核苷酸
- BioLegend抗体鸡尾酒（人273-plex / 小鼠189-plex）

### 输出
- Barcode A：含poly(T)、空间条码（行位置）、连接子区域
- Barcode B：含连接子区域、空间条码（列位置）、UMI区域、PCR引物区域、5'生物素修饰
- ADT cocktail：人273种/小鼠189种抗体衍生标签

### 核心步骤
1. Barcode A设计：poly(T)区域与mRNA/ADT的poly(A)尾杂交作为RT引物，空间条码定义行位置，连接子区域用于与Barcode B连接
2. Barcode B设计：连接子区域连接Barcode A，空间条码定义列位置，UMI用于分子去重，PCR引物区域用于扩增，5'生物素用于链霉亲和素捕获
3. ADT购买：BioLegend的人273-plex（cat. 99502）和小鼠189-plex（cat. 99833）抗体鸡尾酒
4. DNA寡核苷酸溶解于RNase-free水中，100 µM浓度，-20°C储存

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Barcode A数量 | 50 | 行条码数量 |
| Barcode B数量 | 50 | 列条码数量 |
| ADT浓度 | 100 µM | DNA寡核苷酸储存浓度 |
| 人ADT panel | 273种抗体 | 人组织蛋白检测panel |
| 小鼠ADT panel | 189种抗体 | 小鼠组织蛋白检测panel |
| 纯化方式 | HPLC | 高效液相色谱纯化 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ADT | Antibody-Derived Tag，抗体衍生DNA标签，将蛋白质检测转化为测序 |
| Barcode A | 行条码，含poly(T)和空间行位置信息 |
| Barcode B | 列条码，含空间列位置、UMI和PCR引物 |
| UMI | Unique Molecular Identifier，唯一分子标识符，用于去重 |
| Poly(A) tail | mRNA 3'端的腺苷酸尾，被poly(T)捕获 |
| Isotype control | 同型对照抗体，用于评估非特异性结合 |

## 复现
- 工具/代码/URL
  - IDT（Integrated DNA Technologies）：DNA寡核苷酸合成
  - BioLegend：ADT抗体鸡尾酒（cat. 99502, 99833）
- 代码片段：N/A（试剂制备）

## 生物学意义
Barcode A/B的二维组合设计使50×50=2500个空间像素点各拥有唯一地址码，实现组织内蛋白质和转录组的空间共定位。ADT将蛋白质检测转化为DNA测序，使高通量蛋白质组学与转录组学在同一组织切片上同步进行。

## 涉及 Figures
- **Extended Data Fig. 1a** — ADT结构示意图（PCR handle 21bp + antibody barcode 15bp + poly-A 32bp）
- **Extended Data Fig. 1** — Barcode A/B的功能区域和连接过程
