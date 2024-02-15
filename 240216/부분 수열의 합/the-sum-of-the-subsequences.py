n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

dp = [-1] * (m+1)

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= arr[j]:
            dp[i] = max(dp[i], dp[i - arr[j]] + 1)

if dp[m] == -1:
    print("No")
else:
    print("Yes")