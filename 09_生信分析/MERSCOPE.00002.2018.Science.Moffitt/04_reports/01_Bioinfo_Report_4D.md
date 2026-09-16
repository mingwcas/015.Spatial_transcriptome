# 四维度生信分析报告 — 下丘脑视前区分子、空间与功能单细胞图谱

> **论文**：Molecular, spatial, and functional single-cell profiling of the hypothalamic preoptic region
> **作者**：Jeffrey R. Moffitt, Dhananjay Bambah-Mukku, Stephen W. Eichhorn, Eric Vaughn, Karthik Shekhar, Julio D. Perez, Nimrod D. Rubinstein, Junjie Hao, Aviv Regev, Catherine Dulac, Xiaowei Zhuang
> **期刊**：Science 362, eaau5324 (2018) | **DOI**：[10.1126/science.aau5324](https://doi.org/10.1126/science.aau5324)
> **平台**：scRNA-seq + MERFISH | **完成日期**：2026-09-16

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 单细胞转录组 | Drop-seq 改良的液滴式 scRNA-seq，解剖小鼠下丘脑视前区 | droplet-based scRNA-seq | 31,299 个细胞；识别抑制性、兴奋性及非神经元细胞类 |
| scRNA-seq 聚类 | PCA 空间 nearest-neighbor graph + Louvain community detection | Louvain；MAST FDR < 0.01 | 43 个抑制性、23 个兴奋性、3 个 hybrid 神经元集群 |
| 标记基因注释 | 差异表达基因、神经肽/神经调质/转录因子与解剖定位联合注释 | MAST；Allen Brain Atlas | 建立 i1–i45、e1–e24、h1–h3 命名体系 |
| MERFISH 面板 | scRNA-seq 标记基因 + 神经调质基因定向选择 | 135 combinatorial smFISH + 20 sequential FISH | 155 基因，覆盖主要细胞类与最有信息的神经元标记 |
| MERFISH 成像 | 10 μm 组织切片，组合 smFISH、总 polyA mRNA 与 nuclei 共染 | MERFISH | 60 个等距切片中每 5 片成像 1 片，共 12 片；naïve 动物 >400,000 细胞 |
| MERFISH 分割 | 依据 total polyadenylated mRNA 与 nuclei costain 分割 cell soma | 自研图像分析 | 获得单细胞 RNA 分子定位与细胞边界；部分胞外分子提示神经突起/胶质突起 |
| 跨平台整合 | MERFISH 细胞表达谱与 scRNA-seq cluster 平均表达谱相关 | Pearson correlation；z-score profile | 约 90% 神经元集群可用约 75 个最有信息基因恢复；每细胞转录本拷贝数为 scRNA-seq 的 6–8 倍 |
| 空间组织分析 | 细胞空间位置、核团分布、邻域复杂度与纯度 | 邻域 cluster 计数/比例 | ~30% 集群局限单一核团；约半数跨 2–4 个邻近核团 |
| 行为激活 | cFos + MERFISH，比较 parenting、mating、aggression | Binomial test，FDR < 5% | n=3–5 replicates；识别 I-14、I-10、I-15、I-16 等行为特异激活群 |
| 正交验证 | cFos/标记基因双/三重原位杂交；与 Allen Brain Atlas 比较 | ISH，16 μm sections | 验证 cluster marker 与空间核团定位；E-3 与 Sncg/warm-sensitive 表型对应 |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|---------|------------|
| Fig. 1 | 视前区 scRNA-seq 的 tSNE、神经元层级树、marker heatmap | tSNE + heatmap + dendrogram |
| Fig. 2 | Gal、Th、Bdnf/Adcyap1 等既有 marker 细胞的进一步分群 | violin plot |
| Fig. 3 | MERFISH 155 基因测量、主要细胞类、空间组织及与 scRNA-seq 相关性 | 工作流 + 单分子图 + tSNE + 空间图 |
| Fig. 4 | MERFISH 识别的抑制/兴奋神经元 cluster 与 scRNA-seq 对应 | z-score profile + dendrogram + correlation |
| Fig. 5 | neuronal cluster 的局部/弥散空间分布、邻域 complexity/purity | 空间散点 + 核团图 + 统计图 |
| Fig. 6 | Cyp19a1/aromatase、Esr1、Oxtr、Gnrh1 cluster 的空间与分子组织 | expression distribution + 空间图 + 信号模型 |
| Fig. 7 | Gal、Adcyap1、Bdnf cluster 的分区及 Sncg/cFos 原位验证 | 空间图 + violin + ISH |
| Fig. 8 | parenting、mating、aggression 中 cFos 激活 cluster | enrichment barplot + ISH + Venn |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| scRNA-seq | 改良 Drop-seq 液滴平台 | — | ⚠️ 需实验平台 |
| scRNA-seq 聚类 | nearest-neighbor graph + Louvain | — | ✅ 开源算法 |
| 差异表达 | MAST | — | ✅ 开源 |
| MERFISH 成像/分析 | ZhuangLab MERFISH pipeline | — | ✅ 代码公开 |
| 空间聚类对应 | Pearson correlation of z-score profiles | — | 论文自带分析 |
| 原位杂交 | cFos/marker ISH | — | ⚠️ 需实验样本与探针 |
| 解剖定位 | Allen Brain Atlas | — | ✅ 公开资源 |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| Louvain community detection | 图社区发现 | scRNA-seq 与 MERFISH 神经元无监督聚类 |
| PCA | 线性降维 | 构建 nearest-neighbor graph 与表达空间 |
| tSNE | 非线性降维 | 展示 scRNA-seq cluster 结构 |
| Pearson correlation | 相关性度量 | MERFISH cluster 与 scRNA-seq cluster 对应、平均表达谱匹配 |
| MAST | 单细胞差异表达模型 | 筛选 cluster marker（FDR < 0.01） |
| 邻域 complexity/purity | 空间统计指标 | 衡量不同神经元 cluster 的空间混合与局部纯度 |
| Binomial test | 统计检验 | 检验行为后 cFos+ 细胞在特定 cluster 中的富集（FDR < 5%） |
| Allen Atlas 配准/解剖映射 | 参考图谱比较 | 将分子 cluster 映射到下丘脑核团 |

## 局限性

1. scRNA-seq 与 MERFISH 并非同一切片配对测量；cluster 对应依赖表达谱相关而非逐细胞验证。
2. 组织解离使 astrocyte、endothelial、ependymal 等细胞在 scRNA-seq 中比例偏低。
3. MERFISH 只测量 155 个预选基因，约 75 个最有信息基因可恢复约 90% cluster，但无法提供未入 panel 的全转录组信息。
4. 行为刺激动物每只仅测量 4 个切片（naïve 动物 12 片），且 cFos 诱导较弱时可能漏检激活细胞。
5. 核团边界来自 Allen Brain Atlas 与组织 landmark 对齐，存在切片形变与解剖边界不确定性。
6. 论文主文 Materials and Methods 位于 Supplementary Materials；本目录对缺失的补充实验参数明确标注为未在主 PDF 中提供。
