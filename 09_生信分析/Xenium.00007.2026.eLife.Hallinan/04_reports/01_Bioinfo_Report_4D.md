# 四维度生信分析报告 — Xenium 探针脱靶结合 (OPT)

> **论文**：Evidence of off-target probe binding affecting 10x Genomics Xenium gene panels compromise accuracy of spatial transcriptomic profiling
> **作者**：Caleb Hallinan, Hyun Joo Ji, Edmund Tsou, Steven L. Salzberg, Jean Fan
> **期刊**：eLife 14, RP107070 (2026) | **DOI**：[10.7554/eLife.107070](https://doi.org/10.7554/eLife.107070)
> **平台**：10x Genomics Xenium（v1 Human Breast Panel，313 基因 / 2582 探针）
> **文章类型**：Short Report（计算研究，无新数据产生）
> **完成日期**：2026-09-16

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 探针脱靶预测 | 探针靶序列比对到参考转录组，识别完全同源（完美 40 bp 匹配）或末端允许错配的脱靶位点 | OPT（自研 Python 工具）+ nucmer | 完美同源下 GENCODE v47 检出 121 条探针 / 37 个基因脱靶；`-pl 10` 宽松模式下新增 18 个基因（含 ACTG2） |
| 跨注释一致性 | 用 4 套人类注释重复脱靶预测并取并集 | GENCODE basic v47、GENCODE comprehensive v47、RefSeq v110、CHESS v3.1.3（GRCh38） | 蛋白编码脱靶基因：GENCODE 11 / RefSeq 10 / CHESS 9，并集为 **14 个基因** |
| 转录本序列提取 | 从注释 GFF + 参考基因组提取转录本 FASTA | gffread（GRCh38.p14；CHESS 用 p12） | 剔除 alternative scaffolds；RefSeq 重命名 VD(J) 片段并去除 pseudogene |
| 空间平台交叉验证 | 结构对齐 Xenium 与 Visium CytAssist 切片，比较匹配位置上的表达 | STalign v1.0.1（仿射 + 微分同胚映射） | 307/313 基因共享；重叠区 Visium spots 由 4992 降至 3958；Xenium 聚合到 ~55 μm 分辨率 |
| 空间一致性量化 | 匹配分辨率表达矩阵的 RMSE（相对 y = x）与 Pearson r | 自研（思路类比 STcompare） | MS4A1: RMSE 3.746, r 0.382；APOBEC3B 单独 r = nan → 聚合脱靶后 RMSE 4.465, r 0.160 |
| 单细胞平台交叉验证 | Xenium 与 3′ scRNA-seq 整合后比较簇水平表达 | Harmony v1.2.3（30 PCs, theta = 8）+ PCA + UMAP + Leiden（resolution = 1.0） | 12,388 细胞 / 36,601 基因；TUBB2B 单独 r = 0.015 → 加 TUBB2A 后 r = 0.793 |
| 定制面板评估 | HuBMAP 定制面板 BED → FASTA → OPT，再对照组织匹配 RNA-seq | pyfaidx + pandas + OPT（`-pl 10`） | 胎盘面板 49/300 基因脱靶（34 个在胎盘 RNA-seq 中表达）；多组织面板 24/300（心 13 / 肾 12 / 肺 13 表达） |
| IGV 序列确认 | 目视核对探针与脱靶转录本的比对 | Integrative Genomics Viewer (IGV) | 确认序列层面的脱靶比对真实存在 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|---------|------------|
| Fig. 1 | Padlock 探针脱靶结合并产生假荧光信号的原理 | 原理示意图 |
| Fig. 2 | Xenium vs Visium：MS4A1 一致；APOBEC3B 需聚合脱靶基因才与 Xenium 吻合；307 基因总体相关性 | 组织切片表达热图 + 密度散点图 + 散点图 |
| Fig. 3 | Xenium vs scRNA-seq：Harmony 整合 UMAP；APOBEC3B 聚合验证；313 基因总体相关性 | UMAP 表达图 + 散点图 |
| Table 1 | GENCODE v47 完美同源下 37 个脱靶基因及其 71 个脱靶对象、探针数与基因类型 | 数据表 |
| Appendix 1—fig 1, 2 | 跨注释脱靶差异；14 个蛋白编码脱靶基因并集 | 比对示意 + 集合图 |
| Appendix 1—fig 3 | STalign 结构对齐与 Xenium 分辨率匹配示意 | 组织对齐图 |
| Appendix 1—fig 5–8 | 跨技术 UMAP 嵌入；ACTG2 / TUBB2B 的双平台验证 | UMAP + 散点图 |
| Appendix 1—fig 9, 10 | HuBMAP 定制面板脱靶基因的组织表达热图 | 热图 |
| Appendix 1—fig 11–13 | 脱靶基因表达与否的影响；ADH1B 与 HDC 反例 | 表达图 + 热图 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 探针脱靶预测 | OPT（自研） | — | ✅ 开源（MIT/见仓库） |
| 序列比对引擎 | nucmer (MUMmer) | — | ✅ 开源 |
| 转录本提取 | gffread | — | ✅ 开源 |
| 参考注释 | GENCODE basic/comprehensive、RefSeq、CHESS | v47 / v47 / v110 / v3.1.3 | ✅ 公开 |
| 参考基因组 | GRCh38 | p14（CHESS 用 p12） | ✅ 公开 |
| 空间对齐 | STalign | v1.0.1 | ✅ 开源 |
| 单细胞整合 | Harmony | v1.2.3 | ✅ 开源 |
| 降维聚类 | PCA / UMAP / Leiden | — | ✅ 开源 |
| BED→FASTA | pyfaidx + pandas | — | ✅ 开源 |
| 比对可视化 | Integrative Genomics Viewer (IGV) | — | ✅ 开源 |
| 数据来源平台 | 10x Genomics Xenium / Visium CytAssist / Chromium 3′ scRNA-seq | — | ⚠️ 商业仪器，数据公开 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| nucmer（MUMmer） | 序列比对算法（maximal exact match 锚定） | 探针靶序列 vs 参考转录组比对，寻找完美同源 |
| OPT（flip/track/stat/all 四模块） | 规则/比对驱动的预测流水线 | 预测探针脱靶结合；`-pl` 支持末端容错匹配 |
| Perfect homology 判据 | 序列同源性规则 | 要求 100% identity 且覆盖整条 40 bp query |
| Pad-length 容错匹配 | 启发式序列规则 | 允许末端 10 bp 错配，仅要求中间 20 bp（含连接位点）匹配 |
| 同义词合并规则 | 基因命名实体归一 | 比对到靶基因同义名（如 NARS→NARS1）不算脱靶 |
| STalign（仿射 + 微分同胚度量映射） | 图像配准算法 | 对齐 Xenium 与 Visium 组织切片，构建共同坐标空间 |
| Harmony | 批次效应校正（基于 PCA 的软聚类） | 整合 Xenium 与 scRNA-seq，生成共享 UMAP 嵌入 |
| Leiden | 图社区发现聚类 | 跨技术共享簇划分，用于簇水平表达比较 |
| RMSE + Pearson r | 统计一致性度量 | 量化两平台在匹配位置/簇上的表达一致性 |
| 集合取并集（union across annotations） | 集合运算策略 | 跨 4 套注释取并集，得到 14 个高置信蛋白编码脱靶基因 |

---

## 局限性说明

1. **计算研究，无实验验证**：本文为纯计算研究（Data availability 明确声明"no data have been generated"）；脱靶结论基于序列比对与已有公开数据的**事后**一致性分析，未做探针层面的直接生化验证。
2. **预测 ≠ 影响**：序列比对只能提示"可能脱靶"。若脱靶基因在该组织中不表达，则实际影响可忽略（如 ADH1B → ADH1A/ADH1C 案例）。
3. **无法覆盖全部非特异来源**：OPT 不检测探针自杂交、探针-探针互作等非序列同源机制。论文以 HDC 为例说明——HDC 无预测脱靶，但 Xenium 表达模式与 Visium/scRNA-seq 严重不符，提示存在比对无法捕捉的非特异信号。
4. **面板版本差异**：本文所用面板是 Janesick et al. 的早期版本，与商业版 Xenium v1 Human Breast Panel"高度相似但不完全相同"（Appendix Note），结论外推需谨慎。
5. **注释依赖性**：不同注释（GENCODE basic vs comprehensive vs RefSeq vs CHESS）结果差异显著，反映基因组注释本身仍是活跃研究领域；本文因此采用跨注释并集策略。
6. **交叉验证数据非配对**：Visium 与 scRNA-seq 数据来自同一样本的**连续切片/同组织块**而非同一切片，且 Xenium 与 Visium 分辨率不同（需聚合到 55 μm 才可比），存在对齐误差。
7. **作者立场**：作者团队（JEFworks Lab，Jean Fan）同时是 OPT 工具与 STalign 的开发者，存在工具自评的潜在倾向；但结论有正交平台数据支持。
