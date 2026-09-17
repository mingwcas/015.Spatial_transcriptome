# Method: Permeabilization and Reverse Transcription

## 原文（Methods）
> Permeabilization is performed to allow the mRNA to diffuse to and hybridize to the capture oligos. Reverse transcription covalently links the capture oligos with their spatial barcode to the captured mRNA.

## 解读

### 意义
通过透化处理使 mRNA 扩散到捕获寡核苷酸位置并杂交，然后通过逆转录将空间条形码与 mRNA 共价连接。

### 输入
- 带有组织切片的捕获区域
- 胃蛋白酶（Pepsin）
- 2× SSC pH 2.5 缓冲液
- 逆转录混合物（SuperScript IV、dNTPs、RiboLock 等）

### 输出
- 带有空间条形码标记的 cDNA-mRNA 杂交分子

### 核心步骤
1. 称量并溶解胃蛋白酶到 2× SSC pH 2.5 中，制备 7 U/mL 储存液
2. 将胃蛋白酶储存液 1:10 稀释到 0.7 U/mL 工作液
3. 37°C 预热透化混合物
4. 每个样本加入 100 μL 透化混合物
5. 37°C 孵育 45 分钟（对于转移性淋巴结）
6. 移除胃蛋白酶溶液
7. 用 RT 缓冲液清洗一次
8. 加入 100 μL RT 混合物
9. 42°C 过夜孵育

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 胃蛋白酶浓度 | 0.7 U/mL | 透化酶工作浓度 |
| 透化温度 | 37°C | 酶活性最适温度 |
| 透化时间 | 45 min | 转移性淋巴组织化时间 |
| RT 温度 | 42°C | 逆转录温度 |
| RT 时间 | 过夜 | 逆转录孵育时间 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Permeabilization | 透化，使细胞膜通透以便 mRNA 扩散 |
| Pepsin | 胃蛋白酶，用于组织透化 |
| Reverse transcription | 逆转录，以 mRNA 为模板合成 cDNA |
| SuperScript IV | 高效逆转录酶 |
| Spatial barcode | 空间条形码，标记 mRNA 的空间位置 |

## 复现
- 工具/代码/URL：标准分子生物学设备
- 试剂配方：
```
胃蛋白酶储存液：7 U/mL in 2× SSC pH 2.5
胃蛋白酶工作液：0.7 U/mL (1:10 稀释)
RT 混合物：SuperScript IV、dNTPs、RiboLock、BSA、DTT
```

## 生物学意义
透化是空间转录组的关键步骤，决定了 mRNA 的捕获效率。不同组织需要不同的透化条件（Table 1）。胃蛋白酶消化细胞外基质，使 mRNA 能够扩散到捕获位点。逆转录将空间信息编码到 cDNA 中，使得后续测序可以追溯每个转录本的空间来源。

## 涉及 Figures
- **Fig. 2** — Tissue section transferral, imaging, and library preparation
