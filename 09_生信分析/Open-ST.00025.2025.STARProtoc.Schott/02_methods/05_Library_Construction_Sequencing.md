# Method: Library Construction and Sequencing

## 原文（Methods）
> The second strand cDNA is amplified, adding sequencing adapters and an i7 index per sample. After bead purification and size selection the libraries are ready to be sequenced.

## 解读

### 意义
通过 PCR 扩增第二链 cDNA，添加测序接头和样本索引，构建可测序的文库。

### 输入
- 纯化的第二链 cDNA
- PCR 引物（P5 forward、P7 reverse indexing）
- KAPA HiFi Hotstart Readymix
- Nextera XT Index Kit v2 i7 接头

### 输出
- 大小选择后的测序文库（350-1100 bp）
- 浓度和质量验证结果

### 核心步骤
1. 准备 qPCR 主混合物，确定最佳 PCR 循环数
2. 设置 qPCR 程序：95°C 3分钟，然后 40 个循环（95°C 30秒，60°C 1分钟，72°C 1分钟）
3. 根据 qPCR 结果确定循环数（阈值设为 50% 峰值 DRn，减去 5 个循环）
4. 准备文库扩增混合物，使用不同的 i7 索引
5. 将第二链产物加入扩增混合物，分成 4 管 PCR
6. 运行 PCR（循环数由 qPCR 确定）
7. 合并 PCR 产物，用 Ampure XP 磁珠纯化（1:1 比例）
8. 使用 BluePippin 进行大小选择（350-1100 bp）
9. 用 Qubit 测量浓度
10. 用 BioAnalyzer 分析文库质量

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| qPCR 循环数 | 11-14 (减去 5 后) | 最佳扩增循环数 |
| PCR 温度 | 95°C/60°C/72°C | 变性/退火/延伸温度 |
| 磁珠纯化比例 | 1:1 | Ampure XP 与 PCR 产物比例 |
| 大小选择范围 | 350-1100 bp | 目标片段大小 |
| 测序读长 | Read1: 28-32, Read2: 90+ | 测序 cycles |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| qPCR | 定量 PCR，用于确定最佳扩增循环数 |
| i7 index | 测序索引，用于区分不同样本 |
| BluePippin | 自动化凝胶电泳大小选择系统 |
| BioAnalyzer | 自动化电泳分析系统 |
| PhiX | 测序质量控制的参照样本 |

## 复现
- 工具/代码/URL：Illumina NovaSeq 6000 或其他 Illumina 测序平台
- 测序参数：
```
Read 1: 28-32 cycles
Index 1: 8 cycles
Read 2: 90+ cycles
PhiX spike-in: 1%
Loading concentration: 130 pM (NovaSeq 6000)
```

## 生物学意义
文库构建是将捕获的空间转录组信息转化为可测序形式的关键步骤。qPCR 确定最佳循环数可以避免过度扩增导致的文库复杂度降低。大小选择去除了引物二聚体和小片段干扰。每个样本使用唯一的 i7 索引，使得多样本可以混合测序。测序深度约 500M reads 可以达到中位数 800 UMIs/细胞的检测灵敏度。

## 涉及 Figures
- **Fig. 8** — Open-ST library profiles before and after size selection
