# Fig. 3 — Physical organization of the spatially barcoded flow cell, and data processing workflow

## Caption（原文）
> (A) An Illumina NovaSeq6000 S4 flow cell is depicted. We show the hierarchy of the entire flow cell, down into Lanes across surfaces, swaths, and tiles per swath. Each tile contains around 3 million valid barcoded spatial locations after first sequencing.
> (B) The raw sequencing data, in FASTQ format, contains the physical lane, tile ID, and relative X/Y coordinate for each barcode read, as part of the sequence identifier, as well as the barcode and its quality string. These are processed to one CSV file per tile, to map spatial barcodes to their two dimensional coordinates. All files are stored into the same directory, with standard names. A coordinate system can apply offsets at the X/Y values to each tile, converting relative into absolute coordinates.
> (C) Two possible layouts of tiles at a Lane (on a S4 flow cell) with respect to the offset of odd and even columns (1, 2). The global coordinates can be recovered by using a suitable coordinate system (e.g., fc_1_coordinate_system in panel B corresponds to Layout 1).
> (D) Calculation of number of total tiles and valid barcoded locations for NovaSeq 6000 SP and NovaSeq 6000 S4 flow cells.

## Panel-by-Panel 解读

### Panel A — Flow cell hierarchy
**结论**：展示了 S4 flow cell 的层级结构：flow cell → lanes → surfaces → swaths → tiles。

**关键数据**：每个 tile 约含 300 万个有效条形码空间位置。

### Panel B — Data processing workflow
**结论**：展示了原始测序数据到空间坐标映射的处理流程。

**关键数据**：每个 tile 生成一个 CSV 文件，包含条形码和 X/Y 坐标。

### Panel C — Tile layouts
**结论**：展示了两种可能的 tile 布局，奇偶列有不同的偏移。

**关键数据**：不同布局需要不同的坐标系统文件。

### Panel D — Tile calculations
**结论**：展示了 SP 和 S4 flow cell 的 tile 数量和有效条形码位置计算。

**关键数据**：S4 flow cell 有 3744 个 tiles，SP 有 468 个 tiles。

## 总体结论
Fig. 3 详细解释了 Open-ST 的空间编码原理和数据处理流程。Illumina flow cell 上的纳米孔阵列被用作空间条形码，每个 tile 包含数百万个带有唯一空间坐标的捕获位点。原始测序数据经过处理后，生成每个 tile 的条形码-坐标映射文件。不同的 flow cell 可能需要不同的坐标系统来处理 tile 间的偏移。理解 flow cell 的物理组织对于正确处理空间数据至关重要。

## 关联 Figures / Extended Data
- **Fig. 4** — File structure after running spacemake
