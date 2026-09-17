# Method: H&E Staining and Imaging

## 原文（Methods）
> The section was dried before H&E staining by 1 min incubation with isopropanol and air-drying at room temperature. For H&E staining, Mayer's haematoxylin was applied for 5 min, the section was washed ten times in water and incubated with bluing buffer for 2 min. After washing in dH20, the tissue was treated with a 1:1 dilution of eosin Y and 0.45 M tris-acetic acid pH 6 for 1 min. The sections were washed in water and left to air-dry completely before imaging.

## 解读

### 意义
H&E染色提供组织形态学信息，用于细胞分割和组织结构分析，与转录组数据整合实现多模态分析。

### 输入
- 固定在捕获区域上的组织切片
- H&E染色试剂

### 输出
- 高分辨率H&E染色图像
- 用于细胞分割和数据整合的形态学参考

### 核心步骤
1. 组织切片在异丙醇中干燥1分钟
2. 室温下空气干燥
3. 应用Mayer's苏木精染色5分钟
4. 水洗10次
5. 应用蓝化缓冲液2分钟
6. 水洗后应用伊红Y染色1分钟
7. 水洗并完全空气干燥
8. 使用20倍物镜在Keyence BZ-X710显微镜上进行明场成像

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 苏木精染色时间 | 5 min | 细胞核染色时间 |
| 蓝化缓冲液时间 | 2 min | 苏木精蓝化时间 |
| 伊红染色时间 | 1 min | 细胞质染色时间 |
| 成像倍数 | 20x | 显微镜物镜倍数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| H&E | 苏木精-伊红染色，常规组织学染色方法 |
| Mayer's haematoxylin | 苏木精染色液，用于细胞核染色 |
| Eosin Y | 伊红染色液，用于细胞质染色 |
| Bluing buffer | 蓝化缓冲液，用于苏木精显色 |

## 复现
- 工具/代码/URL: 使用标准H&E染色试剂和Keyence显微镜
- 代码片段: 标准H&E染色流程，无特殊代码需求

## 生物学意义
H&E染色是组织病理学的金标准，能够清晰显示组织结构和细胞形态。在Open-ST中，H&E染色图像与转录组数据来自同一切片，实现了形态学和分子信息的精确整合。

## 涉及 Figures
- **Fig. 1D** — H&E染色和成像流程
- **Fig. 2A** — H&E染色图像上的UMI分布
