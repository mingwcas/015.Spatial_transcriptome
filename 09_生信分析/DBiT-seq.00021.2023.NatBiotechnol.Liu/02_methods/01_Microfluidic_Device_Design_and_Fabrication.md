# Method: Microfluidic Device Design and Fabrication

## 原文（Methods）
> We designed the photomask using Autodesk AutoCAD 2021 and had the chrome mask printed by Front Range Photomasks with high resolution (2 µm). The chrome mask was cleaned extensively with acetone and air dried before use. Polymethylsiloxane (PDMS) mold (25-µm channel width) was fabricated in a cleanroom using Photoresist SU-8 2025 (Kayaku Advanced Materials) following standard procedures, including spin coating, soft baking, laser exposure, post-exposure baking, development and hard baking. The mold thickness was measured using Zygo 3D Optical Profiler to be ~25 µm. The mold was placed in a plastic petri dish, and the PDMS mixture (part A: part B = 10:1, GE RTV) was poured in. The petri dish was placed into a vacuum chamber and degassed for ~30 minutes and then placed into a 70 °C oven and incubated for >2 hours or overnight. The cured PDMS slab was cut into a similar size as a 1×3-inch glass slide and stored at room temperature until use. The barcoding flow clamps and lysis clamps were fabricated through laser-cutting an acrylic plastic plate. After each DBiT-seq experiment, the PDMS chip can be reused by cleaning with 30-minute sonication in 1 M NaOH solution, 2 hours soaking in deionized water, 10-minute sonication in isopropanol and air dry at room temperature.

## 解读

### 意义
制备具有50条平行微通道（25 µm宽）的PDMS微流控芯片，用于在组织表面实现空间确定性条码标记。

### 输入
- Autodesk AutoCAD 2021 设计的光掩模
- Chrome mask（Front Range Photomasks，2 µm分辨率）
- Photoresist SU-8 2025（Kayaku Advanced Materials）
- PDMS mixture（GE RTV，A:B = 10:1）

### 输出
- 25 µm通道宽度的PDMS微流控芯片
- 可重复使用的条码流动夹具和裂解夹具

### 核心步骤
1. 使用AutoCAD设计光掩模，由Front Range Photomasks打印chrome mask（2 µm分辨率）
2. 在洁净室中使用SU-8 2025光刻胶制作PDMS模具：旋涂、软烘烤、激光曝光、曝光后烘烤、显影和硬烘烤
3. 使用Zygo 3D光学轮廓仪测量模具厚度（~25 µm）
4. 将PDMS混合物（A:B = 10:1）倒入模具，真空脱气30分钟后70°C固化>2小时
5. 切割PDMS至1×3英寸载玻片大小
6. 激光切割亚克力板制作流动夹具和裂解夹具
7. 实验后芯片清洗再生：1M NaOH超声30min → 去离子水浸泡2h → 异丙醇超声10min → 室温干燥

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 通道宽度 | 25 µm | 微流控通道宽度，决定空间分辨率 |
| 通道数量 | 50 | 每个芯片的平行通道数 |
| 光掩模分辨率 | 2 µm | Chrome mask打印精度 |
| PDMS比例 | A:B = 10:1 | PDMS固化配比 |
| 固化温度/时间 | 70°C / >2h | PDMS固化条件 |
| 模具厚度 | ~25 µm | 与通道宽度匹配 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| PDMS | Polydimethylsiloxane，聚二甲基硅氧烷，常用微流控材料 |
| SU-8 2025 | 负性光刻胶，用于制作微流控模具 |
| Chrome mask | 铬掩模版，用于光刻图案转移 |
| Photomask | 光掩模，定义微通道图案的母版 |

## 复现
- 工具/代码/URL
  - Autodesk AutoCAD 2021
  - SU-8 2025（Kayaku Advanced Materials）
  - GE RTV PDMS
- 代码片段：N/A（硬件制备工艺）

## 生物学意义
微流控芯片是DBiT-seq的核心硬件基础，其25 µm通道宽度实现了接近单细胞水平的空间分辨率。50条平行通道构成50×50的二维网格，产生2500个空间像素点，覆盖2.5 mm × 2.5 mm的组织区域。芯片可重复使用降低了实验成本。

## 涉及 Figures
- **Fig. 1a** — 展示微流控芯片在空间条码标记中的工作流程
- **Extended Data Fig. 1** — 详细的微流控芯片设计和工作流程图
