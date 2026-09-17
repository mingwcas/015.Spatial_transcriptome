# Method: RNA Velocity Analysis (Dynamo)

## 原文（Methods）
> To capture the cell transition trajectories at the spatial level, the raw count matrix was established according to the annotated bam file and Dynamo was used to perform RNA velocity analysis with unspliced and spliced RNA transcripts.

## 解读

### 意义
Dynamo是一个基于转录组向量场的分析方法，利用未剪接和剪接RNA的比例来推断细胞未来的状态变化方向，从而预测细胞分化轨迹和命运决定。

### 输入
- 注释后的bam文件（包含每个转录本的空间信息）
- 未剪接（unspliced）和剪接（spliced）转录本计数矩阵
- 细胞注释信息

### 输出
- RNA velocity向量场
- 细胞命运转换轨迹
- 伪时间（pseudotime）信息
- 基因表达动态变化

### 核心步骤
1. 从bam文件构建raw count矩阵
2. 分离spliced和unspliced转录本
3. 使用Dynamo计算RNA velocity
4. 生成velocity streamline plots
5. 预测细胞转换轨迹

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 分析层面 | 空间水平 | 在空间位置层面进行轨迹分析 |
| 轨迹类型 | reaEGC→rIPC→IMN→nptxEX | 神经再生的细胞转换轴 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RNA velocity | RNA速率，通过spliced/unspliced比率预测细胞未来状态 |
| Dynamo | 单细胞转录组向量场分析工具 |
| Spliced transcripts | 已剪接的mRNA |
| Unspliced transcripts | 未剪接的前体mRNA |
| Streamline plot | 流线图，显示向量场方向 |

## 复现
- **工具/代码/URL**: 
  - Dynamo: https://github.com/aristoteleo/dynamo-release
  - 参考文献: Qiu et al., Cell 2022 (doi: 10.1016/j.cell.2021.12.045)
- **代码片段**: 无特定代码（Dynamo标准流程）

## 生物学意义
RNA velocity分析揭示了蝾螈端脑再生过程中细胞状态转换的动态轨迹，发现了reaEGC→rIPC→IMN→nptxEX的分化路径，为理解损伤诱导的神经再生的分子机制提供了重要线索。

## 涉及Figures
- **Fig. 4D** — RNA velocity流线图显示再生区域细胞命运转换
- **Fig. 5F-H** — 发育和再生过程RNA velocity轨迹比较
