# Method: 碱基判读（Base Calling）

## 原文（Methods）
> Start python, and write base calls to read_data_*.csfasta. The maximum number of missing base calls allowed per read is 6 by default. FISSEQ.ImageData('registered_images','.',6)

## 解读

### 意义
从配准后的图像中识别每个像素的颜色转换序列，转化为SOLiD颜色空间的碱基调用

### 输入
- 配准后的TIFF图像（registered_images文件夹）

### 输出
- read_data_*.csfasta 文件（颜色空间FASTA格式的碱基调用）

### 核心步骤
1. Python中导入FISSEQ模块
2. FISSEQ.ImageData('registered_images', '.', 6) 生成碱基调用
3. 每个读取最多允许6个缺失碱基调用
4. 输出颜色空间FASTA文件

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 最大缺失碱基数 | 6 (默认) | 每个读取允许的缺失碱基调用数 |
| 输出格式 | .csfasta | 颜色空间FASTA |
| Python版本 | 2.7 (Canopy) | 必须使用特定版本 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Color space (csfasta) | SOLiD特有的双碱基颜色编码格式 |
| Base call | 从荧光图像推断的碱基身份 |
| Pixel-level detection | 基于单个像素的颜色转换进行碱基判读 |

## 复现
- 工具：Python 2.7 (Enthought Canopy) + FISSEQ.py模块
- 代码：`FISSEQ.ImageData('registered_images', '.', 6)`
- 关键：必须使用Canopy Python 2.7，其他版本缺少所需模块

## 生物学意义
碱基判读是FISSEQ生物信息学分析的第一步。算法基于像素的特定颜色转换模式识别真实信号，即使在噪声和/或低强度环境中也能工作。颜色空间输出保留了SOLiD双碱基编码的信息，需要在颜色空间中进行后续比对。

## 涉及 Figures
- **Fig. 5c** — 碱基判读与序列聚类示意
- **Fig. 4** — SOLiD颜色编码方案
- **Box 1** — 颜色空间说明
