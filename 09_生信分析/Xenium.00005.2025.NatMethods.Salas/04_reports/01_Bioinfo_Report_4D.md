# 四维度生信分析报告 — Xenium 数据Utility优化

> 论文信息
> - **论文标题**: Optimizing Xenium In Situ data utility by quality assessment and best-practice analysis workflows
> - **DOI**: 10.1038/s41592-025-02617-2
> - **平台**: Xenium (10X Genomics)
> - **完成日期**: 2025-03-13
> - **第一作者**: Marco Salas
> - **通讯作者**: Mats Nilsson
> - **期刊**: Nature Methods

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|----------|------|-----------|----------|
| 细胞分割 | Cellpose (CPn/CPc) | Cellpose | Nuclei和Cyto模型分割性能评估 |
| 细胞分割 | Mesmer | Deepcell | 不同膨胀半径(r20/r30/r40)表现 |
| 细胞分割 | Baysor | Baysor v1.2.0 | Seg.prior参数优化(0-0.99) |
| 细胞分割 | Watershed | scikit-image | 传统方法基准 |
| 细胞分割 | Xenium原生分割 | 10X Xenium | Cell/Nucleus两种模式 |
| 预处理-归一化 | Library-size | Scanpy | target sum 10/100/1000 |
| 预处理-归一化 | SCTransform | Seurat | 正则化负二项回归 |
| 预处理-特征选择 | HVG | Scanpy/Seurat | True/False可选 |
| 预处理-降维 | PCA | Scanpy | 10/20/30 PCs |
| 预处理-聚类 | Leiden SLM | leidenalg 0.8.10 | 分辨率参数优化 |
| 预处理-聚类 | Louvain | louvain 0.7.2 | 社区检测 |
| SVF识别 | SPACEL | spacel | 层次聚类方法 |
| SVF识别 | SpaGCN | spagcn | 图卷积网络 |
| SVF识别 | STAGATE | stagate | 图注意力网络 |
| SVF识别 | deepST | deepst | 深度学习方法 |
| 平台比较 | SRT平台比较 | - | MERSCOPE/MERFISH/CosMx/Xenium/HS-ISS/MC |
| 评估指标 | ARI/NMI/FMI/VI | scikit-learn | 分割和聚类质量评估 |
| 评估指标 | NCP | 自定义 | 负共表达纯度 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|----------|--------------|
| ED Fig. 4 | Xenium与SRT平台比较：检测效率、转录本分配、NCP | 热图、箱线图、散点图 |
| ED Fig. 5 | 分割策略基准测试：Cellpose/Mesmer/Baysor/Watershed/Xenium | 热图、散点图、ROI图像 |
| ED Fig. 6 | 预处理流程优化：25个数据集、315种配置评估 | 热图、流程图 |
| ED Fig. 7 | SVF识别算法比较：运行时间、性能排名 | 线图、柱状图、空间地图 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|-----------|
| Xenium分析 | Xenium Ranger | - | 商业(10X) |
| 数据预处理 | Scanpy | 1.9.1 | 开源 |
| 数据预处理 | anndata | 0.8.0 | 开源 |
| 空间分析 | squidpy | 1.2.2 | 开源 |
| 聚类 | leidenalg | 0.8.10 | 开源 |
| 聚类 | louvain | 0.7.2 | 开源 |
| 分割 | Cellpose | - | 开源 |
| 分割 | Baysor | 1.2.0 | 开源 |
| 分割 | Mesmer | - | 商业(Deepcell) |
| SVF识别 | SPACEL | - | 开源 |
| SVF识别 | SpaGCN | - | 开源 |
| SVF识别 | STAGATE | - | 开源 |
| 统计分析 | R: Seurat | 4.3.0 | 开源 |
| 统计分析 | R: Giotto | 1.1.2 | 开源 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| Cellpose (CPn/CPc) | 深度学习分割 | 细胞/细胞核分割 |
| Mesmer | 深度学习分割 | 组织细胞分割 |
| Baysor | 贝叶斯分割 | 转录本空间感知分割 |
| Leiden/Louvain | 图聚类 | 细胞类型聚类 |
| SPACEL | 层次聚类 | SVF识别 |
| SpaGCN | 图卷积网络 | 空间域检测 |
| STAGATE | 图注意力网络 | 空间转录组分析 |
| deepST | 深度学习 | 空间转录组分析 |
| SCTransform | 正则化负二项 | 归一化 |

---

## 局限性与利益冲突

### 局限性
1. **样本量限制**: 由于Xenium产品商业化时间较短，可用的数据集有限，n=1的情况较多
2. **无生物重复**: 缺乏足够的生物重复样本，技术重复仅来自小鼠脑数据集
3. **图像基PDF**: Methods全文无法从PDF提取，图注和Figure内容来自OCR
4. **平台依赖**: 主要针对Xenium平台优化，其他平台结论的普适性需验证

### 利益冲突
- 论文未披露明显的利益冲突
- 作者单位包括Stockholm University和Mats Nilsson Lab
- GitHub代码开源可获取

---

## 核心发现总结

1. **分割策略**: Baysor结合分割先验表现最佳，Cellpose和Mesmer是优秀的替代方案
2. **预处理流程**: Library-size归一化(target sum=1000)和HVG选择是关键步骤
3. **SVF识别**: 不同算法在准确性和计算效率间存在权衡，HOTSPOT和SINFONIA速度快
4. **平台比较**: Xenium在检测效率和转录本分配方面与其他SRT平台相当
