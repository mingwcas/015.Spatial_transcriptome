# Method: Open-ST Capture Area Generation

## 原文（Methods）
> These steps describe the processing of the NovaSeq 6000 S4 barcoded flow cell from "before you begin" Step 23 to generate ready-to-use capture areas for Open-ST library preparation. Approximately 360 capture areas at 3 × 4 mm can be generated from one NovaSeq 6000 S4 flow cell, however, it is possible to make pieces of different dimensions up to a maximum size of 7 × 89 mm (the uninterrupted sequenced area of the flow cell).

## 解读

### 意义
将 Illumina NovaSeq 6000 测序 flow cell 转化为空间转录组捕获区域，实现低成本、高分辨率的空间条形码捕获。

### 输入
- Illumina NovaSeq 6000 S4 flow cell（已完成条形码测序）
- DraI 酶、Exonuclease I 酶、CIAP 酶
- 3D 打印切割导板
- NaOH、Tris-HCl 等缓冲液

### 输出
- 约 360 个 3×4 mm 捕获区域（从一个 S4 flow cell）
- 每个捕获区域表面带有空间条形码寡核苷酸

### 核心步骤
1. 用核酸酶-free 水清洗 flow cell 三次
2. 准备 DraI 反应混合物，加入每个 lane
3. 37°C 过夜孵育（15-18 小时）
4. 用 80% 乙醇和水清洗 flow cell
5. 准备 Exonuclease I 混合物，孵育 45 分钟
6. 打开 flow cell，分离玻璃层
7. 用 0.1 M NaOH 变性获得单链捕获寡核苷酸
8. 使用 3D 打印切割导板和玻璃切割器将 flow cell 切割成小块捕获区域
9. 将捕获区域粘贴到板封膜上便于操作

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| DraI 浓度 | 2 U/mL | 限制性内切酶浓度 |
| DraI 孵育时间 | 15-18 h | 酶切时间 |
| ExoI 孵育时间 | 45 min | 消化未杂交的单链寡核苷酸 |
| NaOH 浓度 | 0.1 M | 变性浓度 |
| 捕获区域尺寸 | 3×4 mm | 标准捕获区域大小 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Flow cell | Illumina 测序芯片，含有规则排列的纳米孔 |
| Spatial barcode | 空间条形码，用于标记 mRNA 的空间位置 |
| Capture oligos | 捕获寡核苷酸，poly-dT 序列用于捕获 mRNA |
| DraI | 限制性内切酶，用于切割测序接头 |
| Exonuclease I | 核酸外切酶，消化未杂交的单链 DNA |

## 复现
- 工具/代码/URL：https://github.com/rajewsky-lab/openst
- 3D 打印文件：https://rajewsky-lab.github.io/openst
- 代码片段：
```bash
# 测序 flow cell 上的条形码
openst flowcell_map \
  --bcl-in /path/to/fc/bcl \
  --tiles-out /path/to/fc_tiles \
  --crop-seq 5:30 \
  --rev-comp
```

## 生物学意义
Open-ST 通过 repurposing Illumina 测序 flow cell，以极低成本（约 $2/捕获区域）实现亚细胞分辨率（0.6 μm）的全转录组空间捕获。这种方法使空间转录组技术更加可及，适用于任何组织类型，包括临床样本。

## 涉及 Figures
- **Fig. 1** — Flow cell opening and capture area generation
