# Method: Application of DNA-Antibody Conjugates to Tissue Slide

## 原文（Methods）
> In order to obtain spatial proteomic information, we incubated the fixed tissue slide with a cocktail of DNA-antibody conjugates prior to microfluidic spatial barcoding. The cocktail was prepared by combining 0.1 mg of each DNA-antibody conjugates (see Table S1). The tissue slide was first blocked with 1% BSA/PBS plus RNase inhibitor, and then incubated with the cocktail for 30 minutes at 4°C. Afterward, the tissue slide was washed 3 times with a washing buffer containing 1% BSA + 0.01% Tween 20 in 1X PBS and one time with DI water prior to attaching the first PDMS microfluidic chip.

## 解读

### 意义
该方法将蛋白质检测引入DBiT-seq技术，通过抗体-DNA结合物实现空间蛋白质组学映射，使DBiT-seq成为真正的多组学技术。

### 输入
- 固定的组织载玻片
- DNA-抗体结合物混合物（Table S1，每种0.1mg）
- 1% BSA/PBS + RNase抑制剂封闭液
- 洗涤缓冲液（1% BSA + 0.01% Tween 20 in 1X PBS）

### 输出
- 结合了DNA-抗体 conjugates的组织载玻片，准备进行空间条码操作

### 核心步骤
1. 制备混合物：每种DNA-抗体结合物0.1mg混合（Table S1）
2. 组织载玻片用1% BSA/PBS + RNase抑制剂封闭
3. 4°C孵育cocktail 30分钟
4. 洗涤缓冲液（1% BSA + 0.01% Tween 20 in 1X PBS）洗3次
5. DI水洗1次
6. 准备安装第一个PDMS微流控芯片

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 每种抗体用量 | 0.1 mg | DNA-antibody conjugates |
| 封闭液 | 1% BSA/PBS + RNase inhibitor | 减少非特异性结合 |
| Cocktail孵育温度 | 4°C | 减少抗体降解 |
| 孵育时间 | 30分钟 | 充分结合 |
| 洗涤缓冲液 | 1% BSA + 0.01% Tween 20 in PBS | 温和洗涤 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DNA-antibody conjugate | 抗体-DNA结合物，类似CITE-seq/Ab-seq技术 |
| Cocktail | 混合物，包含22种蛋白对应的抗体-DNA结合物 |
| Tween 20 | 非离子型表面活性剂，减少非特异性吸附 |

## 复现
- 工具/代码/URL：TotalSeq antibodies (BioLegend, Table S1)
- 关键调用：NA

## 生物学意义
通过引入DNA-antibody conjugates，DBiT-seq实现了mRNA和蛋白质的联合空间检测。本文使用了22种蛋白的抗体套餐，实现了空间多组学映射。这项技术使得研究者可以在同一组织切片上同时获得转录组和蛋白质组的空间信息。

## 涉及 Figures
- **Fig. 1A** — Workflow中包含ADT应用步骤
- **Fig. 2F** — mRNA与蛋白表达相关性分析
