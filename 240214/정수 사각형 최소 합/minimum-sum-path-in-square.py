n = int(input())
dp = [[0] * n for _ in range(n)]

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp[0][n-1] = arr[0][n-1]

for i in range(n-2, -1, -1):
    dp[0][i] = arr[0][i] + dp[0][i+1]

for i in range(1, n):
    dp[i][0] = arr[i][0] + dp[i-1][0]
    dp[i][n-1] = arr[i][n-1] + dp[i-1][n-1]

for i in range(n-2, 0, -1):
    dp[n-1][i] = arr[n-1][i] + dp[n-1][i+1]

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end = " ")
#     print()

for i in range(1, n):
    for j in range(n-2, -1, -1):
        if j == 0:
            dp[i][0] = min(dp[i-1][0] + arr[i][0], dp[i][1] + arr[i][0])
        else:
            dp[i][j] = min(dp[i][j+1] + arr[i][j], dp[i-1][j] + arr[i][j])

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end = " ")
#     print()

print(dp[n-1][0])