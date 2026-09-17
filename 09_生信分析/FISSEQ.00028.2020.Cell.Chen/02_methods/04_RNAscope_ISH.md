# Method: Multiplexing RNAscope and Immunohistochemistry

## 原文（Methods）
> OCT-embedded hemispheres of 3 AppNL-G-F mice at 18-month of age were cryosectioned coronally into 14 μm and layered onto SuperFrost Plus glass slides. RNAscope experiments were performed using the Manual Fluorescent Multiplex kit v1 (Advanced Cell Diagnostics, Newark, CA) following manufacturer's recommendations with minor adjustments. Briefly, after fixation and protease digestion, probe hybridization was carried out at 40°C for 2 h with the indicated probe sets. After amplification steps to obtain the RNAscope signals, we immediately performed immunohistochemistry to acquire the immunofluorescence picture of amyloid-beta plaques in the tissues. After immunostaining, sections were incubated in 1X TrueBlack solution for 30 s to reduce lipofuscin autofluorescence. 6 different areas within hippocampus per coronal section were imaged via a Leica TCS SP8 X confocal microscope using a 40X objective with 10 z stacks spacing of 1um per image.

## 解读

### 意义
RNAscope是一种多重RNA原位杂交技术，用于在单细胞水平验证ST和ISS发现的关键基因表达，并结合免疫荧光同时检测Aβ斑块，验证基因表达与斑块的空间关系。

### 输入
- AppNL-G-F小鼠18月龄冷冻切片（14 μm）
- RNAscope探针组（Cst7, Cd68, C4, C1qa, Clu, Syp, Mbp, Slc1a3, Itgam）
- 6E10抗体（Aβ检测）
- 脑区选择：海马体6个不同区域

### 输出
- 每个细胞中各基因的RNAscope荧光斑点数量
- 斑块周围5个同心环的基因表达量化
- 细胞类型特异性基因表达验证

### 核心步骤
1. 冷冻切片固定和蛋白酶消化
2. 探针杂交（40°C，2小时）
3. RNAscope信号扩增（AMP1-4）
4. 6E10免疫荧光染色检测Aβ斑块
5. TrueBlack处理减少脂褐素自发荧光
6. DAPI染色和封片
7. Leica TCS SP8 X共聚焦显微镜成像（40X，10层z-stack，1μm间距）
8. NIS-elements GA3协议自动检测细胞和斑点

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 杂交温度 | 40°C | 探针杂交温度 |
| 杂交时间 | 2小时 | 探针杂交时间 |
| 成像物镜 | 40X | 共聚焦成像放大倍数 |
| Z-stack | 10层，1μm间距 | 三维成像参数 |
| 同心环数 | 5个 | 斑块周围分析区域 |
| Ring 1扩展 | 10 μm | 斑块边界扩展距离 |
| 环间距 | 18.2 μm (65 pixels) | 相邻环之间的距离 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| RNAscope | ACD公司开发的RNA原位杂交技术 |
| GA3 protocol | NIS-elements软件中的自定义细胞分割和量化协议 |
| Ring 1 (plaque cellular niche) | 斑块细胞微环境，斑块边界扩展10μm |
| Ring 5 | 最远离斑块的环，距离ring 1约54.6 μm |
| Maximum intensity projection | 最大强度投影，z-stack的2D投影方法 |

## 复现
- 工具/代码/URL
  - RNAscope Manual Fluorescent Multiplex kit v1 (ACD, 320850)
  - NIS-elements software 5.20.01 (Nikon)
  - Leica TCS SP8 X confocal microscope
- 代码片段
```
# RNAscope探针列表
probes = ["Mm-Cst7", "Mm-Cd68-C3", "Mm-C4b", "Mm-C1qa", 
          "Mm-Clu", "Mm-Syp-C3", "Mm-Mbp-C3", "Mm-Slc1a3-C3", 
          "Mm-Itgam-C2"]
# GA3协议: 基于DAPI分割细胞核，扩展10μm获得细胞ROI
# 计算每个细胞ROI内的RNAscope斑点数
```

## 生物学意义
RNAscope验证了ST和ISS的关键发现：C1qa由小胶质细胞（Itgam+）表达，Clu由星形胶质细胞（Slc1a3+）表达，C4由少突胶质细胞（Mbp+）表达——均在淀粉样斑块附近富集。RNAscope与ST数据的Pearson相关系数为0.92（p=0.009），强有力地验证了空间转录组学方法的可靠性。

## 涉及 Figures
- **Fig. 2D-E** — RNAscope验证ST差异表达结果
- **Fig. 4I** — 补体成分的RNAscope验证
- **Fig. 6E-F** — OLIG基因的RNAscope验证
- **Figure S4B-C** — 补体成分的RNAscope量化
- **Figure S5D-E** — OLIG模块的RNAscope全冠状切片分析
