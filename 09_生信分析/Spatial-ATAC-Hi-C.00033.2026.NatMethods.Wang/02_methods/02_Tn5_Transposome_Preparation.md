# Method: Preparation of Tn5 transposome

## 原文（Methods）
> Unloaded Tn5 transposase (cat. no. C01070010) were purchased from Diagenode, and the transposome was assembled following the manufacturer's guidelines. The oligonucleotides (Supplementary Table 1) applied for transposome assembly were: Tn5ME-A, 5′-TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG-3′; Tn5MErev, 5′-/5Phos/CTGTCTCTTATACACATCT-3′; Tn5ME-B, 5′-/5Phos/CATCGGCGTACGACTAGATGTGTATAAGAGACAG-3′

## 解读

### 意义
制备Tn5转座酶复合物用于染色质可及性分析（ATAC-seq部分），实现DNA片段化和测序接头的插入

### 输入
- 未加载的Tn5转座酶（Diagenode, cat. no. C01070010）
- 寡核苷酸序列：
  - Tn5ME-A: 5′-TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG-3′
  - Tn5MErev: 5′-/5Phos/CTGTCTCTTATACACATCT-3′
  - Tn5ME-B: 5′-/5Phos/CATCGGCGTACGACTAGATGTGTATAAGAGACAG-3′

### 输出
- 组装完成的Tn5转座酶复合物（转座体）
- 用于后续原位转座反应

### 核心步骤
1. 购买未加载的Tn5转座酶（Diagenode）
2. 准备寡核苷酸：Tn5ME-A、Tn5MErev、Tn5ME-B
3. 按照制造商指南组装转座体
4. 将寡核苷酸与Tn5转座酶结合形成活性转座复合物
5. 保存组装好的转座体用于后续实验

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Tn5转座酶来源 | Diagenode (C01070010) | 商品化未加载Tn5转座酶 |
| 寡核苷酸纯化方式 | HPLC纯化 | 确保寡核苷酸质量 |
| 转座体组装 | 按制造商指南 | 标准化组装流程 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Tn5转座酶 | 来源于细菌的转座酶，能够切割DNA并插入测序接头 |
| 转座体 | Tn5转座酶与寡核苷酸形成的活性复合物 |
| Tn5ME-A/B | Tn5转座酶识别的mosaic end序列，用于插入测序接头 |
| 5′-/5Phos/ | 5′端磷酸化修饰，用于寡核苷酸的连接反应 |

## 复现
- 工具/代码/URL
  - Tn5转座酶：Diagenode, cat. no. C01070010
  - 寡核苷酸合成：Integrated DNA Technologies (IDT)
  - 组装方案：Diagenode制造商指南
- 代码片段
  ```bash
  # Tn5转座体组装流程（概念性）
  # 1. 准备寡核苷酸溶液（100 μM）
  # 2. Tn5ME-A + Tn5MErev退火形成双链
  # 3. Tn5ME-B + Tn5MErev退火形成双链
  # 4. 退火产物与Tn5转座酶孵育
  # 5. 组装转座体复合物
  ```

## 生物学意义
Tn5转座酶在Spatial-ATAC-Hi-C中发挥关键作用：
- **ATAC-seq功能**：切割开放染色质区域，插入测序接头，用于检测染色质可及性
- **双接头设计**：Tn5ME-A和Tn5ME-B携带不同接头，允许后续区分不同来源的DNA片段
- **原位转座**：在组织切片上原位进行转座反应，保持空间信息

该方法的技术优势：
- 转座效率高，能够快速标记开放染色质区域
- 原位操作保持组织空间结构
- 与Hi-C技术兼容，实现联合分析

局限性：
- Tn5转座酶可能产生序列偏好性
- 转座效率受组织固定和通透化程度影响
- 需要优化转座条件以平衡效率和特异性

## 涉及 Figures
- **Fig. 1a** — Spatial-ATAC-Hi-C实验流程，展示Tn5转座步骤
- **Supplementary Table 1** — 寡核苷酸序列详细信息
