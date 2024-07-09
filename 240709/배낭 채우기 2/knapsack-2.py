n, m = map(int, input().split())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

dp = [-1] * (m + 1)
dp[0] = 0

for i in range(n):
    for j in range(1, m + 1):
        if j - arr[i][0] >= 0:
            dp[j] = max(dp[j], dp[j - arr[i][0]] + arr[i][1])

print(max(dp))