n, m = map(int, input().split())

arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

s = 0
for k in arr:
    s += k[0]

import sys
MAX = sys.maxsize
dp = [MAX] * (s + 1)

dp[0] = 0
for j in range(n):
    for i in range(s, 0, -1):
        if i - arr[j][0] >= 0:
            if i - arr[j][0] == MAX:
                continue
            dp[i] = min(dp[i], dp[i - arr[j][0]] + arr[j][1])

Min = MAX
for i in range(m, s + 1):
    if Min > dp[i]:
        Min = dp[i]
    # print(dp[i], end = " ")

if Min == MAX:
    print(-1)
else:
    print(Min)