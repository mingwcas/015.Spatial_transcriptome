# Method: Multiplex Immunofluorescence (mIF)

## 原文（Methods）
> mIF was performed on serial FFPE sections using the Opal Polaris 7-Color Manual IHC Kit. Staining was performed using the Bond RX automated staining system, followed by imaging via the Vectra Polaris multispectral imaging system. The panel included antibodies against the following: NR2F2, FYN, HIF1A, SERPINA1, COL6A2, DHRS2, CD4, CD8, FOXP3, CD20, CD3D, and CD68. For antibody details, see the key resources table.

## 解读

### 意义
 multiplex immunofluorescence (mIF) 用于在同一切片上同时检测多个蛋白标记物，验证CosMx SMI发现的关键蛋白表达模式，特别是淋巴结转移相关恶性细胞亚群的标记物。

### 输入
- FFPE组织连续切片
- Opal Polaris 7-Color Manual IHC Kit (AKOYA Biosciences)
- Bond RX自动化染色系统
- 一抗混合液：NR2F2, FYN, HIF1A, SERPINA1, COL6A2, DHRS2, CD4, CD8, FOXP3, CD20, CD3D, CD68

### 输出
- 多光谱mIF图像
- 蛋白共表达验证数据（用于验证空间转录组发现的细胞类型）

### 核心步骤
1. FFPE连续切片准备
2. Bond RX自动化染色系统进行mIF染色
3. Opal Polaris 7-Color Kit多重荧光染色
4. Vectra Polaris多光谱成像系统获取图像
5. 图像分析验证蛋白共表达

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 试剂盒 | Opal Polaris 7-Color Manual IHC Kit | 7色多重荧光 |
| 染色系统 | Bond RX (Leica) | 自动化染色 |
| 成像系统 | Vectra Polaris | 多光谱成像 |
| 检测标记物 | NR2F2, FYN, HIF1A, SERPINA1, COL6A2, DHRS2, CD4, CD8, FOXP3, CD20, CD3D, CD68 | 12个标记物 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| mIF | Multiplex immunofluorescence，多重免疫荧光 |
| Opal Polaris | AKOYA Biosciences的多重荧光染色技术 |
| Vectra Polaris | 多光谱成像系统，用于mIF图像采集 |

## 复现
- 工具/代码/URL：Opal Polaris 7-Color Manual IHC Kit (Cat#NEL861001KT, AKOYA Biosciences)
- 抗体信息详见原文Key Resources Table

## 生物学意义
mIF作为空间转录组学的独立验证手段，证实了C5 (FYN+NR2F2+)、C6 (SERPINA1+DHRS2+)、C9 (HIF1A+COL6A2+)亚群在PT-LNM和LNMT样本中的蛋白水平共表达，增强了研究结果的可靠性。

## 涉及 Figures
- **Fig. 2D** — mIF验证C6标记物SERPINA1和DHRS2在PT-LNM和LNMT中的共表达
- **Fig. S3D** — Additional mIF validation
