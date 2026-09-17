# Method: Stereo-seq Chip N Preparation

## 原文（Methods）
> Stereo-seq Chip N are modified by stereo-seq chip T (STOmics, 200CT114). Chip T are generated as described. We use a 15nt oligo (capture generation probe) that is reverse complement to capture probe of chip T and hybridize it with the capture probe in a 5×SSC (Thermo Fisher Scientific, AM9770) at 37°C for 30 minutes. Then we treated the chip T with Exonuclease I (GCATBio, LS-EZ-E-00010O, 0.5 U/μL, 1× Exonuclease I reaction buffer) at 37°C for 30 minutes. Finally, the chip was washed twice with 90°C Nuclease-free water (Thermo Fisher Scientific, AM9937) to strip the capture generation probe, each time for 3 minutes. This produces capture probes containing a 25 nt CID barcode, a 15 deoxynucleotides for cDNA capture and ligation.

## 解读

### 意义
该方法通过酶切处理将Stereo-seq芯片T改造为芯片N，产生新的捕获探针用于后续FFPE样品的RNA捕获。

### 输入
- Stereo-seq Chip T (STOmics, 200CT114)
- 15nt oligo (capture generation probe)
- 5×SSC buffer
- Exonuclease I

### 输出
- Stereo-seq Chip N：含有25nt CID barcode、15deoxynucleotides用于cDNA捕获和连接的捕获探针

### 核心步骤
1. 将15nt oligo与Chip T上的捕获探针在5×SSC中37°C杂交30分钟
2. 用Exonuclease I处理芯片37°C 30分钟
3. 90°C Nuclease-free water洗涤两次，每次3分钟

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 杂交温度 | 37°C | oligo与捕获探针杂交 |
| 杂交时间 | 30分钟 | |
| Exonuclease I浓度 | 0.5 U/μL | 酶切处理 |
| 酶切温度 | 37°C | |
| 酶切时间 | 30分钟 | |
| 洗涤温度 | 90°C | 剥离capture generation probe |
| CID barcode长度 | 25 nt | 坐标身份标识 |
| cDNA捕获长度 | 15 nt | 用于捕获和连接 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| CID (Coordinate Identity) | Stereo-seq中的空间坐标条码 |
| Chip T | 原始Stereo-seq芯片 |
| Chip N | 改造后的新一代芯片 |

## 复现
- 试剂：STOmics 200CT114, Thermo Fisher AM9770, GCATBio LS-EZ-E-00010O
- 原始文献：Chen et al., 2022, Cell

## 生物学意义
Chip N的改造使得探针结构更适合FFPE样品的RNA捕获，为后续随机引物捕获奠定基础。

## 涉及 Figures
- Fig. 1A (workflow diagram)
