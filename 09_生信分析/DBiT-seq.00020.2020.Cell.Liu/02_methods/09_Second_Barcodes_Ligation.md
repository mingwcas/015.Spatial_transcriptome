# Method: Adding the Second Set of Barcodes and Ligation

## 原文（Methods）
> After drying the tissue slides, the second PDMS chip with the microfluidic channels perpendicular to the direction of the first PDMS chip in the tissue barcoding region was carefully aligned and attached to the tissue slide such that the microfluidic channels cover the tissue region of interest. The ligation mix was prepared as follows: 69.5 μL of RNase free water, 27 μL of T4 DNA ligase buffer (10X, New England Biolabs), 11 μL T4 DNA ligase (400 U/mL, New England Biolabs), 2.2 μL RNase inhibitor (40 U/mL, Enzymatics), 0.7 μL SuperaseIn RNase Inhibitor (20 U/mL, Ambion), 5.4 μL of Triton X-100 (5%). To perform the second flow barcoding, we added to each channel a total of 5 μL of solution consisting of 2 μL of the aforementioned ligation mix, 2 μL of NEB buffer 3.1(1X, New England Biolabs) and 1 μL of DNA barcode B (25 μM). Reaction was allowed to occur at 37°C for 30 minutes and then the microfluidic channels were washed by flowing 1X PBS supplemented with 0.1% Triton X-100 and 0.25% SUPERase In RNase Inhibitor for 10 minutes. Again, the images showing the location of the microfluidic channels on the tissue slide could be taken during the flow step under the light or dark field optical microscope (Thermo Fisher EVOS fl) before peeling off the second PDMS chip.

## 解读

### 意义
这是DBiT-seq形成二维空间像素阵列的关键步骤。通过第二次正交流動和连接反应，将Barcode B与已固定的Barcode A连接，形成完整的空间条码AiBj。

### 输入
- 带有Barcode A标记cDNA的组织载玻片
- 第二PDMS芯片（通道正交于第一套）
- 连接混合液（T4 DNA ligase + buffer）
- NEB buffer 3.1
- 50种DNA Barcode B溶液（B1-B50，25μM）

### 输出
- 二维空间条码阵列（AiBj, i=1-50, j=1-50）
- 完整的空间位置编码

### 核心步骤
1. 干燥载玻片
2. 对齐并放置第二个PDMS芯片（通道与第一次正交）
3. 制备连接混合液：69.5μL RNase-free水 + 27μL T4 DNA ligase buffer(10X) + 11μL T4 DNA ligase(400U/mL) + 2.2μL RNase抑制剂(40U/mL) + 0.7μL SuperaseIn(20U/mL) + 5.4μL Triton X-100(5%)
4. 每通道加入5μL溶液（2μL连接混合液 + 2μL NEB buffer 3.1 + 1μL Barcode B，25μM）
5. 37°C孵育30分钟（连接反应）
6. 1X PBS + 0.1% Triton X-100 + 0.25% SUPERase In清洗10分钟
7. 成像记录（如需要）
8. 剥离第二个PDMS芯片

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Barcode B浓度 | 25 μM | 与Barcode A等摩尔 |
| 每通道体积 | 5 μL | 完全充满通道 |
| 连接温度 | 37°C | T4 DNA ligase最适温度 |
| 连接时间 | 30分钟 | 充分连接 |
| 清洗缓冲液 | PBS + 0.1% Triton X-100 + 0.25% SUPERase In | 温和去除未结合物 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| T4 DNA ligase | T4 DNA连接酶，催化DNA双链连接 |
| Ligation | 连接反应，形成Barcode A与Barcode B的共价连接 |
| Orthogonal channels | 正交通道，形成二维交叉点阵列 |

## 复现
- 工具/代码/URL：T4 DNA ligase (New England Biolabs, M0202L)
- 关键调用：NA

## 生物学意义
这是DBiT-seq技术形成最终二维像素的关键步骤。A和B条码的交叉点形成了独特的空间条码组合（AiBj），实现了组织像素的二维地址编码。T4 DNA连接酶催化形成稳定的磷酸二酯键，将两条条码共价连接。

## 涉及 Figures
- **Fig. 1A** — Schematic workflow showing ligation
- **Fig. 1C** — 验证结果：绿色FITC标记的Barcode B像素（交叉点）
