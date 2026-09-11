# Method: Cellpose Segmentation

## 原文（Methods）
> 引用论文 Methods 段落原文（完整抄录，1–5 句）

**来源**: Extended Data Fig. 5 分割策略比较
> Cellpose segmentation was included in the comparison (CPn: nuclei, CPc: cyto models). Hyperparameters for each method are described in methods.

## 解读

### 意义
Cellpose 是一个基于深度学习的细胞分割算法，可自动分割细胞核（nuclei）和细胞质（cytoplasm）模型，适用于 Xenium 空间转录组数据的细胞边界识别。

### 输入
- DAPI 染色图像（细胞核）
- 可选：细胞质标记图像
- 细胞分割参数（模型类型：CPn 或 CPc）

### 输出
- 细胞分割掩膜（mask）
- 分割后的细胞边界
- 分配给每个细胞的转录本

### 核心步骤
1. 加载 DAPI 图像和可选的细胞质标记
2. 选择分割模型（CPn: nuclei model, CPc: cyto model）
3. 运行 Cellpose 分割
4. 生成细胞掩膜
5. 将转录本分配到分割的细胞

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| CPn | nuclei model | 细胞核分割模型 |
| CPc | cyto model | 细胞质分割模型 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Cellpose | 基于深度学习的细胞分割工具 |
| CPn | Cellpose nuclei model，细胞核分割 |
| CPc | Cellpose cyto model，细胞质分割 |
| Segmentation | 细胞边界划分过程 |

## 复现
- 工具/代码/URL：Cellpose (https://github.com/MouseLand/cellpose)
- 代码片段：
```python
# Cellpose segmentation for Xenium data
from cellpose import Cellpose
cp = Cellpose(gpu=True, model_type='nuclei')
masks = cp.eval(dapi_image, diameter=50)
```

## 生物学意义
准确的细胞分割是空间转录组分析的基础，直接影响转录本到细胞的分配准确性。Cellpose 提供了自动化、可重复的分割方案，相比传统方法更加稳健。

## 涉及 Figures
- **ED Fig. 5** — Extended Data Fig. 5 分割策略比较，包含 Cellpose nuclei (CPn) 和 Cellpose cyto (CPc) 模型评估
