# Method: Snakemake Analysis Pipeline

## 原文（Methods）
> Given the raw Xenium data and the curated snRNA-seq reference, we implemented a reproducible Snakemake pipeline to coordinate the above sophisticated analysis on a high-performance cluster. The number of threads and the amount of memory for each task were allocated dynamically, with a limit of 48 threads and 1 TB memory, and the run time was limited to 3 days (72 h). Tasks that failed due to out-of-memory errors were excluded from the results.

## 解读

### 意义
使用Snakemake工作流管理工具协调整个分析流程，确保分析的可重复性和计算资源的高效利用。

### 输入
- 原始Xenium数据
- 整理好的snRNA-seq参考图谱
- 分析配置文件

### 输出
- 完整的分析结果文件
- 中间文件（分割、注释、校正结果）
- 最终可视化数据

### 核心步骤
1. 定义分析规则（Snakefile）
2. 配置资源限制（48线程，1TB内存，72小时）
3. 动态分配计算资源
4. 处理内存错误导致的失败任务
5. 生成完整分析报告

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| max_threads | 48 | 单任务最大线程数 |
| max_memory | 1 TB | 单任务最大内存 |
| timeout | 72 h | 任务超时时间 |
| OOM handling | exclude | 内存溢出任务排除 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Snakemake | 基于Python的工作流管理系统 |
| HPC | 高性能计算集群 |
| OOM | Out of Memory，内存溢出 |

## 复现
- 工具：Snakemake (https://snakemake.readthedocs.io/)
- Pipeline代码：https://github.com/bdsc-tds/xenium_analysis_pipeline

## 生物学意义
可重复的分析流程对于科学研究的严谨性至关重要。Snakemake确保从原始数据到最终结果的每一步都可追溯、可重复，支持复杂的多步骤空间转录组分析。

## 涉及 Figures
- 无直接关联（基础设施方法）

## 关联性说明
本文尚未直接可视化Snakemake流程图，所有结果图表均依赖于此pipeline生成的数据。
