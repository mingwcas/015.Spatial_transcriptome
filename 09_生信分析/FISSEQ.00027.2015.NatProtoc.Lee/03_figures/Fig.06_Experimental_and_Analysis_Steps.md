# Fig. 6 — FISSEQ实验与分析步骤概览

## Caption（原文）
> Schematic overview of FISSEQ experimental and analysis steps. FOV, field of view; SBL, SOLiD sequencing-by-ligation.

## Panel-by-Panel 解读

### 实验步骤（左侧流程）
**结论**：展示FISSEQ从样品准备到测序的完整实验流程

**关键数据**：
- Steps 2-16: 细胞固定（10% formalin）→ 透化 → 原位RT → 交联 → RNA降解 → 环化 → RCA → 扩增子交联 → 控制探针杂交 → 成像 → 探针剥离
- 库验证：adapter特异性荧光探针杂交、rRNA特异性荧光探针杂交
- Steps 25-33: SOLiD连接法测序（30 cycles）
- 明场成像、DAPI染色
- 时间：2-3天（库构建）+ 10天（测序）

### 分析步骤（右侧流程）
**结论**：展示从图像到数据的分析流程

**关键数据**：
- FOV优化
- 3D反卷积 → MATLAB命令（2D图像配准）
- Python命令（碱基判读）
- Bowtie 1.0命令（序列比对）→ Steps 44-51
- Python命令（空间聚类）
- R和MATLAB（数据分析）
- 时间：1-3天

### 步骤时间标注
**关键数据**：
- Steps 1-21（库构建）：2-3天
- Steps 22-33（测序成像）：10天
- Steps 34-36（图像预处理）：6-12小时
- Steps 37-49（图像分析）：6-12小时
- Steps 50-51（数据分析）：1天

## 总体结论
Fig. 6提供了FISSEQ实验和分析的完整路线图，总耗时约14-17天。实验部分（库构建+测序）需要分子生物学技能和显微镜操作经验；分析部分需要Unix、MATLAB、Python和R的计算技能。图中清晰标注了每个步骤的软件工具（MATLAB、Python、Bowtie、R），便于用户跟随操作。

## 关联 Figures / Extended Data
- **Fig. 1** — 文库构建详细原理
- **Table 3** — 故障排除
- 论文PROCEDURE部分的详细步骤说明
