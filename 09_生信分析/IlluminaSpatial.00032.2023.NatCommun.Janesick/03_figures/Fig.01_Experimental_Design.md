# Fig. 1 — Experimental design

## Caption（原文）
> A single FFPE tissue block was analyzed with a trio of complementary technologies. Top: the Chromium Single Cell Gene Expression Flex workflow with the Miltenyi FFPE Tissue Dissociation protocol (scFFPE-seq). Middle: Visium CytAssist enabled whole transcriptome analysis with spatial context, and was readily integrated with single-cell data from serially adjacent FFPE tissue sections. Bottom: The Xenium In Situ technology uses a microscopy based readout. A 5 μm tissue section was sectioned onto a Xenium slide, followed by hybridization and ligation of specific DNA probes to target mRNA, followed by rolling circle amplification. The slide was placed in the Xenium Analyzer instrument for multiple cycles of fluorescent probe hybridization and imaging. Each gene has a unique optical signature, facilitating decoding of the target gene, from which a spatial transcriptomic map was constructed across the entire tissue section. The Xenium data could be easily registered with post-Xenium immunofluorescence (IF)/H&E images (as the workflow is non-destructive to the tissue) and integrated with scFFPE-seq and Visium data. Metrics from these experiments are contained in Supp. Table 1.

## Panel-by-Panel 解读

### Panel Top — Chromium scFFPE-seq workflow
**结论**：展示使用 Miltenyi FFPE 组织解离方案和 Chromium Single Cell Gene Expression Flex（scFFPE-seq）从 FFPE 组织块获取单细胞全转录组数据的工作流程。

**关键数据**：从 2 × 25 μm FFPE curls 出发，获得 17 个聚类，中位数每细胞检测到 1,480 个基因。

### Panel Middle — Visium CytAssist workflow
**结论**：展示 Visium CytAssist 空间转录组工作流程，该技术可从标准玻片转移分析物至 Visium 玻片，提供全转录组空间数据。

**关键数据**：与 scFFPE-seq 使用相同的探针组（18,536 个基因，54,018 个探针），产生 17 个空间聚类，中位数每 spot 检测到 5,712 个基因。

### Panel Bottom — Xenium In Situ workflow
**结论**：展示 Xenium In Situ 原位分析技术，通过荧光探针杂交和成像循环实现亚细胞空间分辨率的靶向基因表达检测。

**关键数据**：使用 313 基因靶向面板，5 μm 组织切片，通过滚动循环扩增和多轮荧光成像解码目标基因，构建全切片空间转录组图谱。

## 总体结论
该图展示了本研究的核心实验设计——对同一 FFPE 乳腺癌组织块的连续切片分别使用三种互补技术（scFFPE-seq、Visium CytAssist 和 Xenium In Situ）进行分析。每种技术提供不同层次的信息：单细胞全转录组、全转录组空间信息、以及靶向高分辨率原位检测。这种整合策略使得研究人员能够从多个维度解析肿瘤微环境的异质性，且 Xenium 工作流程的非破坏性特征使得后续 H&E 染色和免疫荧光可与 RNA 数据精确配准。

## 关联 Figures / Extended Data
- Supp. Table 1（实验指标汇总）
- Supp. Figure 1b（Xenium 基因面板设计）
- Supp. Figure 5（技术重复性验证）
