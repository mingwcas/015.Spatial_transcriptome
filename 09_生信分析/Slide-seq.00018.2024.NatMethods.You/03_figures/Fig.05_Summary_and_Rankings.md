# Fig. 5 — Summary of Results and Characteristics of sST Methods

## Caption（原文）
> Fig. 5 Summary of results and characteristics of sST methods. The sST methods have been ranked based on their performance in the specified categories, with the highest-performing methods positioned at the top. In the left panel, each ranking is represented by color and spot size. In the right panel, essential characteristics of the sST methods examined are outlined. Set-up complexity represent how difficult it is to build the method from scratch.

## Panel-by-Panel 解读

### Left Panel — Performance Rankings
**结论**：综合比较显示各平台在不同维度上各有优劣，没有单一平台在所有指标上都是最佳。

**关键数据**：
- 原始reads下灵敏度：Stereo-seq > BMKMANU S1000 > Visium > Slide-seq V2 > DBiT-seq
- 归一化灵敏度：Slide-seq V2 > 其他
- 扩散控制（脑组织）：Slide-seq V2 > BMKMANU S1000 > Visium > PIXEL-seq > Stereo-seq
- 扩散控制（眼球组织）：Stereo-seq > Slide-seq V2 > 其他
- 聚类性能：Slide-seq V2 ≈ Stereo-seq > BMKMANU S1000 > Visium
- 标记基因检测：Slide-seq V2最高

### Right Panel — Platform Characteristics
**结论**：各平台在技术特征上存在显著差异，影响其适用场景。

**关键数据**：
- Spot大小：Stereo-seq < HDST < Slide-seq < DBiT-seq < Visium < BMKMANU
- 设置复杂度：DBiT-seq最高（微流控），Visium最低（商业化）
- 成本：商业平台（Visium）vs 研究用平台

## 总体结论
Fig. 5是本研究的核心总结，强调了选择sST平台时需要综合考虑多个因素：测序深度需求、灵敏度、扩散控制需求、预算和技术成熟度。没有一种方法在所有场景下都是最优选择。

## 关联 Figures / Extended Data
- Table 1 — 各平台详细protocol比较
