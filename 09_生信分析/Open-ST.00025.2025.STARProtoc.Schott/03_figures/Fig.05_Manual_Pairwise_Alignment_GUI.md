# Fig. 5 — Manual Pairwise Alignment Graphical User Interface (GUI) for Open-ST data

## Caption（原文）
> (A) The graphical user interface for manual alignment of imaging and spatial transcriptomics data. (1) Imaging modality view, showing the tissue section with manually selected corresponding visual landmarks (blue circles). Visual landmarks can be any two similar areas of tissue morphology or, more specifically, the small fiducial circles visible across both images (see Figure 2C). (2) Spatial transcriptomics modality view, displaying gene expression data with corresponding selected keypoints (red circles). (3) Overlay view of both modalities for alignment verification, after applying "Preview alignment". (4) Layer selector for individual tile selection during fine alignment. (5) 'Render' button to update views after parameter changes. (6) 'Preview alignment' button for testing and confirming alignments. Not highlighted: 'Keypoints properties' dropdown menu for saving and loading keypoint data, and sliders for adjusting image opacity in the overlay view.
> (B) Workflow diagram for the manual alignment process, using the command-line application (first and last steps), and the GUI.

## Panel-by-Panel 解读

### Panel A — GUI interface
**结论**：展示了手动对齐 GUI 的界面，包含成像视图、转录组视图和叠加视图。

**关键数据**：用户可以选择至少 3 个对应点进行对齐。

### Panel B — Workflow diagram
**结论**：展示了手动对齐的工作流程，结合命令行和 GUI 操作。

**关键数据**：手动对齐通常每 tile 不到 1 分钟。

## 总体结论
Fig. 5 展示了 Open-ST 的手动对齐 GUI，这是自动对齐失败时的重要备选方案。GUI 允许用户在成像和转录组数据上选择对应的视觉标记（如基准圆），然后实时预览对齐效果。用户可以对整个 tile 集合进行粗对齐，然后对单个 tile 进行细对齐。这种交互式方法特别适用于组织形态复杂或自动对齐困难的样本。

## 关联 Figures / Extended Data
- **Fig. 2C** — 显示基准圆的缝合图像
