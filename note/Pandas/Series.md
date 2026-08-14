Series 是一维数组
```python
pd.Series([1, 2, 3, 4, 5], name="hello")
```

显示索引，即包含开始又包含结束

分位数的 nearest 插值类型，进行舍入的是下标值，采用银行家舍入法
```python
s = pd.Series([10,20,30,40,50])  
s.quantile(0.125, interpolation='nearest')
# np.int64(10)
```
