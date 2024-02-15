n = int(input())

arr = list(map(int, input().split()))

dp = [0] * 1001

for i in range(n):
    for j in range(i):
        if arr[i] >= arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans + 1)