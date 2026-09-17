# Method: cDNA交联与环化

## 原文（Methods）
> To cross-link cDNA molecules containing aminoallyl-dUTP, add 20 µl of reconstituted BS(PEG)9 in 980 µl of PBS to the sample for 1 h at room temperature. Aspirate and wash the sample with PBS and quench it with 1 M Tris (pH 8.0) for 30 min. Add 10 µl of DNase-free RNase and 5 µl of RNase H in 1× RNase H buffer for 1 h at 37 °C. Prepare a CircLigase reaction mixture and incubate at 60 °C for 1 h.

## 解读

### 意义
将cDNA交联固定在细胞蛋白基质上防止扩散，降解残余RNA，将线性cDNA环化用于后续RCA扩增

### 输入
- 含aminoallyl-dUTP修饰的原位合成cDNA
- BS(PEG)9交联剂、RNase/RNase H、CircLigase II

### 输出
- 交联固定的环状cDNA分子

### 核心步骤
1. BS(PEG)9交联cDNA（室温1小时）— NHS酯与氨基烯丙基-dUTP的伯胺形成共价键
2. 1 M Tris (pH 8.0)淬灭30分钟
3. DNase-free RNase + RNase H降解残余RNA（37°C, 1小时）— 关键步骤，跳过会导致少扩增子
4. 无核酸酶水洗涤去除磷酸盐
5. CircLigase II环化反应（60°C, 1小时）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| BS(PEG)9浓度 | 20 µl in 980 µl PBS | 交联剂工作浓度 |
| 交联时间 | 1 h (RT后)；1 h (RCA后) | 两次交联 |
| Tris淬灭 | 1 M, pH 8.0, 30 min | 终止交联反应 |
| CircLigase II | 1 U µl⁻¹ | 环状连接酶 |
| MnCl2 | 2.5 mM | CircLigase辅因子 |
| Betaine | 0.5 M | 提高连接效率 |
| 环化温度/时间 | 60°C, 1 h | 环化反应条件 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| BS(PEG)9 | 双(琥珀酰亚胺基)九(乙二醇)交联剂，NHS酯双功能团 |
| NHS ester | N-羟基琥珀酰亚胺酯，与伯胺反应形成酰胺键 |
| CircLigase | ATP依赖的单链DNA连接酶，用于cDNA环化 |
| RNase H | 特异性降解RNA:DNA杂交体中的RNA |

## 复现
- 关键试剂：BS(PEG)9 (Thermo 21582), CircLigase II kit (Epicentre CL9025K)
- 注意：BS(PEG)9在DMSO重悬后1个月失效，多次冻融后更短；跳过RNA降解步骤会导致极少扩增子

## 生物学意义
交联步骤是FISSEQ的核心创新之一：通过氨基烯丙基-dUTP和BS(PEG)9将cDNA共价固定在细胞蛋白基质上，防止后续反应中cDNA扩散，保持空间信息。RNA降解步骤去除RNA模板，防止其竞争性抑制CircLigase。环化后的cDNA可进行滚环扩增。

## 涉及 Figures
- **Fig. 1a** — 交联与环化流程示意
- **Fig. 6** — 实验步骤4-8
- **Supplementary Fig. 3** — RNA降解效果
- **Table 3** — 故障排除（交联相关）
