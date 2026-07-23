---
title: "TOPSIS 法（逼近理想解排序法）"
type: "algorithm"
category: "评价模型"
tags: [TOPSIS, 综合评价, 理想解, 距离评价, 多属性决策]
difficulty: "⭐"
created: 2026-07-23
source: "Hwang & Yoon (1981)"
---

## 📖 算法原理

**TOPSIS 法（Technique for Order Preference by Similarity to Ideal Solution）** 的核心思想：最优方案应**距正理想解最近**，**距负理想解最远**。

### 算法步骤

#### 1. 原始数据矩阵正向化

将所有指标统一为**极大型**（越大越好），常见转换：
- **极小型→极大型：** $x' = \max - x$ 或 $x' = 1/x$
- **中间型→极大型：** $x' = 1 - \frac{|x - x_{\text{best}}|}{\max|x - x_{\text{best}}|}$
- **区间型→极大型：** 距最优区间越近得分越高

#### 2. 标准化处理

消除量纲影响，常用向量归一化：

$$
z_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}
$$

#### 3. 加权标准化

$$
v_{ij} = w_j \cdot z_{ij}
$$

其中 $w_j$ 为第 $j$ 个指标的权重（可用 AHP 或熵权法确定）。

#### 4. 确定正负理想解

$$
\begin{aligned}
V^+ &= (\max v_{i1}, \max v_{i2}, \ldots, \max v_{im}) \\
V^- &= (\min v_{i1}, \min v_{i2}, \ldots, \min v_{im})
\end{aligned}
$$

#### 5. 计算距离（欧氏距离）

$$
D_i^+ = \sqrt{\sum_{j=1}^{m} (v_{ij} - v_j^+)^2}, \quad
D_i^- = \sqrt{\sum_{j=1}^{m} (v_{ij} - v_j^-)^2}
$$

#### 6. 计算相对接近度

$$
C_i = \frac{D_i^-}{D_i^+ + D_i^-}
$$

$C_i \in [0, 1]$，越大越优。

---

## 🎯 适用场景

| 问题类型 | 具体例子 |
|---------|---------|
| 方案综合评价 | 多指标下多个方案的排序优选 |
| 绩效评估 | 多部门/多人绩效打分排名 |
| 质量评价 | 不同供应商的产品质量综合排名 |

---

## 💻 使用方法 (Python)

```python
import numpy as np

def topsis(data, weights, indicators):
    """
    TOPSIS 评价
    参数:
        data: (m×n) 评价矩阵, m个方案, n个指标
        weights: 权重向量 (需和为 1)
        indicators: 'max' 或 'min', 表示各指标方向
    返回:
        各方案的得分和排名
    """
    m, n = data.shape
    # 正向化
    for j in range(n):
        if indicators[j] == 'min':
            data[:, j] = data[:, j].max() - data[:, j]
    
    # 标准化
    normed = data / np.sqrt((data**2).sum(axis=0))
    
    # 加权
    weighted = normed * weights
    
    # 理想解
    V_plus = weighted.max(axis=0)
    V_minus = weighted.min(axis=0)
    
    # 距离
    D_plus = np.sqrt(((weighted - V_plus)**2).sum(axis=1))
    D_minus = np.sqrt(((weighted - V_minus)**2).sum(axis=1))
    
    # 得分
    scores = D_minus / (D_plus + D_minus)
    ranks = np.argsort(-scores)
    
    return scores, ranks+1

# 示例
data = np.array([[90, 85, 80], [80, 90, 70], [85, 75, 90]])
scores, ranks = topsis(data, weights=[0.3, 0.4, 0.3], indicators=['max', 'max', 'max'])
for i in range(len(scores)):
    print(f"方案 {i+1}: 得分={scores[i]:.4f}, 排名={ranks[i]}")
```

---

## 🔗 关联算法

- [[层次分析法 (AHP)]] — 可确定 TOPSIS 中的指标权重
- [[熵权法]] — 客观赋权法，与 TOPSIS 天然搭配
