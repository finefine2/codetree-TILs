n, m = map(int, input().split())

s = 0
arr = []
for i in range(n):
    a, b = map(int, input().split())
    s += a
    arr.append((a, b))

import sys
dp = [sys.maxsize] * (s + 1)

dp[0] = 0
for i in range(n):
    for j in range(s, 0, -1):
        if j - arr[i][0] >= 0:
            dp[j] = min(dp[j], dp[j - arr[i][0]] + arr[i][1])


ans = sys.maxsize
for i in range(m, s + 1):
    ans = min(ans, dp[i])

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)