RReLU(Randomized Leaky ReLU)
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
RReLU 还是和 Leaky ReLU 有一样的表达式，但是它的参数 $\alpha$ 是在训练时从==均匀分布==中随机选择的参数。
## 图像
![[Pasted image 20260827142911.png]]