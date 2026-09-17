# Method: Cell Segmentation Using Cellpose

## 原文（Methods）
> Nuclei were segmented with cellpose 2.2, upon fine-tuning the cyto2 model on pairs of H&E images from the metastatic lymph node sample and manually refined segmentation masks from the same pretrained model. Segmentation of all images was performed with –diameter 20 (~7 μm), –flow_threshold 2, and –cellprob_threshold –1. Segmented nuclei were extended 10 pixels (~3.45 μm), radially and in a non-overlapping manner.

## 解读

### 意义
细胞分割是将转录组数据与单个细胞关联的关键步骤，实现了单细胞水平的空间转录组分析。

### 输入
- H&E染色图像
- 预训练的Cellpose模型

### 输出
- 细胞分割掩码
- 单细胞转录组矩阵

### 核心步骤
1. 使用CUT模型对H&E图像进行预处理和风格迁移
2. 使用微调的Cellpose 2.2模型进行细胞核分割
3. 应用径向扩展（10像素，约3.45 μm）以包含细胞质区域
4. 对于含有脂肪细胞的样本，使用两轮分割策略
5. 合并不同大小的分割掩码
6. 将转录本分配到分割的细胞中

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Cellpose直径 | 20 pixels (~7 μm) | 预期细胞核大小 |
| 流阈值 | 2 | 分割流动阈值 |
| 细胞概率阈值 | -1 | 细胞检测概率阈值 |
| 径向扩展 | 10 pixels (~3.45 μm) | 细胞核到细胞质的扩展距离 |
| 脂肪细胞直径 | 100 pixels (~34.5 μm) | 脂肪细胞分割直径 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Cellpose | 基于深度学习的细胞分割算法 |
| 径向扩展 | 从细胞核边界向外扩展以包含细胞质区域 |
| 分割掩码 | 标记每个像素属于哪个细胞的图像 |
| IoU | 交并比，用于评估分割精度 |

## 复现
- 工具/代码/URL: https://github.com/MouseLand/cellpose
- 代码片段:
```python
from cellpose import model
model = model.CellposeModel(gpu=True, pretrained_model='cyto2')
masks, flows, styles = model.eval(image, diameter=20, flow_threshold=2, cellprob_threshold=-1)
```

## 生物学意义
细胞分割的准确性直接影响下游分析的质量。Open-ST使用微调的Cellpose模型和径向扩展策略，能够适应不同组织类型和细胞大小，为异质性组织提供可靠的单细胞分割。

## 涉及 Figures
- **Fig. 1E** — 细胞分割和数据整合流程
- **Fig. S1G-H** — 分割模型性能评估
