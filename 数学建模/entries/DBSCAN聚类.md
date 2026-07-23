---
title: "DBSCAN 密度聚类"
type: "algorithm"
category: "聚类模型"
tags: [DBSCAN, 密度聚类, 聚类, 离群点检测, 噪声, 任意形状]
difficulty: "⭐⭐"
created: 2026-07-23
source: "Ester et al. (1996)"
---

## 📖 算法原理

**DBSCAN** 是一种**基于密度**的聚类算法，将"密度相连"的样本归为一类，能发现**任意形状**的簇，并能自动识别**噪声点**。

### 核心概念

| 概念 | 定义 |
|------|------|
| $\varepsilon$-邻域 | 距离样本点不超过 $\varepsilon$ 的区域 |
| **核心点** | 其 $\varepsilon$-邻域内**至少包含 MinPts** 个样本 |
| **边界点** | 不是核心点，但在核心点的邻域内 |
| **噪声点** | 既不是核心点也不是边界点 |

### 算法思想

- 对每个核心点，将其 $\varepsilon$-邻域内的所有点归入同一簇
- 不断扩展——核心点的邻域内的核心点的邻域也归入该簇
- 边界点被"吸纳"但不继续扩展
- 噪声点不属于任何簇

### 参数

| 参数 | 含义 | 调参建议 |
|------|------|---------|
| $\varepsilon$ | 邻域半径 | 根据 k-距离图选择拐点 |
| **MinPts** | 核心点阈值 | 一般取 2×维度数 |

---

## 🎯 适用场景

| 问题类型 | 具体例子 |
|---------|---------|
| 任意形状簇 | 环状、S 形、不规则形状聚类 |
| 离群点检测 | 自动识别异常数据 |
| 地理空间聚类 | 经纬度点聚类 |

**优势：** 无需指定簇数 $k$，能识别噪声，发现任意形状簇。

---

## 💻 使用方法 (Python)

```python
from sklearn.cluster import DBSCAN
import numpy as np

X = np.random.rand(100, 2)

db = DBSCAN(eps=0.15, min_samples=5)
labels = db.fit_predict(X)

n_clusters = len(set(labels) - {-1})
n_noise = list(labels).count(-1)
print(f"簇数: {n_clusters}, 噪声点: {n_noise}")

# labels = -1 表示噪声点
```

---

## 🔗 关联算法

- [[K-Means 聚类]] — 只能发现凸形簇，需指定 $k$
- [[层次聚类]] — 可树状图展示，计算量大
