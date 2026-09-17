# Fig. 2: 克服分辨率限制和增强信噪比 (Overcoming Resolution Limitations and Enhancing Signal-to-Noise Ratio)

## Caption（原文）

(A) Ligation of fluorescent oligonucleotides occurs when the sequencing primer ends are perfectly complementary to the template. Extending sequencing primers by one or more bases, one can randomly sample amplicons at 1/4th, 1/16th, and 1/256th of the original density in fibroblasts (scale bar: 5 mm). N, nucleus; C, cytoplasm. (B) Rather than using an arbitrary intensity threshold, color sequences at each pixel are used to identify objects. For sequences of L bases, the error rate is approximately n/4L per pixel, where n is the size of the reference. By removing unaligned pixels, the nuclear background noise is reduced in fibroblasts (scale bar: 20 mm).

## Panel-by-Panel 解读

### Panel A: 分区测序
- **内容**：不同长度测序引物对扩增子密度的影响
- **关键信息**：
  - 标准引物：原始密度
  - 延伸 1 个碱基：1/4 密度
  - 延伸 2 个碱基：1/16 密度
  - 延伸 3 个碱基：1/256 密度
- **尺度**：5 μm
- **意义**：展示了如何通过控制引物长度来调节分子密度

### Panel B: 基于序列的对象识别
- **内容**：基于序列而非强度阈值的对象识别
- **关键信息**：
  - 为每个像素确定核苷酸序列
  - 与参考序列比对
  - 未对齐像素被去除
  - 核背景噪声被减少
- **尺度**：20 μm
- **意义**：展示了如何克服自发荧光和背景噪声

## 总体结论

Fig. 2 展示了 FISSEQ 技术的两个关键创新：
1. **分区测序**：通过控制引物长度来调节分子密度，解决高密度成像问题
2. **序列识别**：基于序列而非强度来识别对象，克服背景噪声

## 关联 Figures / Extended Data

- **fig. S5**: SOLiD 连接测序细节
- **fig. S8**: 测序错误率分析
- **fig. S9**: 自动化分析流程
