# Method: In Situ Sequencing (ISS)

## 原文（Methods）
> OCT-embedded hemispheres of mice at 18-month of age were cryosectioned coronally into 14 μm and layered onto SuperFrost Plus glass slides. Samples were shipped on dry ice to CARTANA (Solna, Sweden) for tissue fixation, reverse transcription, probe ligation, rolling cycle amplification with reagents and according to the procedures supplied in the Neurokit (1010-01, CARTANA, Sweden), followed by fluorescence labeling, and sequencing by sequential images at 20X objective. Five probes were designed for each gene, except Itgam, which has 10 customized probes to increase the detection sensitivity. We included probes for 7 additional genes that do not belong to the PIG module but significantly react to the presence of amyloid plaques at 18-months of age. To reduce lipofuscin autofluorescence, 1X TrueBlack (Biotium, Fremont, CA) was applied for 30 s before fluorescence labeling. The result table of the spatial coordinates of each molecule of 84 targets together with the reference DAPI image per sample were provided by CARTANA.

## 解读

### 意义
In Situ Sequencing (ISS) 是一种正交验证方法，能够在组织原位以单细胞分辨率检测数百个选定转录本的空间分布，用于验证ST发现的PIG和OLIG模块基因在细胞水平的表达模式。

### 输入
- 冷冻切片（14 μm厚度）组织样本
- 84个目标基因的定制探针组（PIGs + 细胞类型标记基因）
- CARTANA Neurokit试剂盒

### 输出
- 每个荧光斑点（punctum）的空间坐标
- 84个目标基因的原位表达图谱
- DAPI参考图像
- 每个基因的细胞类型分配结果

### 核心步骤
1. 冷冻切片（14 μm）放置于SuperFrost Plus载玻片
2. 运送至CARTANA进行组织固定和逆转录
3. 探针连接（每个基因5个探针，Itgam 10个探针）
4. 滚环扩增（Rolling Circle Amplification, RCA）
5. 荧光标记和连续成像（20X物镜）
6. TrueBlack处理减少脂褐素自发荧光
7. 返回Leuven实验室进行Aβ免疫染色（6E10抗体）
8. QuPath软件叠加多靶标空间图像

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 14 μm | ISS切片厚度（比ST厚） |
| 探针数/基因 | 5个 | 每个基因的探针数量 |
| Itgam探针数 | 10个 | 增加微小胶质细胞标记检测灵敏度 |
| 目标基因数 | 84个 | PIGs + 细胞类型标记 |
| 成像物镜 | 20X | 成像放大倍数 |
| TrueBlack | 1X, 30秒 | 减少脂褐素自发荧光 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| ISS (In Situ Sequencing) | 原位测序，基于连接酶的原位barcode测序技术 |
| RCA (Rolling Circle Amplification) | 滚环扩增，用于信号放大 |
| CARTANA Neurokit | 商业化ISS试剂盒 |
| Puncta | ISS检测到的单个RNA分子荧光信号点 |
| L2OR (Log2 Odds Ratio) | 以2为底的对数优势比，衡量基因在斑块周围的富集程度 |

## 复现
- 工具/代码/URL
  - CARTANA ISS Neurokit (1010-01, CARTANA, Sweden)
  - QuPath: https://qupath.github.io/
  - 数据: https://repo-prod.prod.sagebase.org/repo/v1/doi/locate?id=syn22153884&type=ENTITY
- 代码片段
```
# ISS由CARTANA商业化服务完成
# 数据分析使用QuPath进行图像叠加
# 细胞类型分配使用自定义方法（见Method 07）
```

## 生物学意义
ISS提供了单细胞分辨率的原位验证，确认了ST发现的PIG响应主要由小胶质细胞和星形胶质细胞贡献，部分PIGs在多种细胞类型中表达。ISS还揭示了在淀粉样斑块微环境中，一些基因（如Ctsl和Apoe）仅在斑块附近的小胶质细胞中表达，揭示了斑块诱导的细胞类型特异性基因激活。

## 涉及 Figures
- **Fig. 4** — ISS鉴定PIGs的细胞特征
- **Fig. 7** — 人脑中PIG和OLIG模块的ISS可视化
- **Figure S4** — 补体成分的ISS细胞特征
- **Figure S7** — 无分割细胞类型分配方法
