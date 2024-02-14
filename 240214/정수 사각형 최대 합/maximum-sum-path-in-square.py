n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp[i][j] = max(dp[i-1][j] + arr[i][j], dp[i][j-1] + arr[i][j])
    
# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end = " ")
#     print()

print(dp[n-1][n-1])