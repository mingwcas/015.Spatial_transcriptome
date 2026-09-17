# 伤口愈合实验分析 (Wound Healing Assay Analysis)

## 原文 (Methods)

We also sequenced primary fibroblasts in situ after simulating a response to injury, obtaining 156,762 reads (>5 pixels), representing 8102 annotated genes. Pearson's r was 0.99 and 0.91 between different wound sites and growth conditions, respectively. In medium with epidermal growth factor (EGF), 82.7% of the amplicons were rRNA compared to 42.7% in fetal bovine serum (FBS) medium. When the 100 highest ranked genes were clustered, cells in FBS medium were enriched for fibroblast-associated GO terms, whereas rapidly dividing cells in EGF medium were less fibroblast-like with alternative splicing of FN1. In regions containing migrating cells versus contact-inhibited cells, 12 genes showed differences in relative gene expression (Fisher's exact test P < 0.05 and >fivefold change), eight of which were associated with the extracellular matrix (ECM)–receptor–cytoskeleton interaction.

## 解读

### 意义
伤口愈合实验分析展示了 FISSEQ 技术在研究细胞迁移和伤口修复中的应用。通过比较不同条件下的基因表达，揭示了伤口愈合过程中的分子机制。

### 输入
- 模拟伤口愈合的成纤维细胞
- EGF 和 FBS 培养基
- 迁移和接触抑制细胞区域

### 输出
- 156,762 个读数（>5 像素）
- 8,102 个注释基因
- 不同条件下的基因表达谱
- 差异表达基因列表

### 核心步骤
1. **伤口模拟**：在成纤维细胞中模拟伤口反应
2. **FISSEQ 测序**：对不同条件下的细胞进行测序
3. **读数过滤**：过滤 >5 像素的读数
4. **基因注释**：注释 8,102 个基因
5. **条件比较**：比较 EGF 和 FBS 条件
6. **区域分析**：比较迁移和接触抑制细胞区域
7. **差异表达分析**：识别差异表达基因

### 关键参数
- 读数数量：156,762 个
- 基因数量：8,102 个
- 重复性：Pearson's r = 0.99（不同伤口部位）
- 条件相关性：Pearson's r = 0.91（不同生长条件）
- rRNA 比例：EGF 82.7% vs FBS 42.7%
- 差异表达基因：12 个（P < 0.05，>5 倍变化）

## 名词/参数/指标

| 术语 | 定义 |
|------|------|
| 伤口愈合实验 | 模拟细胞迁移和修复的体外实验 |
| EGF | 表皮生长因子 |
| FBS | 胎牛血清 |
| GO 术语 | 基因本体论术语 |
| 差异表达基因 | 在不同条件下表达水平显著不同的基因 |

## 复现

### 所需试剂
- 人原代成纤维细胞
- EGF
- FBS
- 伤口愈合实验试剂

### 所需设备
- 细胞培养设备
- 共聚焦显微镜
- 高性能计算设备

## 生物学意义

伤口愈合实验分析揭示了：
- FISSEQ 可以检测伤口愈合过程中的基因表达变化
- EGF 条件下 rRNA 比例更高
- FBS 条件下成纤维细胞特征更明显
- 迁移细胞中 ECM-受体-细胞骨架相互作用基因差异表达
- 12 个基因在迁移和接触抑制细胞中差异表达

这对于理解伤口愈合、细胞迁移和组织修复具有重要意义。

## 涉及 Figures

- **Fig. 4**: 伤口愈合实验功能分析
- **fig. S13**: 伤口愈合实验补充数据
- **fig. S14**: FN1 选择性剪接
- **table S4**: 差异表达基因列表
