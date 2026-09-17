# Method: Alternative Splicing Analysis

## 原文（Methods）
> We detected a total of 3,879 distinct alternative splicing events in 2,368 genes when at least 2 splice-junction-spanning read counts were required.

## 解读

### 意义
分析组织中的可变剪接事件，揭示RNA加工的空间模式

### 输入
- 空间转录组数据
- 剪接连接读段
- 基因注释

### 输出
- 可变剪接事件列表
- 空间剪接模式
- 区域特异性剪接

### 核心步骤
1. 剪接连接读段检测
2. 可变剪接事件识别
3. 空间剪接模式分析
4. 区域特异性剪接比较

### 关键参数（本文设置）
| 参数 | 值 | 含义 |
|------|-----|------|
| 读段阈值 | ≥2个剪接连接读段 | 可靠性阈值 |
| 事件数量 | 3,879个事件 | 检测范围 |
| 基因数量 | 2,368个基因 | 覆盖基因 |

## 名词/参数/指标
| 名词 | 定义 |
|------|------|
| 可变剪接 | RNA前体的不同剪接方式 |
| 剪接连接 | 外显子-外显子连接处 |
| 外显子包含 | 外显子在成熟RNA中的保留 |

## 复现
- 工具/代码/URL（如有）
- 代码片段（关键调用，≤10 行）

## 生物学意义
可变剪接是基因表达调控的重要机制，空间分辨的剪接分析揭示了组织特异性的RNA加工模式。

## 涔及 Figures
- **Fig. 2** — Spatial co-mapping of gene expression and RNA processing in the mouse brain
