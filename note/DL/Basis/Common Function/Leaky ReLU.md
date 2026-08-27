Leaky ReLU(Leaky Rectified Linear Unit)
## 表达式
$$
f(x)=
\begin{cases}
\alpha x,x\le0\\
x,x>0
\end{cases}
$$
$$
f'(x)=
\begin{cases}
\alpha,x\le0\\
1,x>0
\end{cases}
$$
注意，这里 $\alpha$ 是一个很小的常数，目的是再负数区域引入一个小的斜率
## 图像
![[Pasted image 20260827141331.png]]