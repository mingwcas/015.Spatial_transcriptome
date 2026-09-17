# Method: CellChat v1.6.1 (Cell Communication Analysis)

## 原文（Methods）
> Cell communication analysis was then performed on spots with distinct annotated cell types, using methods including Cellchat (v1.6.1), CellPhoneDB (v4). Cellchat used the CellChatDB database of the mouse, creating cellchat objects based on annotation information, and employed the default 'Trimean' statistical method.

## 解读

### 意义
CellChat是一种基于配体-受体数据库推断细胞间通讯的算法，本研究用于分析不同空间转录组技术检测到的细胞类型之间的通讯模式。

### 输入
- 细胞类型注释结果
- 表达矩阵
- CellChatDB小鼠数据库

### 输出
- 配体-受体相互作用对
- 细胞通讯网络
- 通讯强度矩阵

### 核心步骤
1. 创建CellChat对象
2. 使用CellChatDB数据库进行配体-受体分析
3. 推断细胞间通讯
4. 可视化通讯网络

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| CellChat version | v1.6.1 | 细胞通讯分析方法版本 |
| Database | CellChatDB (mouse) | 配体-受体数据库 |
| Statistical method | Trimean | 默认统计方法 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Ligand-receptor interaction | 配体-受体相互作用 |
| CellChatDB | 细胞通讯数据库 |

## 复现
- 工具/代码/URL：https://github.com/sqjin/CellChat

## 生物学意义
本研究未发现跨平台一致性的细胞通讯结果，表明细胞通讯分析的稳定性和可重复性仍需提高。

## 涉及 Figures
- **Supplementary Figure 20** — 细胞通讯分析结果
