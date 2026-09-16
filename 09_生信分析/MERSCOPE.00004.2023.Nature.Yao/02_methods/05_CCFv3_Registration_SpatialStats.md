# Method: CCFv3配准与空间统计

## 原文（Methods）
> ANTS registration ... (1) 3D global affine (12 dof) ... (2) 2D affine ... (3) 2D multi-scale, symmetric diffeomorphic registration (step size=0.2, sigma=3). We used the Gini function from DescTools ... Shannon ... vegan.

## 解读
### 意义
将MERFISH切片对齐Allen CCFv3并量化区域组成。
### 输入
MERFISH坐标/spot；scRNA区域标签；CCFv3分区。
### 输出
区域归属、富集矩阵、Gini、Shannon、神经元/胶质和递质比例。
### 核心步骤
1. 10×10 µm聚合spot建label map。2. ANTs 3D affine→2D affine→对称微分配准。3. 过滤错配。4. 区域归一化并计算指标。
### 关键参数（本文设置）
|参数|值|含义|
|---|---|---|
|分辨率|10 µm|平面网格|
|形变|step=0.2,sigma=3|局部配准|
|空间分析细胞|3,062,367|51/59切片|
|排除|subclass区域<5%|去错配|

## 名词/参数/指标
|名词|定义|
|---|---|
|Gini|分布不均衡度，0均匀、1单区|
|Shannon|组成丰富度/均匀度指数|

## 复现
- ANTs；DescTools::Gini；vegan::diversity
- `DescTools::Gini(x); vegan::diversity(x, index="shannon")`

## 生物学意义
揭示区域特异性和多样性；空间结论依赖配准准确度。

## 涉及 Figures
- **Fig. 6**；Extended Data Fig. 14–16
