# Method: A/B compartment analysis

## 原文（Methods）
> Single-pixel A/B compartments were inferred using Higashi at 100-kb resolution96, generating a pixel-by-region PC1 value matrix. Cell type-specific A/B compartments were identified using ArchR97. In brief, the PC1 matrix was first smoothed using the imputeMatrix function, followed by differential analysis using FindAllMarkers. Regions with P < 0.01 and log2 fold change > 0.15 were defined as cell type-specific differential A/B compartment regions. To generate pseudobulk A/B compartment profiles for distinct cell types within a sample, we used cooltools98 to calculate the PC1 value at 100-kb resolution.

## 解读

### 意义
分析Spatial-ATAC-Hi-C数据中的A/B区室结构，识别细胞类型特异性的染色质区室组织

### 输入
- 插补后的Hi-C接触矩阵（100 kb分辨率）
- 细胞类型注释信息
- 参考基因组信息

### 输出
- 单像素A/B区室标签（PC1值矩阵）
- 细胞类型特异性差异A/B区室区域
- 伪批量A/B区室谱

### 核心步骤
1. **单像素A/B区室推断**：
   - 使用Higashi在100 kb分辨率下推断A/B区室
   - 生成像素×区域的PC1值矩阵
   - PC1正值表示A区室（活跃），负值表示B区室（抑制）

2. **细胞类型特异性A/B区室识别**：
   - 使用ArchR进行分析
   - imputeMatrix函数平滑PC1矩阵
   - FindAllMarkers进行差异分析
   - 定义标准：P < 0.01，log2 fold change > 0.15

3. **伪批量A/B区室谱生成**：
   - 使用cooltools计算100 kb分辨率的PC1值
   - 为样本内不同细胞类型生成伪批量谱
   - 用于比较不同细胞类型的区室组织

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 分析工具 | Higashi | 单细胞Hi-C数据分析工具 |
| 分辨率 | 100 kb | A/B区室分析的基因组分辨率 |
| 差异分析工具 | ArchR | 单细胞染色质可及性分析工具 |
| P值阈值 | < 0.01 | 统计显著性阈值 |
| log2FC阈值 | > 0.15 | 差异倍数阈值 |
| 伪批量工具 | cooltools | Hi-C数据分析Python工具包 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| A/B区室 | A区室（活跃区室）和B区室（抑制区室），反映染色质的功能状态 |
| PC1值 | 第一主成分值，用于区分A区室（正值）和B区室（负值） |
| Higashi | 多尺度单细胞Hi-C分析工具，整合图神经网络 |
| cooltools | Hi-C数据分析工具包，用于区室和TAD分析 |
| 伪批量 | Pseudobulk，将多个单细胞数据合并以提高统计功效 |

## 复现
- 工具/代码/URL
  - Higashi: https://github.com/ma-compbio/Higashi
  - ArchR: https://github.com/GreenleafLab/ArchR
  - cooltools: https://github.com/open2c/cooltools
- 代码片段
  ```bash
  # A/B区室分析流程
  
  # 1. Higashi单像素区室推断（Python）
  from higashi.Higashi import Higashi
  # 加载100 kb分辨率的接触矩阵
  # 运行Higashi区室推断
  # 输出PC1值矩阵
  
  # 2. ArchR差异分析（R）
  library(ArchR)
  # 加载PC1矩阵
  # 平滑矩阵：imputeMatrix
  # 差异分析：FindAllMarkers
  # 筛选：P < 0.01 & log2FC > 0.15
  
  # 3. cooltools伪批量分析（Python）
  import cooltools
  # 计算100 kb分辨率的PC1值
  # 按细胞类型分组生成伪批量谱
  ```

## 生物学意义
A/B区室分析揭示了Spatial-ATAC-Hi-C数据的重要生物学特征：

**染色质功能组织**：
- A区室：基因活跃表达的开放染色质区域
- B区室：基因沉默的抑制染色质区域
- 区室组织反映细胞的转录状态

**细胞类型特异性**：
- 不同细胞类型具有不同的A/B区室组织
- 细胞类型特异性区室与基因调控相关
- 揭示细胞身份和功能的表观遗传基础

**空间信息整合**：
- 空间分辨的区室分析揭示组织结构
- 发现空间模式与细胞类型的关联
- 理解组织微环境对染色质结构的影响

该分析方法的优势：
- 单像素分辨率，保留空间信息
- 整合多种工具，分析全面
- 差异分析识别细胞类型特异性区域

局限性：
- 100 kb分辨率限制了精细结构的分析
- 区室推断受数据质量影响
- 差异分析需要足够的重复和样本量
- PC1值解释需要结合其他生物学信息

## 涉及 Figures
- **Fig. 5** — A/B区室分析和细胞类型特异性区室
- **Extended Data Fig. 8** — 区室分析验证和比较
- **Supplementary Fig. 3** — 不同分辨率的区室分析结果
