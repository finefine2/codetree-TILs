n = int(input())

dp = [0] * 1001

arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if arr[j] <= arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans + 1)