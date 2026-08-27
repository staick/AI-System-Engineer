ELU(Exponential Linear Unit)
## 表达式
$$
f(x)=
\begin{cases}
\alpha(e^x-1),x\le0\\
\qquad x,x>0
\end{cases}
$$
$$
f'(x)=
\begin{cases}
\alpha e^x,x\le0\\
\quad 1,x>0
\end{cases}
$$
这里 $\alpha$ 通常取 1.
### 与 ReLU 的关系
ELU 通过给负数区域定义一个非 0 的函数，使得神经元死亡的问题得到了解决。并且 ELU 在 x = 0时平滑。但是 ELU 是一个saturate 的函数，当 $x \rightarrow -\infty$ 时，$f(x)\rightarrow -\alpha$，$f'(x)\rightarrow 0$ 会造成梯度消失。
## 图像
![[Pasted image 20260827145724.png]]