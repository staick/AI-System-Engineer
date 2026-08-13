## Cross Product (叉积)

```python
np.cross(a, b)
```

## norm (范数)
用来衡量向量的大小

### $L^1$ 范数
$$
||V||_1 = |a|+|b|+|c|
$$
### $L^2$ 范数
$$
||V||_2=\sqrt{a^2+b^2+c^2}
$$
### $L^p$ 范数
$$
||V||_p=(\sum^n_{i=1}{|x_i|^p})^{1/p}
$$
### $L^\infty$ 范数
$$
||V||_\infty=max(|a|,|b|,|c|)
$$

在机器学习中用于正则化

### 在 Python 中计算范数
```python
np.linalg.norm(v, p)

np.linalg.norm([1,2], 1)  # L1 范数
np.linalg.norm([1,2], 2)  # L2 范数
np.linalg.norm([1,2], np.inf)  # 无穷范数
```