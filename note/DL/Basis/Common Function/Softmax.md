## 表达式
$$
y_k = \frac{e^{x_k}}{\sum^n_{i=1}e^{x_i}},\qquad k = 1\sim n\\[6pt]
$$
$$
\frac{\partial y_k}{\partial x_i}=
\begin{cases}
y_i\,(1-y_i),k=i,\\[4pt]
-y_k\,y_i, \quad k\neq i
\end{cases}
$$

### 与 [[DL/Basis/Common Function/Sigmoid]] 的关系
Softmax 相当于是 Sigmoid 在多分类问题上的扩展。
对于 Sigmoid，可以将其看作是 $y=1$ 时的概率
$$
\begin{aligned}
&P(y=1|x)=\frac{1}{1+e^{-x}}\\
&P(y=0|x)=1-P(y=1|x)=1-\frac{1}{1+e^{-x}}
\end{aligned}
$$
对于 Softmax，观察其二分类情况
$$
\begin{aligned}
Softmax(z_1, z_2)&= \frac{e^{z_1}}{e^{z_1}+e^{z_2}}\\
Softmax(z_1, z_2) &= \frac{1}{1+e^{z_2-z_1}}\\
Softmax(z_1, z_2) &= Sigmoid(z_2-z_1)
\end{aligned}
$$

## 概念
Softmax将一个任意的实数向量转换为一个概率分布，确保输出值的总和为 1。
Softmax常用于多分类问题的输出层，用来表示类别的预测概率。
Softmax会放大输入中较大的值，使得最大输入值对应的输出概率较大，其他较小的值会被压缩。即在类别之间起到了一定的区分作用。

## 代码实现
最基础的代码实现
```python
def softmax_basis(x):  
    return np.exp(x) / np.sum(np.exp(x))
```
防止 x 过大导致指数函数溢出，进行改进
```python
def softmax_advanced(x):  
    x -= np.max(x)  
    return np.exp(x) / np.sum(np.exp(x))
```
考虑到 x 可能为矩阵，进一步改进
```python
def softmax(x):  
    if x.ndim == 2:  
        # 转置是为了方便进行广播  
        x = x.T  
        x = x - np.max(x, axis=0)  
        y = np.exp(x) / np.sum(np.exp(x))  
        return y.T  
  
    x = x - np.max(x)  
    return np.exp(x) / np.sum(np.exp(x))
```