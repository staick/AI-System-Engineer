## min-heap
可以使用 Python 的库 `heapq` 来实现小根堆
```python
import heapq

# 转化为小根堆
 heap = [3, 1, 2, 5, 4]
 heapq.heapify(heap)
 
 # 插入数据
 heapq.heappush(heap, 6)
 
 # 查询最小值
 heap[0]
 
 # 弹出最小值
 x = heapq.heappop(heap)

```

## max-heap
Python 没有默认支持大根堆，但可以将使用相反数将小根堆转为大根堆
```python
import heapq
nums = [3, 1, 2, 5, 4]
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

x = heapq.heappop(max_heap)
print(-x)

```