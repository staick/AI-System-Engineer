也称 Sigmoid Linear Unit, SiLU
## 表达式
$$
f(x)=\frac{x}{1+e^{-\beta x}}=x\times Sigmoid(\beta x)
$$
$$
f'(x)=\frac{1+e^{-x}+xe^{-x}}{(1+e^{-x})^2}=Sigmoid(x)[1+x(1-Sigmoid(x))]
$$
$\beta$ 通常取 1
### 与 [[DL/Basis/Common Function/Sigmoid]]、[[ReLU]] 以及 [[Softplus]] 的关系
$SiLU(x)=x\times Sigmoid(\beta x)$，而 $\beta$ 通常取 1，所以$SiLU(x)=x\times Sigmoid(x)$。当 x 在正数方向逐渐变大时，$Sigmoid(x)\rightarrow 1$，所以 $SiLU(x)\rightarrow x$；当 x 在负数方向逐渐变大时，$Sigmoid(x)\rightarrow 0$，所以 $SiLU(x)\rightarrow 0$，这就使得 SiLU 与 ReLU 的变化情况相近。但是 SiLU 在x = 0 的时候是平滑的。并且不同于 Softplus 一直是正数，SiLU 可以取的较小的负数。
SiLU 函数最大的特点是它不是单调的，较小的负值不会被忽略，这可以帮助进行优化
此外，SiLU 的导函数不是仅仅只有 0 和 1 两个取值，它会随着 x 的变化平滑地进行变化。
## 图像
![[Pasted image 20260827154422.png]]
