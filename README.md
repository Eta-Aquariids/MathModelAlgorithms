# 📐 MathModelAlgorithms

**数学建模算法知识库**——系统整理常见数学建模算法的原理、数学模型、实现代码与实例应用。

---

## 📚 知识库结构

```
MathModelAlgorithms/
├── INDEX.md                        # 总索引
├── README.md                       # 本文件
└── 📐 数学建模/
    ├── INDEX.md                    # 板块索引（按算法分类）
    └── entries/                    # 算法条目（共 27 条）
```

## 🗂️ 算法分类

### 🏆 评价模型（3条）
| 算法 | 难度 | 说明 |
|------|------|------|
| [TOPSIS 法（逼近理想解排序法）](数学建模/entries/TOPSIS法.md) | ⭐ | TOPSIS 法（Technique for Order Preference by Similarity to Ide... |
| [层次分析法 (Analytic Hierarchy Process, AHP)](数学建模/entries/层次分析法.md) | ⭐⭐ | 层次分析法（AHP） 是一种将定性与定量相结合的多准则决策方法，由美国运筹学家 Saaty 于 1970 年代提出。核心... |
| [熵权法 (Entropy Weight Method)](数学建模/entries/熵权法.md) | ⭐ | 熵权法 是一种客观赋权方法，基于信息熵原理：指标的变异程度越大（信息量越大），熵越小，权重越大。 |
### 🔮 预测模型（2条）
| 算法 | 难度 | 说明 |
|------|------|------|
| [灰色预测模型 (GM(1,1))](数学建模/entries/灰色预测模型.md) | ⭐⭐ | 灰色预测 GM(1,1) 模型 是灰色系统理论的核心，适用于小样本、贫信息的短期预测。用"累加生成"将杂乱原始数据转化为... |
| [线性回归 (Linear Regression)](数学建模/entries/线性回归.md) | ⭐ | 线性回归 假设因变量 y 与自变量 x1, ldots, xp 之间存在线性关系： |
### ⚡ 优化模型（10条）
| 算法 | 难度 | 说明 |
|------|------|------|
| [Dijkstra 最短路径算法](数学建模/entries/Dijkstra最短路径.md) | ⭐⭐ | Dijkstra 算法 求解单源最短路径问题——给定一个起点，计算它到图中所有其他节点的最短距离。适用于边权非负的图。 |
| [Floyd-Warshall 多源最短路径](数学建模/entries/Floyd多源最短路径.md) | ⭐⭐ | Floyd-Warshall 算法 求解任意两点之间的最短路径，基于动态规划思想。 |
| [动态规划 (Dynamic Programming, DP)](数学建模/entries/动态规划.md) | ⭐⭐⭐ | 动态规划（Dynamic Programming, DP） 是一种将多阶段决策问题分解为一系列单阶段子问题的优化方法，由... |
| [匈牙利算法（指派问题）](数学建模/entries/匈牙利算法.md) | ⭐⭐⭐ | 匈牙利算法 求解指派问题——将 n 项任务分配给 n 个人，每人做一项，使总成本最小（或总效益最大）。 |
| [整数规划 (Integer Programming, IP)](数学建模/entries/整数规划.md) | ⭐⭐⭐ | 整数规划（Integer Programming, IP） 是线性规划的扩展，要求部分或全部决策变量取整数。当变量表示人... |
| [最小生成树 (Prim & Kruskal)](数学建模/entries/最小生成树.md) | ⭐⭐ | 最小生成树 (MST) 在一个带权无向连通图中找一棵包含所有顶点的树，使所有边的权值之和最小。 |
| [有向无环图 (DAG) 与拓扑排序](数学建模/entries/有向无环图与拓扑排序.md) | ⭐⭐ | 有向无环图 (Directed Acyclic Graph, DAG) 是没有环的有向图，是图论中最常用的结构之一，因为... |
| [线性规划 (Linear Programming, LP)](数学建模/entries/线性规划.md) | ⭐⭐ | 线性规划（Linear Programming, LP） 是数学规划中最基本、应用最广泛的分支，研究在线性约束下对线性目... |
| [贪心算法 (Greedy Algorithm)](数学建模/entries/贪心算法.md) | ⭐⭐ | 贪心算法 在每一步决策时都选择当前状态下最优的选择（局部最优），期望通过一系列局部最优选择达到全局最优。 |
| [非线性规划 (Nonlinear Programming, NLP)](数学建模/entries/非线性规划.md) | ⭐⭐⭐ | 非线性规划（Nonlinear Programming, NLP） 指目标函数或约束条件中含有非线性成分的优化问题。现实... |
### 🧩 分类模型（2条）
| 算法 | 难度 | 说明 |
|------|------|------|
| [支持向量机 (Support Vector Machine, SVM)](数学建模/entries/支持向量机.md) | ⭐⭐⭐ | SVM 的核心思想是在特征空间中找到一个间隔最大的超平面来分隔不同类别的样本。 |
| [逻辑回归 (Logistic Regression)](数学建模/entries/逻辑回归.md) | ⭐⭐ | 逻辑回归 是最常用的二分类模型，用 Sigmoid 函数将线性回归的输出映射到 0,1 区间作为概率。 |
### 🔗 聚类模型（2条）
| 算法 | 难度 | 说明 |
|------|------|------|
| [DBSCAN 密度聚类](数学建模/entries/DBSCAN聚类.md) | ⭐⭐ | DBSCAN 是一种基于密度的聚类算法，将"密度相连"的样本归为一类，能发现任意形状的簇，并能自动识别噪声点。 |
| [K-Means 聚类](数学建模/entries/K均值聚类.md) | ⭐ | K-Means 是最经典的划分聚类算法，将 n 个样本划分为 k 个簇，使每个样本到其簇中心的距离平方和（SSE）最小： |
### 📉 降维算法（1条）
| 算法 | 难度 | 说明 |
|------|------|------|
| [主成分分析 (Principal Component Analysis, PCA)](数学建模/entries/主成分分析.md) | ⭐⭐ | 主成分分析（PCA） 是最常用的无监督线性降维方法，通过正交变换将 p 个相关变量转换为 q 个不相关的综合变量（主成分... |
### 🧠 智能算法 / 启发式算法（4条）
| 算法 | 难度 | 说明 |
|------|------|------|
| [模拟退火算法 (Simulated Annealing, SA)](数学建模/entries/模拟退火算法.md) | ⭐⭐ | 模拟退火算法（Simulated Annealing, SA） 是一种受金属退火物理过程启发的随机优化算法。1983 年... |
| [粒子群算法 (Particle Swarm Optimization, PSO)](数学建模/entries/粒子群算法.md) | ⭐⭐ | 粒子群算法（Particle Swarm Optimization, PSO） 是一种基于群体智能的随机优化算法，由 K... |
| [蚁群算法 (Ant Colony Optimization, ACO)](数学建模/entries/蚁群算法.md) | ⭐⭐⭐ | 蚁群算法（Ant Colony Optimization, ACO） 是一种模拟蚂蚁觅食行为的群体智能优化算法，由意大利... |
| [遗传算法 (Genetic Algorithm, GA)](数学建模/entries/遗传算法.md) | ⭐⭐ | 遗传算法（Genetic Algorithm, GA） 是一种模拟生物进化过程的随机搜索算法，由 John Hollan... |
### 📊 统计与时间序列（3条）
| 算法 | 难度 | 说明 |
|------|------|------|
| [NC抽样法（计数标准型抽样检验）](数学建模/entries/NC抽样法.md) | ⭐⭐ | NC抽样法即 (n, c) 计数标准型抽样检验方案，是统计质量控制中最基础、应用最广泛的固定样本量计数抽样方法。所谓"计... |
| [声称质量水平检验法（DQL检验）](数学建模/entries/声称质量水平检验法.md) | ⭐⭐ | 声称质量水平检验法（Declared Quality Level Testing, DQL 检验） 是一种基于 统计假设... |
| [序贯概率比检验法 (SPRT)](数学建模/entries/序贯概率比检验法.md) | ⭐⭐⭐ | 序贯概率比检验法（Sequential Probability Ratio Test, SPRT） 由著名统计学家 Ab... |

---

## 📖 每条算法的内容结构

每条算法条目都包含以下模块：

| 模块 | 内容 |
|------|------|
| **📖 算法原理** | 核心数学思想 + 公式推导 + 参数详解 |
| **🎯 适用场景** | 适用问题类型 + 具体例子 + 数据要求 |
| **📋 详细步骤** | 分步操作流程 + 设计要点 |
| **⚖️ 优缺点** | 对比表格 |
| **💻 Python 代码** | 可直接运行的实现代码 + 注释 |
| **📊 实例应用** | 结合具体背景的实例分析 |
| **🔗 关联算法** | 与其他算法的联系与对比 |
| **📝 补充说明** | 注意事项、扩展阅读 |

---

*知识如海，积少成多 🌊*
