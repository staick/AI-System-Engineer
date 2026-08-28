## 表达式
$$
L=-\frac{1}{n}\sum^n_{i=1}t_i\log y_i
$$

## 代码实现

```python
def cross_entropy_error(y, t):  
    if y.ndim == 1:  
        y = y.reshape(1, y.size)  
        t = t.reshape(1, t.size)  
  
    if y.size == t.size:  
        t = np.argmax(t, axis=1)  
  
    batch_size = y.shape[0]  
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
```
> [!NOTE]
> 1. `if y.dim == 1`：判断 y 的维度，然后将其转换成多维的目的是为了后续的处理：后续需要获取 y 的 `shape[0]`，如果 y 是一维的话，它的 `shape` 就是 `(n,)` 。会由它的 size 决定。
> 2. `if y.size == t.size`：这是判断 t 是否使用的独热编码
> 3. 最后加的 1e-7 是防止出现 log0的情况
