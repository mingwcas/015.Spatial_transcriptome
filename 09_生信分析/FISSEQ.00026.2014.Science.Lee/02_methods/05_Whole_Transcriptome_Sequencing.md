# 全转录组测序 (Whole Transcriptome Sequencing)

## 原文 (Methods)

We then sequenced the transcriptome in human primary fibroblasts in situ and generated sequencing reads of 27 bases with a median per-base error rate of 0.64%. Using an automated analysis pipeline, we identified 14,960 amplicons with size >5 pixels, representing 4171 genes, of which 13,558 (90.6%) amplicons mapped to the correct annotated strand. We found that mRNA (43.6%) was relatively abundant even though random hexamers were used for RT. Ninety genes with the highest expression counts included fibroblast markers, such as fibronectin (FN1); collagens (COL1A1, COL1A2, COL3A1); matrix metallopeptidases and inhibitors (MMP14, MMP2, TIMP1); osteonectin (SPARC); stanniocalcin (STC1); and the bone morphogenesis–associated transforming growth factor (TGF)–induced protein (TGFBI).

## 解读

### 意义
全转录组测序展示了 FISSEQ 技术在大规模基因表达分析中的应用。通过 27 个碱基的读长，可以检测数千个基因的表达，并与传统的 RNA-seq 方法进行比较。

### 输入
- 人原代成纤维细胞
- 固定和处理的样本

### 输出
- 27 个碱基的测序读数
- 14,960 个扩增子
- 4,171 个基因的表达谱
- 亚细胞定位信息

### 核心步骤
1. **文库构建**：在固定细胞内构建 FISSEQ 文库
2. **测序**：生成 27 个碱基的读数
3. **质量控制**：中位每碱基错误率 0.64%
4. **自动分析**：使用自动化分析流程
5. **对象识别**：识别大小 >5 像素的扩增子
6. **序列比对**：将读数比对到参考基因组
7. **基因注释**：注释基因和转录本

### 关键参数
- 读长：27 个碱基
- 错误率：0.64%（中位每碱基）
- 扩增子数量：14,960 个（>5 像素）
- 基因数量：4,171 个
- 正链对齐率：90.6%
- mRNA 比例：43.6%

## 名词/参数/指标

| 术语 | 定义 |
|------|------|
| 扩增子 | RCA 扩增产生的 DNA 分子 |
| 读长 | 测序读取的碱基数量 |
| 错误率 | 测序错误的碱基比例 |
| 正链对齐率 | 对齐到正确注释链的扩增子比例 |

## 复现

### 所需试剂
- 人原代成纤维细胞
- FISSEQ 文库构建试剂
- 测序试剂

### 所需设备
- 共聚焦显微镜
- 高性能计算设备

## 生物学意义

全转录组测序结果表明：
- FISSEQ 可以检测数千个基因的表达
- 成纤维细胞特征基因（FN1, COL1A1 等）高表达
- mRNA 在随机六聚体引物逆转录下仍占 43.6%
- 与 RNA-seq 相关性良好（Pearson's r = 0.52-0.69）

## 涉及 Figures

- **Fig. 3**: 全转录组原位 RNA-seq
- **fig. S8**: 测序错误率分析
- **fig. S9**: 自动化分析流程
- **fig. S10**: 扩增子比对统计
- **table S1**: 基因表达数据
