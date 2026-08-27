PReLU(Parametric Rectified Linear Unit)
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
PReLU 和 Leaky ReLU 的表达式看起来一样，但是要注意 PReLU 里的 $\alpha$ 是一个==可以训练的参数==，而不是和 Leaky ReLU 中一样是一个固定的很小的常数。
## 图像
![[Pasted image 20260827142229.png]]