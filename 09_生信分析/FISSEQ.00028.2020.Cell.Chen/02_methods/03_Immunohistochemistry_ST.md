# Method: Immunohistochemistry of Spatial Transcriptomics

## 原文（Methods）
> Immunohistochemistry was performed on two extra sections adjacent to the section used for sequencing. After fixation in 4% ice-cold paraformaldehyde (PFA) for 20 min and a wash with PBS, we performed antigen retrieval by microwave boiling the tissue 3 times in 10 mM sodium citrate at pH 6.0. After cooling down to room temperature for 20 min, brain tissues were washed and blocked in TBS-buffer solution containing 0.5% Triton X-100 and 5% normal goat serum for 2h. The serum-blocked tissues were then stained with mouse Alexa Fluor 488 anti-Aβ1-16 antibody, 6E10 at 4°C overnight, and guinea pig anti-NeuN antibody and rabbit anti-Gfap antibody in blocking buffer at 4°C overnight. The immuno-stained tissues were then incubated with goat Alexa 568 anti-guinea pig IgG (H+L) antibody and goat Alexa 647 anti-rabbit IgG (H+L) antibody for 1.5 h at RT. After incubation with DAPI and mounting with mowiol, imaging was carried out on Zeiss Axio Scan.Z1 slidescanner using a 20X objective.

## 解读

### 意义
免疫组化用于在ST切片的相邻切片上获取Aβ斑块、神经元、星形胶质细胞和细胞核的蛋白水平空间信息，为每个TD提供病理学和细胞学注释。

### 输入
- ST切片的相邻冠状切片（10 μm）
- 一抗：6E10（Aβ）、anti-NeuN（神经元）、anti-GFAP（星形胶质细胞）
- 二抗：Alexa 568、Alexa 647
- DAPI（细胞核）

### 输出
- Aβ免疫荧光图像
- GFAP免疫荧光图像
- NeuN免疫荧光图像
- DAPI核染色图像
- 每个TD的5个量化参数（均值、中位数、总和、标准差、阳性面积百分比）

### 核心步骤
1. 4% PFA冰上固定20分钟
2. 10 mM柠檬酸钠（pH 6.0）微波抗原修复3次
3. 0.5% Triton X-100 + 5%正常山羊血清封闭2小时
4. 一抗4°C过夜孵育（6E10、anti-NeuN、anti-GFAP）
5. 二抗室温孵育1.5小时
6. DAPI染色和Mowiol封片
7. Zeiss Axio Scan.Z1载玻片扫描仪20X成像

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| PFA浓度 | 4% | 固定液浓度 |
| 抗原修复 | 10 mM柠檬酸钠, pH 6.0, 微波3次 | 抗原表位暴露 |
| 封闭液 | 0.5% Triton X-100 + 5% NGS | 减少非特异性结合 |
| 一抗孵育 | 4°C, 过夜 | 一抗结合条件 |
| 成像深度 | 16-bit | 允许宽范围强度值 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 6E10 | 抗Aβ1-16单克隆抗体，识别淀粉样斑块 |
| GFAP | 胶质纤维酸性蛋白，星形胶质细胞活化标记 |
| NeuN | 神经元核抗原，神经元标记 |
| DAPI | 4',6-二脒基-2-苯基吲哚，DNA荧光染料 |
| Ab index | Aβ指数，TD内像素强度的标准差 |

## 复现
- 工具/代码/URL
  - Fiji: https://fiji.sc/
  - Zeiss Axio Scan.Z1
- 代码片段
```groovy
// Fiji groovy script - 图像处理和分析
// 手动对齐HE和Cy3-spot图像
// 使用Fiji "Landmark correspondences" 插件
// 计算每个TD的5个免疫染色量化参数
```

## 生物学意义
免疫组化为ST数据提供了关键的病理学背景，使研究者能够将转录组变化与Aβ沉积程度直接关联。通过专家评估验证，像素强度标准差是Aβ负荷的最佳代表指标，而阳性面积百分比最适合GFAP、DAPI和NeuN的量化。

## 涉及 Figures
- **Fig. 1A** — 实验设计示意
- **Fig. 2A-C** — Aβ免疫染色和量化
- **Figure S2** — Aβ沉积和星形胶质细胞增生
