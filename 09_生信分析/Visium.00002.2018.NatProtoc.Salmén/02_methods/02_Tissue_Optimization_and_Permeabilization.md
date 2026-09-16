# Method: Tissue optimization and pepsin permeabilization

## 原文（Methods）
> “The conditions for the permeabilization and tissue-removal steps must be optimized whenever a new type of tissue is used.” Cy3-dCTP is added during RT to visualize the cDNA footprint; “a strong and morphologically correct fluorescent print” indicates optimal treatment (PDF pp.5–6; Fig.2; Steps 25–30, 41).

## 解读
### 意义
针对组织类型确定RNA释放与扩散之间的最佳平衡。
### 输入
组织优化array（非条码poly-A probe smear）、组织切片、HBSS/BSA/collagenase或MOB exonuclease预处理、pepsin。
### 输出
532 nm扫描的Cy3-cDNA footprint及最佳pepsin时间/条件。
### 核心步骤
1. 预渗透（多数组织37°C 20 min；MOB 30 min）。 2. 以5、10、15 min等梯度pepsin处理。 3. 含Cy3-dCTP的RT。 4. 去组织后扫描并按信号强度、形态和扩散判定条件。
### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|---|---|---|
| 预渗透 | 37°C，20–30 min | 提高捕获效率 |
| pepsin | 37°C，5–20 min；优化梯度 | 控制通透性 |
| 判定 | strong + morphology-correct | 最佳窗口 |

## 名词/参数/指标
| 名词 | 定义 |
|---|---|
| cDNA footprint | 组织去除后表面荧光cDNA留下的形态印迹 |
| under/over-permeabilized | 信号弱/扩散模糊，分别代表通透不足/过度 |

## 复现
- 工具/代码/URL：扫描仪，532 nm；无需测序。
- 代码片段：不适用。

## 生物学意义
优化减少低捕获和RNA扩散；条件依组织而异，不能直接跨组织照搬。

## 涉及 Figures
- **Fig. 2** — 直接展示优化判据。
