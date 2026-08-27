激活函数的作用：为神经网络引入非线性，使得神经网络能够学习和表示复杂的线性关系。因此==激活函数必须为非线性函数==。

常用的激活函数有：[[Idenity|恒等函数]]、[[Binary Step|阶跃函数]]、[[Sigmoid|Sigmoid 函数]]、[[Tanh|Tanh 函数]]、[[Softmax|Softmax 函数]]、[[ReLU|ReLU 函数]]以及[[Leaky ReLU]]、[[PReLU]]、[[RReLU]]、[[ELU]]、[[GELU|GeLU 函数]]、[[Swish|Swish 函数]]、[[Softplus]]等[[ReLU#ReLU 的变体|ReLU 函数的变体]]。
```
                  Activation functions
                         │
            ┌────────────┴────────────┐
            │                         │
      Saturating classic       ReLU-like family
            │                         │
       Sigmoid / Tanh                 ReLU
                                      │
                 ┌────────────────────┼─────────────────────┐
                 │                    │                     │
           fix negative side      smooth ReLU         soft gating
                 │                    │                     │
        Leaky ReLU / ELU          Softplus          Swish / GELU
```
![[Pasted image 20260827172740.png]]