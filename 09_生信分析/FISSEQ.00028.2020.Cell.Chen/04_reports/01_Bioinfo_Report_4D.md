# 四维度生信分析报告 — FISSEQ 2020 Cell Chen

> **论文信息**
> - **标题**: Spatial Transcriptomics and In Situ Sequencing to Study Alzheimer's Disease
> - **作者**: Wei-Ting Chen, Ashley Lu, Katleen Craessaerts, et al.
> - **期刊**: Cell, 2020, 182(4), 976-991
> - **DOI**: 10.1016/j.cell.2020.06.038
> - **平台**: Spatial Transcriptomics (ST) + In Situ Sequencing (ISS)
> - **完成日期**: 2026-09-18

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 空间转录组 | Spatial Transcriptomics (ST) | Spatial Transcriptomics平台, Illumina NextSeq500 | 每个TD平均31,283±7,441 UMI, 6,578±987基因 |
| 原位测序 | In Situ Sequencing (ISS) | Cartana AB定制探针 | 84个基因（PIGs和细胞标记物）的单细胞分辨率表达 |
| Aβ负荷定量 | 像素强度标准差分析 | 自定义ImageJ脚本 | Aβ指数与基因表达相关性r=0.39 |
| WGCNA共表达网络 | 加权基因共表达网络分析 | R WGCNA包 | 鉴定PIGs（57基因）和OLIG（165基因）模块 |
| 差异表达分析 | 线性模型 | R limma/edgeR | 识别Aβ相关差异表达基因 |
| 功能富集分析 | GO/KEGG通路分析 | GOrilla, DAVID | PIGs富集于补体、溶酶体、免疫通路 |
| 细胞类型分配 | 基于标记物的puncta分配 | 自定义R脚本 | PIGs主要由小胶质细胞和星形胶质细胞贡献 |
| 原位杂交验证 | RNAscope ISH | ACD Bio RNAscope | 验证补体成分C1qa、C4、Clu的细胞表达 |
| 人类样本验证 | ISS on human brain | Cartana AB | 45个PIGs和42个OLIGs在人类AD大脑中验证 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|--------------|
| Fig. 1 | 空间转录组实验设计和质量控制 | t-SNE聚类, 组织切片 |
| Fig. 2 | Aβ负荷与基因表达关联 | 免疫染色, 散点图, RNAscope |
| Fig. 3 | PIGs鉴定和细胞类型关联 | 热图, 维恩图, 散点图 |
| Fig. 4 | ISS验证PIGs细胞分辨率 | ISS图像, 同心环分析 |
| Fig. 5 | PIGs共表达网络动态 | Circos图, 网络可视化 |
| Fig. 6 | OLIG模块时空响应 | 散点图, 3D曲面图, RNAscope |
| Fig. 7 | 人类大脑PIGs/OLIGs验证 | ISS图像, 定量条形图 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 样本制备 | 冷冻切片, H&E染色 | 标准组织学 | 开源 |
| ST文库构建 | Spatial Transcriptomics试剂盒 | Lot#10001 | 商业 |
| 测序 | Illumina NextSeq500 | - | 商业 |
| 数据预处理 | STAR aligner | 标准版本 | 开源 |
| 空间分析 | 自定义R/Python脚本 | - | 论文自带 |
| WGCNA | R WGCNA包 | 最新版 | 开源 |
| ISS成像 | 共聚焦显微镜 | Zeiss | 商业 |
| 图像分析 | ImageJ/FIJI | 最新版 | 开源 |
| 统计分析 | R (limma, edgeR) | 最新版 | 开源 |
| 可视化 | ggplot2, Circos | 最新版 | 开源 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| WGCNA | 无监督聚类 | 识别共表达基因模块（PIGs, OLIG） |
| 线性模型 (limma) | 统计建模 | 差异表达分析，校正批次效应 |
| t-SNE | 降维可视化 | 转录组数据点聚类和可视化 |
| 基于标记物的细胞分配 | 启发式算法 | 将ISS puncta分配给细胞类型 |
| 同心环分析 | 空间统计 | 量化基因表达与Aβ斑块的距离依赖性 |
| Pearson相关分析 | 相关性分析 | 验证ST与RNAscope结果的一致性 |
| Mann-Whitney U检验 | 非参数检验 | 比较不同Aβ负荷组的基因表达差异 |
| Benjamini-Hochberg校正 | 多重检验校正 | 控制假阳性率 |

---

## 局限性分析

1. **样本量**: 小鼠模型样本量有限，人类样本仅6个个体
2. **技术平台**: 使用早期Spatial Transcriptomics平台（100μm直径），分辨率有限
3. **探针设计**: ISS仅检测84个预设基因，非全转录组
4. **时间点**: 仅3、6、12、18个月四个时间点，可能遗漏关键变化窗口
5. **脑区覆盖**: 主要关注皮层和海马，其他脑区分析有限
6. **验证方法**: RNAscope仅验证少数基因，未进行大规模验证
7. **纵向设计**: 每个时间点独立小鼠，非真正的纵向追踪
8. **Aβ模型**: AppNL-G-F模型可能不完全代表人类AD
9. **统计功效**: 某些分析（如环1的PIGs）统计功效有限
10. **机制研究**: 描述性研究为主，未深入机制验证

---

## 生物学意义

本研究首次将空间转录组学应用于阿尔茨海默病研究，揭示了淀粉样斑块周围的多细胞基因共表达网络。主要发现：

1. **PIGs网络**: 57个Aβ斑块诱导基因，涉及补体系统、溶酶体、氧化应激和炎症
2. **OLIG模块**: 165个少突胶质细胞相关基因，显示早期响应
3. **细胞特异性**: PIGs主要由小胶质细胞和星形胶质细胞贡献
4. **剂量依赖性**: PIGs共表达随Aβ积累逐渐增强
5. **人类验证**: 在人类AD大脑中确认了主要发现

这些发现为理解AD病理提供了新的空间维度视角，识别了潜在的治疗靶点。
