n = int(input())
arr = list(map(int, input().split()))

import sys
ans = -sys.maxsize
s = 0
for i in range(n):
    if s >= 0:
        s += arr[i]
    else:
        s = arr[i]
    ans = max(ans, s)

print(ans)