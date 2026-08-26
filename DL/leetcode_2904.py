s = "100011001"
k = 3

def solution(s, k):
    if s.count('1') < k:
        return ''
    cnt = left = 0
    ans = s
    for right, digit in enumerate(s):
        cnt += int(digit)
        while cnt > k or s[left] == '0':
            cnt -= int(s[left])
            left += 1

        if cnt == k:
            cur = s[left:right + 1]

            if len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                ans = cur

    return ans

print(solution(s, k))