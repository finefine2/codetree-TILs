n = int(input())

arr = list(map(int, input().split()))

dp = [0] * 1001

for i in range(n):
    for j in range(i):
        if dp[j] == 0:
            continue
        if j + arr[j] <= arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans + 1)