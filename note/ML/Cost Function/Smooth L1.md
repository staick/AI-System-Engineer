平滑 L1：当误差较小时（$|y_i-\hat{y_i}|<1$ ）使用 L2 Loss，使得损失函数平滑可导。当误差较大时（$|y_i-\hat{y_i}|\ge1$）使用 L1 Loss 降低异常值的影响。
## 表达式
$$
Smooth L1=
\begin{cases}
\frac{1}{2}(y_i-\hat{y_i})^2,|y_i-\hat{y_i}|<1\\[10pt]
|y_i-\hat{y_i}|-\frac{1}{2},|y_i-\hat{y_i}|\ge1
\end{cases}
$$
## 图像
![[Pasted image 20260828152537.png]]