---
tags:
  - "#easy"
  - "#stack"
ctime: 2026-08-13
---

```python
class Solution:  
    def romanToInt(self, s: str) -> int:  
        ans = 0  
        stack = [s[0]]  
        top = s[0]  
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  
        for c in s[1:]:  
            if c == top:  
                stack.append(c)  
            else:  
                if roman_dict[c] > roman_dict[top]:  
                    ans += roman_dict[c] - roman_dict[top]  
                    stack.pop()  
                    top = c  
                    continue  
                while stack:  
                    ans += roman_dict[stack.pop()]  
                stack.append(c)  
                top = c  
        while stack:  
            ans += roman_dict[stack.pop()]  
  
        return ans
```
