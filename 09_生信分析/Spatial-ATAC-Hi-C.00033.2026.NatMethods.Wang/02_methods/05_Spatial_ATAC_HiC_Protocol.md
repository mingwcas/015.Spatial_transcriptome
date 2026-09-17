# Method: Experimental protocol for Spatial-ATAC-Hi-C

## 原文（Methods）
> Frozen tissue slides were thawed for 10 min at room temperature. Tissue was fixed with formaldehyde (2%) for 20 min and quenched with 2.5 M glycine (final concentration: 0.2 M) for 5 min. After fixation, the tissue was washed twice with 1 ml of DPBS. The device was assembled by putting a PDMS block with a PDMS reservoir capable of holding ~200 μl liquid on top of the slide and then fixed with an acrylic clamp and four sets of screws and nuts. The tissue was permeabilized with 30 μl Lysis Buffer (1 μl of 1 M Tris, pH 8.0, 0.2 μl of 5 M NaCl, 2 μl 10% NP-40 and proteinase inhibitor) at 4 °C for 20 min. We added 36 μl of 10% SDS solution and incubated the tissue section at 62 °C for 10 min depending on tissue type. Next, 30 μl of 1% Triton X-100 was added to the PDMS block and the clamp was covered with parafilm with incubation at 37 °C for 15 min. A total of 20.5 μl of the enzyme mix (11 μl, 10× cut smart buffer, 1 μl 10% Triton X-100, 8 μl DpnII (NEB, R0543L) and 1.5 μl HinfI (NEB, R0155L)) was added with incubation at 37 °C for 1 h after gently tilting the slide. The tissue section was washed twice with 200 μl of deionized water at room temperature for 2–5 min. We then added 50 μl end repair mix (20 μl 0.4 mM biotin-14-dATP; 1 μl of 10 mM dCTP; 1 μl of 10 mM dGTP, 1 μl of 10 mM dTTP, 5 μl of 5 U μl−1 DNA polymerase I, Large (Klenow) Fragment (NEB, M0210L); 5 μl 10× cut smart buffer and 17 μl H2O) with incubation at room temperature for 1 h. Then the ligation mix (10 μl 10× T4 DNA ligation buffer; 1 μl 20 mg ml−1 BSA; 1 μl 10% Triton X-100; 10 μl T4 DNA ligase (NEB, M0202L) and 78 μl H2O) was added and incubated at 16 °C overnight. The tissue section was washed with 200 μl of Pre-tagmentation-wash buffer (1 M Tris pH 7.4; 5 M NaCl, 1 M MgCl2, 10% Tween-20, 5% BSA, H2O) at room temperature for 5 min after removing the ligation mix. Then, 100 µl of transposition mix (7.5 μl of home-made transposome, 50 µl 2× tagmentation buffer, 33 µl 1× DPBS, 1 µl 10% Tween-20, 3.5 µl nuclease-free H2O) was added followed by incubation at 37 °C for 1 h. Next, 100 µl of 40 mM EDTA was added for incubation at room temperature for 5 min to stop transposition. The tissue section was washed twice with 500 µl 1× NEBuffer 3.1 for 5 min after removing all liquid from the reservoir.

## 解读

### 意义
在组织切片上原位执行ATAC-Hi-C联合实验，同时捕获染色质可及性和3D基因组结构信息

### 输入
- 冷冻组织切片（固定在poly-L-lysine包被玻片上）
- PDMS微流控芯片和组装装置
- 各种酶和反应试剂

### 输出
- 完成原位酶处理的组织切片
- DNA片段已进行末端修复、连接和转座标记
- 准备好进行条形码标记的样本

### 核心步骤
1. **组织解冻和固定**：
   - 室温解冻10分钟
   - 2%甲醛固定20分钟
   - 2.5 M甘氨酸淬灭5分钟
   - DPBS洗涤两次

2. **装置组装**：
   - 将PDMS块（带储液池）放在玻片上
   - 用丙烯酸夹具和螺丝固定

