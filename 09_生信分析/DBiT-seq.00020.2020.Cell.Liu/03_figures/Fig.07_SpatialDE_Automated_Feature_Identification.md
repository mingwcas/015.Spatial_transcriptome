# Fig. 7 — SpatialDE for Automated Feature Identification

## Caption（原文）
> (A) Major features identified in a E10 mouse embryo sample (see Figure 4). It revealed several additional tissue types in addition to eye. Pixel size, 10 μm. Scale bar, 200 μm.
> (B) Major features identified in the lower body of a E11 mouse embryo tissue sample (see Figure 6), which showed a variety of tissue types developed in E11. Pixel size, 25 μm. Scale bar, 500 μm.
> (C) Major features identified in the lower body of a E12 mouse embryo sample (see Table S4), which showed more tissue types and developing organs at this embryonic age (E12). Pixel size, 50 μm. Scale bar, 1 mm.

## Panel-by-Panel 解读

### Panel A — E10 Eye Region Features
**结论**：SpatialDE自动识别出眼、耳、肌肉、前脑、上皮等多种组织特征
**关键数据**：20个features；眼和肌肉特征清晰可辨；耳特征不明显（可能因发育早期）；前脑仅部分覆盖

### Panel B — E11 Lower Body Features
**结论**：E11下半身显示多种发育中的组织类型
**关键数据**：检测到心脏、肝脏、背主动脉、神经管等结构

### Panel C — E12 Lower Body Features
**结论**：E12胚胎显示最丰富的器官发育特征
**关键数据**：仅分析1/3胚胎组织即识别出40个features；包括心脏、肺、泌尿生殖系统、消化系统、男性生殖腺（睾丸）等

## 总体结论
Fig. 7 证明了SpatialDE算法在DBiT-seq数据上自动发现空间组织特征的强大能力，无需依赖先验的细胞类型注释。从E10到E12，识别出的features数量增加（20→25→40个），反映了发育进程中新器官的逐渐形成。

## 关联 Figures / Extended Data
- **ED Fig. S7** — E10全胚胎和E11下半身的完整SpatialDE分析
