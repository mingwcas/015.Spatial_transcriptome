# Method: Immunofluorescence and Imaging

## 原文（Methods）
> Human prenatal brain tissue sections were incubated at 37 °C for 30 min, washed 1x in 1x PBS for 15 min, fixed with 70% methanol on ice for 10 min, washed 1x in 1x PBS for 5 min, incubated with 70% methanol on ice for 5 min, or fixed with 4% paraformaldehyde for 7 min, washed 3x in 1x PBS for 15 min each, and incubated with normal donkey serum blocking buffer (AB_2337254) at room temperature for 1 hour. Antigen retrieval was performed for the LINE1-ORF1p antibody using Tris/EDTA pH 9.0 buffer solution in a microwave, following the Abcam protocol.

## 解读

### 意义
免疫荧光染色和成像技术在蛋白质水平验证转录组发现，提供DS神经发育异常的形态学证据，支持分子发现的生物学意义。

### 输入
- 产前人脑组织冰冻切片
- 一抗：SOX2, LMNB1, LINE1 ORF1p, TP53, NEUN, ROBO1
- 二抗：Alexa Fluor 488/555/647偶联抗体

### 输出
- 共聚焦显微镜图像（60×油镜）
- 荧光强度定量分析
- 蛋白质表达变化的统计显著性

### 核心步骤
1. 37°C孵育30 min，PBS洗涤
2. 70%甲醇冰上固定10 min（或4% PFA固定7 min）
3. 正常驴血清封闭1小时
4. 一抗孵育（4°C过夜或室温）
5. 二抗孵育（室温，1小时）
6. DAPI复染
7. 共聚焦显微镜（60×1.2油镜）成像
8. Imaris软件进行细胞选择和强度定量
9. ImageJ进行背景扣除和统计分析

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 固定方法 | 70%甲醇 or 4% PFA | 组织固定 |
| 封闭液 | 正常驴血清 | 非特异性结合阻断 |
| 抗原修复 | Tris/EDTA pH 9.0 (LINE1) | 热诱导表位修复 |
| 共聚焦物镜 | 60× 1.2油镜 | Nikon A1R |
| 定量软件 | Imaris, ImageJ | 细胞选择和强度测量 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| IF | Immunofluorescence，免疫荧光 |
| DAPI | 4',6-diamidino-2-phenylindole，细胞核染料 |
| ROI | Region of Interest，感兴趣区域 |

## 复现
- 抗体来源：Abcam, Santa Cruz, Thermo Fisher, Millipore
- 显微镜：Nikon A1R共聚焦显微镜
- 分析软件：Imaris (RRID:SCR_007370), ImageJ (RRID:SCR_003070)

## 生物学意义
免疫荧光验证了关键发现：TP53在DS NPC中显著降低（p=0.006）、ROBO1在DS皮层神经元中显著降低（p=0.017）、LINE1-ORF1在DS SOX2+细胞中显著增加（p=0.022）、LMNB1在DS NPC中显著降低（p=0.0001）。这些验证确认了转录组和蛋白质组发现的生物学意义。

## 涉及 Figures
- **Fig. 2** — ROBO1 immunostaining validation
- **Supplementary Fig. 2** — TP53 and LMNB1 validation
- **Supplementary Fig. 3** — LINE1-ORF1 validation
