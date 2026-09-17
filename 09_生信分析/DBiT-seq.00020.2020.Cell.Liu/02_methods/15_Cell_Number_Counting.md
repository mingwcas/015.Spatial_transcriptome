# Method: Cell Number Counting in Each Pixel

## 原文（Methods）
> Cell numbers for each pixel were counted manually using DAPI and ethidium homodimer-1 stained tissue images (Figure S1B). The total cell counts were obtained by summing the nucleus numbers in each of the pixels. If a nucleus appeared at the edge of a pixel, we would count it as 1 if more than half of the nucleus lied within the pixel and as 0 if otherwise. A total of 50 pixels were counted and the averaged numbers were reported.

## 解读

### 意义
该方法通过细胞核计数建立像素大小与细胞数的关系，为理解DBiT-seq的空间分辨率提供定量依据。

### 输入
- DAPI和ethidium homodimer-1染色的组织图像
- 50个像素区域

### 输出
- 每个像素的平均细胞数
- 像素大小与细胞数的关系数据

### 核心步骤
1. DAPI和ethidium homodimer-1染色组织
2. 成像获取像素区域图像
3. 手动计数每个像素内的细胞核数
4. 对于边界像素：核面积>50%在像素内计为1，否则计为0
5. 统计50个像素取平均值

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 染料 | DAPI + ethidium homodimer-1 | 细胞核染色 |
| 统计像素数 | 50个 | 充分采样 |
| 边界计数规则 | 核面积>50%计入 | 避免重复计数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| DAPI | 细胞核蓝色荧光染料 |
| Ethidium homodimer-1 | 红色荧光染料，染色死细胞核 |

## 复现
- 工具/代码/URL：NA（手动计数）
- 关键调用：NA

## 生物学意义
像素大小与细胞数的关系是评估空间组学技术的关键指标。论文数据显示10μm像素平均含1.7个细胞，50μm像素平均含25.1个细胞。这说明10μm像素已接近单细胞级别，为后续单细胞分辨率的空间组学分析提供了技术基础。

## 涉及 Figures
- **Fig. 1G** — 细胞数与像素大小关系
- **Fig. S1B** — 细胞核染色图像
