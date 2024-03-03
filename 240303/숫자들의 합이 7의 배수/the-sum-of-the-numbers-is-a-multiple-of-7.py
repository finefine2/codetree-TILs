n = int(input())

arr = [0]
for i in range(n):
    a = int(input())
    arr.append(a)

import sys
MAX = sys.maxsize
seven = [MAX] * 7

k = 0
ans = 0
for i in range(1, n+1):
    k += arr[i]
    k %= 7

    ans = max(ans, i - seven[k])
    seven[k] = min(i, seven[k])

print(ans)