n, m = map(int, input().split())

arr = []
arr.append((0,0,0))
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        for k in range(m):
            if j != k:
                dp[i+1][k] = max(dp[i+1][k], dp[i][j] + arr[i+1][k])

print(max(dp[n]))