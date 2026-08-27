GELU，Gaussian Error Linear Unit。这是目前 Transformers 和 LLMs 最常使用的函数。
## 表达式
$$
\begin{aligned}
&GELU(x)=x\Phi(x)\\
&\Phi(x)=P(Z\le x),Z\sim N(0,1)
\end{aligned}
$$
或
$$
GELU(x)=\frac{x}{2}\left[1+erf(\frac{x}{\sqrt2})\right]
$$
由于直接计算 GeLU 耗费很大，所以通常使用近似
$$
GELU(x)\approx \frac{1}{2}x\left[1+tanh\left(\sqrt{\frac{2}{\pi}}(x+0.044715x^3)\right)\right]
$$
注意：这里的 [[erf]] 为误差函数
### 与 ReLU 的关系
可以把 ReLU 看作一个 hard gate： $ReLU(x) = xI$，其中 $I$ 当 $x\le0$ 时为 0，当 $x>0$ 时为 1。这样 ReLU就是一个 hard binary decision。
而 GeLU：$GeLU(x)=x\times\Phi(x)$ ，其中 $0<\Phi(x)<1$，是一个概率值，它不会简单地进行负舍正留，而是根据数值大小，符号以及概率来决定去留。
### 与 [[Swish]] 的关系
GeLU 和 Swish 有着几乎相同的结构 $x\times soft\ gate$ ，只是 gating function 不同
$$
\begin{aligned}
&Swish:x\sigma(x)\\
&GeLU:x\Phi(x)
\end{aligned}
$$
并且 Sigmoid 和 Gaussian CDF 都是 S 型函数，两者函数曲线看起来也很相似