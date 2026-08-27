## 表达式
$$
\begin{aligned}
f(x)&=\frac{1}{1+e^{-x}} \\
f'(x)&=\frac{1}{1+e^{-x}}(1-\frac{1}{1+e^{-x}})=f(x)(1-f(x))
\end{aligned}
$$
### 求导过程

## 图像
![[Pasted image 20260825153642.png]]

## 概念
Sigmoid（也叫Logistic函数）平滑的、可微的，能将任意输入映射到区间 (0, 1)。
### 局限
1. 涉及指数运算，计算量相对较高。
2. Sigmoid 的输入在 \[-6,6\] 之外时，其输出值变化很小，可能导致信息丢失。
3. Sigmoid 的输出并非以 0 为中心 (Not zero-centered)，其输出值均＞0，导致后续层的输入权重始终同号，参数更新经常需要来回拐弯，影响梯度更新方向。
4. Sigmoid 的导数范围为 (0, 0.25)，梯度较小。当输入在 \[-6,6\] 之外时，导数接近 0，此时网络参数的更新将会极其缓慢。使用 Sigmoid 作为激活函数，可能出现梯度消失（**sigmoid's vanishing-gradient problem**。在逐层反向传播时，梯度会呈指数级衰减）。
## 应用
多用于二分类问题的输出层或者层次比较少的隐藏层
## 代码实现
```python
def sigmoid(x):
	return 1 / (1 + np.exp(-x))
```