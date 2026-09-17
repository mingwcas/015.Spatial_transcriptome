# Method: 原位逆转录（RT in situ）

## 原文（Methods）
> RT in situ. The length of RT primers should be <25 bases to prevent self-circularization. We perform RT overnight for most samples, but 1 h is often sufficient for cell monolayers. Random hexamers (24 bases) and poly-dT primers (33 bases) work well across all conditions.

## 解读

### 意义
在细胞内将RNA原位转化为cDNA，同时引入氨基烯丙基-dUTP用于后续交联

### 输入
- 固定透化的细胞/组织样品
- RT反应混合物（含dNTP、aminoallyl-dUTP、RT引物、M-MuLV逆转录酶）

### 输出
- 细胞内原位合成的cDNA，含有氨基烯丙基修饰

### 核心步骤
1. 冰上准备RT混合物（含DEPC-H2O、M-MuLV RT buffer、dNTP、aminoallyl-dUTP、RT引物、RNase inhibitor、M-MuLV逆转录酶）
2. 4°C孵育10分钟促进引物退火
3. 37°C过夜孵育（培养细胞单层1-2小时足够）
4. PBS洗涤

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| RT引物长度 | <25 bases | 防止自环化 |
| Random hexamer引物 | 24 bases | 随机六聚体引物 |
| Poly-dT引物 | 33 bases | 用于polyA+ RNA |
| dNTP终浓度 | 250 µM | 核苷酸浓度 |
| Aminoallyl-dUTP终浓度 | 40 µM | 用于交联的修饰核苷酸 |
| M-MuLV RT浓度 | 5 U µl⁻¹ | 逆转录酶浓度 |
| 孵育温度/时间 | 37°C过夜 | 逆转录反应 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| M-MuLV | Moloney小鼠白血病病毒逆转录酶 |
| Aminoallyl-dUTP | 氨基烯丙基修饰的dUTP，提供伯胺基团用于交联 |
| CircLigase | 环状DNA连接酶，用于cDNA环化 |
| Self-circularization | 引物自身环化，可通过缩短引物长度避免 |

## 复现
- 试剂：M-MuLV RT (Enzymatics P7040L), dNTP (Enzymatics N2050L), Aminoallyl-dUTP (AnaSpec 83203)
- 关键：RT引物长度<25 bases；加入阴性对照（无RT酶）排除自环化

## 生物学意义
原位RT将细胞内RNA转化为cDNA，aminoallyl-dUTP的掺入为后续BS(PEG)9交联提供位点，防止cDNA扩散出细胞。随机六聚体引物可实现全转录组覆盖，poly-dT引物特异性捕获mRNA。

## 涉及 Figures
- **Fig. 1a** — RT引物与cDNA合成示意
- **Fig. 6** — 实验流程步骤2-3
- **Table 3** — 故障排除（RT相关问题）
