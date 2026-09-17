# Method: Photomask fabrication and PDMS microfluidic chip fabrication

## 原文（Methods）
> The design of the chrome photomask with a 50-μm channel width has been described previously91 and the actual photomasks were ordered from the company Front Range Photomasks. The silicone molds were fabricated in the microfabrication and nanofabrication facility (NUFAB) core at Northwestern University, following clean room guidelines. In brief, a thin layer of SU-8 3025 (Kayaku Advanced Materials) was spin coated on a plasma-treated prime-grade silicon wafer at 2,500 rpm for 40 s. The spin-coated wafer was then heat-treated and exposed to a total of 400 mJ cm−2 UV light under the photomask. The resulting wafer was developed and hard baked. The final thickness of the mold was ~35 μm. Polydimethylsiloxane (PDMS) chips were fabricated as described previously91. In brief, Part A and Part B of the PDMS precursor (SYLGARD 184 Silicone Elastomer, Dow Corning) was mixed in a 10:1 ratio and poured onto the silicone mold mentioned above. The mixture was degassed completely, and heat cured at 65 °C for ~2.5 h or overnight. The hardened PDMS piece was extracted and trimmed to match the dimension of the glass slide. Inlet and outlet holes were punched at 2 mm in diameter, using Titanium-coated Follicle Unit Extraction punches (Robbins Instruments). Visual inspection was carried out to ensure the integrity of channels, inlet and outlet holes before usage. Each piece of the PDMS chip was single use only.

## 解读

### 意义
制备聚二甲基硅氧烷（PDMS）微流控芯片，用于在组织切片上创建微通道系统，实现空间条形码的引入

### 输入
- 光掩模设计（50 μm通道宽度）
- SU-8 3025光刻胶（Kayaku Advanced Materials）
- 硅晶圆（prime-grade，等离子处理）
- PDMS前体（SYLGARD 184 Silicone Elastomer, Dow Corning）

### 输出
- PDMS微流控芯片（50 μm通道，匹配玻片尺寸）
- 用于空间条形码标记的微流控装置

### 核心步骤
1. **光掩模制备**：设计50 μm通道宽度的铬光掩模，订购自Front Range Photomasks
2. **硅模具制备**：
   - 在等离子处理的硅晶圆上旋涂SU-8 3025光刻胶（2500 rpm，40秒）
   - 热处理后在光掩模下曝光（400 mJ cm⁻² UV）
   - 显影和硬烘烤，形成~35 μm厚度的模具
3. **PDMS芯片制备**：
   - 混合PDMS前体A和B（10:1比例）
   - 倒入硅模具，完全脱气
   - 65°C热固化~2.5小时或过夜
   - 提取硬化PDMS块，修剪至匹配玻片尺寸
4. **芯片加工**：
   - 使用钛涂层打孔器（Robbins Instruments）打孔（直径2 mm）
   - 视觉检查通道、入口和出口孔的完整性
5. **使用说明**：每个PDMS芯片仅限单次使用

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 通道宽度 | 50 μm | 微流控通道的宽度 |
| SU-8厚度 | ~35 μm | 光刻胶层的最终厚度 |
| PDMS比例 | 10:1 (A:B) | PDMS前体混合比例 |
| 固化温度/时间 | 65°C / 2.5h或过夜 | PDMS热固化条件 |
| 打孔直径 | 2 mm | 入口和出口孔的直径 |
| UV曝光量 | 400 mJ cm⁻² | 光刻曝光能量 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| PDMS | 聚二甲基硅氧烷，一种透明、柔性的硅基聚合物，用于微流控芯片制造 |
| 光掩模 | Photomask，用于光刻工艺的图案化掩模 |
| SU-8 3025 | 负性光刻胶，用于制造微结构模具 |
| 旋涂 | Spin coating，将液体材料均匀涂覆在旋转基底上的工艺 |
| 脱气 | Degassing，去除PDMS混合物中的气泡 |

## 复现
- 工具/代码/URL
  - 微流控设备制备设施：NUFAB (Northwestern University)
  - 光掩模供应商：Front Range Photomasks
  - PDMS材料：Dow Corning SYLGARD 184
  - 打孔器：Robbins Instruments (Titanium-coated Follicle Unit Extraction punches)
  - 参考文献：Su, G. et al. STAR Protoc. 2, 100532 (2021)
- 代码片段
  ```bash
  # PDMS芯片制备流程（概念性）
  # 1. 硅晶圆等离子处理
  # 2. 旋涂SU-8 3025（2500 rpm, 40s）
  # 3. 软烘烤（95°C, 分钟）
  # 4. UV曝光（400 mJ/cm²）
  # 5. 显影和硬烘烤
  # 6. PDMS混合（A:B = 10:1）
  # 7. 脱气和固化（65°C, 2.5h）
  # 8. 提取和打孔（2mm直径）
  ```

## 生物学意义
PDMS微流控芯片在Spatial-ATAC-Hi-C中发挥关键作用：
- **空间编码实现**：通过微通道将条形码精确引入组织切片的特定位置
- **流体控制**：微通道确保试剂均匀分布，提高反应效率
- **空间分辨率**：50 μm通道宽度决定了空间像素的大小
- **可扩展性**：设计允许根据需要调整通道数量和布局

该技术的优势：
- 制造工艺成熟，成本相对较低
- PDMS生物相容性好，适合细胞和组织分析
- 芯片设计灵活，可根据实验需求定制

局限性：
- 每个芯片仅限单次使用，增加实验成本
- 需要专门的微制造设施（如NUFAB）
- 通道尺寸限制了空间分辨率的进一步提升
- PDMS可能吸附某些小分子，影响某些生化反应

## 涉及 Figures
- **Fig. 1a** — Spatial-ATAC-Hi-C实验流程，展示微流控芯片设计
- **Extended Data Fig. 2** — 微流控芯片制备和验证
