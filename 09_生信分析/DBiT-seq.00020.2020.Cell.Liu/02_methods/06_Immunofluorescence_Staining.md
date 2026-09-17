# Method: Immunofluorescence Staining

## 原文（Methods）
> Immunofluorescence staining was performed either on the same tissue slide or an adjacent slide to yield validation data. Three fluorescent-labeled antibodies listed below were used for visualizing the expression of three target proteins: Alexa Fluor 647 anti-mouse CD326 (Ep-CAM) Antibody, Alexa Fluor 488 anti-mouse Panendothelial Cell Antigen Antibody, PE anti-P2RY12 Antibody. The procedure to stain the mouse embryo tissue slide is as follows. (1) Fix the fresh frozen tissue sections with 4% Formaldehyde for 20 mins, wash three times with PBS. (2) Add 1% bovine serum albumin (BSA) in PBS to block the tissue and incubate for 30 mins at RT. (3) Wash the tissue with PBS for three times. (4) Add the mixture of three antibodies (final concentration 25 μg/mL in 1% BSA, PBS) to the tissue, need around 50 μL. Incubate for 1 hour in dark at RT. (5) Wash the tissue with PBS for three times, with 5 mins washing each time. (6) Dip the tissue in water shortly and air dry the tissue. (7) Image the tissue using EVOS (Thermo Fisher EVOS fl), at a magnification of 10 x. Filters used are Cy5, RFP and GFP.

## 解读

### 意义
免疫荧光染色用于验证DBiT-seq检测的蛋白质表达的空间分布，提供独立的技术验证。

### 输入
- 新鲜冷冻组织切片
- Alexa Fluor 647 anti-mouse CD326 (Ep-CAM) Antibody
- Alexa Fluor 488 anti-mouse Panendothelial Cell Antigen Antibody
- PE anti-P2RY12 Antibody
- 1% BSA/PBS封闭液

### 输出
- 免疫荧光染色的组织图像
- 用于与DBiT-seq结果对比的验证数据

### 核心步骤
1. 4%甲醛固定20分钟，PBS洗3次
2. 1% BSA/PBS封闭30分钟（室温）
3. PBS洗3次
4. 混合三种抗体（终浓度25μg/mL in 1% BSA/PBS），约50μL，室温暗处孵育1小时
5. PBS洗3次，每次5分钟
6. 短浸水后空气干燥
7. EVOS显微镜10倍镜下成像（Cy5, RFP, GFP滤光片）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 抗体浓度 | 25 μg/mL | 最佳染色浓度 |
| 封闭液 | 1% BSA in PBS | 减少非特异性结合 |
| 孵育时间 | 1小时（室温，暗处） | 抗体结合时间 |
| 洗涤 | PBS 3次×5分钟 | 去除未结合抗体 |
| 成像放大倍数 | 10× | 整体组织视图 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Immunofluorescence | 免疫荧光，使用荧光标记抗体检测蛋白 |
| Ep-CAM | 上皮细胞粘附分子，pan-epithelial marker |
| PECA | Pan-endothelial cell antigen，内皮细胞marker |
| P2RY12 | 小胶质细胞marker |

## 复现
- 工具/代码/URL：EVOS显微镜（Thermo Fisher）
- 关键调用：NA

## 生物学意义
免疫荧光染色提供了空间蛋白表达的独立验证方法。与DBiT-seq的蛋白检测结果对比，可以验证DBiT-seq多组学数据的可靠性。文中使用Ep-CAM、PECA和P2RY12分别标记上皮细胞、内皮细胞和小胶质细胞。

## 涉及 Figures
- **Fig. 3E** — Validation by immunofluorescence staining
- **Fig. S3D** — EpCAM immunostaining validation
