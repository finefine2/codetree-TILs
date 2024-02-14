n = int(input())
dp = [[0] * n for _ in range(n)]

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp[0][0] = arr[0][0]

for i in range(n):
    dp[0][i] = arr[0][i]
    dp[i][0] = arr[i][0]

for i in range(0, n-1):
    for j in range(0, n-1):
        dp[i+1][j+1] = max(min(dp[i+1][j], arr[i][j]), min(dp[i][j+1], arr[i][j]))

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end = " ")
#     print()

print(dp[n-1][n-1])