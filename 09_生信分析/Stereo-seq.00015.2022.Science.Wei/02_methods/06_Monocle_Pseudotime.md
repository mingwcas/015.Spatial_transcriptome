# Method: Monocle Pseudotime Analysis

## 原文（Methods）
> For modeling and further clarifying different trajectories on the same section, Monocle2 and Monocle3 were used to perform pseudotime analysis with selected cell types involved in specific developmental or regenerative processes. For modeling trajectories across regeneration stages, RPCA with SCT-normalized data was used to integrate regeneration-related cell types across regeneration stages, and Monocle3 analysis was then performed downstream.

## 解读

### 意义
Monocle通过伪时间（Pseudotime）分析重构细胞发育或分化的时间顺序，将单细胞快照数据转化为动态轨迹，揭示细胞状态转换的时序关系。

### 输入
- 单细胞转录组表达矩阵
- 细胞类型注释
- 空间位置信息（对于同截面分析）
- 时间点信息（跨时间点分析）

### 输出
- 伪时间轨迹
- 细胞状态转换顺序
- 沿轨迹的基因表达动态变化
- 分支点分析（cell fate decisions）

### 核心步骤
1. 数据准备：选择感兴趣细胞类型构建轨迹
2. 降维：使用DDRTree或UMAP进行降维
3. 轨迹构建：Monocle2/3构建伪时间轨迹
4. 轨迹可视化：按细胞类型或伪时间着色
5. 基因动态分析：沿伪时间分析基因表达变化
6. 跨阶段整合：使用RPCA整合不同再生阶段的数据

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 同截面分析工具 | Monocle2 + Monocle3 | 验证轨迹一致性 |
| 跨阶段整合方法 | RPCA + SCT-normalized data | Monocle3分析 |
| 分析轴 | reaEGC→rIPC1→IMN→nptxEX | 再生神经发生轨迹 |
| 分析阶段 | 2, 5, 10, 15, 20, 30, 60 DPI | 再生时间序列 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Pseudotime | 伪时间，重构的发育/分化时间顺序 |
| DDRTree | 降维方法，用于轨迹构建 |
| RPCA | Robust PCA，用于数据整合 |
| Cell fate decision | 细胞命运决定点 |

## 复现
- **工具/代码/URL**: 
  - Monocle2: http://cole-trapnell-lab.github.io/monocle-release/
  - Monocle3: https://cole-trapnell-lab.github.io/monocle3/
  - 参考文献: Qiu et al., Nat Methods 2017; Cao et al., Nature 2019
- **代码片段**: 无特定代码（Monocle标准流程）

## 生物学意义
伪时间分析揭示了蝾螈端脑再生过程中神经干细胞（reaEGC）如何通过中间祖细胞（rIPC）和未成熟神经元（IMN）分化为成熟神经元（nptxEX）。这种分析为理解损伤诱导的神经再生提供了时间维度的分子调控图谱。

## 涉及Figures
- **Fig. 4E** — Monocle2和Monocle3伪时间轨迹分析
- **Fig. 4H-I** — 跨再生阶段的伪时间轨迹
