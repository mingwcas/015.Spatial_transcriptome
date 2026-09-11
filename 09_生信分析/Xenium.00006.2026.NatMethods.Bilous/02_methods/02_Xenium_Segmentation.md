# Method: Xenium Segmentation

## 原文（Methods）
> Unless the multimodal segmentation kit is used, the default 10x segmentation algorithm expands from the nucleus outward—up to 5 µm or until it reaches the boundary of an adjacent cell. In our study, the multimodal segmentation kit was applied only to the 5K panel. Therefore, we used the default 5-µm nuclear expansion-based segmentation for all other panels.
> Several alternative segmentation methods have been developed to improve upon the default 10x approach. In this study, we evaluated Baysor (v0.7.0), ProSeg (v2) and Segger—all of which utilize transcript-level information to guide segmentation. We applied these methods with default arguments to all Xenium samples. Specifically, when running Segger, we used 6,000 tokens for samples from the 5K panel and 500 tokens for others.

## 解读

### 意义
细胞分割是将转录本分配到单个细胞的核心步骤，直接影响数据质量和细胞类型注释准确性。不同分割方法对Xenium数据的下游分析结果有显著影响。

### 输入
- Xenium原始转录本坐标数据（x, y, z）
- DAPI核染色图像
- （5K panel额外）多模态染色图像（核+胞质+膜）

### 输出
- 每个细胞的边界定义（GeoJSON格式）
- 细胞-转录本对应关系
- 分割后的单细胞基因表达矩阵

### 核心步骤
1. **默认10x分割**：核半径5µm扩展至细胞边界
2. **多模态分割**（5K panel）：结合核、胞质、膜染色
3. **Baysor**：基于转录本分布建模的分割
4. **ProSeg**：概率性转录本分配
5. **Segger**：转录本空间信息引导分割

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| expansion_radius | 5µm | 默认核扩展半径 |
| Baysor version | v0.7.0 | - |
| ProSeg version | v2 | - |
| Segger tokens (5K) | 6,000 | 5K panel token数 |
| Segger tokens (others) | 500 | 其他panel token数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Multimodal segmentation | 多模态分割，结合核/膜/胞质染色 |
| GeoJSON | 分割结果的矢量格式 |
| Baysor | 利用转录本空间分布进行细胞分割的工具 |
| ProSeg | 基于转录本坐标的概率分割方法 |

## 复现
- 工具：Baysor v0.7.0 (https://github.com/kharchenkolab/Baysor), ProSeg v2 (https://github.com/dcjones/proseg), Segger (https://github.com/bdsc-tds/segger_dev)
- 代码：https://github.com/bdsc-tds/xenium_analysis_pipeline

## 生物学意义
分割算法直接影响转录本分配：核扩展分割简单但可能包含邻近细胞信号；ProSeg等概率方法能更好处理转录本溢出，但可能引入其他噪声。5K panel因基因数多、光学拥挤风险，推荐使用多模态分割。

## 涉及 Figures
- **Fig. 4a,b** — 不同分割方法的UMAP和细胞类型分离比较
- **ED Fig. 9a** — 乳腺癌panel的分割方法比较
