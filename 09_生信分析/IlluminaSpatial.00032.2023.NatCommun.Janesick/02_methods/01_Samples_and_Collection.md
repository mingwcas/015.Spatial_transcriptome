# Method: Samples and Sample Collection

## 原文（Methods）
> Sample #1. A single formalin-fixed, paraffin-embedded (FFPE) breast cancer tissue block (TNM stage T2N1M0, ER+/HER2+/PR−) was collected on 2021-07-26 and obtained from Discovery Life Sciences. Corresponding dissociated tumor cells, fresh frozen in liquid nitrogen, were also sampled from the same biopsy (patient matched). 5 μm sections were taken from the FFPE tissue using a microtome (Thermo Scientific HM355S; MX35 blades). For the Chromium Single Cell Gene Expression Flex (scFFPE-seq) workflow, 25 μm FFPE curls were collected into a tube prior to serial sectioning for Visium CytAssist and Xenium (two replicates of 5 μm sections for each spatial platform), then an additional 25 μm FFPE curl was collected into the same tube reserved for scFFPE-seq. These pooled 25 μm curls (50 μm total) were treated as a single replicate. Another replicate could not be performed due to the large amount of input material required by scFFPE-seq and needing to reserve the same block for multiple technologies. Sample #2. A formalin-fixed, paraffin-embedded (FFPE) breast cancer tissue block (AJCC pathologic stage pT2 pN1a pMX, ER−/HER2+/PR−) was collected on 2009-07-24 and obtained from Discovery Life Sciences. 5 μm sections were taken from the FFPE tissue using a microtome (Thermo Scientific HM355S; MX35 blades).

## 解读

### 意义
确定实验所需的FFPE组织样本来源、病理分型及切片方式，为多平台（scFFPE-seq、Visium、Xenium）整合分析提供统一的组织材料基础

### 输入
- 两例FFPE乳腺癌组织块（Sample #1: ER+/HER2+/PR−; Sample #2: ER−/HER2+/PR+）
- 配对的冻存解离肿瘤细胞（仅Sample #1）

### 输出
- 5 μm组织切片（用于Visium CytAssist和Xenium，每平台2个重复）
- 25 μm FFPE curls（用于scFFPE-seq，共50 μm合并为1个重复）

### 核心步骤
1. 从Discovery Life Sciences获取FFPE乳腺癌组织块及配对冻存细胞
2. 使用切片机（Thermo Scientific HM355S; MX35 blades）切取5 μm连续切片
3. 先收取25 μm curls用于scFFPE-seq，随后连续切片用于Visium和Xenium
4. 再收取25 μm curls与前一份合并，共计50 μm作为scFFPE-seq单重复
5. 保留同一组织块用于三种技术平台，确保空间连续性

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织切片厚度 | 5 μm | 用于Visium和Xenium的空间分析 |
| scFFPE-seq curls厚度 | 2×25 μm（总计50 μm） | 用于单细胞解离 |
| 每平台重复数 | 2（Visium/Xenium），1（scFFPE-seq） | scFFPE-seq因材料限制仅1个重复 |
| 切片机型号 | Thermo Scientific HM355S | 标准病理切片设备 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| FFPE | 福尔马林固定石蜡包埋（Formalin-Fixed Paraffin-Embedded），临床标准组织保存方法 |
| TNM分期 | 肿瘤-淋巴结-转移分期系统，T2N1M0表示肿瘤≤5cm、1-3个淋巴结转移、无远处转移 |
| ER/PR/HER2 | 雌激素受体/孕激素受体/人表皮生长因子受体2，乳腺癌分型关键标志物 |
| FFPE curl | 用切片机卷取的较厚组织切片，用于需要更多起始材料的实验 |
| 连续切片（serial sections） | 从同一组织块依次切取的切片，保证空间连续性 |

## 复现
- 工具/代码/URL：无特定代码；需获取FFPE组织样本及切片设备
- 代码片段：N/A

## 生物学意义
本研究使用两例不同受体分型的乳腺癌FFPE样本，通过连续切片策略将同一组织块分配给三种互补技术平台（scFFPE-seq、Visium、Xenium），确保了数据整合的空间对应性。Sample #1（ER+/HER2+/PR−）用于主要分析，Sample #2（ER−/HER2+/PR+）用于验证和发现罕见边界细胞。FFPE兼容性使该方法可应用于大量存档临床样本。局限性：仅2例样本，且scFFPE-seq因材料需求仅1个重复。

## 涉及 Figures
- **Fig. 1** — 实验设计示意图，展示单个FFPE组织块如何分配给三种互补技术
