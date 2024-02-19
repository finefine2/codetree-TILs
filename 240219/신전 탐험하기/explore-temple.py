n = int(input())

dp = [[0] * 3 for _ in range(n+1)]

arr = []
arr.append((0,0,0))
for i in range(n):
    l, m, r = map(int, input().split())
    arr.append((l, m, r))

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i+1][k] = max(dp[i+1][k], dp[i][j] + arr[i+1][k])

print(max(dp[n]))