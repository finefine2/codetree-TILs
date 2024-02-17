n, k = map(int, input().split())

arr = [0] + list(map(int, input().split()))

import sys
MIN = -sys.maxsize
dp = [[MIN] * (k+1) for _ in range(n+1)]

ans = MIN
dp[0][0] = 0
for i in range(1, n+1):
    if arr[i] < 0:
        for j in range(1, k+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])
            ans = max(ans, dp[i][j])
    else:
        for j in range(k+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j] + arr[i])
            ans = max(ans, dp[i][j])

print(ans)