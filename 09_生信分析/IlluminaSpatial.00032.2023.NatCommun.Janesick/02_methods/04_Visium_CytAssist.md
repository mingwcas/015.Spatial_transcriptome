# Method: Visium CytAssist

## 原文（Methods）
> Whole transcriptome spatial data. Our goal in producing Visium CytAssist data was to obtain whole transcriptome, spatially-barcoded sequence data in serial sections. The histology workflow was performed using the Visium CytAssist Spatial Gene Expression for FFPE (Demonstrated Protocol CG000520). The tissue was sectioned as described in Visium CytAssist Spatial Gene Expression for FFPE – Tissue Preparation Guide (Demonstrated Protocol CG000518). 5 µm sections were placed on a Superfrost™ Plus Microscope Slide (Fisherbrand™) and H&E-stained following deparaffinization. Sections were imaged, decoverslipped, followed by hematoxylin destaining and decrosslinking (Demonstrated Protocol CG000520). The glass slide with tissue section was processed with a Visium CytAssist instrument to transfer analytes to a Visium CytAssist Spatial Gene Expression slide with a 0.42 cm² capture area. The probe extension and library construction steps follow the standard Visium for FFPE workflow outside of the instrument. Libraries were sequenced with paired-end dual-indexing (28 cycles Read 1, 10 cycles i7, 10 cycles i5, 90 cycles Read 2). Sequencing libraries were demultiplexed with bcl2fastq (Illumina). The Space Ranger pipeline v2022.0705.1 (10x Genomics) and the GRCh38-2020-A reference were used to process FASTQ files.

## 解读

### 意义
获取全转录组空间条码化测序数据，揭示细胞类型在组织中的空间分布，并与scFFPE-seq数据整合进行细胞类型反卷积

### 输入
- 5 μm FFPE组织切片（连续切片，与scFFPE-seq相邻）
- 标准玻璃载玻片（Superfrost™ Plus）

### 输出
- 全转录组空间基因表达数据
- 17个空间聚类，中位5712个基因/spot
- H&E染色图像

### 核心步骤
1. 将5 μm FFPE切片置于Superfrost™ Plus载玻片上
2. 去蜡后进行H&E染色并成像
3. 去盖玻片，进行苏木精脱色和去交联处理（Protocol CG000520）
4. 使用Visium CytAssist仪器将分析物从标准载玻片转移至Visium空间基因表达载玻片（0.42 cm²捕获区）
5. 在仪器外进行探针延伸和文库构建（标准Visium for FFPE流程）
6. Illumina NovaSeq测序（28+10+10+90 cycles双端双索引）
7. bcl2fastq解复用，Space Ranger v2022.0705.1处理

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 组织切片厚度 | 5 μm | 标准空间转录组切片厚度 |
| 捕获面积 | 0.42 cm² | Visium CytAssist空间条码区域 |
| 探针集 | 18,536 genes / 54,018 probes | 与scFFPE-seq共享相同探针集 |
| Space Ranger版本 | v2022.0705.1 | 空间转录组数据处理软件 |
| 参考基因组 | GRCh38-2020-A | 10x Genomics人类参考 |
| 测序模式 | PE双端双索引 (28+10+10+90) | Read1 28bp, i7 10bp, i5 10bp, Read2 90bp |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| Visium CytAssist | 10x Genomics空间基因表达平台，通过仪器将分析物从标准载玻片转移至专用条码载玻片 |
| CytAssist仪器 | 将组织切片中的分析物转移至Visium条码化载玻片的自动化设备 |
| Space Ranger | 10x Genomics空间转录组数据处理软件，完成比对、定量和空间聚类 |
| 捕获区域（capture area） | 载玻片上含有空间条码oligo的区域，用于捕获来自组织的mRNA |
| spot | Visium载玻片上的空间捕获点，每个包含多个空间条码，直径约55 μm |
| 反卷积（deconvolution） | 利用单细胞参考数据推断每个空间点中不同细胞类型的比例 |

## 复现
- 工具/代码/URL：Space Ranger v2022.0705.1（10x Genomics），需商业许可
- 代码片段：
```bash
# Space Ranger count
spaceranger count --id=visium_sample \
  --transcriptome=/ref/GRCh38-2020-A \
  --fastqs=/data/fastqs/ \
  --sample=visium_sample \
  --slide=V12F31-034 \
  --area=A1
```

## 生物学意义
Visium CytAssist提供了全转录组空间信息，弥补了scFFPE-seq缺乏空间背景的不足。Visium能够分辨三个空间上不同的肿瘤亚型（DCIS #1、DCIS #2和侵袭性肿瘤），这在病理报告中未被捕捉。Visium还能回收脂肪细胞的转录本——这些细胞在scFFPE-seq解离过程中容易丢失。与scFFPE-seq共享相同探针集使得两种数据类型的整合非常直接。局限性：Visium缺乏真正的单细胞分辨率（spot直径~55 μm），混合细胞类型区域的空间解离不精确。

## 涉及 Figures
- **Fig. 1** — 实验设计示意图，展示Visium CytAssist流程
- **Fig. 2b, c** — Visium空间聚类及H&E参考图像
- **Fig. 5g, h** — Visium识别的三阳性受体区域
- **Supp. Fig. 8b-g** — Visium与Xenium的定量比较
- **Supp. Fig. 10** — Spot interpolation方法
