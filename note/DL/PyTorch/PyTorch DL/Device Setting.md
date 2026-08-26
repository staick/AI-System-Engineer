在创建时指定设备，默认设备为 cpu
```python
input = torch.randn(1, 5, device=torch.device('cuda'))
print(input.device)  # cuda:0
```

创建后也可以指定设备
```python
input = torch.randn(1, 5).to(device='cuda')
```

工程中一般使用全局变量设置 `device`，然后在每次创建变量时加上参数 `device=device`
```python
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = 'cuda' if torch.cuda.is_available() else 'cpu'
input = torch.randn(1, 5, device=device)
```