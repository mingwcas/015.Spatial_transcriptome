# Fig. 4 — Immunofluorescence Artifacts in DSP

## Caption（原文）
> FIGURE 4 | Micro photographs showing artifacts in immunoﬂuorescence DSP slide from a non-small cell lung carcinoma tumor sample. (A) ROI was drawn with a polygon ROI, avoiding elastic fibers (red arrows) that emit non-speciﬁ c £uorescence signal (yellow). (B) Area on the right (red arrows) show numerous red blood cells emitting non-speciﬁ c £uorescence signal (yellow). Both, elastic fibers and red blood cells, interfered with segmentation for B-cells. (C) Tumor area on the left shows ﬁbrosis with non-speciﬁ c £uorescent signals (white arrow). (D) An area out of focus (white arrow) is observed on the left side of the image.

## Panel-by-Panel 解读

### Panel A — 弹性纤维假阳性
**结论**：多边形 ROI 应主动避开弹性纤维（红箭头所示黄色非特异性荧光信号），否则会干扰 segmentation 并影响 B 细胞计数。

**关键数据**：弹性纤维是非特异性荧光的常见来源，可在 CD20 分割时产生假阳性

### Panel B — 红细胞假阳性
**结论**：红细胞（右图红箭头）也会产生非特异性荧光（黄色），同样会干扰 B 细胞 segmentation。

**关键数据**：红细胞在组织切片中常见，其非特异性荧光与真实 B 细胞信号难以区分

### Panel C — 纤维化区域假阳性
**结论**：肿瘤区域的纤维化组织（左图白箭头）同样产生非特异性荧光信号，是 ROI 选择的潜在干扰因素。

**关键数据**：纤维化是肿瘤微环境的常见特征，其荧光信号需在 ROI 圈定时被排除

### Panel D — 离焦区域
**结论**：图像焦距不一致（白箭头所示离焦区域）也会影响 segmentation 的准确性。

**关键数据**：DSP 图像采集时需确保整张切片处于同一焦面；离焦区域的数据不可靠

## 总体结论
Figure 4 警示了 DSP 实验中常见的四类假阳性干扰源：弹性纤维、红细胞、纤维化组织和离焦区域。这些因素在传统病理学评估中可能被忽略，但对 DSP 的 segmentation 和计数准确性有显著影响。研究者在 ROI 选择时应综合考虑这些因素，优先使用多边形 ROI 精确排除非目标区域。建议在实验设计阶段就纳入这些潜在干扰因素的评价，并在 ROI 选择标准操作流程中明确排除准则。

## 关联 Figures / Extended Data
- 与 Methods 03（ROI Selection）和 Methods 07（Experimental Design）直接关联
- Fig. 3 展示了多边形 ROI 规避假阳性的策略
