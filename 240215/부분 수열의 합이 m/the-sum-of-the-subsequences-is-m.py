n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

import sys
MAX = sys.maxsize
dp = [MAX] * (m+1)

dp[0] = 0
for i in range(1, n+1):
    for j in range(m, -1, -1):
        if j >= arr[i]:
            if dp[j - arr[i]] == MAX:
                continue
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

ans = dp[m]
if ans == MAX:
    ans = -1

print(ans)