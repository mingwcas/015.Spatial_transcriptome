# Method: 神经递质判定与TF共表达模块

## 原文（Methods）
> We performed WGCNA analysis on 534 transcription factor marker genes ... power=6 and TOMType="signed", and detectCutHeight=0.998. Genes in the ‘grey’ module were removed.

## 解读
### 意义
用转运体/合成酶定义递质类型，识别TF身份模块。
### 输入
cluster/subclass平均表达；8,460 marker和534 TF genes。
### 输出
8类递质标签及52个TF模块。
### 核心步骤
1. canonical transporter+enzyme且log2CPM>3判定递质。2. subclass平均表达运行WGCNA。3. 去grey和泛神经元模块，拆分重排。
### 关键参数（本文设置）
|参数|值|含义|
|---|---|---|
|TF genes|534|模块输入|
|power|6|软阈值|
|TOMType|signed|拓扑重叠|
|detectCutHeight|0.998|模块切割|

## 名词/参数/指标
|名词|定义|
|---|---|
|WGCNA|加权基因共表达网络分析|
|递质阈值|log2(CPM)>3并要求转运体与合成酶共表达|

## 复现
- WGCNA；`blockwiseModules(datExpr, power=6, TOMType="signed", detectCutHeight=.998)`

## 生物学意义
连接TF共表达与细胞身份；相关性不等于因果，模块依赖参数。

## 涉及 Figures
- **Fig. 3、Fig. 5**；Extended Data Fig. 9,13
