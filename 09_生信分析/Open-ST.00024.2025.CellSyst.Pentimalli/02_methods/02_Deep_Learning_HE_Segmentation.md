# Method: Deep Learning-based H&E Whole-Slide Image Segmentation

## 原文（Methods）
> For learning a tissue segmentation model, we collected around 5,000 representative pathologist annotations for 4 morphological sub-categories on H&E tissue morphology: 'Carcinoma', 'Stroma', 'Necrosis', and 'Normal lung' for model training. For the segmentation model, we used a U-Net architecture with a ResNet101 backbone. We trained models over various hyperparameters for 50 epochs using the Adam optimizer and selected the top ﬁve models based on the global F1 performance on a validation set. We then combined these ﬁve models into a mean ensemble, which achieved a global F1 performance of 0.93 on a hold-out test set.

## 解读

### 意义
利用深度学习对全切片H&E图像进行语义分割，自动识别肿瘤、基质、坏死和正常肺组织区域，用于指导ROI选择和空间转录组分析区域。

### 输入
- 全切片H&E染色图像
- ~5,000个病理学家标注的训练样本（4类：癌、基质、坏死、正常肺）

### 输出
- 语义分割图：Carcinoma（红）、Stroma（橙）、Normal lung（未着色）
- 用于选择16mm²的ROI区域

### 核心步骤
1. 收集约5,000个病理学家标注（4个形态学子类别）
2. 使用U-Net + ResNet101架构训练分割模型
3. 多超参数训练50个epoch，Adam优化器
4. 基于验证集F1性能选择top 5模型
5. 5模型集成（mean ensemble），在测试集上达到F1≈0.93

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 架构 | U-Net + ResNet101 | 语义分割网络架构 |
| 训练epoch | 50 | 训练轮次 |
| 优化器 | Adam | 随机梯度下降优化器 |
| 集成模型数 | 5 | top 5模型的mean ensemble |
| 测试集F1 | ~0.93 | 全局F1性能 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| U-Net | 经典的编码器-解码器语义分割网络架构 |
| ResNet101 | 101层残差网络，用作U-Net的编码器骨干网络 |
| 语义分割 | 将图像中每个像素分配到预定义类别的任务 |
| F1 score | 精确率和召回率的调和平均，评估分割性能 |

## 复现
- U-Net: Weng & Zhu, 2015 (IEEE Access)
- ResNet101: He et al., 2016 (CVPR)
- Adam optimizer: Kingma & Ba, 2014 (ICLR)
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
深度学习H&E分割使ROI选择标准化、可重现，避免了人工选择偏倚。选择同时包含肿瘤和癌相关基质的区域进行ST分析，确保了TME的完整表征。该方法可推广至其他肿瘤类型的空间转录组研究中。

## 涉及 Figures
- **Fig. 1B** — 展示H&E全切片语义分割结果和ROI选择
