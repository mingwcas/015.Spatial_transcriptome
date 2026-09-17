# Method: Image Analysis and Aβ Quantification

## 原文（Methods）
> HE and Cy3-spot images were acquired from the middle ST sections. Fluorescent amyloid-beta, astrocyte, neuron, and nuclei images were acquired from the two adjacent sections stained by 6E10, anti-Gfap antibody, anti-NeuN antibody, and DAPI. Manually aligned HE and Cy3-spot images were used to bridge the transcriptomics picture with the immunostaining pictures. To de-barcode the spatial localization of each transcriptomic profile, we converted the pixel coordinates of the 1007 TDs on the Cy3-spot image into the theoretical coordinates described in the ID-file of the spatially barcoded array. To acquire the spatially corresponding amyloid and cellular information per TD, we manually aligned and transformed fluorescence images into the corresponding HE images. To annotate the anatomic brain regions, we manually aligned and transformed the reference atlas from Allen Brain Institute into the corresponding HE images. We developed a Fiji groovy script package to automate the image processing and analysis. Spots with coverage area of tissue > 90%, damaged area of tissue < 30%, and coverage area of Cy3-detectable spot > 90% are filtered. We computed 5 parameters for the Aβ, the Gfap, the NeuN and the DAPI staining within each TD: (1) mean pixel intensity, (2) median pixel intensity, (3) sum of pixel intensity, (4) standard deviation of pixel intensity, and (5) percentage of area of the computed positive signals per TD.

## 解读

### 意义
图像分析是将ST转录组数据与组织病理学信息关联的关键步骤，通过图像配准和量化为每个TD提供Aβ负荷、细胞类型和解剖区域的注释。

### 输入
- H&E图像和Cy3-spot图像（ST切片）
- 免疫荧光图像（相邻切片：6E10, GFAP, NeuN, DAPI）
- Allen Brain Atlas参考图谱
- 1007个TD的空间坐标ID文件

### 输出
- 每个TD的Aβ指数（像素强度标准差）
- 每个TD的GFAP、NeuN、DAPI量化值
- 每个TD的解剖区域注释（14个脑区）
- 质量控制后的500-600个有效TD

### 核心步骤
1. 手动对齐H&E和Cy3-spot图像
2. 将Cy3-spot像素坐标转换为理论坐标（de-barcode）
3. 手动对齐免疫荧光图像到H&E图像
4. 使用Allen Brain Atlas标注解剖脑区
5. Fiji groovy脚本自动化图像处理
6. 质量过滤（组织覆盖>90%, 损伤<30%, Cy3覆盖>90%）
7. 专家评估选择最佳量化参数
8. 计算每个TD的5个免疫染色参数

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织覆盖阈值 | >90% | TD质量过滤 |
| 损伤面积阈值 | <30% | TD质量过滤 |
| Cy3覆盖阈值 | >90% | TD质量过滤 |
| Aβ最佳参数 | 像素强度标准差 | 66.51%正确率 |
| GFAP最佳参数 | 阳性面积百分比 | 80.14%正确率 |
| DAPI最佳参数 | 阳性面积百分比 | 79.35%正确率 |
| NeuN最佳参数 | 阳性面积百分比 | 72.13%正确率 |
| 解剖区域数 | 14 | Allen Brain Atlas定义 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Ab index | Aβ指数，TD内6E10像素强度的标准差 |
| De-barcode | 将Cy3像素坐标转换为阵列理论坐标 |
| Landmark correspondences | Fiji图像配准插件 |
| ROI (Region of Interest) | 感兴趣区域 |
| Expert ranking | 专家评估，用于选择最佳量化参数 |
| MWU (Mann Whitney U test) | Mann Whitney U检验 |

## 复现
- 工具/代码/URL
  - Fiji: https://fiji.sc/
  - Fiji groovy script package（论文自带）
  - Allen Brain Atlas: https://mouse.brain-map.org/
- 代码片段
```groovy
// Fiji Groovy脚本核心步骤
// 1. 图像对齐和坐标转换
// 2. 质量过滤
// 3. 计算5个免疫染色参数
// 参数选择: Aβ用SD, 其他用阳性面积百分比
```

## 生物学意义
图像分析方法学的一个重要创新是使用专家评估来选择最佳的免疫染色量化参数。令人惊讶的是，Aβ负荷的最佳指标是像素强度标准差而非简单的阳性面积，这可能反映了斑块大小和密度的异质性。该方法为每个TD提供了高质量的病理学注释，使得后续的差异表达分析可以与Aβ负荷直接关联。

## 涉及 Figures
- **Fig. 1A-B** — 实验设计和TD分布
- **Fig. 2A-C** — Aβ量化和区域分布
- **Figure S1** — 数据质量控制
