# Method: Cell-Cell Communication Analysis

## 原文（Methods）
> The communication between cells in the local microenvironment is pivotal for coordinated regeneration responses. To examine cell-cell communication during the early regeneration period, we divided the 2 DPI section into 10 regions according to spatially constrained clustering analysis and predicted potential ligand-receptor interactions in each region.

## 解读

### 意义
细胞间通讯分析通过预测配体-受体相互作用，揭示再生过程中细胞间的信号交流模式，为理解组织再生的分子调控机制提供线索。

### 输入
- 单细胞表达矩阵
- 细胞类型注释
- 细胞空间位置
- 配体-受体数据库

### 输出
- 配体-受体相互作用对
- 每个区域的通讯强度
- 参与的细胞类型
- 涉及的信号通路

### 核心步骤
1. 区域划分：将2 DPI截面分为10个区域（空间约束聚类）
2. 配体-受体对预测：识别每个区域中的配体和受体表达
3. 相互作用评分：计算配体-受体对的相互作用强度
4. 功能富集：分析涉及的信号通路

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 分析截面 | 2 DPI | 早期再生阶段 |
| 区域划分数 | 10个区域 | 空间约束聚类 |
| 主要发现 | VZ区相互作用最强，涉及增殖、细胞迁移、细胞外基质重塑 | 活跃的EGC响应 |
| 关键配体-受体对 | Tnc-Sdc1 | reaEGC与WSN之间的相互作用 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Ligand-receptor interaction | 配体-受体相互作用 |
| TNC | Tenascin-C，细胞外基质糖蛋白 |
| SDC1 | Syndecan-1，跨膜硫酸乙酰肝素蛋白聚糖 |
| VZ | Ventricular Zone，脑室区 |

## 复现
- **工具/代码/URL**: 无特定工具（自定义分析）
- **代码片段**: 无

## 生物学意义
细胞间通讯分析揭示了再生过程中EGC与受伤神经元之间的Tnc-Sdc1相互作用，提示这种信号交流在协调神经再生响应中发挥重要作用。这些发现为理解损伤诱导的神经再生的分子调控机制提供了新视角。

## 涉及Figures
- **Fig. 3G-H** — Tnc和Sdc1配体-受体对的空间分布和相互作用
- **Fig. S11H** — 各区域配体-受体相互作用分析
