# Method: Second Harmonic Generation (SHG) Imaging for ECM Profiling

## 原文（Methods）
> Label free imaging of collagen and elastin was performed on a Zeiss LSM 880 NLO equipped with a Plan-Apochromat 10x NA 0.45 objective and a tunable femtosecond titanium-sapphire laser (Chameleon-Ultra II). Using an excitation wavelength of 800 nm, the second-harmonic generation signal from collagen was collected through a 395–405 nm spectral window on to a GaAsP detector and autoﬂuorescence emission from elastin was collected through a 435–480 nm spectral window on to a PMT.

## 解读

### 意义
利用二次谐波成像（SHG）无标记定量检测细胞外基质（ECM）中胶原蛋白和弹性蛋白的含量，将ECM组成与空间转录组数据整合分析。

### 输入
- FFPE组织切片（section 3用于SHG，section 4用于CosMx ST）
- 双光子显微镜采集

### 输出
- 胶原蛋白SHG信号（395-405nm）
- 弹性蛋白自荧光信号（435-480nm）
- 每个细胞邻域的ECM组成量化

### 核心步骤
1. 使用Zeiss LSM 880 NLO双光子显微镜，800nm激发波长
2. SHG信号通过395-405nm滤光片收集胶原蛋白
3. 自荧光通过435-480nm收集弹性蛋白
4. 将SHG图像与CosMx ST数据配准
5. 量化每个细胞50×50μm邻域内的平均胶原和弹性蛋白强度
6. k-means聚类（k=3）识别3个ECM区室

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 显微镜 | Zeiss LSM 880 NLO | 双光子共聚焦显微镜 |
| 物镜 | Plan-Apochromat 10x NA 0.45 | 10倍物镜 |
| 激光 | Chameleon-Ultra II飞秒钛蓝宝石激光器 | 可调谐超快激光器 |
| 激发波长 | 800 nm | 双光子激发波长 |
| 胶原收集窗口 | 395-405 nm | SHG信号检测窗口 |
| 弹性蛋白收集窗口 | 435-480 nm | 自荧光检测窗口 |
| ECM邻域量化面积 | 50×50 μm | 以细胞质心为中心的方形区域 |
| k-means k | 3 | ECM区室聚类数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| SHG | 二次谐波成像（Second Harmonic Generation），无标记检测胶原纤维的非线性光学技术 |
| ECM | 细胞外基质（Extracellular Matrix），由胶原、弹性蛋白等组成的组织支架 |
| Homeostatic ECM | 稳态ECM，富含弹性蛋白，正常肺组织特征 |
| Degraded ECM | 降解ECM，胶原和弹性蛋白均少，肿瘤bed特征 |
| Desmoplastic ECM | 促结缔组织增生ECM，富含胶原，肿瘤进展标志 |
| Matrisome | 基质组，包括ECM结构蛋白、调控因子和ECM相关蛋白 |

## 复现
- SHG显微镜: 需要双光子显微镜（Zeiss LSM 880 NLO或类似）
- Van Gieson染色验证: Verhoef's Van Gieson试剂盒
- 代码: https://github.com/rajewsky-lab/3D_lung

## 生物学意义
SHG成像揭示了TME中ECM的动态组成：从弹性蛋白丰富的稳态ECM到胶原丰富的促结缔组织增生ECM的连续转变，反映了肿瘤进展过程中的ECM重塑。三种ECM区室（homeostatic, degraded, desmoplastic）与多细胞niche高度对应，为理解ECM在肿瘤生物学中的作用提供了空间维度。

## 涉及 Figures
- **Fig. 5A-C** — SHG成像、ECM区室鉴定和空间映射
- **Fig. S5A-B** — Van Gieson染色验证和k-means screeplot
