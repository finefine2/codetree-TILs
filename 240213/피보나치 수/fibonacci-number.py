n = int(input())

dp = [0] * 46
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(44):
    dp[i+2] = dp[i+1] + dp[i]

print(dp[n])