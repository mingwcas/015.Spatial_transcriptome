# Method: smFISH 验证、bulk RNA-seq 与层次聚类

## 原文（Methods）

> Pools of 48 fluorescently-labeled (Quasar 670) oligonucleotide probes per RNA were purchased from Biosearch Technologies. 30-nt probe sequences were taken directly from a random subset of the targeting regions used for the multiplexed measurements. … 10 μL of 250 nM oligonucleotide probes in encoding hybridization buffer (described above) was added to the cell-containing coverslip … Samples were then incubated in a humid chamber inside a 37°C-hybridization oven for 18 hours.
>
> Total RNA was extracted from IMR90 cells cultured as above using the Zymo Quick RNA MiniPrep kit (R1054) according to the manufacturer's instructions. polyA RNA was then selected (NEB; E7490), and a sequencing library was constructed using the NEBNext Ultra RNA library preparation kit (NEB; E7530), amplified with custom oligonucleotides, and 150-bp reads were obtained from on a MiSeq. These sequences were aligned to the human genome (Gencode v18) and isoform abundance was computed with cufflinks (45).
>
> First, the distance between every pair of genes was determined as 1 minus the Pearson correlation coefficient of the cell-to-cell variation of the measured copy numbers of these two RNA species, both normalized by the total RNA counted in the cell. … An agglomerative hierarchical cluster tree was then constructed from these distances using the Unweighted Pair Group Method with Arithmetic mean (UPGMA).
>
> To identify genes that have similar spatial distributions, we subdivided each of the measured cells into 2x2 regions and calculated the fraction of each RNA species present in each of these bins. … we then determined the Pearson correlation coefficient of the region-to-region variation in enrichment of these two RNA species for each cell and averaged the correlation coefficients over ~400 cells imaged in 7 independent data sets.

## 解读

### 意义
用两条独立证据链给 MERFISH 的拷贝数定量"上保险"：一是同一样本上的 conventional smFISH（同一批靶向序列、无编码误差），二是同一细胞系的 bulk RNA-seq（无成像干扰）。同时用层次聚类把逐基因的拷贝数/空间分布，转化为可解释的共调控基因模块与功能假设。

### 输入
- 15 个基因（选自横跨 3 个数量级丰度范围）用于 smFISH 验证；1001 基因实验另验证 10 个 RNA species
- 每 RNA 48 条 Quasar 670 标记探针（Biosearch），30-nt 序列取自 encoding probe 靶向区的随机子集
- IMR90 total RNA → polyA RNA → NEBNext Ultra 文库 → MiSeq 150-bp reads
- MERFISH 输出的每细胞每基因拷贝数矩阵与单分子坐标

### 输出
- MERFISH/smFISH 拷贝数比值：0.82 ± 0.06（15 个 RNA species 的 mean ± SEM）
- 与 bulk RNA-seq 的 Pearson 相关：r = 0.89（140 基因）、r = 0.76（1001 基因，73% 高置信基因）
- 层次聚类树 + 基因分组（140 基因实验 7 组；1001 基因实验约 100 组）+ GO 富集（Tables S2 / S4）
- RNA 空间分布相关性矩阵与 group I / group II（Fig. 4B–E）

