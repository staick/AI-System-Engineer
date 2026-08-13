---
tags:
  - "#easy"
ctime: 2026-08-13
---

```python
class Solution:  
    def lengthOfLastWord(self, s: str) -> int:  
        ans = 0  
        p = len(s) - 1  
        while s[p] == ' ':  
            p -= 1  
  
        while p >= 0 and s[p] != ' ':  
            p -= 1  
            ans += 1  
  
        return ans
```