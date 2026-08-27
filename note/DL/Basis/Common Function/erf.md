erf，error function，误差函数
## 表达式
$$
erf(x)=\frac{2}{\sqrt{\pi}}\int^x_0e^{-t^2}dt
$$
### 特性
$$
eft(0)=0
$$
$$
\lim_{x\rightarrow+\infty}erf(x)=1
$$
$$
\lim_{x\rightarrow-\infty}erf(x)=-1
$$
erf 是奇函数 $$erf(-x) = -erf(x)$$
### 与 [[GeLU]] 的关系
erf 是一个专门用来表示 $e^{-x^2}$ 这种高斯型函数积分的特殊函数。
高斯（Gaussian）分布/标准正态分布的 [[Math/Probability/Concepts#PDF|PDF]] 为$$f(x)=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$$
高斯（Gaussian）分布/标准正态分布的 [[Math/Probability/Concepts#CDF|CDF]] 为$$\Phi(x)=\int^x_{-\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}dt$$
出现了 $e^{\frac{-x^2}{2}}$，而 erf 中有 $e^{-x^2}$，所以经过变量代换就可以得到
$$
\Phi(x) = \frac{1}{2}\left[1+erf\left(\frac{x}{\sqrt2}\right)\right]
$$
