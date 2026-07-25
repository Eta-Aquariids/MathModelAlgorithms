---
title: "Floyd-Warshall 多源最短路径"
type: "algorithm"
category: "优化模型"
tags: [图论, 多源最短路径, Floyd, 动态规划, 任意两点间最短路径]
difficulty: "⭐⭐"
created: 2026-07-23
source: "Floyd (1962) / Warshall (1962)"
---

## 📖 算法原理

**Floyd-Warshall 算法** 求解**任意两点之间**的最短路径，基于**动态规划**思想。

### 核心递推

设 $dist[k][i][j]$ 表示从 $i$ 到 $j$ 只经过编号 $\leq k$ 的中间点的最短路径长度：

$$
dist[k][i][j] = \min\left(dist[k-1][i][j],\; dist[k-1][i][k] + dist[k-1][k][j]\right)
$$

压缩到二维空间：

$$
\boxed{dist[i][j] = \min(dist[i][j],\; dist[i][k] + dist[k][j])}
$$

三层循环，$k$ 在外层：

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

### 时间复杂度

$O(V^3)$，适合节点数不超过几百的图。

---

## 🎯 适用场景

| 问题类型 | 具体例子 |
|---------|---------|
| 多源查询 | 地图中任意两个城市之间的最短距离 |
| 网络直径 | 计算图中最远两点之间的距离 |
| 传递闭包 | 判断图中任意两点是否连通 |
| 选址问题 | 选一个点使得到其他所有点的距离之和最小 |

---

## 💻 使用方法 (Python)

```python
import numpy as np

def floyd_warshall(dist):
    """dist: 邻接矩阵，inf 表示无边"""
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# 示例
INF = float('inf')
dist = np.array([
    [0, 3, INF, 7],
    [3, 0, 2, INF],
    [INF, 2, 0, 1],
    [7, INF, 1, 0]
])
result = floyd_warshall(dist)
print(result)
```

---

## 🔗 关联算法

- [[Dijkstra 最短路径]] — 单源最短路径，效率更高（$O(E\log V)$）
- **Bellman-Ford** — 可处理负权边
