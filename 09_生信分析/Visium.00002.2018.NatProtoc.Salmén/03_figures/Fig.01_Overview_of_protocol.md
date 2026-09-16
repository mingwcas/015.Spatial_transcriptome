# Fig. 1 — Overview of the protocol

## Caption（原文）
> Fig. 1 | Overview of the protocol. a, The barcoded oligo-dT microarray slides are divided into six subarrays, each with a size of 6.2 × 6.6 mm. Each subarray contains 1,007 circular spatial spots, each with a unique spatial barcode and an approximate diameter of 100 μm; the spots are arranged with a center-to-center distance of 200 μm. The 5′ end of each probe is attached to the microarray glass slide and has a section of deoxyuridine bases, which are cleaved during the probe release. The probe also contains (5′ to 3′), a T7 promoter for in vitro transcription (IVT), a partial Illumina handle for the sequencing, a spatial barcode, a unique molecular identifier (UMI) to remove amplification duplicates and a poly-A capture sequence. b, (1) Thin tissue sections are obtained from fresh-frozen tissue using a cryostat. One tissue section is attached and fixed to each subarray on the microarray slide. (2) The tissue is then fixed, stained and imaged to determine the morphology and the spatial location of each region in relation to the spatial spots. (3) The tissue is permeabilized ... Reverse transcription ... cDNA ... tissue removal. (4) probes/cDNA fragments are released ... (5) cDNA is amplified and converted to finished paired-end libraries. (6) libraries are sequenced and further processed to map expressed genes to spatial locations. c, bright-field and spatial-spot images ... Most spatial spots are present ... some are missing or irregular. Scale bars, 500 μm.

## Panel-by-Panel 解读
### Panel a — 条码阵列与探针结构
**结论**：六个subarray、每个1,007个100 μm spot构成空间索引捕获面。
**关键数据**：spot直径约100 μm、中心距200 μm；探针含spatial barcode、UMI、poly-A capture、T7和Illumina handle。
### Panel b — 实验流程
**结论**：从冷冻切片到捕获、RT、释放、建库、测序形成闭环。
**关键数据**：每张array可并行处理六个subarray。
### Panel c — 组织图与spot图
**结论**：明场形态图和释放后的荧光spot图提供空间配准依据。
**关键数据**：大多数spot圆形可见，但可能缺失或变形。

## 总体结论
该图定义了Spatial Transcriptomics的核心机制：在保留组织形态的同时，以唯一空间条码和UMI捕获poly(A) RNA，并将测序计数回投到组织坐标。

## 关联 Figures / Extended Data
- Fig. 5：计算处理和图像配准；Fig. 7：典型计数结果。
