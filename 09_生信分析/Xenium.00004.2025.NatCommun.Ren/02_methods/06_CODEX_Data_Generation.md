# Method: CODEX Data Generation

## 原文（Methods）
> Tissues embedded in FFPE were sliced, spread out in RNase-free water at 42 °C, and loaded onto the slides (Fisher Scientific #1255015) within the scan area (with a maximum size of 3.5 × 1.8 cm). The slides were dried at room temperature for 30 min and baked at 65 °C for 30 min. The follow-up experiment was carried out after baking overnight at 60 °C. A 16-plex commercial antibody panel was used to target 16 proteins. The sample preparation, tissue staining, and imaging followed the PhenoCycler-Fusion User Guide_2.2.0 (PD-000011 REV M, Akoya Biosciences). After overnight baking, the slides were subjected to deparafﬁnization and antigen retrieval using a sodium citrate solution for 20 min at 11.6PSI/110 °C. Subsequently, the slides were washed using a hydration buffer (P/N 7000017, Akoya Biosciences) and incubated in a staining buffer (P/N 7000017, Akoya Biosciences) at room temperature for 20 min. A mixture of antibodies, blocking solution, and staining solution was prepared. The slides were incubated with the staining mix at room temperature for 3 h. The antibody dilution ratio was determined based on pre-tests, along with the cycle information summarized in Supplementary Data 7. Following staining, the tissues were sequentially fixed with PFA, ice-cold methanol, and a final fixative solution. The slides were washed, loaded onto the PhenoCycler-Fusion instrument (PhenoCycler-Fusion 2.0), and imaged according to the instrument's instructions.
> For the FF samples, cryosections were cut at a thickness of 10 μm in a Leica CM1950 cryostat, loaded onto the slides (Fisher Scientific #1255015) within the scan area (with a maximum size of 3.5 × 1.8 cm) and stored at −80 °C before the experiment. The sample preparation, tissue staining, and imaging followed the PhenoCycler-Fusion User Guide_2.2.0 (PD-000011 REV M, Akoya Biosciences). The slides were dried and warmed for 5 min at room temperature, fixed in acetone for 10 min, incubated with the hydration buffer (P/N 7000017, Akoya Biosciences), fixed with 1.6% PFA for 10 min, and finally balanced with staining buffer (P/N 7000017, Akoya Biosciences) at room temperature for 20 min. A mixture of antibodies, blocking solution, and staining solution was prepared. Then the slides were incubated with the staining mix at room temperature for 3 h. Following staining, the tissues were sequentially fixed with PFA, ice-cold methanol, and a final fixative solution. The slides were washed, loaded onto the PhenoCycler-Fusion instrument (PhenoCycler-Fusion 2.0), and imaged according to the instrument's instructions.

## 解读

### 意义
CODEX（Co-Detection by indexing）是Akoya Biosciences的表型多重蛋白成像平台，使用16-plex抗体面板在相邻组织切片上进行蛋白表达分析，作为本研究的空间蛋白组学ground truth参考，用于评估各ST平台的转录本-蛋白空间一致性。

### 输入
- FFPE组织块或冷冻组织块
- Fisher Scientific #1255015载玻片（扫描面积最大3.5 × 1.8 cm）
- 16-plex商业抗体面板（靶向16种蛋白）
- PhenoCycler-Fusion 2.0仪器

### 输出
- 多重荧光蛋白图像
- QuPath/StarDist处理的细胞分割结果
- KNN分类器注释的细胞类型

### 核心步骤
**FFPE样本：**
1. 5 μm切片 → 42°C铺展 → 载玻片（最大3.5 × 1.8 cm）→ 室温30 min干燥 → 65°C烤30 min → 60°C过夜烘烤
2. 脱蜡 → 柠檬酸钠抗原修复（11.6PSI/110°C，20 min）
3. 水化缓冲液洗涤 → 染色缓冲液室温20 min
4. 抗体+封闭液+染色液混合液 → 室温3 h孵育
5. 依次PFA → 冰甲醇 → 最终固定液固定
6. 洗涤 → PhenoCycler-Fusion 2.0成像

**冷冻样本：**
1. 10 μm冰冻切片 → -80°C保存
2. 室温5 min干燥 → 丙酮固定10 min → 水化缓冲液孵育 → 1.6% PFA固定10 min → 染色缓冲液平衡20 min
3. 同上抗体孵育和固定流程
4. PhenoCycler-Fusion 2.0成像

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| FFPE切片厚度 | 5 μm |  |
| 冷冻切片厚度 | 10 μm |  |
| 扫描面积 | 最大3.5 × 1.8 cm |  |
| 抗体plex数 | 16-plex | 靶向16种蛋白 |
| 抗原修复 | 柠檬酸钠，11.6PSI/110°C，20 min |  |
| 抗体孵育 | 室温3 h |  |
| 固定液 | PFA → 冰甲醇 → 最终固定液 | 依次固定 |
| 仪器 | PhenoCycler-Fusion 2.0 (Akoya Biosciences) |  |
| 操作指南 | PhenoCycler-Fusion User Guide_2.2.0 (PD-000011 REV M) |  |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CODEX | Co-Detection by indexing，多重蛋白荧光成像 |
| PhenoCycler-Fusion | Akoya的自动化多重成像系统（原Phenocycler） |
| KNN分类器 | k-最近邻分类器，用于CODEX细胞类型注释 |
| StarDist | 基于深度学习的细胞核分割算法 |

## 复现
- 仪器：PhenoCycler-Fusion 2.0 (Akoya Biosciences)
- 耗材：Fisher Scientific #1255015
- 缓冲液：P/N 7000017 (Akoya Biosciences)
- 操作指南：PhenoCycler-Fusion User Guide_2.2.0 (PD-000011 REV M)
- 分割注释工具：QuPath v.0.5.1, StarDist v.0.5.0

## 生物学意义
CODEX作为高分辨率蛋白表达参考，用于评估ST平台的转录本-蛋白空间一致性和细胞类型注释准确性。研究发现Xenium 5K和Visium HD FFPE与CODEX具有更高的空间一致性，证明了其空间定量准确性。

## 涉及 Figures
- **Fig. 3** — 转录本-蛋白相关性评估
- **Fig. 5** — 细胞类型注释与CODEX的空间对齐
- **Fig. 6** — 空间聚类与CODEX的一致性比较
