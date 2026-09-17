# Method: Tissue Sectioning and H&E Staining

## 原文（Methods）
> This section describes the cryosectioning of the tissue sample and the transferal of sections to the capture area. The tissue sections are stained with hematoxylin and eosin (H&E) and subsequently imaged. This later allows nuclei-based cell segmentation of the aligned imaging and transcriptomics modalities.

## 解读

### 意义
将冷冻组织切片转移到捕获区域并进行 H&E 染色，为后续成像和细胞分割提供组织形态学信息。

### 输入
- OCT 包埋的新鲜冷冻组织
- 捕获区域（来自方法 1）
- 甲醇、异丙醇、苏木精、伊红 Y、蓝化缓冲液

### 输出
- 带有组织切片的捕获区域
- H&E 染色的组织图像

### 核心步骤
1. 将 OCT 包埋组织放入冷冻切片机平衡 20 分钟
2. 准备预冷的甲醇用于固定
3. 切割 10 μm 厚度的组织切片
4. 将捕获区域放在组织切片上，组织会融化到捕获区域上
5. 在 -20°C 甲醇中固定 30 分钟
6. 用异丙醇脱水
7. 苏木精染色 5 分钟
8. 蓝化缓冲液处理 2 分钟
9. 伊红 Y 染色 1 分钟
10. 使用 20× 物镜明场成像

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 切片厚度 | 10 μm | 组织切片厚度 |
| 固定时间 | 30 min | 甲醇固定时间 |
| 苏木精染色 | 5 min | 细胞核染色时间 |
| 伊红染色 | 1 min | 细胞质染色时间 |
| 成像倍率 | 20× | 显微镜物镜倍率 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| OCT | Optimal Cutting Temperature，冷冻切片包埋介质 |
| Cryosection | 冷冻切片 |
| H&E | Hematoxylin and Eosin，苏木精-伊红染色 |
| Cryostat | 冷冻切片机 |
| Methanol fixation | 甲醇固定，用于保存 RNA |

## 复现
- 工具/代码/URL：Keyence BZ-X710 显微镜或任何明场显微镜
- 成像设置：
```
Channel: Brightfield
Camera: Color
Transmitted light: 100%
Aperture Stop: 20%
Resolution: High resolution
Objective: 20× 0.75/1.00 mm
```

## 生物学意义
H&E 染色是组织病理学的标准方法，可以清晰显示细胞核和细胞质结构。在 Open-ST 中，H&E 图像用于：1）指导细胞分割；2）与转录组数据对齐；3）提供组织形态学背景。甲醇固定同时保存了 RNA 完整性。

## 涉及 Figures
- **Fig. 2** — Tissue section transferral, imaging, and library preparation
