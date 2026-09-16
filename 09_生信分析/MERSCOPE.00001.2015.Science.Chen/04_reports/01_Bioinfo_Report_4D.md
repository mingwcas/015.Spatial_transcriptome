# 四维度生信分析报告 — MERFISH 原始方法（高多重 RNA 成像）

> **论文**：Spatially resolved, highly multiplexed RNA profiling in single cells
> **作者**：Kok Hao Chen, Alistair N. Boettiger, Jeffrey R. Moffitt, Siyuan Wang, Xiaowei Zhuang
> **期刊**：Science 348, aaa6090 (2015) | **DOI**：[10.1126/science.aaa6090](https://doi.org/10.1126/science.aaa6090)
> **平台**：MERFISH（Multiplexed Error-Robust FISH）— 后续 MERSCOPE 商业平台的原始方法学论文
> **完成日期**：2026-09-16

---

## 维度一：分析方法 / Methods

| 分析类型 | 方法 | 工具/版本 | 关键结果 |
|---------|------|----------|---------|
| 编码方案设计 | 误差稳健组合编码（汉明距离约束） | 自研 MHD4 / MHD2 编码 | 16-bit MHD4 支持 140 个码字；14-bit MHD2 支持 1001 个码字 |
| 探针设计 | 阵列合成 oligopool → 编码探针 | 自研（Table S1/S3/S5） | 编码探针 = 中央 ~30 nt 靶向序列 + 两侧 readout 序列 + PCR 引物；140 基因 ~192 probes/gene，1001 基因 ~94 probes/gene |
| 引物正交性筛选 | 熔解温度 + 重复序列 + GC clamp + BLAST+ 筛查 | BLAST+ | 剔除与人类转录组有 ≥14 nt 连续同源的引物；readout 序列同源性 ≤11 nt、基因组脱靶 ≤14 nt |
| 单分子成像 | 组合标记 + 顺序杂交 + 光漂白循环 | Olympus IX71, 1.45 NA 100× oil, EMCCD Andor iXon-897 | 167 nm/pixel；641 nm (Cy5) / 561 nm (fiducial) / 405 nm (Hoechst)；16 轮（140 基因）或 14 轮（1001 基因） |
| 图像分析 | 多 Gaussian 拟合定位 + fiducial 对齐 + 二进制解码 | 自研 | 对齐误差 ~20 nm；误差纠正后每细胞检出 RNA 分子数 ~4×、species 数 ~2× |
| 性能评估 | Calling rate / misidentification rate 建模与实测 | 自研 + 1→0 误差 10%、0→1 误差 4% | MHD4 calling rate ~80%；MHD2 ~27%（约 1/3） |
| 正交验证 | 常规 smFISH + bulk RNA-seq 比较 | 48 探针/RNA（Biosearch Quasar 670）；NEBNext Ultra + MiSeq 150-bp + Cufflinks | MERFISH vs smFISH 拷贝数比 0.82 ± 0.06；vs RNA-seq Pearson r = 0.89（140 基因）/ 0.76（1001 基因） |
| 共变分析 | 细胞间表达变异的成对相关 + 层次聚类 | UPGMA（距离 = 1 − Pearson r） | 140 基因 → 7 个基因群；1001 基因 → ~100 个基因群 |
| 空间分布分析 | mRNA 空间密度谱的成对相关 + GO 富集 | 自研 + GO | 识别 perinuclear（Group I）与 cell periphery（Group II）两类空间模式 |
| 噪声建模 | Fano factor（方差/均值）分析 | 自研 | 多数基因 Fano factor ≫ 1，显著偏离 Poisson 期望 |

---

## 维度二：结果图表

| 图 | 内容摘要 | 主要图形类型 |
|----|---------|------------|
| Fig. 1 | MERFISH 原理：N-bit 编码、可寻址 RNA 数/calling rate/misidentification rate vs 位数、MHD4 实现示意 | 原理示意图 + 性能曲线 |
| Fig. 2 | 140 基因 MERFISH 实测：16 轮杂交图像、单分子定位、误差纠正前后拷贝数、Fano factor、置信比、与 RNA-seq 相关性 | 荧光图像 + 散点图 + 箱线图 |
| Fig. 3 | 140 基因的细胞间变异与成对相关：相关矩阵、层次聚类 7 群、30 个 GO term 富集 | 相关热图 + 树状图 + 富集图 |
| Fig. 4 | RNA 空间分布：4 个 RNA 的空间模式、空间密度谱相关矩阵、Group I/II 分布、到核/细胞边缘距离 | 单分子空间图 + 相关热图 + 距离分析 |
| Fig. 5 | 1001 基因 MERFISH：单细胞 430 species 定位、与 bulk RNA-seq 相关性、与 140 基因实验重叠基因一致性 | 单分子定位图 + 散点图 |
| Fig. 6 | 1001 基因共变分析：~100 个相关基因群、20 个 GO term 富集、心脏发育与核糖体 RNA 加工新群 | 相关热图 + 树状图 + 富集图 |

---

## 维度三：Pipelines

| 阶段 | 工具 | 版本 | 开源/商业 |
|------|------|------|----------|
| 编码方案生成 | 自研（MHD4/MHD2 码本） | — | 论文自带（Table S1/S3） |
| 寡核苷酸池合成 | 阵列合成 oligopool | — | ⚠️ 商业合成服务 |
| 探针制备 | PCR → IVT → 逆转录 → 纯化 | — | 论文自带（Table S5 模板序列） |
| 引物/readout 筛选 | BLAST+ | — | ✅ 开源 |
| 成像 | Olympus IX71 + EMCCD + 3 激光 | — | ⚠️ 商业仪器 |
| 图像分析 | 自研（Gaussian 拟合 + 解码） | — | 论文自带 |
| smFISH 验证 | Biosearch Quasar 670 探针 | — | ⚠️ 商业探针 |
| Bulk RNA-seq | Zymo Quick RNA MiniPrep + NEBNext Ultra + MiSeq | — | ⚠️ 商业试剂/仪器 |
| 表达定量 | Cufflinks | — | ✅ 开源 |
| 聚类 | UPGMA（自研实现） | — | ✅ 算法公开 |
| GO 富集 | GO 数据库 | — | ✅ 公开 |

---

## 维度四：算法与 AI

| 算法/模型 | 类型 | 用途 |
|-----------|------|------|
| MHD4 编码 | 组合编码理论（汉明距离 = 4，固定 4 个"1"位） | 可检测并纠正单比特错误，支持 140 个码字（16-bit） |
| MHD2 编码 | 组合编码理论（汉明距离 = 2） | 仅可检测错误、不能纠正，支持 1001 个码字（14-bit） |
| 简单二进制编码（对照） | 组合编码 | 使用全部 2^N−1 码字，无误差稳健性 |
| 误差稳健解码 | 最近邻汉明距离解码 + 单比特纠错 | 将实测二进制词映射回码本，纠正 1→0 翻转 |
| 多 Gaussian 拟合 | 亚像素单分子定位算法 | 从荧光图像中定位单分子 spot，精度达 ~20 nm |
| Fiducial 配准 | 基准点对齐算法 | 跨多轮杂交图像对齐 |
| Fano factor 分析 | 统计噪声模型（方差/均值） | 判断基因表达是否偏离 Poisson（即是否存在超散布/转录爆发） |
| 层次聚类（UPGMA） | 无监督聚类 | 基于细胞间表达变异相关性对基因分群 |
| 空间密度谱相关 | 空间统计 | 量化 mRNA 亚细胞分布模式的相似性 |
| 基因调控网络约束 | 相关分析（~10⁴–10⁶ 基因对） | 用共变关系推断基因调控关系、预测未注释基因功能 |

---

## 局限性说明

1. **非全转录组**：140 基因 / 1001 基因均为靶向 panel，非全转录组测量；1001 基因实验中仅 430 个 species 被检出（~43%）。
2. **MHD2 灵敏度下降**：1001 基因实验的 calling rate 约为 140 基因实验的 1/3（~27% vs ~80%），因 MHD2 缺乏纠错能力。
3. **单细胞系验证**：主体验证在 IMR90 人胚肺成纤维细胞系完成，细胞状态相对均一；未在复杂组织中进行高多重测量。
4. **仪器与操作门槛高**：~20 小时连续成像、自定义显微镜与流体/杂交系统，技术门槛显著，是后续 MERSCOPE 商业化要解决的核心痛点。
5. **编码规模与成像轮次权衡**：MHD4 随位数增加可寻址数增长较慢（32-bit/4 个"1"位 → 1240 species），扩展至全转录组需更多轮次或更多"1"位（32-bit/6 个"1"位 → 27,776 species）。
6. **方法学论文性质**：本文是 MERFISH 的方法学开山之作，重点在技术可行性验证（误差稳健性、灵敏度、可扩展性），而非特定生物学问题；生物学结论主要来自基因共变与空间分布的一般性观察。
7. **光漂白依赖**：每轮杂交后需 200 mW 光漂白 3 s，限制了可使用的荧光团与轮次上限。
