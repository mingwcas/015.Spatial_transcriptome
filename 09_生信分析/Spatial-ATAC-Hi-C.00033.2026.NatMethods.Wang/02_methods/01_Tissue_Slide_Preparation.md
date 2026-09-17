# Method: Preparation of tissue slides

## 原文（Methods）
> Mouse C57 Anterior Hypothalamus Coronal Frozen Sections Reg. 6 (cat. no. MF-201-06-C57), Mouse C57 Hippocamp/thalamus/hypothal Coronal Frozen Section Reg. 8 (cat. no. MF-201-08-C57) and human brain cerebellum frozen sections (cat. no. HF-202) were purchased from Zyagen. Brains of C57BL/6 mice were snap-frozen in OCT without any fixative and sectioned in coronal orientation at a thickness of 7–10 μm. Tissue sections were collected on poly-L-lysine-coated glass slides (Electron Microscopy Sciences, cat. no. 63478-AS). Glioma brain tumor specimens were collected fresh from the operating room at Northwestern Memorial Hospital using a protocol approved by the Institutional Review Board (STU00095863). All patients underwent informed consent for molecular analysis and research studies. After resection, specimens were flash-frozen in Optimal Cutting Temperature (Tissue-Tek) before storage in −80 °C until further analysis. An accompanying block from each tumor underwent H&E staining, and adequate tumor content was verified by a board-certified neuropathologist. In preparation for spatial profiling, poly-L-lysine-coated slides (Electron Microscopy Sciences; cat. no. 63478-AS) were chilled, and the samples sectioned into 10-μm thick slices using a cryostat, with temperature set at −20 °C (Leica). Excess OCT was manually trimmed before placement on each slide. Several adjacent slides were prepared for each sample to enable profiling with other modalities, including H&E stains on either side of the characterized slide.

## 解读

### 意义
为Spatial-ATAC-Hi-C实验准备高质量的组织切片，确保组织结构完整性和后续微流控条形码标记的成功

### 输入
- 小鼠脑组织（C57BL/6品系）
- 人类小脑冷冻切片
- 胶质瘤患者新鲜手术标本

### 输出
- 固定在poly-L-lysine包被玻片上的组织切片（7-10 μm厚度）
- 用于后续Spatial-ATAC-Hi-C实验的样本

### 核心步骤
1. 购买或获取组织样本（小鼠脑冷冻切片或人类手术标本）
2. 使用OCT包埋并快速冷冻组织
3. 使用冷冻切片机（Leica）在-20°C下切片（7-10 μm厚度）
4. 将切片收集到poly-L-lysine包被的玻璃玻片上
5. 对于人类肿瘤样本，进行H&E染色验证肿瘤含量
6. 准备连续切片用于其他模态分析（如H&E染色）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 7-10 μm | 组织切片的标准厚度 |
| 切片温度 | -20°C | 冷冻切片机的工作温度 |
| 玻片包被 | poly-L-lysine | 增强组织附着的包被材料 |
| 冷冻保护剂 | OCT (Tissue-Tek) | 组织包埋介质 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| OCT | Optimal Cutting Temperature，用于冷冻组织包埋的介质 |
| poly-L-lysine | 多聚赖氨酸，用于增强组织在玻片上附着的包被材料 |
| 冷冻切片机 | Cryostat，用于在低温下切割组织的设备 |
| H&E染色 | 苏木精-伊红染色，组织学常规染色方法 |

## 复现
- 工具/代码/URL
  - 冷冻切片机：Leica
  - 玻片：Electron Microscopy Sciences, cat. no. 63478-AS
  - OCT包埋剂：Tissue-Tek
- 代码片段
  ```bash
  # 组织切片准备流程（标准操作）
  # 1. 组织OCT包埋
  # 2. -20°C冷冻切片（7-10 μm）
  # 3. 收集到poly-L-lysine包被玻片
  # 4. 室温干燥10分钟
  ```

## 生物学意义
组织切片准备是Spatial-ATAC-Hi-C实验的基础步骤，直接影响：
- 组织结构的完整性：确保后续微流控通道能够均匀覆盖组织
- 细胞核的可及性：适当的厚度保证细胞核能够被后续酶处理
- 条形码标记效率：良好的组织附着确保微流控条形码能够有效标记空间位置
- 多模态分析：连续切片设计允许同时进行H&E染色和其他分析

该方法的局限性在于：
- 冷冻切片可能产生组织伪影
- 切片厚度限制了空间分辨率
- 需要新鲜或正确冷冻保存的组织样本

## 涉及 Figures
- **Fig. 1a** — Spatial-ATAC-Hi-C实验流程示意图，展示组织切片准备步骤
- **Extended Data Fig. 1** — 组织切片质量控制和H&E染色验证
