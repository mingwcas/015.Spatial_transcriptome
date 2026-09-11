# Method: Collection of Gene Sets

## 原文（Methods）
> Cell membrane proteins, which span or embed within the plasma membrane, facilitate communication between cells and the extracellular environment. Both experimental and computational approaches have been employed to identify and predict cell-surface membrane proteins. However, each method has inherent limitations, often resulting in incomplete coverage and false positives46–48. Among the various resources available, we selected the latest and most comprehensive database related to cancer research49. Ligands, receptors, cytokines, and transcription factors were also collected from previously published studies and databases50–54.

## 解读

### 意义
收集用于下游分析的特征基因集（gene sets），包括细胞膜蛋白、配体、受体、细胞因子和转录因子，为细胞类型注释、细胞通讯分析和通路富集分析提供参考资源。

### 输入
- 已发表研究中的配体、受体、细胞因子、转录因子数据库
- 最新、最全面的癌症研究相关数据库

### 输出
- 整理后的各类基因集列表
- 用于后续细胞类型注释和通路分析的参考特征基因

### 核心步骤
1. 收集细胞膜蛋白信息（来自最新癌症研究数据库）
2. 收集配体信息（来自CellPhoneDB等）
3. 收集受体信息
4. 收集细胞因子信息（来自已发表研究）
5. 收集转录因子信息（来自人类转录因子图谱）
6. 整合为统一格式的基因集资源

### 关键参数（本文设置）
| 参数 | 来源 | 含义 |
|------|------|------|
| 膜蛋白 | 最新癌症研究综合数据库 (Hu et al., Nat Cancer 2021) | 细胞表面蛋白 |
| 配体 | CellPhoneDB等数据库 |  |
| 受体 | 已发表研究 |  |
| 细胞因子 | 已发表研究和数据库 |  |
| 转录因子 | Lambert et al. 2018, Ng et al. 2021, Joung et al. 2023 | 人类转录因子图谱 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 配体 (Ligand) | 与受体结合的信号分子 |
| 受体 (Receptor) | 细胞表面或细胞内蛋白，接收信号 |
| 细胞因子 (Cytokine) | 免疫细胞分泌的信号蛋白 |
| 转录因子 (TF) | 调控基因表达的DNA结合蛋白 |

## 复现
参考数据库和文献：
- CellPhoneDB (Efremova et al., Nat Protoc 2020)
- 细胞因子转录调控数据库 (Carrasco Pro et al., Nucleic Acids Res 2018)
- 人类转录因子数据库 (Lambert et al., Cell 2018; Ng et al., Nat Biotechnol 2021; Joung et al., Cell 2023)
- 癌症表面蛋白组数据库 (Hu et al., Nat Cancer 2021)

## 生物学意义
特征基因集是细胞类型注释和空间通讯分析的基础资源。研究中使用scRNA-seq数据鉴定的差异表达基因构建细胞类型特征，用于评估各ST平台与CODEX的空间一致性。

## 涉及 Figures
- **Supplementary Fig. 8** — 从scRNA-seq鉴定的细胞类型标记基因
- **Supplementary Fig. 16** — 空间通路富集分析中使用的差异表达基因
