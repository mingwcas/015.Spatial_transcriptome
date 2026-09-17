# Method: Tissue Preparation

## 原文（Methods）
> OCT embedded mouse spleen (mouse CD1 spleen frozen sections, MF-701), colon (mouse CD1 colon frozen sections, MF-311), intestine (CD1 intestine, jejunum frozen sections, MF-308) and kidney (mouse CD1 kidney frozen sections, MF-901) sections were purchased from Zyagen and stored at −80 °C until use. In a typical protocol, OCT tissue blocks were sectioned into 10-µm-thickness sections and placed in the center of poly-l-lysine slides (Electron Microscopy Sciences, 63478-AS) and shipped with dry ice. The human tonsil sections (human tonsil frozen sections, HF-707) were also purchased from Zyagen. Human skin samples were obtained from the Yale Department of Neurology and sectioned into a 10-µm thickness. For human skin sample, a 68-year-old male with a history of bullous pemphigoid in clinical remission, off systemic immunosuppressive or immunomodulatory therapy, was immunized for COVID-19 with the Moderna mRNA vaccine under FDA Emergency Use Authorization as standard of care; biopsies were performed on the immunized and unimmunized skin of the upper arms just below the vaccination site 2 days after the second and third vaccine doses.

## 解读

### 意义
准备多物种（小鼠、人）多组织类型的冷冻切片，为后续空间CITE-seq实验提供高质量组织样本。

### 输入
- OCT包埋的冷冻组织块
- Poly-L-lysine载玻片（EMS, 63478-AS）
- 临床皮肤活检样本

### 输出
- 10 µm厚度的冷冻组织切片，固定在poly-L-lysine载玻片上

### 核心步骤
1. 购买Zyagen的OCT包埋小鼠组织（脾、结肠、小肠、肾）和人扁桃体冷冻切片，-80°C储存
2. 将OCT组织块切成10 µm厚度切片
3. 将切片放置在poly-L-lysine载玻片中心
4. 干冰运输保存
5. 人皮肤样本：68岁男性患者，大疱性类天疱疮缓解期，接受Moderna mRNA COVID-19疫苗注射后2天取活检

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 10 µm | 组织切片厚度 |
| 储存温度 | -80°C | 冷冻组织保存温度 |
| 载玻片 | Poly-L-lysine | 促进组织粘附 |
| 小鼠品系 | CD1 | 使用的小鼠品系 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| OCT | Optimal Cutting Temperature compound，最优切片温度包埋剂 |
| Poly-L-lysine | 多聚赖氨酸，用于增强组织在载玻片上的粘附 |
| Bullous pemphigoid | 大疱性类天疱疮，一种自身免疫性水疱病 |

## 复现
- 工具/代码/URL
  - Zyagen：预制冷冻组织切片（MF-701, MF-311, MF-308, MF-901, HF-707）
  - Electron Microscopy Sciences：Poly-L-lysine载玻片（63478-AS）
- 代码片段：N/A（样本制备）

## 生物学意义
涵盖多种小鼠组织（脾、结肠、小肠、肾）和人组织（扁桃体、脾、胸腺、皮肤），验证了spatial-CITE-seq的广泛适用性。特别地，COVID-19疫苗注射部位皮肤活检展示了该方法在临床免疫学研究中的应用价值。

## 涉及 Figures
- **Fig. 1b** — 小鼠脾、结肠、小肠、肾的空间蛋白质组和转录组聚类
- **Fig. 2a** — 人皮肤活检组织明场图像
- **Extended Data Fig. 5** — 人脾和胸腺的空间CITE-seq映射
