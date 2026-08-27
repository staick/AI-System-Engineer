Softplus——Smooth ReLU
## 表达式
$$
f(x)=ln(1+e^x)
$$
$$
f'(x)=\frac{1}{1+e^{-x}}
$$
### 与 ReLU 的关系
相较于 ReLU，Softplus 在 0 处是平滑的，并且 Softplus 的导函数是 Sigmoid，意味着它的梯度是在(0, 1) 之间平滑的变化的，而不是像 ReLU 一样跳转。但是由于指数和对数运算，导致 Softplus 的运算复杂度高，并且当 $x\rightarrow -\infty$ 时，$f'(x)\rightarrow 0$ ，还是有可能导致梯度消失的问题。所以在实际应用中不如 ReLU
## 图像
![[Pasted image 20260827153144.png]]