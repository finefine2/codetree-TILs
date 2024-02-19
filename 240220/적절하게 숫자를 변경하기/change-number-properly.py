n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

import sys
MIN = -sys.maxsize
dp = [[[MIN for _ in range(5)] for _ in range(m+1)] for _ in range(n+1)]

for k in range(1, 5):
    if k == arr[1]:
        dp[1][0][k] = 1
    else:
        dp[1][0][k] = 0

for i in range(2, n+1):
    for j in range(m+1):
        for k in range(1, 5):
            for l in range(1, 5):
                if l == k:
                    if arr[i] == k:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][l] + 1)
                    else:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][l])

                if l != k and j > 0:
                    if arr[i] == k:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][l] + 1)
                    else:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][l])

ans = 0
for j in range(m+1):
    for k in range(1, 5):
        ans = max(ans, dp[n][j][k])

print(ans)