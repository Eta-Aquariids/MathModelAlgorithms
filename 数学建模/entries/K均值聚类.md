---
title: "K-Means 聚类"
type: "algorithm"
category: "聚类模型"
tags: [K-Means, 聚类, 无监督学习, 划分聚类, 欧氏距离, 轮廓系数]
difficulty: "⭐"
created: 2026-07-23
source: "MacQueen (1967)"
---

## 📖 算法原理

**K-Means** 是最经典的**划分聚类**算法，将 $n$ 个样本划分为 $k$ 个簇，使每个样本到其簇中心的**距离平方和（SSE）最小**：

$$
\text{SSE} = \sum_{i=1}^{k} \sum_{\mathbf{x} \in C_i} \|\mathbf{x} - \boldsymbol{\mu}_i\|^2
$$

其中 $\boldsymbol{\mu}_i$ 是簇 $C_i$ 的质心（均值向量）。

### 算法步骤

1. **初始化：** 随机选择 $k$ 个样本作为初始质心
2. **分配：** 每个样本分配到距离最近的质心所属的簇
3. **更新：** 重新计算每个簇的质心（均值）
4. **重复 2~3** 直到质心不再变化或达到最大迭代次数

### $k$ 值的选择

| 方法 | 做法 |
|------|------|
| **肘部法则** | 绘制 SSE ~ $k$ 曲线，找拐点 |
| **轮廓系数** | 取平均轮廓系数最大的 $k$ |
| **Gap 统计量** | 比较与随机数据的聚类差异 |

---

## 🎯 适用场景

| 问题类型 | 具体例子 |
|---------|---------|
| 客户分群 | 根据消费行为划分客户群体 |
| 图像分割 | 像素颜色聚类实现图像分割 |
| 数据预处理 | 大样本数据先聚类再分类 |
| 异常检测 | 离群点远离所有簇中心 |

**局限：** 只适用于**凸型簇**，对异常值敏感，需预先指定 $k$。

---

## 💻 使用方法 (Python)

```python
from sklearn.cluster import KMeans
import numpy as np

# 生成示例数据
X = np.random.rand(100, 2)

# K-Means 聚类
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

print(f"簇标签: {labels}")
print(f"簇中心:\n{centers}")
print(f"SSE: {kmeans.inertia_:.4f}")
```

---

## 🔗 关联算法

- [[DBSCAN]] — 密度聚类，识别任意形状簇，无需指定 $k$
- [[层次聚类]] — 无需指定 $k$，可输出树状图
- **K-Medoids** — 对异常值更鲁棒
