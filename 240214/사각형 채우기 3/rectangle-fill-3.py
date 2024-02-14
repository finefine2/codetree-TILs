num = 1000000007

n = int(input())

dp = [0] * 1001

dp[0] = 1
dp[1] = 2  
dp[2] = 7  
dp[3] = 22
dp[4] = 71
# 142  88
# 228
# 44 28
for i in range(5, n+1):
    dp[i] = (dp[i-1] * 3 + dp[i-2] - dp[i-3]) % num

print(dp[n])