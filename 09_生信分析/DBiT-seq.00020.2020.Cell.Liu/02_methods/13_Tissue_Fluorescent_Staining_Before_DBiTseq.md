# Method: Tissue Fluorescent Staining Before DBiT-seq

## 原文（Methods）
> Fluorescent staining of tissue sections with either common nucleus staining dyes or fluorescent labeled antibodies can be performed before the DBiT-seq to facilitate the identification of tissue region of interest. After the DBiT-seq fixation procedure with formaldehyde, the whole tissue was permeabilized with 0.5% Triton X-100 in PBS for 20 minutes and cleaned with 1X PBS for three times. Working solution mixture of DAPI and phalloidin (FITC labeled) were added on top of the tissue and then incubate at room temperature for 20 minutes. After washing thrice with 1X PBS, tissue sections were blocked with 1% BSA for 30 minutes. Finally, antibody with fluorescent labels (here we use P2RY12) were added and incubated at room temperature for 1 hour. Images of the tissue were taken using EVOS microscope (Thermo Fisher EVOS fl), using 10 x objective. Filters used were DAPI, GFP and RFP. DBiT-seq barcoding procedure could be continued after staining.

## 解读

### 意义
该方法展示在DBiT-seq前进行荧光染色的可行性，允许研究者在空间条码操作前选择感兴趣区域并进行细胞分割验证。

### 输入
- 甲醛固定后的组织载玻片
- DAPI（细胞核染料）
- Phalloidin-FITC（肌动蛋白染料）
- 荧光标记抗体（如P2RY12）
- 1% BSA封闭液

### 输出
- 荧光染色的组织图像，用于区域选择和细胞分割

### 核心步骤
1. 0.5% Triton X-100 PBS透化20分钟
2. 1X PBS洗3次
3. DAPI + Phalloidin-FITC混合液孵育20分钟（室温）
4. 1X PBS洗3次
5. 1% BSA封闭30分钟
6. 荧光标记抗体（P2RY12）孵育1小时（室温）
7. 1X PBS洗3次
8. EVOS显微镜10倍镜成像（DAPI, GFP, RFP滤光片）
9. 可继续DBiT-seq流程

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 透化剂 | 0.5% Triton X-100 | 20分钟 |
| DAPI/Phalloidin孵育 | 20分钟（室温） | 核和细胞骨架染色 |
| 抗体孵育 | 1小时（室温） | P2RY12标记小胶质细胞 |
| 成像放大倍数 | 10× | 整体组织视图 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DAPI | 4',6-diamidino-2-phenylindole，蓝色荧光DNA染料 |
| Phalloidin-FITC | 绿色荧光标记的鬼笔环肽，结合肌动蛋白丝 |
| P2RY12 | 小胶质细胞特异性G蛋白偶联受体 |

## 复现
- 工具/代码/URL：EVOS显微镜（Thermo Fisher）
- 关键调用：NA

## 生物学意义
这种组合方案允许在同一组织切片上进行形态学成像（DBiT-seq前）和空间组学分析。荧光染色帮助识别组织区域和进行细胞分割，使DBiT-seq像素可以与特定细胞类型关联。这对于10μm像素大小的分析特别有价值，因为此时像素接近单细胞级别。

## 涉及 Figures
- **Fig. S8** — DBiT-seq与免疫荧光染色结合
