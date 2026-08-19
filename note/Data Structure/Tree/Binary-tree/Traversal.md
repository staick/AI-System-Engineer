## 前序遍历
### 递归实现
递归序 
```python
def pre(head):
	if head == None:
		return
	print(head.value)
	pre(head.left)
	pre(head.right)
```
## 中序遍历
### 递归实现
```python
def pre(head):
	if head == None:
		return
	pre(head.left)
	print(head.value)
	pre(head.right)
```
## 后序遍历
### 递归实现
```python
def pre(head):
	if head == None:
		return
	pre(head.left)
	pre(head.right)
	print(head.value)
```
