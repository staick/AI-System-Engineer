激活函数的作用：为神经网络引入非线性，使得神经网络能够学习和表示复杂的线性关系。因此==激活函数必须为非线性函数==。

## 常用的激活函数
[[Idenity|恒等函数]]、[[Binary Step|阶跃函数]]、[[DL/Basis/Common Function/Sigmoid|Sigmoid 函数]]、[[Tanh|Tanh 函数]]、[[Softmax|Softmax 函数]]、[[ReLU|ReLU 函数]]以及[[Leaky ReLU]]、[[PReLU]]、[[RReLU]]、[[ELU]]、[[GELU|GeLU 函数]]、[[Swish|Swish 函数]]、[[Softplus]]等[[ReLU#ReLU 的变体|ReLU 函数的变体]]。
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
## 选择激活函数
### 隐藏层
- 首选 [[ReLU]]，如果效果不好可尝试 [[Leaky ReLU]] 等。
- [[DL/Basis/Common Function/Sigmoid]] 在隐藏层易导致梯度消失，应尽量避免。
- [[Tanh]] 的输出均值为 0，对中心化数据更友好，但仍可能引发梯度消失，仅适用于浅层网络。
- 大模型如 Bert，Chat GPT3 多采用 [[GELU]]
- 最新的大模型多采用 [[SwiGLU]]
### 输出层
- 二分类：[[DL/Basis/Common Function/Sigmoid]]
- 多分类：[[Softmax]]
- 回归：[[Idenity]]