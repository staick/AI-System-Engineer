## 概念
Binary Step，阶跃函数是最简单的激活函数。
它为输入设置一个阈值，当输入大于阈值就切换输出。
## 表达式
$$
f(x)=
\begin{cases}
0,x\le0 \\[4pt]
1,x>0
\end{cases}\qquad f'(x)=0
$$
## 图像
![[Pasted image 20260825152159.png]]

## 应用
由于导数一直为 0，无法在梯度下降和[[Backward Propagation|反向传播]]中更新参数，所以在深度学习中较少使用。

## 代码实现
当 $x$ 只取一个值时：
```python
def step_function(x):
	return 1 if x > 0 else 0
```

当 $x$ 为数组时：
```python
def step_function(x):
	return np.array(x > 0, dtype=int)
```
