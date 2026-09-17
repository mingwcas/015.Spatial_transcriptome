# Method: Post-Xenium Histology (H&E and IF Staining)

## 原文（Methods）
> The post-Xenium H&E staining followed Demonstrated Protocol CG000160. For post-Xenium IF staining, sections were washed with PBST, then incubated in a blocking buffer (ScyTek AAA999) for 30 min at room temperature. The primary antibody in the blocking buffer was added and incubated in the dark at 4 °C overnight. The following day, the sections were washed three times (10 min each) with PBST then incubated with secondary antibodies and DAPI in a blocking buffer, in the dark at room temperature, for two hours. Next, the sections were washed three times (10 min each) with PBST. Sections were imaged in a proprietary Xenium imaging buffer and imaged on a Zeiss Axioimager with a 40x dipping objective. The Zen Blue software was used for tiling, image acquisition, and exporting TIFF files. Post-Xenium H&E and IF images were registered to Xenium data using Fiji BigWarp.

## 解读

### 意义
在Xenium分析后对同一组织切片进行H&E和免疫荧光（IF）染色，实现分子表达数据与组织形态学/蛋白表达的直接对应，验证RNA检测结果

### 输入
- Xenium分析完成后的组织切片（非破坏性工作流保留了组织完整性）
- 一抗：CD20（鼠源，Abcam AB219329，1:200）和HER2（兔源，Abcam AB134182，1:1500）
- 二抗：Mouse IgG Alexa 488（ThermoFisher A-11029，1:500）和Rabbit IgG Alexa 594（Abcam AB150088，1:500）

### 输出
- H&E染色图像（可与Xenium数据配准）
- IF荧光图像（HER2和CD20蛋白表达）
- 注册后的多模态叠加图像

### 核心步骤
1. **Post-Xenium H&E染色**：按照Protocol CG000160进行标准H&E染色
2. **Post-Xenium IF染色**：
   - PBST洗涤组织切片
   - 封闭缓冲液（ScyTek AAA999）室温封闭30分钟
   - 加入一抗（CD20和HER2），4°C暗处孵育过夜
   - PBST洗涤3次（每次10分钟）
   - 加入荧光标记二抗和DAPI，室温暗处孵育2小时
   - PBST洗涤3次（每次10分钟）
3. **成像**：在Xenium成像缓冲液中，使用Zeiss Axioimager（40x浸没物镜）成像
4. **图像处理**：使用Zen Blue软件进行拼图、图像采集和TIFF导出
5. **图像配准**：使用Fiji BigWarp将Post-Xenium H&E和IF图像与Xenium数据配准

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 一抗CD20 | 鼠源，Abcam AB219329，1:200 | B细胞标记 |
| 一抗HER2 | 兔源，Abcam AB134182，1:1500 | 肿瘤标记 |
| 二抗Mouse IgG | Alexa 488，ThermoFisher A-11029，1:500 | 绿色荧光标记 |
| 二抗Rabbit IgG | Alexa 594，Abcam AB150088，1:500 | 红色荧光标记 |
| 封闭液 | ScyTek AAA999 | 减少非特异性抗体结合 |
| 成像物镜 | Zeiss 40x dipping objective | 浸没式高倍物镜 |
| 成像软件 | Zen Blue | Zeiss显微镜控制和图像采集 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| H&E | 苏木精-伊红染色（Hematoxylin and Eosin），标准组织病理学染色方法 |
| IF | 免疫荧光（Immunofluorescence），利用荧光标记抗体检测蛋白表达 |
| PBST | 含Tween的磷酸盐缓冲液（Phosphate-Buffered Saline with Tween），用于洗涤 |
| Fiji BigWarp | Fiji/ImageJ的图像配准插件，支持手动和自动关键点配准 |
| Post-Xenium | Xenium分析后的下游处理，得益于Xenium工作流对组织的非破坏性 |
| 二抗（secondary antibody） | 识别一抗的荧光标记抗体，用于信号放大和可视化 |

## 复现
- 工具/代码/URL：Zeiss Axioimager显微镜，Zen Blue软件，Fiji BigWarp插件
- 代码片段：N/A（标准免疫荧光染色和显微镜成像操作）

## 生物学意义
Post-Xenium组织学是验证Xenium原位转录组数据的关键步骤。Xenium工作流的非破坏性特性使得同一组织切片可以先进行分子检测，再进行形态学和蛋白水平的验证。H&E染色使病理学家能够直接对Xenium分析区域进行形态学注释，确认肿瘤区域的诊断。IF染色验证了HER2 RNA与蛋白表达的高度一致性（Supp. Fig. 9），以及CD20 B细胞标记的空间分布，证明了Xenium探针的特异性和灵敏度。这种多模态数据叠加为分子发现提供了形态学层面的证据支持。

## 涉及 Figures
- **Fig. 3c** — Post-Xenium H&E染色，显示Xenium对组织完整性的影响极小
- **Fig. 4c** — Post-Xenium H&E验证ROI区域的病理形态
- **Fig. 6c, c′** — Post-Xenium H&E与Xenium分子数据的对应
- **Supp. Fig. 9** — HER2和CD20的IF与RNA表达叠加验证
