# Method: scRNA-seq for Human Skin Biopsy Sample

## 原文（Methods）
> Skin punch biopsies were placed immediately into MACS Tissue Storage Solution (Miltenyi Biotec, 130-100-008) and processed into single-cell suspensions using the Whole Skin Dissociation Kit (Miltenyi Biotec, 130-101-540) according to the manufacturer's recommendations. In brief, the tissue was placed in the enzyme solution and incubated in a 37 °C water bath for 3 hours. Thereafter, the tissue cells were dissociated using the MACS Dissociator (Miltenyi Biotec, 130-093-235), pre-programmed for skin cell isolation (program h-skin-01). The cells were then resuspended in DMEM, and mononuclear cells were isolated by Ficoll-Paque PLUS (GE Healthcare) gradient centrifugation. Single-cell preparations were loaded into the Chromium Controller (10x Genomics) for emulsion generation, and libraries were prepared using the Chromium Single Cell 5′ Reagent Kit for version 1.1 chemistry per the manufacturer's protocol. Libraries were sequenced on the NovaSeq 6000 for gene expression and BCR/TCR libraries.

## 解读

### 意义
从同一皮肤活检样本中获取单细胞RNA测序数据，用于与spatial-CITE-seq数据整合分析和细胞类型注释。

### 输入
- 皮肤穿刺活检组织
- MACS组织保存液
- Whole Skin Dissociation Kit

### 输出
- 单细胞转录组数据（10x Genomics 5'文库）
- BCR/TCR文库

### 核心步骤
1. 皮肤活检立即放入MACS组织保存液
2. 使用Whole Skin Dissociation Kit处理：酶溶液37°C水浴3小时
3. MACS Dissociator机械解离（程序h-skin-01）
4. DMEM重悬，Ficoll-Paque PLUS密度梯度离心分离单核细胞
5. Chromium Controller（10x Genomics）乳液生成
6. Chromium Single Cell 5' Reagent Kit v1.1建库
7. NovaSeq 6000测序（基因表达和BCR/TCR文库）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 解离时间 | 37°C, 3h | 酶解离时间 |
| 解离程序 | h-skin-01 | MACS Dissociator预设程序 |
| 5'试剂盒 | v1.1 chemistry | 10x Genomics试剂版本 |
| 测序平台 | NovaSeq 6000 | 测序系统 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| scRNA-seq | Single-cell RNA sequencing，单细胞RNA测序 |
| Chromium Controller | 10x Genomics单细胞封装仪器 |
| Ficoll-Paque PLUS | 密度梯度离心介质，分离单核细胞 |
| BCR/TCR | B细胞受体/T细胞受体，免疫组库测序 |
| MACS | Magnetic Activated Cell Sorting，磁激活细胞分选 |

## 复现
- 工具/代码/URL
  - Miltenyi Biotec：MACS Tissue Storage Solution（130-100-008）
  - Miltenyi Biotec：Whole Skin Dissociation Kit（130-101-540）
  - Miltenyi Biotec：MACS Dissociator（130-093-235）
  - 10x Genomics：Chromium Single Cell 5' Reagent Kit v1.1
  - GE Healthcare：Ficoll-Paque PLUS
- 代码片段：N/A（标准10x Genomics实验流程）

## 生物学意义
scRNA-seq数据与spatial-CITE-seq数据的整合分析是本文的关键分析策略。通过label transfer，将单细胞水平的细胞类型注释映射到空间像素上，实现了细胞类型的空间可视化。这特别适用于识别COVID-19疫苗注射部位的Tph细胞等稀有免疫细胞亚群。

## 涉及 Figures
- **Fig. 2g** — scRNA-seq和spatial转录组整合分析的UMAP
- **Fig. 2h** — 细胞类型label transfer后的空间分布
- **Extended Data Fig. 7** — scRNA-seq数据质量、加权最近邻分析和SPOTlight去卷积
