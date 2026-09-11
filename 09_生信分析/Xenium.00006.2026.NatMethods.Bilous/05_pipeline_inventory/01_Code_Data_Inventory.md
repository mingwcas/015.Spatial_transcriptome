# 代码与数据清单 — Xenium敏感性、特异性和信号污染

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| Xenium分析管道 | https://github.com/bdsc-tds/xenium_analysis_pipeline | MIT | Snakemake管道 |
| SPLIT R包 | https://github.com/bdsc-tds/SPLIT | MIT | SPLIT方法实现 |
| 复现分析代码 | https://github.com/bdsc-tds/Bilous2026 | MIT | 图表复现代码 |
| Baysor | https://github.com/kharchenkolab/Baysor | - | 分割工具 |
| ProSeg | https://github.com/dcjones/proseg | - | 分割工具 |
| Segger (修改版) | https://github.com/bdsc-tds/segger_dev | - | 分割工具 |
| ResolVI | https://github.com/bdsc-tds/xenium_analysis_pipeline/issues/83 | - | 讨论页 |
| ovrlpy | https://github.com/HiDiHlabs/ovrl.py | - | 校正工具 |
| RCTD | https://github.com/dmcable/RCTD | - | 细胞类型解卷积 |
| scib-metrics | https://github.com/YosefLab/scib-metrics | - | 批次效应评估 |
| Seurat | https://github.com/satijalab/seurat | - | 单细胞分析 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| Xenium数据（本研究） | NCBI GEO | GSE311609 | 41个组织切片的Xenium数据 |
| snRNA-seq参考（匹配） | cellxgene | https://cellxgene.cziscience.com/collections/bd552f76-1f1b-43a3-b9ee-0aace57e90d6 | 匹配肺和乳腺癌snRNA-seq |
| 外部肺scRNA-seq参考 | cellxgene | https://cellxgene.cziscience.com/collections/edb893ee-4066-4128-9aec-5eb2b03f8287 | 318患者，>100万细胞 |
| 外部乳腺癌scRNA-seq | NCBI GEO | GSE176078 | Wu et al. 2021 |
| IHC图像 | - | - | 2张post-Xenium切片，5个组织样本 |
|  Supplementary Tables | 论文补充材料 | - | 面板基因列表，标记基因集 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| snRNA-seq预处理 | ✅ 可完全复现 | Seurat标准流程，开源代码 |
| Xenium分割 | ⚠️ 部分受限 | 商业平台需Xenium仪器，替代分割开源 |
| RCTD注释 | ✅ 可完全复现 | 开源R包，参考数据公开 |
| 空间溢出分析 | ✅ 可完全复现 | 代码公开，数据可获取 |
| SPLIT校正 | ✅ 可完全复现 | SPLIT包开源，R实现 |
| ResolVI/ovrlpy | ✅ 可完全复现 | 开源工具 |
| 完整管道复现 | ⚠️ 部分受限 | 需Xenium原始数据（商业获取） |
| IHC验证 | ❌ 无法直接复现 | 需相同样本和仪器 |

### 状态说明

- ✅ 可完全复现（工具/代码开源可获取）
- ⚠️ 部分受限（需注册/需商业许可）
- ❌ 无法直接复现（需原始样本/仪器）

## 四、关键发现总结

1. **Xenium数据质量高、可重复性强**：41样本数据显示低技术变异
2. **靶向面板敏感性优于5K panel**：尽管基因数少，但检测深度更高
3. **转录本溢出是普遍问题**：恶性细胞是主要污染源，T细胞最易受影响
4. **SPLIT有效校正污染**：提升细胞类型分离和生物学保真度
5. **ProSeg+SPLIT组合最优**：分割和校正方法可叠加使用
