---
title: "Dijkstra 最短路径算法"
type: "algorithm"
category: "优化模型"
tags: [图论, 最短路径, Dijkstra, 贪心算法, 单源最短路径, 非负权图]
difficulty: "⭐⭐"
created: 2026-07-23
source: "Edsger W. Dijkstra (1956)"
---

## 📖 算法原理

**Dijkstra 算法** 求解**单源最短路径**问题——给定一个起点，计算它到图中所有其他节点的最短距离。适用于**边权非负**的图。

### 核心思想

**贪心策略：** 每次从未确定的节点中选距离起点最近的，标记为已确定，然后用它松弛相邻节点。

### 算法步骤

1. 初始化：起点距离 $dist[s]=0$，其他为 $\infty$，所有节点未确定
2. 从未确定节点中选 $dist$ 最小的节点 $u$
3. 标记 $u$ 为已确定
4. 对 $u$ 的每个邻接节点 $v$：若 $dist[u] + w(u,v) < dist[v]$，则更新 $dist[v]$
5. 重复 2~4 直到所有节点确定

### 时间复杂度

| 实现方式 | 时间复杂度 | 适用场景 |
|---------|-----------|---------|
| 朴素实现 | $O(V^2)$ | 稠密图 |
| 优先队列优化 | $O((V+E)\log V)$ | 稀疏图（最常用） |

---

## 🎯 适用场景

| 问题类型 | 具体例子 |
|---------|---------|
| 交通导航 | 地图上两点间最短行车路线 |
| 物流配送 | 配送中心到各客户的最短路径 |
| 网络路由 | 数据包在计算机网络中的最优转发路径 |
| 城市应急 | 消防站到火灾点的最快路线 |

**前提条件：** 图中**不能有负权边**（有负权用 Bellman-Ford）。

---

## 💻 使用方法 (Python)

```python
import heapq

def dijkstra(graph, start):
    """
    graph: 邻接表 {节点: [(邻居, 权重), ...]}
    start: 起点
    返回: dist 字典, prev 字典
    """
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    
    pq = [(0, start)]  # (距离, 节点)
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    return dist, prev

# 示例
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}
dist, prev = dijkstra(graph, 'A')
for node in dist:
    print(f"A → {node}: {dist[node]}")
```

---

## 🔗 关联算法

- **Floyd-Warshall 算法** — 多源最短路径，任意两点间
- **Bellman-Ford 算法** — 可处理负权边，检测负环
- **A\* 算法** — 有启发式信息的最短路径，比 Dijkstra 更快
