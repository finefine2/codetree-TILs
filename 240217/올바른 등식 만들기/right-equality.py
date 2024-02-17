n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

s = sum(arr)

dp = [[0] * 41 for _ in range(n+1)]

dp[0][20] = 1

for i in range(1, n+1):
    for j in range(41):
        if j + arr[i] <= 40:
            dp[i][j] += dp[i-1][j + arr[i]]
        
        if j - arr[i] >= 0:
            dp[i][j] += dp[i-1][j - arr[i]]


print(dp[n][m+20])