3. **组织通透化**：
   - 裂解缓冲液（Tris, NaCl, NP-40, 蛋白酶抑制剂）4°C处理20分钟
   - 10% SDS 62°C处理10分钟
   - 1% Triton X-100 37°C处理15分钟

4. **限制性内切酶消化**：
   - 酶切混合物（DpnII + HinfI）37°C处理1小时
   - 去离子水洗涤两次

5. **末端修复**：
   - 末端修复混合物（含biotin-14-dATP）室温处理1小时

6. **连接反应**：
   - 连接混合物（T4 DNA连接酶）16°C过夜连接

7. **转座反应**：
   - 预转座洗涤缓冲液洗涤
   - 转座混合物（自制转座体）37°C处理1小时
   - 40 mM EDTA终止反应
   - NEBuffer 3.1洗涤两次

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 甲醛浓度 | 2% | 组织固定浓度 |
| 甘氨酸终浓度 | 0.2 M | 甲醛淬灭剂浓度 |
| DpnII酶量 | 8 μl | 限制性内切酶（识别GATC位点） |
| HinfI酶量 | 1.5 μl | 限制性内切酶（识别GANTC位点） |
| 连接温度/时间 | 16°C / 过夜 | T4 DNA连接酶反应条件 |
| 转座温度/时间 | 37°C / 1小时 | Tn5转座反应条件 |
| 生物素标记 | biotin-14-dATP | 用于后续链霉亲和素捕获 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DpnII | 限制性内切酶，识别并切割GATC序列 |
| HinfI | 限制性内切酶，识别并切割GANTC序列 |
| biotin-14-dATP | 生物素标记的dATP，用于标记DNA片段末端 |
| T4 DNA连接酶 | 连接DNA片段的酶 |
| 转座 | Tn5转座酶插入测序接头的过程 |
| EDTA | 金属螯合剂，用于终止酶反应 |

## 复现
- 工具/代码/URL
  - 限制性内切酶：NEB (DpnII: R0543L, HinfI: R0155L)
  - T4 DNA连接酶：NEB (M0202L)
  - DNA聚合酶I大片段：NEB (M0210L)
  - 转座体：自制（见方法2）
- 代码片段
  ```bash
  # Spatial-ATAC-Hi-C实验流程（概念性）
  # 1. 组织固定（2%甲醛，20分钟）
  # 2. 通透化（裂解缓冲液 + SDS + Triton X-100）
  # 3. 酶切（DpnII + HinfI，37°C，1小时）
  # 4. 末端修复（含biotin-14-dATP，室温，1小时）
  # 5. 连接（T4连接酶，16°C，过夜）
  # 6. 转座（自制转座体，37°C，1小时）
  # 7. 终止反应（40 mM EDTA）
  ```

## 生物学意义
Spatial-ATAC-Hi-C实验协议实现了两个关键生物学过程的原位分析：

**ATAC-seq部分（染色质可及性）**：
- Tn5转座酶切割开放染色质区域
- 插入测序接头，标记可及性区域
- 原位操作保持空间信息

**Hi-C部分（3D基因组结构）**：
- 限制性内切酶消化染色质
- 生物素标记用于捕获空间邻近的DNA片段
- 连接反应形成3D基因组相互作用

**联合分析的优势**：
- 同一样本同时获得染色质可及性和3D结构信息
- 空间分辨率保持组织原位信息
- 为理解基因调控提供多层次信息

该方法的技术创新：
- 将ATAC-seq和Hi-C整合到同一实验流程
- 原位操作保持组织空间结构
- 微流控技术实现空间编码

局限性：
- 实验步骤复杂，需要优化多个反应条件
- 组织固定可能影响某些生化反应
- 酶切效率受组织类型和固定程度影响
- 实验时间较长（需要过夜连接）

## 涉及 Figures
- **Fig. 1a** — Spatial-ATAC-Hi-C完整实验流程图
- **Fig. 1b** — 实验原理和步骤示意图
- **Extended Data Fig. 3** — 实验条件优化和验证
