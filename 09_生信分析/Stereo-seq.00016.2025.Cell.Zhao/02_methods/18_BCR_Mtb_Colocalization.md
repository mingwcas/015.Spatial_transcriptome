# Method: Colocalization of BCR and M. tb

## 原文（Methods）
> To avoid data noise, only spots with more than 1 UMI count of M. tb genes are considered to be valid infected spots. The KDTree function in python Scipy package was used for Nearest Neighbor Search (NNS). The average distance and average

## 解读

### 意义
分析BCR克隆与Mtb感染区域的空间共定位关系，研究免疫细胞如何趋化到感染部位。

### 输入
- Mtb感染spot坐标
- BCR克隆空间分布

### 输出
- BCR克隆与感染区域的空间距离
- 克隆多样性随距离的变化
- 突变频率随距离的变化

### 核心步骤
1. 过滤：仅保留Mtb UMI>1的spot作为有效感染spot
2. 使用KDTree进行最近邻搜索
3. 计算BCR克隆与感染区域的平均距离
4. 分析克隆多样性和突变频率与距离的关系

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| Mtb过滤阈值 | UMI >1 | 有效感染spot |
| 距离计算 | KDTree NNS | |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| KDTree | 空间最近邻搜索 |
| NNS | Nearest Neighbor Search |

## 复现
- Scipy: https://github.com/scipy/scipy
- 版本：1.10.1

## 生物学意义
空间共定位分析揭示了BCR克隆在感染部位的分布规律，支持抗体介导的免疫应答。

## 涉及 Figures
- Fig. 7C, 7D (BCR clone spatial distribution)
