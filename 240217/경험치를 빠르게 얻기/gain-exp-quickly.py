n, m = map(int, input().split())

arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

import sys
MAX = sys.maxsize
dp = [MAX] * 1000001

dp[0] = 0
for i in range(m, -1, -1):
    for j in range(n):
        if i - arr[j][0] >= 0:
            if i - arr[j][0] == MAX:
                continue
            dp[i] = min(dp[i], dp[i - arr[j][0]] + arr[j][1])

print(dp[m])