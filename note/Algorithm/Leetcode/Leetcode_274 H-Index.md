---
tags:
  - medium
ctime: 2026-08-13
---
```python
class Solution:  
    def hIndex(self, citations: List[int]) -> int:  
        citations.sort()  
        i = len(citations) - 1  
        count = 0  
  
        while i >= 0 and count < citations[i]:  
            i -= 1  
            count += 1  
  
        return count
```