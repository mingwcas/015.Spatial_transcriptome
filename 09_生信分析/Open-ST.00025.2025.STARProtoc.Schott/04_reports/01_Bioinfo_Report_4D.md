# 四维度生信分析报告 — Open-ST 3D Spatial Transcriptomics Protocol

> **论文信息**
> - 论文标题：Protocol for high-resolution 3D spatial transcriptomics using Open-ST
> - DOI：10.1016/j.xpro.2024.103521
> - 期刊：STAR Protocols
> - 年份：2025
> - 平台：Open-ST
> - 第一作者：Marie Schott
> - 完成日期：2025

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 捕获区域生成 | Illumina flow cell repurposing | 3D打印切割导板、DraI酶 | 约360个3×4mm捕获区域/S4 flow cell |
| 组织切片与染色 | Cryosectioning + H&E staining | Cryostat, Keyence BZ-X710 | 10μm切片，20×成像 |
| 透化与逆转录 | Pepsin permeabilization + RT | SuperScript IV | 45min透化，过夜RT |
| 组织去除与二链合成 | Proteinase K digestion + Klenow | Ampure XP beads | 2h二链合成，1.8:1纯化 |
| 文库构建与测序 | PCR扩增 + 大小选择 | KAPA HiFi, BluePippin | 350-1100bp文库，~500M reads |
| 数据处理 | spacemake流程 | spacemake v.0.7.9 | QC报告，h5ad输出 |
| 成像-转录组对齐 | Pairwise alignment | openst v.0.2.3 | 自动/手动对齐 |
| 细胞分割 | Cellpose分割 | Cellpose v.2.2 | 单细胞分辨率 |
| 3D重建 | STIM对齐 | STIM v.0.3.0 | 虚拟组织块 |
| 下游分析 | 聚类、差异表达、可视化 | scanpy v.1.9.3, ParaView v.5.11.0 | 细胞类型识别，3D可视化 |

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|---|---------|------------|
| Fig. 1 | Flow cell打开和捕获区域生成过程 | 实验流程图、照片 |
| Fig. 2 | 组织切片转移、成像和文库构建 | 实验流程图、显微图像、qPCR曲线 |
| Fig. 3 | Flow cell物理结构和数据处理流程 | 示意图、流程图、计算表格 |
| Fig. 4 | spacemake输出结构和质量评估 | 文件树、统计图、空间图 |
| Fig. 5 | 手动配对对齐GUI界面 | GUI截图、流程图 |
| Fig. 6 | Napari细胞分割可视化 | 显微图像叠加、分割掩码 |
| Fig. 7 | 条形码flow cell质量指标 | 热图、柱状图 |
| Fig. 8 | 大小选择前后文库分布 | BioAnalyzer traces |
| Fig. 9 | 跨切片QC评估 | 柱状图、空间QC图 |
| Fig. 10 | 下游分析工作流程 | 流程图、示意图 |

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 条形码映射 | openst flowcell_map | v.0.2.3 | 开源 |
| 读段处理 | spacemake | v.0.7.9 | 开源 |
| 序列比对 | STAR | v.2.7.10b | 开源 |
| rRNA过滤 | Bowtie2 | v.2.5.1 | 开源 |
| 空间映射 | spacemake/openst | v.0.7.9/v.0.2.3 | 开源 |
| 成像-转录组对齐 | openst pairwise_aligner | v.0.2.3 | 开源 |
| 细胞分割 | Cellpose | v.2.2 | 开源 |
| 3D对齐 | STIM | v.0.3.0 | 开源 |
| 下游分析 | scanpy | v.1.9.3 | 开源 |
| 3D可视化 | ParaView | v.5.11.0 | 开源 |
| 图像查看 | Napari | v.0.4.19 | 开源 |
| 图像处理 | Fiji | v.1.53t | 开源 |

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|----------|------|------|
| RANSAC | 几何估计 | 配对对齐中的鲁棒变换估计 |
| Cellpose | 深度学习 | 细胞分割（HE_cellpose_rajewsky模型） |
| Leiden聚类 | 图聚类 | 细胞类型识别 |
| PCA | 降维 | 高维数据可视化 |
| Klenow聚合酶 | 酶促反应 | 第二链cDNA合成（含UMI） |
| Randomer | 随机引物 | UMI生成 |
| Gaussian blur | 图像处理 | 组织隔离和对齐预处理 |

## 局限性与注意事项

1. **样本要求**：仅适用于新鲜冷冻组织，FFPE组织需要方案调整
2. **RNA质量**：依赖poly-dT捕获，RNA降解会影响捕获效率（推荐RIN>7）
3. **3'偏倚**：存在强3'端基因检测偏倚，可能低估内含子读段
4. **空间覆盖**：tile间存在小间隙（约5%总面积），可能导致空间不连续
5. **细胞分割**：基于核分割和径向扩展，可能不准确代表细胞边界（如神经元）
6. **分辨率差异**：x-y平面0.6μm与z轴10μm的分辨率差异可能导致信号混合
7. **3D对齐**：仅支持刚体变换，对折叠或碎片化组织可能对齐不良
8. **条形码纠错**：spacemake v.0.7.9不支持Hamming距离0的纠错，约10%读段无法分配
9. **利益冲突**：E.F., N.K., G.M., N.R., M.S., E.S.为相关专利申请的发明人
