# Method: Tissue Handling

## 原文（Methods）
> Formaldehyde fixed tissue or frozen tissue slides were obtained from a commercial source Zyagen (San Diego, CA). The embryo sagittal frozen sections were prepared by Zyagen (San Diego, CA) as following: the freshly dissected embryos were immersed into OCT and snapped frozen with liquid nitrogen. Before sectioning, the frozen tissue block was warmed to the temperature of cryotome cryostat (–20°C). Tissue block was then sectioned into thickness of ~7 μm and placed in the center of a poly-L-lysine coated glass slide (CatLog no. 63478-AS, electron microscopy sciences). The frozen slides were then fixed with 4% formaldehyde or directly kept at –80°C if a long-time storage is needed.

## 解读

### 意义
该方法描述了组织样本的获取和初步处理流程，确保DBiT-seq实验使用的是高质量、低RNA降解的组织样本。

### 输入
- 新鲜解剖的小鼠胚胎
- OCT包埋剂
- 多聚赖氨酸包被的玻璃载玻片

### 输出
- 甲醛固定的组织载玻片
- 冷冻组织载玻片（-80°C储存）

### 核心步骤
1. 新鲜解剖的胚胎浸入OCT包埋剂
2. 液氮速冻
3. 冷冻块在-20°C平衡
4. 切片厚度约7μm
5. 放置在多聚赖氨酸包被的载玻片中心
6. 4%甲醛固定或直接-80°C储存

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织来源 | Zyagen, C57BL/6NCrl胚胎 | 商业来源 |
| 切片厚度 | ~7μm | 标准组织切片厚度 |
| 固定剂 | 4%甲醛 | 交联固定 |
| 储存温度 | -80°C（未固定） | 长期储存 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| OCT | Optimal Cutting Temperature compound，组织包埋剂 |
| Poly-L-lysine coated glass slide | 多聚赖氨酸包被载玻片，增强组织贴附 |

## 复现
- 工具/代码/URL：Zyagen (https://zyagen.com/)
- 关键调用：NA

## 生物学意义
高质量的组织样本是空间组学实验成功的前提。7μm切片厚度适合单细胞级别分析，多聚赖氨酸包被载玻片确保组织在后续实验中不易脱落，甲醛固定保留了RNA-蛋白质的空间关联。

## 涉及 Figures
- 无直接关联

## 备注
本文使用的胚胎样本为E10-E12 C57BL/6小鼠胚胎矢状切面。
