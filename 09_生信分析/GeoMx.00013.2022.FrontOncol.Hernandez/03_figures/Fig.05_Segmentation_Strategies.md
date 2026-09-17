# Fig. 5 — Segmentation Strategies in NSCLC

## Caption（原文）
> FIGURE 5 | Microphotograph of immunoﬂuorescence sections of surgical resected non-small cell carcinoma (A) Squamous cell carcinoma; (B) adenocarcinoma) using DSP assay with PanCK (tumor), CD3 (T-cells), CD20 (B-cells) and Syto13 (nuclei) as visualization markers. (B, D) illustrates different segmentation strategies for tumor, stroma and T cells. In B the segmentation was performed in tumor (cyan mark up) and stroma (yellow mark up) segments based in panCK expression, with this strategy, tumor segments include tumor cells and Intra-epithelial immune cells (white arrows), and stroma segments include all tissue elements among tumor segments (B), In (C), segmentation was performed in tumor-(cyan mark up), B-cell (yellow mark up) and T-cells (red mark up) segments based in cell biomarker profile, intra-tumor T-cells (white arrows) are included in the T-cell compartment (D).

## Panel-by-Panel 解读

### Panel A/B (Left) — 鳞状细胞癌
**结论**：鳞状细胞癌的免疫荧光染色（PanCK + CD3 + CD20 + Syto13）显示了肿瘤与免疫细胞的空间分布，可用于后续 segmentation。

**关键数据**：PanCK 阳性区域对应肿瘤上皮；CD3 和 CD20 分别标记 T 和 B 淋巴细胞

### Panel B (Right) — 肿瘤/间质分割策略
**结论**：基于 PanCK 表达的分割策略将组织分为肿瘤区（青色）和间质区（黄色）。但此策略的局限在于肿瘤区包含了上皮内免疫细胞（白箭头），导致肿瘤区信号可能混杂免疫细胞来源。

**关键数据**：
- 肿瘤 segment：PanCK+ 细胞（包含上皮内 T 细胞）
- 间质 segment：PanCK- 所有组织成分

### Panel C (Left) — 腺癌
**结论**：腺癌同样可采用相同 VM 组合（PanCK + CD3 + CD20 + Syto13），展示了 DSP 在不同 NSCLC 亚型中的通用性。

**关键数据**：两种 NSCLC 亚型均可使用相同 VM 组合

### Panel D (Right) — 细胞 biomarker 分割策略
**结论**：基于细胞 biomarker 的分割策略将组织分为肿瘤区（青色）、B 细胞区（黄色）和 T 细胞区（红色）。此策略的精准之处在于上皮内 T 细胞（白箭头）被计入 T 细胞区而非肿瘤区。

**关键数据**：
- 肿瘤 segment：PanCK+ 细胞
- B 细胞 segment：CD20+ 细胞
- T 细胞 segment：CD3+ 细胞（包含上皮内 T 细胞）
- **两种分割策略的选择取决于研究问题**：若关注肿瘤本身则用第一种；若关注免疫细胞空间分布则用第二种

## 总体结论
Figure 5 展示了 DSP 的两种核心 segmentation 策略及其生物学取舍。肿瘤/间质分割（PanCK-based）适合研究肿瘤与微环境的整体相互作用，但会将上皮内免疫细胞归入肿瘤区；细胞类型分割（CD3/CD20-based）则可精准定位特定免疫细胞亚群的空间分布，但需要更多 VMs。该图强调：ROI segmentation 策略应在项目启动前明确定义，并记录于标准操作流程中，以保证结果的可重复性和生物学解释的准确性。

## 关联 Figures / Extended Data
- 与 Methods 03（ROI Selection）直接关联
- Fig. 2 提供了 VM 组合的参考
