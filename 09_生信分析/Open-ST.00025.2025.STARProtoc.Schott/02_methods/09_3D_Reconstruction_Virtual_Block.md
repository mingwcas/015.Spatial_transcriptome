# Method: 3D Reconstruction into Virtual Tissue Block

## 原文（Methods）
> This step integrates multiple 2D Open-ST datasets into a cohesive 3D representation, creating a virtual tissue block. It involves aligning serial tissue sections using STIM (Spatial Transcriptomics as Images) software, which enables the reconstruction of 3D gene expression patterns and tissue architecture from individual 2D datasets.

## 解读

### 意义
将多个 2D 空间转录组数据集整合为 3D 虚拟组织块，重建三维基因表达模式和组织结构。

### 输入
- 多个连续组织切片的分割后 h5ad 文件
- STIM 软件

### 输出
- 3D 对齐的 h5ad 文件
- 3D 可视化结果（使用 ParaView）

### 核心步骤
1. 安装 STIM 软件（通过 mamba）
2. 创建容器数据集，添加各个切片
3. 执行成对切片对齐（st-align-pairs）
4. 执行全局对齐并计算最终变换（st-align-global）
5. 使用 GUI 工具（st-bdv-view, st-bdv-view3d）可视化评估对齐质量
6. 使用 openst from_3d_registration 将 STIM 容器转换为单一 h5ad 对象
7. 使用 ParaView 进行 3D 可视化

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| maxEpsilon | 0 | 最大 epsilon 值 |
| range | 2 | 搜索范围 |
| scale | 0.03 | 缩放因子 |
| skipICP | - | 跳过 ICP（迭代最近点）对齐 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| STIM | Spatial Transcriptomics as Images，基于图像的空间转录组对齐工具 |
| Virtual tissue block | 虚拟组织块，3D 重建的组织模型 |
| Serial sections | 连续切片，从同一组织块连续切割的切片 |
| ParaView | 开源 3D 数据可视化软件 |
| ICP | Iterative Closest Point，迭代最近点算法 |

## 复现
- 工具/代码/URL：
  - STIM: https://github.com/PreibischLab/STIM
  - stimwrap: https://github.com/rajewsky-lab/stimwrap
  - ParaView: https://www.paraview.org
- 代码片段：
```bash
# 安装 STIM
mamba create -n stim -c conda-forge -c bioconda stim
mamba activate stim

# 添加切片到容器
st-add-slice -c openst_3d_example.n5 -i /path/to/sample_1/stitched_segmented.h5ad
st-add-slice -c openst_3d_example.n5 -i /path/to/sample_2/stitched_segmented.h5ad
st-add-slice -c openst_3d_example.n5 -i /path/to/sample_3/stitched_segmented.h5ad

# 成对对齐
st-align-pairs -c openst_3d_example.n5 -n 15 --maxEpsilon 0 --range 2 --scale 0.03

# 全局对齐
st-align-global -c openst_3d_example.n5 --skipICP

# 转换为 h5ad
openst from_3d_registration --input openst_3d_example.n5 --output output.h5ad
```

## 生物学意义
3D 重建是 Open-ST 的独特优势，可以将多个 2D 切片整合为连续的 3D 组织模型。这对于理解组织的空间组织、细胞分布和基因表达的三维模式至关重要。STIM 软件使用基于图像的方法进行对齐，支持刚体变换，可以处理大多数连续切片。用户可以通过 GUI 工具交互式地精调对齐。3D 虚拟组织块可以用于研究发育过程、疾病进展和组织微环境的空间异质性。

## 涉及 Figures
- **Fig. 10** — Typical downstream analysis workflow for Open-ST data (3D visualization)
