# 代码与数据清单 — Open-ST 3D TME Multimodal Profiling

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| 3D_lung (全部分析代码) | https://github.com/rajewsky-lab/3D_lung | 论文未明确 | 复现所有结果和图表的完整代码 |
| STIM v0.2.0 | https://github.com/PreibischLab/STIM | 开源 | 3D空间转录组对齐工具 |
| Cellpose | https://github.com/MouseLand/cellpose | 开源 | 细胞分割 |
| Seurat v4.0.4 | https://satijalab.org/seurat/ | 开源 | 单细胞分析R包 |
| CellChat | http://www.cellchat.org/ | 开源 | 细胞间通讯分析 |
| Slingshot v2.2.1 | https://github.com/kstreet13/slingshot | 开源 | 伪时间分析 |
| ParaView v5.10 | https://www.paraview.org/ | 开源 (BSD) | 3D可视化 |
| Fiji v1.53t | https://imagej.net/software/fiji/ | 开源 | 图像处理 |
| ASHLAR v1.17.0 | — | 开源 | IF图像拼接配准 |
| wsireg 0.3.7 | — | 开源 | 全切片图像配准 |
| Background_subtraction v0.3.3 | https://github.com/SchapiroLabor/Background_subtraction | 开源 | IF背景校正 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| CosMx空间转录组数据 | Zenodo | https://doi.org/10.5281/zenodo.7899173 | 原始和处理后的图像+ST数据 |
| SHG数据 | Zenodo | https://doi.org/10.5281/zenodo.7899173 | 胶原和弹性蛋白SHG图像 |
| 交互式3D浏览器 | MDC Berlin | http://lung-3d-browser.mdc-berlin.de/ | 在线3D数据浏览 |
| 健康肺细胞图谱 | Synapse | syn21041850 | Travaglini et al., 2020 (Nature) |
| NSCLC单细胞数据 | GEO | GSE131907 | Kim et al., 2020 (Nat Commun) |
| FFPE组织样本 | Charité病理研究所 | 不公开 | 临床样本，不对外提供 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 单细胞聚类和细胞类型注释 | ✅ 可完全复现 | Seurat开源，代码和数据均公开 |
| 3D配准 (STIM) | ✅ 可完全复现 | STIM开源，数据在Zenodo |
| 2D/3D邻域分析 | ✅ 可完全复现 | 自定义Python脚本+Seurat，代码公开 |
| 细胞间通讯分析 | ✅ 可完全复现 | CellChat开源，数据公开 |
| 肿瘤伪时间分析 | ✅ 可完全复现 | Slingshot开源，代码公开 |
| SHG ECM分析 | ✅ 可完全复现 | SHG数据在Zenodo，分析代码公开 |
| 成纤维细胞亚聚类 | ✅ 可完全复现 | 基于公开数据和代码 |
| 3D可视化 | ✅ 可完全复现 | ParaView开源，数据公开 |
| CosMx数据采集 | ❌ 无法直接复现 | 需要CosMx仪器和FFPE组织样本 |
| SHG数据采集 | ❌ 无法直接复现 | 需要双光子显微镜和FFPE组织样本 |
| IF数据采集 | ❌ 无法直接复现 | 需要Zeiss Axioscan7和FFPE组织样本 |
| H&E深度学习分割模型训练 | ⚠️ 部分受限 | 需要病理学家标注的训练数据（~5000个标注） |
| Verhoef's Van Gieson染色 | ❌ 无法直接复现 | 需要FFPE组织样本和染色试剂 |
| 交互式3D浏览器 | ✅ 可访问 | http://lung-3d-browser.mdc-berlin.de/ |
