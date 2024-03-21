n, h, t = map(int, input().split())

arr = list(map(int, input().split()))

import sys
ans = sys.maxsize
for i in range(n):
    s = 0
    for j in range(i, i+t):
        if j >= n:
            break
        s += abs(arr[j] - h)
    
    ans = min(ans, s)

print(ans)