n = int(input())
dp = [0] * 1001


dp[2] = 1
dp[3] = 1
dp[4] = 1

for i in range(5, n+1):
    dp[i] = ((dp[i-2] % 10007) + (dp[i-3] % 10007)) % 10007

print(dp[n])