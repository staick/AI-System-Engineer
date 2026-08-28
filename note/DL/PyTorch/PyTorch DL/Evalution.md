在 PyTorch 中使用如下方式进入评估模式
```python
model.eval()
```
在评估模式中
- Dropout 会被禁用
- 不用从数据中训练参数，直接调用训练得到的参数 