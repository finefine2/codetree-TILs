n = int(input())
MOD = 10**9 + 7

dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(1004)]

# T B G

dp[1][0][1] = 1
dp[1][1][0] = 1
dp[1][0][0] = 1

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            dp[i+1][j+1][0] = (dp[i+1][j+1][0] + dp[i][j][k]) % MOD
            dp[i+1][j][0] = (dp[i+1][j][0] + dp[i][j][k]) % MOD
            dp[i+1][j][k+1] = (dp[i+1][j][k+1] + dp[i][j][k]) % MOD

ans = 0
for j in range(3):
    for k in range(3):
        ans = (ans + dp[n][j][k]) % MOD

print(ans)