# Method: Puck Sequencing

## 原文（Methods）
> Pucks were sequenced using a sequencing-by-ligation approach with a SOLiD dibase-encoding strategy previously described1,43 and with a monobase-encoding strategy developed for this work... Imaging was performed using a Nikon Eclipse Ti microscope with a Yokogawa CSU-W1 confocal scanner unit and an Andor Zyla 4.2 Plus camera.

## 解读

### 意义
Puck sequencing通过sequencing-by-ligation确定每个bead的唯一barcode，建立从荧光图像到空间位置的信息桥梁。

### 输入
- Prepared pucks (beads on glass)
- Fluorescently-labeled sequencing oligonucleotides
- Flow cell system (Bioptechs FCS2)

### 输出
- 每个bead的barcode序列
- 荧光图像用于base calling
- 6,030 × 6,030像素的拼接图像

### 核心步骤
1. **Flow cell设置**: Bioptechs FCS2 flow cell + RP-1蠕动泵 + Hamilton MVP
2. **荧光成像**: 每轮ligation后在4个通道成像（488nm, 561nm, 624nm, 647nm）
3. **Ligation循环**: 14轮split-pool测序（8轮5' ligation + 3轮3' ligation + 3轮SEDAL）
4. **Strip**: 每轮后用80% formamide处理20分钟

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Flow rate | 1-3 ml/min | 液体流速 |
| 显微镜 | Nikon Eclipse Ti | 成像设备 |
| 共聚焦 | Yokogawa CSU-W1 | 扫描单元 |
| 相机 | Andor Zyla 4.2 Plus | sCMOS相机 |
| 物镜 | Nikon Plan Apo ×10, 0.45-NA | 成像放大倍数 |
| 图像尺寸 | 6,030 × 6,030 pixels | 拼接后最终图像 |
| Ligation时间 | 40 min (standard), 2 h (SEDAL) | 反应时间 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Sequencing-by-ligation | 通过T4 DNA ligase介导的连接反应读取DNA序列 |
| SOLiD dibase encoding | 双碱基编码测序，每轮读取2个碱基 |
| Monobase encoding | 单碱基逐一测序，本研究开发的开源方案 |
| SEDAL | Sequencing with degenerate primers in solution |
| Fluorescent channels | 4个通道对应A(FAM), C(Cy3), T(Cy5), G(Texas Red/AqP593) |

## 复现
- **设备**: 
  - Nikon Eclipse Ti microscope + Yokogawa CSU-W1 + Andor Zyla 4.2 Plus
  - Bioptechs FCS2 flow cell
  - RP-1 peristaltic pump (Rainin)
  - Hamilton MVP valve positioner
- **URL**: https://github.com/MacoskoLab/PuckCaller/ (image processing)

## 生物学意义
Bead barcode的准确读取是空间转录组数据质量的关键。测序后获得的bead locations与后续RNA-seq reads匹配，实现"which bead"→"which location"的映射。

## 涉及 Figures
- **Supplementary Fig. 1a-c** — Sequencing strategy schematics
- **Fig. 1a** — Method overview
