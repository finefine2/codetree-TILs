n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

dp = [-1] * (m+1)

dp[0] = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= arr[j]:
            if dp[i - arr[j]] == -1:
                continue
            dp[i] = max(dp[i], dp[i - arr[j]] + 1)

if dp[m] == -1:
    print(-1)
else:
    print(dp[m])