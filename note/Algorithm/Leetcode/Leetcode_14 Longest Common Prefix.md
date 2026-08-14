---
ctime: 2026-08-14
---

```python
class Solution:  
    def longestCommonPrefix(self, strs: List[str]) -> str:  
        min_len = len(strs[0])  
        for s in strs:  
            if len(s) < min_len:  
                min_len = len(s)  
        ans = ""  
        flag = False  
        for i in range(min_len):  
            if flag:  
                break  
            check = strs[0][:i + 1]  
            for s in strs:  
                if s[:i + 1] != check:  
                    flag = True  
                    break            else:  
                ans = check  
        return ans
```