### 核心步骤
1. smFISH 验证：每 RNA 用 48 条 Quasar 670 探针（250 nM，10 μL），37°C 杂交 18 h；encoding wash buffer 37°C 洗 3 次 ×10 min；2×SSC 洗 3 次后用同一成像几何成像。
2. bulk RNA-seq：Zymo Quick RNA MiniPrep 提 total RNA → polyA 富集（NEB E7490）→ NEBNext Ultra 建库（NEB E7530）+ 客户定制寡核苷酸扩增 → MiSeq 150-bp reads → 比对 Gencode v18 → Cufflinks 计算 isoform 丰度（FPKM）。
3. 共变分析：对每对基因计算细胞间拷贝数变异的 Pearson r（拷贝数先按细胞内 RNA 总数归一化），距离 = 1 − r。
4. UPGMA 凝聚层次聚类，按树内基因顺序重排相关矩阵；在树上取阈值切出基因组（140 基因约 10 组、每组 ≥4 个成员；1001 基因约 100 组、每组 ≥3 个成员）。
5. 组内显著性：计算该基因与组内其他成员的平均相关 减去 与组外基因的平均相关，用 Student's t 检验给出 p 值（Tables S2 / S4）。
6. 空间分布分析：把每个细胞切成 2×2 区域，计算每个 RNA 在各 bin 中的占比，再除以该 bin 所有基因的平均占比得 enrichment；对每对 RNA 计算 bin 间 enrichment 变异的 Pearson r，并在 ~400 个细胞 / 7 个数据集上平均；随后用同一层次聚类分组。
7. 核/细胞边缘距离：用亮度阈值分割核与细胞边缘，测量每个分子到最近核边界与最近细胞边缘的距离；仅使用 ≥10 counts/cell 的 RNA species 以降低统计误差。
8. GO 富集：对每组基因计算"组内具有该 GO term 的基因比例 ÷ 全部被测基因具有该 term 的比例"，用超几何分布给出 p 值，只保留 p < 0.05。

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| smFISH 探针数 | 48 条/RNA | Biosearch Quasar 670 |
| smFISH 探针浓度 | 250 nM，10 μL | 覆盖一片 coverslip |
| smFISH 杂交 | 37°C, 18 hours | 直接杂交到细胞 RNA |
| smFISH 洗涤 | encoding wash buffer, 37°C, 10 min × 3 | 去除非特异信号 |
| smFISH 验证基因数 | 15（140 基因实验）/ 10（1001 基因实验） | 覆盖 3 个数量级丰度 |
| 拷贝数比值 | 0.82 ± 0.06 | MERFISH/smFISH，与 80% calling rate 一致 |
| RNA 提取 | Zymo Quick RNA MiniPrep（R1054） | total RNA |
| polyA 选择 | NEB E7490 | 去 rRNA |
| 建库 | NEBNext Ultra（NEB E7530） | + 定制寡核苷酸扩增 |
| 测序 | MiSeq, 150-bp reads | 比对 Gencode v18 |
| 定量 | Cufflinks | isoform 丰度（FPKM） |
| MERFISH vs RNA-seq | r = 0.89（140 基因）；r = 0.76（1001 基因） | Pearson |
| 聚类距离 | 1 − Pearson r | 拷贝数按细胞内总 RNA 归一化 |
| 聚类算法 | UPGMA（凝聚式） | 距离取组间基因对算术平均 |
| 分组规模 | 7 组（每组 ≥4）；~100 组（每组 ≥3） | 树阈值切割 |
| 空间 binning | 每细胞 2×2 区域 | 更细 binning 未产生更显著分组 |
| 细胞数（空间分析） | ~400 cells / 7 independent data sets | 相关系数取平均 |
| 距离分析门槛 | ≥10 counts/cell | 降低距离值统计误差 |
| GO 富集 | 超几何检验，p < 0.05 | 用最新 human GO 注释及上下级 term |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Quasar 670 | Biosearch 的橙色荧光染料，用于 conventional smFISH 探针 |
| FPKM | fragments per kilobase per million reads，bulk RNA-seq 的标准化丰度 |
| Fano factor | 方差 ÷ 均值；Poisson 过程为 1，>1 表示超散布 |
| Pairwise correlation coefficient | 两个基因在细胞间表达变异的 Pearson r |
| Enrichment（空间） | 某 RNA 在某一 bin 的占比 ÷ 该 bin 全部基因的平均占比 |
| UPGMA | 非加权配对算术平均法，凝聚式层次聚类 |
| Group（基因组） | 在聚类树上按阈值切出的、内部相关性显著更强的基因集合 |
| Confidence ratio | 精确匹配数 ÷ 一位错匹配数，用于筛选可信基因 |

## 复现
- 软件：Cufflinks v2.1（isoform 丰度）、BLAST+、Gencode v18 注释、scipy/sklearn（UPGMA、超几何检验）
- 试剂：Biosearch Quasar 670 探针；Zymo R1054；NEB E7490 / E7530；Illumina MiSeq
- 关键调用：

```python
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
from scipy.stats import pearsonr, hypergeom

R = np.corrcoef(counts_norm)          # genes x cells, normalized by total RNA per cell
D = 1 - R
Z = linkage(squareform(D, checks=False), method="average")   # UPGMA
groups = fcluster(Z, t=threshold, criterion="distance")
# spatial: 2x2 bins per cell -> enrichment -> mean Pearson r over ~400 cells
# GO enrichment: hypergeom p-value, keep p < 0.05
```

## 生物学意义
这套分析把 MERFISH 从"能测很多基因"变成"能提出生物学假设"：140 基因实验中 Group 1（ECM：FBN1/FBN2/COL5A/COL7A/TNC/VCAN/THBS1 + 未注释基因 KIAA1199）→ 预测 KIAA1199 参与 ECM 代谢（后续被证实为透明质酸调节酶）；Group 6（囊泡运输 + 细胞运动）中的未注释基因 KIAA1462 → 预测参与囊泡运输；空间分析中 group I 富集于核周（粗糙内质网共翻译）、group II 富集于细胞外周（与 β-actin mRNA 分布一致）。局限：UPGMA 是一维聚类，任一基因只能属于一个组，无法识别所有共变模块（作者建议用 PCA / k-means）；smFISH 与 RNA-seq 验证的是相对丰度，绝对拷贝数仍有约 20% 的系统性低估。

## 涉及 Figures
- **Fig. 2G–H** — 两个 shuffled codebook 之间 r = 0.94；MERFISH vs bulk RNA-seq r = 0.89。
- **Fig. 3D–E** — 140 基因的 pairwise 相关矩阵、层次聚类树与 7 个基因组的 GO 富集。
- **Fig. 4B–E** — 空间分布相关系数矩阵、group I/II 分布与 GO 富集。
- **Fig. 6A–B** — 1001 基因的 ~100 个共变基因组与 20 个 GO term 富集。
- **Fig. S8** — 15 个基因的 conventional smFISH 验证（含 1001 基因实验的 10 个 species）。
