# Method: Spatial visualization and downstream analysis

## 原文（Methods）
> “The data can be visualized and further explored using ... ST Viewer ... Alternatively, for more advanced analysis, we recommend using R or Python.” (PDF p.28, Step 157; Fig.5c).

## 解读
### 意义
联合表达矩阵、组织图和坐标进行空间探索与统计分析。
### 输入
unique-gene count矩阵、调整后的spot坐标、3×3配准矩阵、bright-field图。
### 输出
空间表达可视化、区域比较和下游分析结果。
### 核心步骤
1. 将spot计数与坐标/形态图关联。 2. 在ST Viewer中浏览和分析。 3. 复杂分析用R或Python自定义实现。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| Viewer | ST Viewer桌面应用（Linux/Mac/Windows） | 交互式空间探索 |
| 编程环境 | R或Python | 可定制下游分析 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| ST Viewer | 空间表达可视化/分析界面 |
| spot-level matrix | 每空间spot的unique gene count矩阵 |

## 复现
- 工具/代码/URL：https://github.com/jfnavarro/st_viewer；手册 https://github.com/jfnavarro/st_viewer/wiki
- 代码片段：将TSV、坐标和affine matrix导入Viewer；R/Python可进一步分析。

## 生物学意义
把分子信息与组织形态整合，支持区域级空间差异发现；100 μm spot限制单细胞解释。

## 涉及 Figures
- **Fig. 5、Fig. 7** — 分析入口与典型检测分布。
