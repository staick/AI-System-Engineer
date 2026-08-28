MSE，Mean Squared Error，均方误差。由于其与 [[Vector (向量)#$L 2$ 范数|L2 范数]]关系密切，所以也称 L2 Loss。我在学习时经常与 [[SSE]] 混淆，可以进行比较一下。
L2 Loss 对异常值敏感，遇到异常值时易发生梯度爆炸。

## 表达式
$$
L=\frac{1}{n}\sum^n_{i=1}(y_i-\hat{y_i})^2
$$
## 图像
![[Pasted image 20260828151851.png]]

