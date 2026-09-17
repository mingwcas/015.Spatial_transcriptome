# Method: Microfluidic Device Fabrication and Assembly

## 原文（Methods）
> The microfluidic device was fabricated with polydimethylsiloxane (PDMS) using soft lithography. The chrome photomasks with 10 μm, 25 μm and 50 μm channel width were ordered from the company Front Range Photomasks (Lake Havasu City, AZ). The molds were fabricated using SU-8 negative photoresist according to the following microfabrication process. A thin layer of SU-8 resist (SU-8 2010, SU-8 2025 and SU-8 2050, Microchem) was spin-coated on a clean silicon wafer following manufacturer's guidelines. The thickness of the resistant was ~50 μm for the 50-μm-wide microfluidic channel device, ~28 μm for 25-μm-wide device, and ~20 μm for 10-μm-wide device. A protocol to perform SU-8 photo lithography, development, and hard baking was followed based on the manufacturer's (MicroChem) recommendations to yield the silicon molds for PDMS replication.
> PDMS microfluidic chips were then fabricated via a replication molding process. The PDMS precursor was prepared by combining GE RTV PDMS part A and part B at a 10:1 ratio. After stir mixing, degassing, this mixture was poured to the mold described above, degassed again for 30 min, and cured at 75°C for ~2 hours or overnight. The solidified PDMS slab was cut out, peeled off, and the inlet and outlet holes were punched to complete the fabrication. The inlet holes were ~2 mm in diameter, which can hold up to 13 μL of solution. A pair of microfluidic chips with the same location of inlets and outlets but orthogonal microfluidic channels in the center were fabricated as a complete set of devices for flow barcoding a tissue slide. To do that, the PDMS slab was attached to the tissue section glass slides and a custom-designed acrylic clamp was used to firmly hold the PDMS against the tissue specimen to prevent leakage across microfluidic channels without the need for harsh bonding processed such as thermal bonding or plasma bonding (Temiz et al., 2015).

## 解读

### 意义
该方法解决了如何制备微流控芯片以实现组织表面的空间条码递送的问题，是DBiT-seq技术的核心硬件基础。

### 输入
- Chrome photomasks (10μm, 25μm, 50μm通道宽度)
- SU-8负性光刻胶(SU-8 2010, 2025, 2050)
- 硅晶片
- GE RTV PDMS A和B组分

### 输出
- PDMS微流控芯片（带有50条平行微通道）
- 亚克力夹具
- 可容纳~13μL溶液的入口孔（~2mm直径）

### 核心步骤
1. 在硅晶片上旋涂SU-8光刻胶，根据通道宽度选择不同型号（50μm用SU-8 2050，~50μm厚；25μm用SU-8 2025，~28μm厚；10μm用SU-8 2010，~20μm厚）
2. 执行UV曝光、显影和硬烘，形成硅模具
3. 将PDMS预聚体(A:B=10:1)混合、抽真空后浇注到模具上
4. 再次抽真空30分钟后，75°C固化约2小时或过夜
5. 切割、剥离固化的PDMS薄片，打孔形成入口和出口
6. 制备一对正交微通道的芯片作为一套设备
7. 使用亚克力夹具将PDMS固定在组织玻璃载玻片上

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 通道宽度 | 10μm, 25μm, 50μm | 三种规格可选 |
| PDMS A:B比例 | 10:1 | 标准PDMS配比 |
| 固化温度 | 75°C | 热固化条件 |
| 固化时间 | ~2小时或过夜 | 充分固化 |
| 入口孔直径 | ~2mm | 容量~13μL |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| PDMS | Polydimethylsiloxane，聚二甲基硅氧烷，常用于微流控芯片制造 |
| SU-8 | 一种负性光刻胶，用于微米级结构制造 |
| Soft lithography | 软光刻，基于PDMS复模的微纳加工技术 |
| Microfluidic channel | 微流控通道，引导液体流动的微米级通道 |

## 复现
- 工具/代码/URL：无开源代码（硬件制造）
- 关键调用：NA

## 生物学意义
该微流控芯片是DBiT-seq实现空间条码递送的核心硬件。正交的两套芯片实现了二维像素矩阵的构建，三种通道宽度（10/25/50μm）提供了不同的空间分辨率选择。亚克力夹具设计避免了传统等离子键合的复杂工艺，降低了技术门槛，使无微流控经验的研究者也能操作。

## 涉及 Figures
- **Fig. 1B** — Microfluidic device used in DBiT-seq
