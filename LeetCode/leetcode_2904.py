s = "100011001"
k = 3

def solution(s, k):
    s = int(s, 2)
    if s.bit_count() < k:
        return ""
    ans = (1 << (k + 1)) - 1
    # while ans < s:
    #     pass

    return str(bin(ans))

print(solution(s, k))