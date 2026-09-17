# Method: Data preprocessing (TrimGalore, BBtools, Cell Ranger ATAC, runHiC)

## 原文（Methods）
> The raw fastq reads adaptors were first detected and trimmed with TrimGalore (v.0.6.10) (https://github.com/FelixKrueger/TrimGalore). The cleaned fastq files were processed using bbduk function from BBtools (BBMap v.39.01) (https://sourceforge.net/projects/bbmap/), retaining only reads that contained linker sequences (linker1 and linker2). The filtered reads were then converted to Cell Ranger ATAC format (10x Genomics). Specifically, the original paired-end fastq files included Read1 and Read2, with Read2 containing both the genomic DNA sequences and barcode sequences. The original Read2 were split into genomic DNA sequences as the new Read1 and barcode (barcode A and barcode B) sequences as new Read2, and the original Read1 sequences were retained as the new Read3. For spatial-ATAC-seq analysis, the resulting fastq files were aligned to the mouse (mm10) or human (GRCh38) reference genome using Cell Ranger ATAC v.2.0 (https://support.10×genomics.com/single-cell-atac/software/pipelines/latest/what-is-cell-ranger-atac) (10x Genomics). The resulting fragment.tsv file was used for downstream analysis. For spatial Hi-C analysis, the newly generated Read1 and Read3 were aligned to the corresponding reference genome using the runHiC92 pipeline (https://github.com/XiaoTaoWang/HiC_pipeline). The resulting pairs files were further split into 2,500 separate pairs files based on the barcode information in the new Read2. These pairs files were used for downstream analysis.

## 解读

### 意义
处理原始测序数据，进行质量控制、接头去除、序列比对和空间信息提取，为后续分析准备高质量数据

### 输入
- 原始FASTQ文件（双端测序数据）
- 参考基因组（小鼠mm10或人类GRCh38）
- 空间条形码信息

### 输出
- 清洗后的FASTQ文件
- Cell Ranger ATAC格式文件（fragment.tsv）
- 2500个独立的pairs文件（基于空间条形码分割）
- 比对结果和空间坐标信息

### 核心步骤
1. **接头去除**：
   - 使用TrimGalore (v.0.6.10)检测和去除接头序列
   - 质量控制和清洗原始FASTQ文件

2. **连接子过滤**：
   - 使用BBtools (BBMap v.39.01)的bbduk功能
   - 仅保留含有连接子序列（linker1和linker2）的reads

3. **格式转换**：
   - 将过滤后的reads转换为Cell Ranger ATAC格式
   - Read2拆分：基因组DNA序列→新Read1，条形码序列→新Read2
   - 原始Read1→新Read3

4. **空间ATAC-seq分析**：
   - 使用Cell Ranger ATAC v.2.0比对到参考基因组
   - 生成fragment.tsv文件用于下游分析

5. **空间Hi-C分析**：
   - 使用runHiC pipeline比对Read1和Read3
   - 基于条形码信息将pairs文件分割为2500个独立文件
   - 每个文件对应一个空间像素

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| TrimGalore版本 | v.0.6.10 | 接头去除工具版本 |
| BBtools版本 | BBMap v.39.01 | 序列过滤工具版本 |
| Cell Ranger ATAC版本 | v.2.0 | 10x Genomics ATAC-seq分析流程 |
| runHiC | GitHub仓库 | Hi-C数据处理流程 |
| 参考基因组 | mm10 (小鼠), GRCh38 (人类) | 比对参考基因组 |
| 空间像素数量 | 2500 (50×50) | 条形码组合产生的空间像素数 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| TrimGalore | 接头去除和质量控制工具，基于Cutadapt |
| BBtools/bbduk | 序列过滤工具，用于去除污染和低质量reads |
| Cell Ranger ATAC | 10x Genomics的ATAC-seq数据分析流程 |
| runHiC | Hi-C数据处理软件包 |
| fragment.tsv | Cell Ranger ATAC输出的片段文件，包含比对位置和条形码信息 |
| pairs文件 | Hi-C数据格式，包含配对reads的比对位置和条形码信息 |

## 复现
- 工具/代码/URL
  - TrimGalore: https://github.com/FelixKrueger/TrimGalore
  - BBtools: https://sourceforge.net/projects/bbmap/
  - Cell Ranger ATAC: https://support.10xgenomics.com/single-cell-atac/software/pipelines/latest/what-is-cell-ranger-atac
  - runHiC: https://github.com/XiaoTaoWang/HiC_pipeline
- 代码片段
  ```bash
  # 数据预处理流程
  # 1. 接头去除
  trim_galore --paired raw_R1.fastq.gz raw_R2.fastq.gz -o cleaned/
  
  # 2. 连接子过滤
  bbduk in1=cleaned_R1.fastq.gz in2=cleaned_R2.fastq.gz \
        out1=filtered_R1.fastq.gz out2=filtered_R2.fastq.gz \
        literal=linker1,linker2 ktrim=r k=23 mink=11 hdist=1
  
  # 3. 格式转换（自定义脚本）
  python convert_to_cellranger_format.py filtered_R1.fastq.gz filtered_R2.fastq.gz
  
  # 4. Cell Ranger ATAC比对
  cellranger-atac count --id=sample --reference=mm10 --fastqs=converted/
  
  # 5. runHiC比对
  runHiC align -i converted_R1.fastq.gz -i converted_R3.fastq.gz -g mm10
  
  # 6. 按条形码分割pairs文件
  split_pairs_by_barcode.py sample.pairs barcodes.txt
  ```

## 生物学意义
数据预处理是Spatial-ATAC-Hi-C分析的关键步骤：

**质量控制**：
- 接头去除和低质量序列过滤确保数据质量
- 连接子序列验证确保数据来自有效实验
- 参考基因组比对验证数据的生物学相关性

**空间信息提取**：
- 条形码序列识别和分割实现空间编码
- 2500个空间像素对应组织切片的2D位置
- 为后续空间分析提供坐标信息

**数据格式标准化**：
- 转换为Cell Ranger ATAC格式便于使用标准工具
- pairs文件格式适合Hi-C数据分析
- 标准化格式便于数据共享和比较

该预处理流程的优势：
- 整合多个成熟工具，保证分析质量
- 自动化程度高，减少人工干预
- 输出格式标准化，便于下游分析

局限性：
- 需要多个软件工具，安装和配置复杂
- 计算资源需求较高（特别是比对步骤）
- 条形码分割可能引入错误
- 需要优化参数以适应不同组织类型

## 涉及 Figures
- **Fig. 1a** — 数据预处理流程示意图
- **Extended Data Fig. 4** — 数据质量控制和预处理验证
- **Fig. 2** — 预处理后的空间数据展示
