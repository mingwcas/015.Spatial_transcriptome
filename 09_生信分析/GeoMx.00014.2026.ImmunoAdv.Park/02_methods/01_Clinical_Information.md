# Method: Clinical Information

## 原文（Methods）
> A 43-year-old woman was diagnosed with an obstructing ascending colon cancer with resectable liver metastasis. This study encompasses her clinical course from the initial diagnosis in March 2018 through curative resection, palliative chemotherapy, and immunotherapy with pembrolizumab administered between December 2020 and May 2021, accompanied by interval CT evaluations. She subsequently remained under active surveillance, with regular imaging and clinical follow-up extending through May 2025. Following the initial resection, the patient received 12 cycles of palliative chemotherapy with FOLFOX. Two years later, the tumor recurred at multiple sites, including the ovaries, the peritoneum, and the omentum. She received four cycles of pembrolizumab and exhibited heterogeneous responses across metastatic sites—regression in the peritoneum and left ovary, but resistance in the omentum and right ovary. All metastatic lesions evaluated in this study were obtained during a single interval debulking surgery performed after the patient had completed four cycles of pembrolizumab. The right ovary, left ovary, omentum, and peritoneal lesions were resected concurrently, indicating that all specimens represent synchronous metastatic sites collected at an identical therapeutic timepoint. Five years after the recurrence, the patient remains disease-free, with no evidence of progression or relapse, suggesting durable complete remission. dMMR status was confirmed by immunohistochemistry for MLH1, PMS2, MSH2, and MSH6.

## 解读

### 意义
描述研究对象的临床背景信息，包括患者特征、治疗时间线和样本采集方案，为后续多组学分析提供临床上下文。

### 输入
- 患者临床信息（年龄、性别、诊断时间）
- 影像学评估（CT）
- 治疗记录（FOLFOX化疗、Pembrolizumab免疫治疗）

### 输出
- 临床元数据（诊断、分期、治疗时间线）
- 样本采集方案（5个转移部位：结肠、肝、腹膜、左卵巢、右卵巢）

### 核心步骤
1. 收集患者临床病史（2018年3月初始诊断）
2. 根治性切除术后辅助化疗（FOLFOX 12周期）
3. 复发后给予Pembrolizumab（2020-2021年，4周期）
4. 通过CT评估各转移部位治疗反应
5. 间隔减瘤手术获取所有转移灶样本
6. 免疫组化确认dMMR状态（MLH1、PMS2、MSH2、MSH6）

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 患者年龄 | 43岁 | 女性 |
| 初始诊断 | 2018年3月 | 升结肠癌伴肝转移 |
| 化疗方案 | FOLFOX | 12周期 |
| 免疫治疗 | Pembrolizumab | 4周期 |
| 随访截止 | 2025年5月 | 5年无病生存 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| dMMR | Mismatch repair-deficient，DNA错配修复缺陷 |
| MSI-H | Microsatellite instability-high，高度微卫星不稳定 |
| FOLFOX | 氟尿嘧啶+奥沙利铂+亚叶酸钙化疗方案 |
| Pembrolizumab | PD-1抑制剂，免疫检查点阻断剂 |

## 复现
- 伦理批准：GCIRB2024-021（韩国嘉泉大学吉尔医学中心机构审查委员会）
- 患者知情同意：于参与研究前获得书面知情同意

## 生物学意义
该研究采用自身对照设计（同一患者多个转移灶），可最大程度减少个体间变异，揭示转移部位间免疫应答异质性的生物学机制。

## 涉及 Figures
- **Fig. 1** — 研究设计概览，展示多组学整合策略和样本采集部位
