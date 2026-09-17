# Method: Immunohistochemistry (IHC)

## 原文（Methods）
> IHC staining was performed on formalin-fixed, paraffin-embedded (FFPE) SCLC tissue sections using an automated BenchMark ULTRA stainer (Roche Diagnostics). Staining was conducted according to the manufacturer's protocol and validated internal laboratory standards. Primary antibodies and dilutions are as follows: ASCL1 (1:200, Abcam ab74065), NEUROD1 (1:150, Abcam ab60704), POU2F3 (1:300, Bioss bs-21046R), and YAP1 (1:80, Abcam ab52771). All stained slides were digitized using a KFBIO slide scanner (KF-PRO-400-HI) at 40× magnification. Protein expression was quantified in tumor regions by a certified pathologist using QuPath (v0.5.1). An H-score was calculated for each marker by combining staining intensity and the percentage of positive tumor cells.

## 解读

### 意义
IHC用于评估SCLC分子亚型分类标志物（ASCL1、NEUROD1、POU2F3、YAP1）的蛋白表达水平，用于SCLC分子亚型与空间细胞组成的相关性分析。

### 输入
- FFPE SCLC组织切片
- 一抗：ASCL1, NEUROD1, POU2F3, YAP1
- BenchMark ULTRA自动染色机 (Roche Diagnostics)
- KFBIO扫描仪 (KF-PRO-400-HI)

### 输出
- 数字化40×放大全切片图像
- H-score量化数据（染色强度×阳性肿瘤细胞百分比）

### 核心步骤
1. FFPE切片准备
2. BenchMark ULTRA自动IHC染色
3. KFBIO切片扫描仪40×数字化
4. QuPath (v0.5.1)病理学家量化
5. 计算H-score

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| ASCL1稀释比 | 1:200 | 一抗稀释比例 |
| NEUROD1稀释比 | 1:150 | 一抗稀释比例 |
| POU2F3稀释比 | 1:300 | 一抗稀释比例 |
| YAP1稀释比 | 1:80 | 一抗稀释比例 |
| 扫描放大倍数 | 40× | 全切片数字化 |
| 量化工具 | QuPath v0.5.1 | 开源数字病理分析软件 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| H-score | 组织化学评分，结合染色强度和阳性细胞百分比 |
| SCLC分子亚型 | SCLC-A (ASCL1+), SCLC-N (NEUROD1+), SCLC-P (POU2F3+), SCLC-Y (YAP1+) |

## 复现
- 工具/代码/URL：QuPath (v0.5.1) - https://qupath.github.io/
- 抗体：Abcam, Bioss等商业抗体

## 生物学意义
IHC确认了SCLC的四种分子亚型分类（ASCL1、NEUROD1、POU2F3、YAP1），并与空间细胞组成数据整合分析，发现C6亚群特异性地富集于SCLC-Y亚型，而C5和C9分别与不同亚型相关。

## 涉及 Figures
- **Fig. S3E** — 恶性细胞亚群C5、C6、C9与SCLC分子亚型的关联分析
