# 基于序列的对象识别 (Sequence-Based Object Identification)

## 原文 (Methods)

Fluorescence microscopy can be accompanied by tissue-specific artifacts and autofluorescence, which impede accurate identification of objects. If objects are nucleic acids, however, discrete sequences, rather than the analog signal intensity, can be used to analyze the image. For FISSEQ, putative nucleic acid sequences are determined for all pixels. The sequencing reads are then compared with reference sequences, and a null value is assigned to unaligned pixels. With a suitably long read length (L), a large number of unique sequences (n) can be used to identify transcripts or any other objects with a false-positive rate of approximately n/4L per pixel. Because the intensity threshold is not used, even faint objects are registered on the basis of their sequence, whereas background noise, autofluorescence, and debris are eliminated.

## 解读

### 意义
基于序列的对象识别是 FISSEQ 分析的核心创新之一。与传统的基于荧光强度的阈值方法不同，该方法利用离散的核苷酸序列来识别对象，从而克服了组织特异性伪影和自发荧光的干扰。

### 输入
- 去卷积的共聚焦图像
- 参考序列数据库

### 输出
- 对齐的序列读数
- 空间聚类的对象
- 去除背景噪声的清晰图像

### 核心步骤
1. **序列确定**：为所有像素确定推定的核苷酸序列
2. **序列比对**：将测序读数与参考序列进行比较
3. **空值分配**：未对齐的像素被分配空值
4. **对象识别**：基于序列而非强度阈值来识别对象

### 关键参数
- 读长 (L)：27-30 个碱基
- 唯一序列数 (n)：参考序列库大小
- 假阳性率：约 n/4L 每像素

## 名词/参数/指标

| 术语 | 定义 |
|------|------|
| 读长 (L) | 测序读取的碱基数量 |
| 唯一序列数 (n) | 参考序列库中的唯一序列数量 |
| 假阳性率 | 错误识别对象的概率，约为 n/4L 每像素 |
| 空值 | 未对齐像素的赋值 |

## 复现

### 所需软件
- 图像处理软件
- 序列比对工具
- 参考序列数据库

### 所需设备
- 共聚焦显微镜
- 高性能计算设备

## 生物学意义

基于序列的对象识别方法使得：
- 即使是微弱的信号也能被准确检测
- 背景噪声和自发荧光被有效去除
- 可以检测大量不同的转录本
- 实现了高通量的空间转录组学分析

## 涉及 Figures

- **Fig. 2B**: 基于序列的对象识别示意图
- **fig. S8**: 测序错误率分析
- **fig. S9**: 自动化分析流程
