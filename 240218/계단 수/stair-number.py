n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
MOD = 10 ** 9 + 7

for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, n+1):
    for j in range(10):
        if 0 <= j-1 < 10:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= MOD
        if 0 < j+1 < 10:
            dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= MOD

print(sum(dp[n]))