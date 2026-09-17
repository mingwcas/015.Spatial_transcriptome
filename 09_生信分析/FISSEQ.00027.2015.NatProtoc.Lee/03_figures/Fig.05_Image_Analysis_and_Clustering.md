# Fig. 5 — 图像分析、配准与序列聚类示例

## Caption（原文）
> Example of image analysis, registration and sequence clustering. (a) A four-color confocal image stack is deconvolved using a CLME algorithm with ten iterations and a signal-to-noise ratio of two (scale bars, 1 µm). (b) Sequencing images for base 1 and base 4 (left) are aligned using a composite channel across various time points (middle) and then using a composite time projection across various channels (right; scale bars, 5 µm). (c) Individual nonzero pixels are aligned to the reference sequence database (i.e., human RefSeq). Highly related sequences connected to the neighboring pixels are then grouped into a single cluster.

## Panel-by-Panel 解读

### Panel a — 3D反卷积
**结论**：展示原始共聚焦图像与反卷积后图像的对比

**关键数据**：
- CLME算法，10次迭代，SNR=2
- 比例尺1 µm
- 反卷积减少离焦背景，提高碱基判读质量

### Panel b — 图像配准
**结论**：展示多时间点和多通道图像的配准过程

**关键数据**：
- 左：base 1和base 4的原始测序图像
- 中：使用复合通道跨时间点对齐
- 右：使用复合时间投影跨通道对齐
- 比例尺5 µm

### Panel c — 序列比对与空间聚类
**结论**：展示像素级序列比对和空间聚类生成最终数据集

**关键数据**：
- 单个非零像素比对到RefSeq参考数据库
- 空间邻近且序列高度相似的像素聚类为单一对象
- 每个聚类代表一个扩增子
- 最终输出：基因ID、共识序列、x-y位置、聚类大小

## 总体结论
Fig. 5展示了FISSEQ图像分析的三个关键步骤：1）3D反卷积提高图像质量；2）多时间点和多通道图像配准确保位置准确性；3）像素级序列比对和空间聚类将原始图像转化为基因表达数据。这些步骤将原始共聚焦图像转化为包含基因ID、空间坐标和表达量的结构化数据集。

## 关联 Figures / Extended Data
- **Fig. 4** — SOLiD颜色编码
- **Supplementary Fig. 4** — 反卷积参数设置
- **Supplementary Fig. 5** — 配准参数设置
- **Supplementary Videos 1-4** — 配准效果展示
