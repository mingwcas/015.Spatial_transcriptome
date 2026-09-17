# 代码与数据清单 — Spatial-ATAC-Hi-C

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| Spatial-ATAC-Hi-C | https://github.com/wangjuan001/Spatial-ATAC-Hi-C | MIT License | 主分析代码，包含完整pipeline |

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|---------|---------|-----------|------|
| Spatial-ATAC-Hi-C原始数据 | GEO | GSE307620 | 小鼠和人脑组织、GBM及星形细胞瘤样本的空间多组学数据 |
| BICCN snATAC-seq参考数据 | GEO | GSE246791 | 脑细胞图谱单细胞ATAC-seq数据，用于细胞类型注释 |
| snm3C-seq参考数据 | Nemo Archive | - | 单细胞多组学参考数据 |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| 原始数据下载 (GEO) | ✅ 可完全复现 | GSE307620公开可用 |
| 代码获取 | ✅ 可完全复现 | GitHub仓库MIT许可，公开可访问 |
| 质控与比对 (TrimGalore/BBMap) | ✅ 可完全复现 | 开源工具，可通过conda安装 |
| Hi-C处理 (runHiC/pairtools) | ✅ 可完全复现 | 开源pipeline |
| ATAC-seq处理 (Cell Ranger ATAC) | ⚠️ 部分受限 | 需10x Genomics Cell Ranger ATAC（商业软件，有免费学术版） |
| ATAC分析 (ArchR/SnapATAC2) | ✅ 可完全复现 | 开源R/Python包 |
| 多组学整合 (Seurat) | ✅ 可完全复现 | 开源R包 |
| 3D基因组聚类 (ScHiCluster/Higashi) | ✅ 可完全复现 | 开源Python包 |
| 基因组分析 (cooltools/Peakachu) | ✅ 可完全复现 | 开源工具 |
| SV/CNV检测 (EagleC/Delly/Lumpy/NeoLoopFinder) | ✅ 可完全复现 | 开源工具 |
| 数据平滑 (MAGIC) | ✅ 可完全复现 | 开源Python包 |
| 病理分析 (QuPath) | ✅ 可完全复现 | 开源软件 |
| 条形码映射 (AtlasXbrowser) | ✅ 可完全复现 | 开源工具 |
| BICCN参考数据 | ✅ 可完全复现 | GSE246791公开可用 |
| snm3C-seq参考数据 | ⚠️ 部分受限 | Nemo Archive，需检查访问权限 |
| 空间ATAC-Hi-C实验 | ❌ 无法直接复现 | 需PDMS微流控芯片、DBiT-seq平台及新鲜组织样本 |
| 微流控芯片制备 | ❌ 无法直接复现 | 需微加工设备和PDMS材料 |

---

### 复现总结

- **生信分析复现性**: **高** — 大部分计算工具开源，代码公开，主数据存于GEO
- **实验复现性**: **低** — Spatial-ATAC-Hi-C技术依赖定制化微流控平台和新鲜组织样本，非标准实验流程
- **数据获取**: 主要数据(GSE307620)和参考数据(GSE246791)均可公开获取

---

*清单生成日期：2026*
