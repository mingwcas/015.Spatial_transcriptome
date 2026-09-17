# Method: Gene Expression Module Analysis

## 原文（Methods）
> To characterize the molecular dynamics of EGCs during development, we evaluated the expression of composite gene modules defining neural stemness, cell cycle, and translation activity to reveal the proliferative and differentiative potential of EGCs.

## 解读

### 意义
基因表达模块分析通过构建和评估与神经干性、细胞周期和翻译活性相关的复合基因模块，系统性地揭示EGC在发育过程中的分子动态和分化潜能。

### 输入
- 单细胞表达矩阵
- 细胞类型注释
- 预定义的基因模块（神经干性、细胞周期、翻译相关）

### 输出
- 每个细胞/细胞类型的模块评分
- 模块评分的空间分布
- 发育阶段特异性变化
- EGC分化潜能评估

### 核心步骤
1. 定义基因模块：
   - 神经干性模块(NSC module)：Sox2, Vim, Slc1a3, Gfap等
   - 细胞周期模块(Cell cycle module)：细胞周期相关基因
   - 翻译模块(Translation module)：核糖体和翻译相关基因
2. 计算模块评分：对每个细胞计算模块基因的平均表达
3. 空间可视化：展示模块评分的空间分布
4. 时间序列分析：比较不同发育阶段的模块评分变化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 神经干性标记 | Sox2, Vim, Slc1a3, Gfap | EGC特异性标记 |
| 发育早期 | 高NSC、细胞周期、翻译模块评分 | 活跃的干细胞特性 |
| 幼年阶段后 | 模块评分下降，限制在VZ腹侧区域 | ribEGC定位区域 |
| 分析阶段 | St.44, St.54, St.57, Juv., Adult, Meta. | 6个发育阶段 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Gene module | 基因模块，一组功能相关的基因 |
| NSC module | Neural Stem Cell module，神经干细胞模块 |
| Cell cycle module | 细胞周期模块 |
| Translation module | 翻译模块 |
| EGC | Ependymoglial cell，室管膜胶质细胞 |

## 复现
- **工具/代码/URL**: 无特定工具（自定义分析）
- **代码片段**: 无

## 生物学意义
基因模块分析揭示了EGC在发育过程中的分子特征转换：早期EGC高表达神经干性、细胞周期和翻译相关基因，反映活跃的自我更新和分化能力；随着发育进展，这些模块评分下降，EGC转变为静息状态。这些发现为理解EGC在脑发育和再生中的功能转换提供了分子基础。

## 涉及Figures
- **Fig. 2C** — 基因模块评分在发育阶段的变化
- **Fig. 1G-H** — EGC亚型的标记基因表达
