# Fig. 3 — Open-ST Captures Transcripts at Subcellular Resolution

## Caption（原文）
> (A) Spatial distribution of cell types of an E13 mouse head sagittal section.
> (B) Annotation of forebrain, midbrain, hindbrain, and the developing eye on the H&E, and localization of selected marker genes.
> (C) Spatial distribution of E13 mouse forebrain cells colored by annotated Leiden cluster or by label transfer from an E13.5 single-cell reference atlas.
> (D) Localized gene capture of transcription factors Neurod6 and Pbx3 compared with in situ hybridization images from the Allen Atlas.
> (E) Localized gene capture in the hindbrain (Tubb3) and choroid plexus (Ttr).
> (F) Transcript density for Ttr and Atoh7; comparison with ISH images.
> (G) Subcellular transcript capture precision in adult mouse hippocampus.
> (H) Malat1 and mitochondria-encoded transcripts are enriched in the nucleus and cytoplasm, respectively.

## Panel-by-Panel 解读

### Panel A — 细胞类型空间分布
**结论**：Open-ST捕获了E13小鼠头部的主要解剖区域

**关键数据**：鉴定出神经元、放射状胶质细胞、视网膜、脉络丛、成纤维细胞、软骨细胞等多种细胞类型

### Panel B — 标记基因定位
**结论**：标记基因表达与相应细胞类型的空间共定位

**关键数据**：Tbr1、Lhx9、Dmrta2、Atoh7、Ttr等标记基因准确定位

### Panel C — 前脑细胞类型
**结论**：Open-ST聚类结果与参考图谱高度一致

**关键数据**：无监督聚类与E13.5单细胞参考图谱标签转移结果吻合

### Panel D — 与ISH比较
**结论**：Open-ST转录本定位与Allen图谱ISH高度一致

**关键数据**：Neurod6和Pbx3在前脑的区域化表达与ISH匹配

### Panel E — Tubb3和Ttr表达
**结论**：转录本精确定位到相应组织区域

**关键数据**：Tubb3在后脑检测，Ttr在脉络丛特异性表达

### Panel F — 转录本密度分析
**结论**：转录本密度变化在细胞直径尺度可检测

**关键数据**：Ttr信号在脉络丛边界在细胞直径内从最小过渡到最大

### Panel G — 亚细胞精度
**结论**：Open-ST实现亚细胞分辨率的转录本捕获

**关键数据**：Malat1核富集，线粒体转录本细胞质富集

### Panel H — 核质分布
**结论**：转录本定位反映核-细胞质细胞架构

**关键数据**：Malat1 log2(OR) = -1.24 (核富集)，线粒体转录本 log2(OR) = 0.20 (细胞质富集)

## 总体结论
Fig. 3证明Open-ST能够以亚细胞分辨率捕获转录本，准确反映细胞的核-细胞质架构，标记基因定位与ISH高度一致。

## 关联 Figures / Extended Data
- Fig. S3 — 局部转录本捕获和细胞类型注释
- Fig. S4 — 前脑区域标记基因和生物学重复
