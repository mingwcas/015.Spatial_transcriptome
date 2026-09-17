# Method: 样品固定与透化处理

## 原文（Methods）
> FISSEQ library construction in cultured cells or tissue sections. (A) Cultured adherent cells on a glass-bottom dish: Fix the cells using 2 ml of 10% formalin in PBS for 15 min at 25 °C. Wash the cells with 2 ml of PBS three times. Add 2 ml of 0.25% (vol/vol) Triton X-100 in DEPC-PBS for 10 min, or 70% (vol/vol) ethanol for 2 min. (B) Tissue sections on a glass-bottom dish: Mount 10–20-µm-thick formalin-fixed tissue sections onto an RNase-free glass coverslip. Add 200 µl of 0.1% (wt/vol) pepsin in 0.1 N HCl for up to 10–30 min.

## 解读

### 意义
固定细胞/组织以保持细胞形态和RNA空间分布，同时透化使后续反应试剂能够进入细胞内

### 输入
- 培养的贴壁细胞（玻璃底培养皿）或组织切片（10–20 µm厚）

### 输出
- 固定且透化的细胞/组织样品，附着在玻璃底培养皿上

### 核心步骤
1. 用10%福尔马林/PBS固定细胞15分钟（25°C）
2. PBS洗涤3次
3. 透化处理：0.25% Triton X-100（10分钟）或70%乙醇（2分钟）
4. （可选）0.1 N HCl酸处理改善透化
5. 对于组织切片：使用0.1% pepsin/0.1 N HCl消化10–30分钟

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 福尔马林浓度 | 10% (vol/vol) | 固定剂浓度 |
| 固定时间 | 15 min (25°C) | 固定时间 |
| Triton X-100浓度 | 0.25% (vol/vol) | 透化剂浓度 |
| Pepsin浓度 | 0.1% (wt/vol) in 0.1 N HCl | 组织切片透化 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DEPC-treated H2O | 焦碳酸二乙酯处理的水，去除RNase |
| FFPE | 福尔马林固定石蜡包埋组织 |
| PFA | 多聚甲醛，固定剂 |
| pepsin | 胃蛋白酶，用于组织透化 |

## 复现
- 工具/试剂：10% formalin, PBS, Triton X-100, pepsin, HCl
- 注意：温度变化可导致mRNA定位改变，使用温福尔马林直接加入培养基以保持亚细胞结构

## 生物学意义
固定步骤保持细胞形态和RNA空间分布，透化步骤使RT试剂能够进入细胞。Triton X-100比乙醇更好地保持亚细胞结构。FFPE组织和新鲜冷冻切片均可用于FISSEQ。

## 涉及 Figures
- **Fig. 1** — 实验流程示意（步骤1-2）
- **Table 1** — 测试的样品类型
- **Supplementary Fig. 1** — 温度敏感细胞类型的固定
- **Supplementary Fig. 2** — 酸处理透化效果
