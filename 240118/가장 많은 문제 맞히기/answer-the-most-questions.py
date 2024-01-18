n, t = map(int, input().split())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

dp = [0] * 10001

ans = 0
for i in range(n):
    for j in range(t, arr[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j-arr[i][0]] + arr[i][1])
    
    ans = max(ans, dp[t])

print(ans)