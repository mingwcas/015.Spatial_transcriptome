# Method: Open-ST Workflow for Spatial Transcriptomics

## 原文（Methods）
> Open-ST operates by converting Illumina flow cells into ST capture areas, an approach previously implemented in Seq-Scope. Our method encompasses several key enhancements. First, we use patterned flow cell technology to create densely barcoded areas that capture polyadenylated RNA from a tissue section at a capture spot resolution of ~0.6 μm. To control the fragmentation of the flow cell into distinct capture areas, we provide a 3D-printable cutting guide. Our simplified library preparation only requires standard lab equipment and comes with a total cost of <€130 per 12 mm² capture area.

## 解读

### 意义
Open-ST提供了一种低成本、高分辨率的空间转录组学方法，将Illumina测序流式细胞转换为RNA捕获区域，实现亚细胞分辨率的全转录组捕获。

### 输入
- Illumina NovaSeq 6000 S4流式细胞
- 组织切片（新鲜冷冻样本）
- 标准实验室设备

### 输出
- 空间条形码标记的转录组数据
- 每个捕获区域约12 mm²
- 捕获点分辨率约0.6 μm

### 核心步骤
1. 使用自定义测序引物在Illumina流式细胞上注册空间条形码序列
2. 通过桥式扩增生成密集包装的条形码点
3. 使用DraI酶和Exonuclease I处理寡核苷酸以允许poly(A)转录本捕获
4. 打开流式细胞并使用3D打印切割指南将其切成所需大小的捕获区域
5. 将组织切片放置在捕获区域上并进行固定
6. 使用胃蛋白酶和杂交缓冲液进行组织透化和RNA捕获
7. 进行逆转录和第二链合成
8. 通过qPCR评估PCR循环数并进行文库扩增
9. 进行文库大小选择和测序

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 捕获点分辨率 | ~0.6 μm | 条形码点的中心到中心距离 |
| 捕获区域大小 | 3×4 mm (约12 mm²) | 单个捕获区域的尺寸 |
| 组织切片厚度 | 10 μm | 冷冻切片的厚度 |
| 胃蛋白酶浓度 | 0.7-1.4 U/mL | 用于组织透化的酶浓度 |
| 透化时间 | 15-45 min | 组织透化的时间 |
| PCR循环数 | 12-13 cycles | 文库扩增的循环数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 空间条形码 | 32-nt的DNA序列，用于标记空间位置 |
| poly(dT) | 寡核苷酸末端的poly(dT)区域，用于捕获poly(A) RNA |
| UMI | 唯一分子标识符，用于PCR去重 |
| 桥式扩增 | 在流式细胞表面进行的DNA扩增技术 |

## 复现
- 工具/代码/URL: https://rajewsky-lab.github.io/openst
- 代码片段: 自定义测序引物和3D打印切割指南可在上述网站获取

## 生物学意义
Open-ST提供了一种经济高效的空间转录组学解决方案，特别适用于需要高分辨率和全转录组覆盖的研究。该方法能够以亚细胞分辨率捕获转录本，为研究组织微环境和细胞异质性提供了强大工具。

## 涉及 Figures
- **Fig. 1** — Open-ST工作流程示意图
- **Fig. 2** — Open-ST捕获效率和性能评估
