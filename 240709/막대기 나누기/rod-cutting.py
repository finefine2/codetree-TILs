n = int(input())

arr = list(map(int, input().split()))

dp = [-1] * (n + 1)

dp[0] = 0
for i, num in enumerate(arr):
    for j in range(1, n + 1):
        if j - (i + 1) >= 0:
            dp[j] = max(dp[j], dp[j - i - 1] + num)

print(dp)