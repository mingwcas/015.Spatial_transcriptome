# Method: In Situ Hybridization with Padlock Probes (Validation)

## 原文（Methods）
> To validate the expression of marker genes, we performed in-situ hybridization and imaging following a simplified version of targeted ExSeq. More specifically, we used 4 fixed barcode regions for distinct fluorescent probes (FAM6, CY3, TXRED, CY5) so we could detect at most 4 genes at the same time without performing muli-round imaging for in-situ sequencing.

## 解读

### 意义
原位杂交验证用于确认空间转录组数据中检测到的标记基因表达模式，是独立的验证实验。

### 输入
- 组织切片
- 设计好的padlock探针
- 荧光标记探针

### 输出
- 标记基因的空间表达模式图像
- 验证转录组数据的准确性

### 核心步骤
1. 组织切片准备（10 µm厚）
2. 4%多聚甲醛固定
3. 70%冷乙醇渗透（-20°C过夜）
4. Padlock探针杂交（37°C过夜）
5. SplintR连接
6. RCA扩增（30°C过夜）
7. 荧光探针杂交
8. 共聚焦显微镜成像

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Section thickness | 10 µm | 切片厚度 |
| Fixation | 4% formaldehyde, 15 min | 固定条件 |
| Permeabilization | 70% EtOH, -20°C overnight | 渗透条件 |
| Padlock probe conc. | 5 nM per probe | 探针浓度 |
| Hybridization | 37°C overnight | 杂交温度 |
| RCA | 30°C overnight, Phi29 enzyme | 滚环扩增 |
| Imaging | Nikon A1 confocal, 10X objective | 成像系统 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Padlock probe | 锁式探针，用于原位测序 |
| RCA | Rolling Circle Amplification，滚环扩增 |
| ExSeq | Expansion Sequencing，扩展测序 |

## 复现
- 详细protocol：dx.doi.org/10.17504/protocols.io.5qpvo379dv4o/v1

## 生物学意义
通过原位杂交验证了Slc17a7、Ptgds和Pmel等标记基因的空间表达模式，为空间转录组数据的准确性提供了独立验证。

## 涉及 Figures
- **Supplementary Figure 9-11** — 标记基因原位杂交验证
