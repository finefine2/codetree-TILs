n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
#       21
#       43

for i in range(5, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007



print(dp[n])