# 四维度生信分析报告 — Molecular cartography of the human down syndrome and trisomic mouse brain

> **论文信息**
> - 标题：Molecular cartography of the human down syndrome and trisomic mouse brain
> - DOI：https://doi.org/10.1038/s41467-025-63752-0
> - 平台：Slide-seq + MERFISH
> - 完成日期：2025年
> - 期刊：Nature Communications

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 单细胞核测序 | snRNA-seq | 10x Chromium + Seurat v5 | 122,663个细胞核，13个主要细胞类型，38个细分类 |
| 空间转录组 | Slide-seqV2 | Curio Bioscience + RCTD | 心室区14,490像素，新皮层159,508像素 |
| 空间转录组 | MERFISH | Vizgen MERSCOPE + Cellpose | >240,000细胞，500基因面板 |
| 蛋白质组 | DIA LC-MS/MS | Spectronaut v18.7 + Orbitrap Astral | 884个差异蛋白(66.7%上调) |
| RNA速率分析 | scVelo | v0.3.1 | DS中NPC分化轨迹减速 |
| 差异表达分析 | MAST | R包 | DS中1,000+ DEGs per cell type |
| 通路富集分析 | GSEA/GO/Reactome | ClusterProfiler v4.10.1 | 细胞周期、翻译、染色质通路下调 |
| 转座元件分析 | SoloTE | v1.09 | LINE1在NPC中去抑制 |
| 微环境分析 | 空间邻近分析 | 自定义(LMM) | oRG near IP减少 |
| 免疫荧光 | IF | Nikon A1R共聚焦 | 4个关键蛋白验证 |
| 批次校正 | Harmony/SCT | Seurat | 多样本整合 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|---------|-------------|
| Fig. 1 | DS与整倍体产前脑细胞类型和空间分布 | UMAP + Dotplot + 空间图 |
| Fig. 2 | NPC转录失调：细胞周期、翻译、SLIT-ROBO通路 | Barplot + 火山图 + 空间图 |
| Fig. 3 | 神经元和胶质细胞转录改变 + 微环境变化 | 火山图 + 热图 |
| Fig. 4 | 分化轨迹改变 + 蛋白质组 + TE去抑制 | UMAP + 火山图 + 热图 |
| Fig. 5 | Ts65Dn小鼠脑空间细胞图谱 | UMAP + 空间分布图 |
| Fig. 6 | Ts65Dn中NPC转录改变 + 微环境异常 | 火山图 + 热图 |
| Fig. 7 | 人鼠比较：保守和分化机制 | 讨论总结 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|---------|
| 单细胞分析 | Seurat | v5 | 开源 |
| 空间去卷积 | RCTD | - | 开源 |
| 细胞分割 | Cellpose | 2.0 | 开源 |
| 差异分析 | MAST | - | 开源 |
| 通路分析 | ClusterProfiler | v4.10.1 | 开源 |
| RNA速率 | scVelo | v0.3.1 | 开源 |
| TE分析 | SoloTE | v1.09 | 开源 |
| 质谱搜库 | Spectronaut | v18.7 | 商业 |
| 批次校正 | Harmony | - | 开源 |
| Doublet检测 | Scrublet | - | 开源 |
| 样本制备 | 10x Chromium | - | 商业 |
| 空间平台 | Curio Slide-seqV2 | - | 商业 |
| 空间平台 | Vizgen MERSCOPE | - | 商业 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| SCTransform | 标准化方法 | 单细胞RNA-seq标准化 |
| Harmony | 批次效应校正 | 多样本整合 |
| UMAP | 降维可视化 | 单细胞数据可视化 |
| RCTD | 空间去卷积 | Slide-seq细胞类型注释 |
| Cellpose | 深度学习分割 | MERFISH细胞分割 |
| Scrublet | 机器学习 | doublet检测 |
| Linear Mixed Effects Model | 统计模型 | 微环境分析 |
| GSEA | 基因集富集 | 通路分析 |
| scVelo | 动力学模型 | RNA速率分析 |

---

## 局限性与利益冲突

### 局限性
1. **样本量限制**：产前人脑组织仅来自窄时间窗口（13-19 PCW），样本量有限
2. **模型局限性**：Ts65Dn小鼠模型与人类DS存在生物学差异，不能完全模拟人类疾病
3. **MERFISH局限**：依赖有限的人工筛选基因面板，可能遗漏重要发现
4. **技术局限**：成像空间转录组依赖细胞边界分割，可能导致转录本错误分配
5. **蛋白质组**：非单细胞水平，无法与snRNA-seq直接配对

### 利益冲突
作者声明无利益冲突 (The authors declare no competing interests)
