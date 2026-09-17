# Method: Tissue Removal and Second Strand Synthesis

## 原文（Methods）
> These steps remove the tissue section from the capture area and denature the mRNA strand from the cDNA-mRNA hybrid. Using random priming, a second cDNA strand is synthesized from the first strand cDNA. The random priming site will later act as a unique molecular identifier.

## 解读

### 意义
去除组织残留并合成第二链 cDNA，为后续 PCR 扩增和测序文库构建做准备。

### 输入
- 完成逆转录的捕获区域
- 组织去除混合物（Tris-HCl、NaCl、SDS、EDTA、Proteinase K）
- 第二链合成混合物（Klenow exo-、randomer、dNTPs）

### 输出
- 去除组织的捕获区域
- 双链 cDNA（含有 UMI 信息）

### 核心步骤
1. 移除 RT 混合物
2. 加入 Exonuclease I 混合物，37°C 孵育 45 分钟（消化未杂交的捕获寡核苷酸）
3. 加入组织去除混合物，37°C 孵育 40 分钟
4. 用核酸酶-free 水清洗三次
5. 用 0.1 N NaOH 清洗三次，每次 5 分钟
6. 用 0.1 M Tris (pH 7.5) 清洗三次
7. 用核酸酶-free 水清洗三次
8. 加入第二链合成混合物，37°C 孵育 2 小时
9. 用 0.1 N NaOH 洗脱第二链产物
10. 用 Ampure XP 磁珠纯化（1.8:1 比例）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| ExoI 孵育时间 | 45 min | 消化未杂交寡核苷酸 |
| 组织去除时间 | 40 min | Proteinase K 消化时间 |
| NaOH 浓度 | 0.1 N | 变性和洗脱浓度 |
| 第二链合成时间 | 2 h | Klenow 聚合时间 |
| 磁珠比例 | 1.8:1 | Ampure XP 纯化比例 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Exonuclease I | 核酸外切酶，消化单链 DNA |
| Proteinase K | 蛋白酶 K，消化蛋白质和组织 |
| Klenow exo- | 大肠杆菌 DNA 聚合酶 I 大片段（无 3'→5' 外切酶活性） |
| Randomer | 随机引物，用于第二链合成，同时作为 UMI |
| Ampure XP beads | 磁珠，用于 DNA 纯化和大小选择 |

## 复现
- 工具/代码/URL：标准分子生物学设备
- 试剂配方：
```
组织去除混合物：
- 100 mM Tris-HCl pH 8.0
- 200 mM NaCl
- 2% SDS
- 5 mM EDTA
- 16 mU/mL Proteinase K

第二链合成混合物：
- 1× NEBuffer-2
- 10 mM randomer
- 1 mM dNTPs
- 0.5 U/mL Klenow exo-
```

## 生物学意义
组织去除步骤释放了捕获的 cDNA，同时去除了可能干扰后续反应的组织残留。第二链合成使用随机引物，这些随机引物的序列成为 UMI（Unique Molecular Identifier），可以用于区分原始 mRNA 分子和 PCR 扩增产生的重复，实现转录本的绝对定量。

## 涉及 Figures
- **Fig. 2** — Tissue section transferral, imaging, and library preparation
