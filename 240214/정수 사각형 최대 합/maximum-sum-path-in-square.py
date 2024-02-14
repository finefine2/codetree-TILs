n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j] + arr[i][j], dp[i][j-1] + arr[i][j])
    

print(dp[n-1][n-1])