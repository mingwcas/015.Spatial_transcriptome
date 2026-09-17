# 代码与数据清单 — Patho-DBiT: Spatial RNA Biology in FFPE Tissues

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| iStar | https://github.com/rajewsky-lab/iStar | MIT | 超分辨率空间转录组算法 |
| scVelo | https://github.com/theislab/scvelo | BSD-3 | RNA速度分析工具 |
| rMATS | https://github.com/Xinglab/rMATS | MIT | 可变剪接检测工具 |
| STAR | https://github.com/alexdobin/STAR | MIT | RNA-seq序列比对工具 |
| HISAT2 | https://daehwankimlab.github.io/hisat2/ | MIT | RNA-seq序列比对工具 |
| featureCounts | https://subread.sourceforge.net/ | GPL-3 | 基因表达定量工具 |
| CODEX分析流程 | PhenoCycler-Fusion系统 | 商业 | 蛋白组学分析 |

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| 原始测序数据 | GEO/SRA | 待发表 | Patho-DBiT测序数据 |
| 处理后表达矩阵 | 论文补充材料 | Cell期刊 | 空间表达矩阵 |
| 小鼠胚胎数据 | 内部数据 | - | E13胚胎验证数据 |
| 小鼠脑数据 | 内部数据 | - | 脑组织空间转录组 |
| AITL临床样本 | 临床存档 | 5年存档FFPE | 人淋巴瘤组织 |
| MALT临床样本 | 临床存档 | FFPE组织 | 人淋巴瘤组织 |
| CODEX蛋白组数据 | 内部数据 | - | 空间蛋白组验证 |
| Allen脑图谱 | Allen Brain Atlas | 公共数据库 | 脑区注释参考 |
| 单细胞参考数据 | 公共数据库 | scRNA-seq数据集 | 细胞类型整合参考 |

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| Patho-DBiT实验流程 | 可复现 | 需要微流控设备和FFPE组织处理经验 |
| 序列比对和定量 | 可复现 | 使用标准开源工具 |
| 可变剪接分析 | 可复现 | rMATS开源可用 |
| RNA编辑分析 | 可复现 | 需要定制分析流程 |
| miRNA分析 | 可复现 | 需要miRNA参考数据库 |
| SNV检测 | 可复现 | 需要RNA变异检测流程 |
| RNA速度分析 | 可复现 | scVelo开源可用 |
| 超分辨率分析 | 可复现 | iStar开源可用 |
| CODEX蛋白组学 | 部分可复现 | 需要CODEX商业平台 |
| 组织病理学验证 | 可复现 | 标准病理学方法 |

## 四、技术难点与注意事项

1. **微流控设备**: 需要定制微流控芯片，技术门槛较高
2. **FFPE样本处理**: 需要优化的脱蜡和去交联条件
3. **原位多聚腺苷酸化**: 需要优化酶反应条件
4. **空间条形码设计**: 需要高质量的条形码引物
5. **数据分析流程**: 多步骤分析流程需要整合

## 五、应用建议

1. **临床病理学**: 适用于存档FFPE组织的回顾性研究
2. **肿瘤异质性**: 空间分辨的亚克隆分析
3. **RNA生物学**: 多种RNA类型的空间分析
4. **药物靶点发现**: 空间特异性表达和调控网络
