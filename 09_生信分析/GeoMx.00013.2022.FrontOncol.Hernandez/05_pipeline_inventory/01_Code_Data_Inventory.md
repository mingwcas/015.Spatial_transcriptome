# 代码与数据清单 — GeoMx DSP Immunoprofiling

> **论文**：Challenges and Opportunities for Immunoprofiling Using a Spatial High-Plex Technology: The NanoString GeoMx® Digital Spatial Profiler
> **DOI**：https://doi.org/10.3389/fonc.2022.890410

---

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| GeoMx Data Analysis Suite (内置) | https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-data-center/ | 商业软件 | DSP 仪器配套，含 QC/归一化/可视化 |
| GeoScript Hub (R scripts) | https://nanostring.com/products/geomx-digital-spatial-profiler/geoscript-hub/ | 开源（NanoString 提供） | 自定义 R 脚本用于高级分析 |
| GeoMx DSP Manual Slide Preparation | https://nanostring.com/wp-content/uploads/2022/06/MAN-10150-01-GeoMx-DSP-Manual-Slide-Preparation-User-Manual.pdf | 产品手册 | 样本制备 SOP |
| GeoMx Morphology Markers | https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-morphology-markers/ | 产品页面 | VM 选择参考 |
| GeoMx 蛋白分析产品页 | https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-protein-assays/ | 产品页面 | 蛋白 panel 规格 |
| nCounter Analysis System | https://nanostring.com/products/ncounter-systems/ | 商业软件 | 原始计数读取平台 |

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| 论文 PDF（原始文献） | 本地存档 | PDF: `05.2022.FrontOncol.GeoMx_immunoprofiling_opportunities.pdf` | Frontiers in Oncology 2022 综述文章 |
| metadata.json（自动生成） | `01_metadata/metadata.json` | 本地文件 | PDF 元数据提取结果 |
| 临时 markdown 参考文件 | `/tmp/05.2022.FrontOncol.GeoMx_immunoprofiling_opportunities.md` | 临时的 tmp 目录 | PDF 转 markdown 结果（Step 完成后清理） |
| 论文补充材料 | Frontiers in Oncology 文章页面 | https://doi.org/10.3389/fonc.2022.890410 | 文章 PDF 页面提供补充材料下载 |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| DSP 实验流程（组织制备→ROI→收集→计数） | ⚠️ 部分受限 | 需要 NanoString GeoMx DSP 仪器和认证试剂；样本制备和染色需专业设备 |
| ROI 选择与 segmentation | ⚠️ 部分受限 | 需要 DSP 仪器配套软件；可用第三方图像分析软件辅助 |
| nCounter 计数读取 | ⚠️ 部分受限 | 需要 nCounter 分析系统（商业平台） |
| 数据 QC（GeoMx Data Analysis Suite） | ⚠️ 部分受限 | 商业软件；GeoScript Hub 提供部分开源脚本可替代 |
| 归一化分析 | ✅ 可部分复现 | GeoScript Hub R 脚本开源可用；标准方法可在 R/Python 中自行实现 |
| 热图可视化 | ✅ 可完全复现 | GeoMx 内置；标准 R (pheatmap) / Python (seaborn) 可替代 |
| 统计分析（t-test/Mann-Whitney/线性混合模型） | ✅ 可完全复现 | 开源 R/Python stats 包即可实现 |
| 平台比较分析 | ✅ 可完全复现 | 综述性质，基于文献比较，无需特殊工具 |
| 最佳实践指南（Best Practices） | ✅ 可完全复现 | Bergholtz et al., Cancers 2021 (doi: 10.3390/cancers13174456) 已发表 SOP |

---

### 状态说明

- ✅ **可完全复现**（工具/代码开源可获取）
- ⚠️ **部分受限**（需注册/需商业许可/需专业仪器）
- ❌ **无法直接复现**（需原始样本/专用仪器/无法获取的工具）

---

### 复现建议

1. **完全复现 DSP wet lab 流程**：需要采购 NanoString GeoMx DSP 仪器和相应试剂盒（商业方案）
2. **数据处理 pipeline**：推荐使用 GeoScript Hub 的开源 R 脚本进行 QC 和归一化分析；对于高级统计分析，可使用 R 的 `lme4` 包（线性混合模型）和 `stats` 包（t-test, Mann-Whitney）
3. **热图可视化**：推荐使用 R 的 `pheatmap` 包或 Python 的 `seaborn` 库
4. **文献中的 SOP**：参考 Bergholtz et al., Cancers 2021 的 DSP Best Practices for Breast Cancer Research

---

*清单生成日期：2025*
*遵循 AGENT.md 工作规范*
