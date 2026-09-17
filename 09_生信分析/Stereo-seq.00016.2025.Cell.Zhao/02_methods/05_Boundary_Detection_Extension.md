# Method: Boundary Detection and Extension in Mouse Brain Tissue

## 原文（Methods）
> To analyze spatial transcriptomics data, we employed SpaceFlow to integrate gene expression data with their spatial locations. We used the default parameter settings to preprocess data and run the model. In particular, the gene with expression in fewer than three cells were removed. As feature inputs, 3000 highly variable genes were selected. The learning rate, training epoch, and regularized weight factor were set at 0.001, 1000, and 0.1, respectively. After training the SpaceFlow model, we conducted spatial segmentation using the sf.segmentation method, setting 50 nearest neighbors and a resolution of 1.2.

> we utilized the st.dd.identify_boundary function from the Spateo package to precisely determine tissue boundaries. Then the mouse brain slices were first processed into binary images, and boundary pixels were extracted and initialized to rough edges using the Contours function from the Python OpenCV library. The edges were smoothed by spline fitting (with a degree of freedom of 8) using Numpy's Polynomial package. After determining the boundaries, KDTree was used to extend 400μm vertically (in both directions) to both sides of the tissue boundaries at a width of 10μm per layer. Moreover, we calculated the dot product of the coordinates between each spot and its nearest boundary line point to determinate the relative position (inside or outside of the region).

## 解读

### 意义
该方法用于精确识别组织边界并进行空间分层分析，用于研究分子扩散现象和组织区域特异基因表达。

### 输入
- 空间转录组表达矩阵
- 空间坐标信息
- SpaceFlow预训练模型参数

### 输出
- 组织边界线坐标
- 边界两侧的空间分层（每层10μm，共400μm）

### 核心步骤
1. 使用SpaceFlow整合基因表达和空间位置
2. 预处理：过滤在<3个细胞中表达的基因
3. 选择3000个高变基因作为特征输入
4. 训练SpaceFlow模型
5. 使用Spateo的st.dd.identify_boundary识别组织边界
6. OpenCV Contours提取边界像素
7. Numpy spline拟合平滑边界（自由度=8）
8. KDTree从边界向两侧扩展400μm（每层10μm）
9. 计算每个spot相对于边界的位置

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 基因过滤阈值 | <3 cells | 表达少于3个细胞的基因 |
| 高变基因数 | 3000 | 特征输入 |
| 学习率 | 0.001 | SpaceFlow训练 |
| 训练轮次 | 1000 | |
| 正则化权重 | 0.1 | |
| 最近邻数 | 50 | sf.segmentation |
| 分辨率 | 1.2 | |
| 边界扩展宽度 | 400μm (每层10μm) | |
| 样条自由度 | 8 | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SpaceFlow | 空间转录组深度学习分割工具 |
| Spateo | 空间转录组分析Python包 |
| LWHM | Left-width at half-maximum，量化分子扩散的指标 |
| KDTree | 空间最近邻搜索算法 |

## 复现
- SpaceFlow: https://github.com/hongleili/SpaceFlow
- Spateo: https://github.com/aristoteleo/spateo-release
- OpenCV: Python cv2 library

## 生物学意义
精确的边界检测是研究组织区域特异性基因表达和分子扩散的基础，对于理解组织结构和功能区室至关重要。

## 涉及 Figures
- Fig. 1D, 1E, 1F (boundary and molecule diffusion analysis)
