# 四维度生信分析报告 — GeoMx DSP Immunoprofiling

> **论文信息**
> - **论文标题**：Challenges and Opportunities for Immunoprofiling Using a Spatial High-Plex Technology: The NanoString GeoMx® Digital Spatial Profiler
> - **DOI**：https://doi.org/10.3389/fonc.2022.890410
> - **平台**：NanoString GeoMx Digital Spatial Profiler (DSP)
> - **期刊**：Frontiers in Oncology
> - **发表年份**：2022
> - **第一作者**：Hernandez S
> - **完成日期**：2025

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 空间蛋白/RNA 分析 | DSP Assay Workflow | GeoMx DSP (NanoString) | 完整5步流程：组织制备→ROI选择→Oligo收集→杂交计数→数据分析 |
| 样本制备 | Tissue Preparation | FFPE/冷冻切片，5 μm | 兼容多种组织类型；最多4个可视化标记(SYTO13+3) |
| ROI 选择 | ROI Selection | DSP 仪器内置软件 | 支持矩形/多边形/轮廓等多种ROI类型；最大660×785 μm |
| 区域分割 | Compartment Segmentation | DSP 图像分析软件 | 支持肿瘤/间质/免疫细胞分割；可基于 panCK/CD45/CD3/CD68 |
| Oligo 收集 | UV-Light Cleavage | DMD (数字微镜装置) | UV照射切割 photo-cleavable DNA tag；微毛细管收集至96孔板 |
| 信号检测 | nCounter Hybridization & Counting | NanoString nCounter 系统 | 单分子计数；动态范围宽；无需 PCR 扩增 |
| 数据 QC | Initial QC (热图可视化) | GeoMx Data Analysis Suite | Binding density、阳性对照、最小核数/面积等QC参数 |
| 归一化策略 | Normalization Methods | Housekeepers (GAPDH/Histone H3/S6; UBB/OAZ1/SDHA/POLR2A), IgG, SNR | Scale to nuclei（暂不推荐）、Scale to area、RN、SNR |
| 统计分析 | Statistical Tests | GeoMx 内置：t-test, Mann-Whitney, 线性混合模型 | 根据数据结构选择适当统计方法 |
| 平台比较 | Platform Comparison | 与 Visium/mIF/CODEX/MIBI/IMC/MERFISH 比较 | 各平台在分辨率、靶标数、样本兼容性上各有优劣 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|--------------|
| Fig. 1 | DSP assay workflow 完整流程示意图（组织制备→ROI→Oligo→杂交计数→分析） | 流程示意图（Schematic） |
| Fig. 2 | 4种肿瘤（黑色素瘤/结直肠癌/乳腺癌/肺癌）的免疫荧光 biomarker 可视化示例 | 免疫荧光显微照片（4 panels） |
| Fig. 3 | 直肠癌活检的多边形 ROI 选择策略，展示 panCK 低表达肿瘤巢的圈选 | 免疫荧光显微照片 + ROI 标记图（2 panels） |
| Fig. 4 | NSCLC 中 IF 假阳性示例：弹性纤维/红细胞/纤维化/离焦区域的干扰 | 免疫荧光显微照片（4 panels） |
| Fig. 5 | NSCLC 两种 segmentation 策略对比：PanCK-based vs. Cell biomarker-based | 免疫荧光显微照片 + 分割标记图（4 panels） |
| Fig. 6 | 热图用于 DSP 数据集初始 QC，识别异常 AOI（housekeeper 信号缺失） | 热图（Heatmap） |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|-----------|
| 样本染色 | GeoMx DSP 仪器 + 染色试剂盒 | — | 商业（NanoString） |
| ROI 选择与扫描 | GeoMx DSP 仪器内置软件 | — | 商业（NanoString） |
| Oligo 收集 | GeoMx DSP 仪器（DMD UV 系统） | — | 商业（NanoString） |
| 信号读取 | nCounter Analysis System | — | 商业（NanoString） |
| 数据 QC 与可视化 | GeoMx Data Analysis Suite / GeoMx Data Center | — | 商业（NanoString） |
| 自定义分析脚本 | GeoScript Hub（R scripts） | — | 开源（NanoString 提供） |
| 图像分析（外部） | 多种第三方软件（支持 x,y 坐标导出） | — | 商业/开源 |
| 平台比较 | 文献对比分析 | — | 综述文章 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| nCounter 单分子计数 | 数字计数算法 | 对每个荧光条码对应分子进行独立计数，无 PCR 偏好 |
| DMD UV 图案化 | 可编程光学算法 | 将 UV 光精确匹配 ROI 形状，实现空间分隔照射 |
| Binding Density QC | 质量控制算法 | 评估探针与组织结合效率，识别过量探针 |
| Housekeeper 归一化 | 统计归一化算法 | 用内参基因/蛋白几何均值校正样本间差异 |
| SNR (Signal-to-Noise Ratio) 归一化 | 信噪比算法 | 用 IgG/阴性探针校正背景非特异性信号 |
| 线性混合模型 | 统计模型 | 处理多 ROI 嵌套数据结构（同一患者多个 ROI） |
| 热图聚类 | 无监督聚类算法 | 识别样本和 biomarker 的相似性模式 |
| 图像分割算法（DSP 内置） | 图像分析算法 | 基于荧光标记识别不同细胞群体和区域 |

---

## 利益冲突 / 局限性说明

1. **无单细胞分辨率**：DSP 的 ROI/AOI 级别分辨率限制了精细的细胞间相互作用研究，多个细胞混合在一起计数。
2. **ROI 面积受限**：最大 660×785 μm，无法覆盖大范围组织；需要预先设计采样策略。
3. **归一化方法尚未标准化**：不同研究可能采用不同的归一化策略，影响跨研究比较。
4. **SNR 归一化对低丰度标记物有偏倚**：PD-L1 等低表达 biomarker 的免疫冷区域数据可能被 SNR 放大失真。
5. **商业平台限制**：GeoMx DSP 仪器和试剂为 NanoString 专有，仪器价格和试剂成本可能限制可及性。
6. **厂商参与的综述**：部分引用来自 NanoString 内部或资助的研究，可能存在利益冲突声明（论文已声明无商业/财务关系）。

---

*报告生成日期：2025*
*分析平台：GeoMx DSP*
*分析流程遵循 AGENT.md 工作规范*
