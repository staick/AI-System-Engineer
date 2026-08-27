## 表达式
$$
\begin{aligned}
f(x)&=max(0,x)=
\begin{cases}
0,x\le 0\\
x,x>0
\end{cases}\\
f'(x)&=
\begin{cases}
0,x\le 0\\
1, x>0
\end{cases}
\end{aligned}
$$
注意：$x=0$ 时，函数不可导，我们默认使用左侧的函数来计算导数
## 图像
![[Pasted image 20260826211623.png]]
## 概念
ReLU（Rectified Linear Unit，修正线性单元）会将小于0的输入转换为0，大于等于0的输入则保持不变。ReLU定义简单，计算量小。常用于隐藏层。
- ReLU作为激活函数不存在梯度消失。
- 当输入小于0时，ReLU 的输出为 0。所以 ReLU 激活的节点只有部分是活跃的，这种稀疏性有助于减少计算量和提高模型的效率。
- ReLU 在 x=0 是不平滑
- 当神经元的输入持续为负数时，ReLU的输出始终为0。此时神经元永远不会被激活，从而导致神经元死亡的问题（“dying ReLU” problem）。这会影响模型的学习能力，特别是大量神经元变成了死神经元。可以通过使用 [[ReLU#Leaky ReLU|Leaky ReLU]] 做为激活函数来解决这个问题。

## 代码实现
```python
def relu(x):  
    return np.maximum(0, x)
```

## ReLU 的变体
