# Fig. 4 — Putative cell lineage transition during telencephalon regeneration

## Caption（原文）
> (A) Bubble plot reflecting the expression dynamics of marker genes defining reaEGC, rIPC1, and IMN, which are major cell types involved in axolotl telencephalon regeneration.
> (B) Spatially visualized heatmap showing the expression pattern of key markers for regeneration-related cells in the injury area of sections, including 15 DPI–2, 15 DPI–3, and 15 DPI–4 cells.
> (C) Spatial distribution of cell types around the regenerating site on the section of 15 DPI–4.
> (D) RNA velocity streamline plots showing the predicted trajectory of cell lineage transition in the regenerating region of axolotl telencephalon in 15 DPI–4 cells. Areas are colored by either annotated cell clusters (left) or pseudotime (right).
> (E) Pseudotime trajectory analysis corresponding to the three designated areas in (C), via Monocle2 (top) and Monocle3 (bottom). Cells are colored by cell type or pseudotime.
> (F) Heatmap showing pseudotemporal transition of the expression level of representative genes in regeneration.
> (G) Scatterplot showing pseudotime dynamics of the expression of Nes, S100a10, Ankrd1, Nptx1, Satb1, and Cdkn1c in clusters of reaEGC, rIPC1, IMN, and nptxEX cells.
> (H) UMAP visualization of the regeneration-related cells across regenerative stages. Cells are colored by cell type annotation (left), pseudotime (top right), and stages (bottom right).
> (I) Spatial visualization of cells in (H) with the pseudotime score in the cell lineage transition process. Cells are colored by the pseudotime score.

## Panel-by-Panel 解读

### Panel A — Marker Gene Expression Dynamics
**结论**：reaEGC、rIPC1和IMN三种细胞类型呈现特征性标记基因表达动态，rIPC1同时表达reaEGC标记（Vim、Nes、Krt18、S100a10）和IMN标记（Ankrd1、Stmn4、Nptx1）。

**关键数据**：Cdkn1a和Cdkn1c从reaEGC到rIPC1到immature nptxEX依次升高，提示增殖潜能沿转换轴降低。

### Panel B — Spatial Heatmap of Key Markers
**结论**：关键标记基因在15 DPI-2、15 DPI-3和15 DPI-4截面的损伤区域呈现特征性表达模式，支持四种细胞状态（reaEGC-rIPC1-IMN-nptxEX）的空间组织。

**关键数据**：reaEGC和IMN标记基因的表达水平和信号波与Stereo-seq图上的细胞类型分布匹配。

### Panel C — Cell Type Distribution at 15 DPI-4
**结论**：15 DPI-4截面显示nptxEX位于IMN邻近区域，提示潜在的状态转换；rIPC1位于reaEGC和IMN之间。

**关键数据**：nptxEX从remote区（15 DPI-4）到 wound center（15 DPI-1）呈高到低的空间梯度。

### Panel D — RNA Velocity Trajectory
**结论**：RNA velocity流线图支持reaEGC-rIPC1-IMN-nptxEX的谱系转换轨迹。

**关键数据**：基于细胞类型和伪时间的着色显示连续的状态转换。

### Panel E — Pseudotime Analysis (Monocle2/3)
**结论**：Monocle2和Monocle3伪时间分析均支持三个指定区域的谱系转换路径。

**关键数据**：两种分析方法结果一致。

### Panel F — Gene Expression Heatmap Along Pseudotime
**结论**：沿伪时间轴基因表达变化热图显示干性标记Nes表达下降，Cdkn1c表达上升，与潜在转换一致。

**关键数据**：Nes表达下降， Cdkn1c沿轴上升。

### Panel G — Pseudotime Dynamics of Key Genes
**结论**：Nes、S100a10、Ankrd1、Nptx1、Satb1、Cdkn1c在reaEGC、rIPC1、IMN、nptxEX四种细胞类型中呈现特征性伪时间动态。

**关键数据**：干性相关基因随伪时间下降，成熟相关基因随伪时间上升。

### Panel H — UMAP of Regeneration Cells Across Stages
**结论**：从2 DPI到60 DPI的再生相关细胞UMAP显示细胞类型注释、伪时间和阶段的分布模式。

**关键数据**：伪时间和阶段分布支持reaEGC-rIPC-IMN-nptxEX的转换模式。

### Panel I — Spatial Visualization of Pseudotime Score
**结论**：伪时间评分空间可视化显示再生过程中细胞状态的时空转换。

**关键数据**：伪时间与真实时间数据匹配。

## 总体结论

本图揭示了蝾螈脑室再生过程中从reaEGC到nptxEX的潜在细胞谱系转换路径。鉴定出rIPC1作为reaEGC和IMN之间的中间细胞类型，同时表达两种细胞的标记基因。RNA velocity和Monocle伪时间分析均支持reaEGC-rIPC1-IMN-nptxEX的转换轴。伪时间动态显示干性标记（Nes）下降和成熟标记（Nptx1、Cdkn1c）上升。reaEGC可能来源于局部wntEGC和sfrpEGC，通过增殖覆盖伤口并分化为中间和成熟神经元，实现组织再生。

## 关联 Figures / Extended Data
- ED Fig. 4（补充Fig. S12-S14 再生谱系详细分析）
