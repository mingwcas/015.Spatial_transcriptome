# Method: cDNA Collection and Purification

## 原文（Methods）
> We devised a square well PDMS gasket, which could be aligned and placed on the tissue slide, creating an open reservoir to load lysis buffer specifically to the flow barcoded tissue region to collect cDNAs of interest. Depending on the area of this region, the typical amount of buffer is 10 - 100 μL of Proteinase K lysis solution, which contains 2 mg/mL proteinase K (Thermo Fisher), 10 mM Tris (pH = 8.0), 200 mM NaCl, 50 mM EDTA and 2% SDS. Lysis was carried out at 55°C for 2 hours. The lysate was then collected and stored at –80°C prior to use. The cDNAs in the lysate were purified using streptavidin beads (Dynabeads MyOne Streptavidin C1 beads, Thermo Fisher). The beads (40 μL) were first washed three times with 1X B&W buffer (Ref to manufacturer's manual) with 0.05% Tween-20, and then stored in 100 μL of 2X B&W buffer (with 2 μL of SUPERase In Rnase Inhibitor). To perform purification from stored tissue lysate, it was allowed to thaw, and the volume was brought up to 100 μL by RNase free water. Then, 5 μL of PMSF (100 mM, Sigma) was added to the lysate and incubated for 10 minutes at room temperature to inhibit the activity of Proteinase K. Next, 100 μL of the cleaned streptavidin bead suspension was added to the lysate and incubated for 60 minutes with gentle rotating. The beads with cDNA were further cleaned with 1X B&W buffer for two times and then with 1X Tris buffer (with 0.1% Tween-20) once.

## 解读

### 意义
该方法从组织中回收空间标记的cDNA，并通过生物素-链霉亲和素系统纯化，为后续文库构建提供高质量模板。

### 输入
- 空间条码化的组织载玻片
- Proteinase K裂解液（2mg/mL，10mM Tris pH8.0，200mM NaCl，50mM EDTA，2% SDS）
- Dynabeads MyOne Streptavidin C1 beads（40μL）
- PMSF（100mM）
- B&W buffer

### 输出
- 纯化的空间标记cDNA（结合在链霉亲和素磁珠上）

### 核心步骤
1. 使用方形孔PDMS垫圈对齐放置在载玻片上，形成开放储液池
2. 加入10-100μL Proteinase K裂解液（覆盖组织区域）
3. 55°C裂解2小时
4. 收集裂解物，-80°C储存
5. 40μL链霉亲和素磁珠用1X B&W buffer + 0.05% Tween-20洗3次
6. 重悬于100μL 2X B&W buffer + 2μL SUPERase In
7. 裂解物解冻，RNase-free水补足到100μL
8. 加入5μL PMSF(100mM)抑制Proteinase K，室温10分钟
9. 加入100μL磁珠悬液，旋转孵育60分钟
10. 1X B&W buffer洗2次，1X Tris buffer(0.1% Tween-20)洗1次

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 裂解温度 | 55°C | Proteinase K最适温度 |
| 裂解时间 | 2小时 | 充分消化组织 |
| 磁珠体积 | 40 μL | 充分捕获生物素标记cDNA |
| 捕获时间 | 60分钟 | 充分结合 |
| PMSF抑制 | 10分钟（室温） | 终止蛋白酶活性 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Proteinase K | 蛋白酶K，消化组织蛋白质释放cDNA |
| Streptavidin beads | 链霉亲和素磁珠，捕获生物素标记的cDNA |
| B&W buffer | Bind & Wash buffer，磁珠结合和洗涤缓冲液 |
| PMSF | Phenylmethylsulfonyl fluoride，丝氨酸蛋白酶抑制剂 |

## 复现
- 工具/代码/URL：Dynabeads MyOne Streptavidin C1 (Thermo Fisher, 65001)
- 关键调用：NA

## 生物学意义
cDNA回收是将空间信息从组织转移到可操作分子的关键步骤。Barcode B上的生物素标签使cDNA可以通过链霉亲和素磁珠高效纯化。PDMS方形垫圈的设计确保只有流动条码区域被消化和收集，避免周围组织的污染。

## 涉及 Figures
- **Fig. 1A** — Workflow中包含cDNA收集步骤
