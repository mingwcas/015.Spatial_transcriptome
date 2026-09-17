# Fig. 1 — FISSEQ文库构建与测序示意图

## Caption（原文）
> Schematic overview of FISSEQ library construction and sequencing. (a) Fixed cells or tissues are permeabilized and reverse-transcribed in situ in the presence of aminoallyl-dUTP and adapter sequence-tagged random hexamers. The cDNA fragments are fixed to the cellular protein matrix using a nonreversible amine cross-linker and circularized after degrading the RNA. The circular templates are amplified using RCA primers complementary to the adapter sequence in the presence of aminoallyl-dUTP and stably cross-linked. The nucleic acid amplicons in cells are then ready for sequencing and imaging (fibroblast shown). (b) Each amplicon contains numerous tandem copies of the cDNA template and adapter sequence. A sequencing primer hybridizes to the adapter sequences in individual amplicons, and fluorescent eight-base probes interrogate the adjacent dinucleotide pair. After imaging, the three bases attached to a fluorophore are cleaved, generating a phosphorylated 5′ end at the ligation complex suitable for additional ligation cycles interrogating every fifth dinucleotide pairs. The whole process is repeated using four other sequencing primers with an offset to interrogate intervening base positions.

## Panel-by-Panel 解读

### Panel a — 文库构建流程
**结论**：展示FISSEQ从固定细胞到测序就绪扩增子的完整文库构建流程

**关键数据**：
- 步骤：固定 → 透化 → 原位RT（含aminoallyl-dUTP和adapter标记的随机六聚体）→ BS(PEG)9交联 → RNA降解 → cDNA环化 → RCA引物杂交 → RCA扩增（含aminoallyl-dUTP）→ 扩增子交联
- 显示成纤维细胞中的扩增子分布

### Panel b — 测序原理
**结论**：展示SOLiD连接法测序在单个扩增子上的工作原理

**关键数据**：
- 每个扩增子含有多个串联重复的cDNA模板和adapter序列
- 测序引物杂交到adapter序列
- 荧光八碱基探针通过T4 DNA连接酶连接，探测相邻双碱基对
- 成像后切割3个碱基和荧光基团，产生磷酸化5'端
- 重复7轮连接-成像-切割循环
- 使用5个偏移引物（N, N-1~N-4）填补间隙

## 总体结论
Fig. 1是理解FISSEQ方法的核心示意图，展示了从细胞固定到原位测序的完整流程。关键创新包括：1）aminoallyl-dUTP介导的cDNA交联固定空间位置；2）RCA扩增单分子为含数百拷贝的扩增子；3）SOLiD连接法在室温下进行原位测序。整个流程可在标准共聚焦显微镜上完成。

## 关联 Figures / Extended Data
- **Fig. 6** — 详细实验步骤时间线
- **Box 1** — SOLiD测序化学详细说明
- **Fig. 4** — SOLiD颜色编码方案
