# Method: Molecule Diffusion Analysis

## 原文（Methods）
> To evaluate the molecule diffusion around and beyond tissue boundaries, we calculated the average expression of marker genes at each layer we defined above. Then we applied the convolve smoothing function of Numpy to fit the continuous gene expression curve at the layers, with the size of the sliding window set to 10. To quantify the molecule diffusion extent, we calculated the left-width-at-half-maximum (LWHM) for the gene expression curve of each sample according to the fitted continuous gene expression curve.

## 解读

### 意义
量化分子在组织边界附近扩散程度的分析方法，用于评估不同技术（V1 vs V2）的空间分辨率。

### 输入
- 边界分层后的基因表达数据
- 标记基因表达值

### 输出
- LWHM值：量化分子扩散程度
- 拟合的基因表达曲线

### 核心步骤
1. 计算每个分层中标记基因的平均表达
2. 使用Numpy convolve进行平滑拟合（窗口大小=10）
3. 计算LWHM值量化扩散程度
4. 比较不同技术/样本的LWHM

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 平滑窗口大小 | 10 | Numpy convolve |
| LWHM | 计算曲线半峰宽 | 分子扩散量化 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| LWHM | Left-width at half-maximum，左半峰宽 |
| Convolve smoothing | 卷积平滑 |

## 复现
- Numpy.convolve函数

## 生物学意义
分子扩散是评估空间转录组技术分辨率的关键指标，LWHM越小表示技术分辨率越高，信号扩散越少。

## 涉及 Figures
- Fig. 1E, 1F (LWHM comparison V1 vs V2)
